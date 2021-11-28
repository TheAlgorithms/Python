import errno
import logging
import operator
import os
import shutil
import site
from optparse import SUPPRESS_HELP, Values
from typing import Iterable, List, Optional

from pip._vendor.packaging.utils import canonicalize_name

from pip._internal.cache import WheelCache
from pip._internal.cli import cmdoptions
from pip._internal.cli.cmdoptions import make_target_python
from pip._internal.cli.req_command import (
    RequirementCommand,
    warn_if_run_as_root,
    with_cleanup,
)
from pip._internal.cli.status_codes import ERROR, SUCCESS
from pip._internal.exceptions import CommandError, InstallationError
from pip._internal.locations import get_scheme
from pip._internal.metadata import get_environment
from pip._internal.models.format_control import FormatControl
from pip._internal.operations.check import ConflictDetails, check_install_conflicts
from pip._internal.req import install_given_reqs
from pip._internal.req.req_install import InstallRequirement
from pip._internal.req.req_tracker import get_requirement_tracker
from pip._internal.utils.distutils_args import parse_distutils_args
from pip._internal.utils.filesystem import test_writable_dir
from pip._internal.utils.misc import (
    ensure_dir,
    get_pip_version,
    protect_pip_from_modification_on_windows,
    write_output,
)
from pip._internal.utils.temp_dir import TempDirectory
from pip._internal.utils.virtualenv import (
    running_under_virtualenv,
    virtualenv_no_global,
)
from pip._internal.wheel_builder import (
    BinaryAllowedPredicate,
    build,
    should_build_for_install_command,
)

logger = logging.getLogger(__name__)


def get_check_binary_allowed(format_control):
    # type: (FormatControl) -> BinaryAllowedPredicate
    def check_binary_allowed(req):
        # type: (InstallRequirement) -> bool
        canonical_name = canonicalize_name(req.name or "")
        allowed_formats = format_control.get_allowed_formats(canonical_name)
        return "binary" in allowed_formats

    return check_binary_allowed


class InstallCommand(RequirementCommand):
    """
    Install packages from:

    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.

    pip also supports installing from "requirements files", which provide
    an easy way to specify a whole environment to be installed.
    """

    usage = """
      %prog [options] <requirement specifier> [package-index-options] ...
      %prog [options] -r <requirements file> [package-index-options] ...
      %prog [options] [-e] <vcs project url> ...
      %prog [options] [-e] <local project path> ...
      %prog [options] <archive url/path> ..."""

    def add_options(self):
        # type: () -> None
        self.cmd_opts.add_option(cmdoptions.requirements())
        self.cmd_opts.add_option(cmdoptions.constraints())
        self.cmd_opts.add_option(cmdoptions.no_deps())
        self.cmd_opts.add_option(cmdoptions.pre())

        self.cmd_opts.add_option(cmdoptions.editable())
        self.cmd_opts.add_option(
            '-t', '--target',
            dest='target_dir',
            metavar='dir',
            default=None,
            help='Install packages into <dir>. '
                 'By default this will not replace existing files/folders in '
                 '<dir>. Use --upgrade to replace existing packages in <dir> '
                 'with new versions.'
        )
        cmdoptions.add_target_python_options(self.cmd_opts)

        self.cmd_opts.add_option(
            '--user',
            dest='use_user_site',
            action='store_true',
            help="Install to the Python user install directory for your "
                 "platform. Typically ~/.local/, or %APPDATA%\\Python on "
                 "Windows. (See the Python documentation for site.USER_BASE "
                 "for full details.)")
        self.cmd_opts.add_option(
            '--no-user',
            dest='use_user_site',
            action='store_false',
            help=SUPPRESS_HELP)
        self.cmd_opts.add_option(
            '--root',
            dest='root_path',
            metavar='dir',
            default=None,
            help="Install everything relative to this alternate root "
                 "directory.")
        self.cmd_opts.add_option(
            '--prefix',
            dest='prefix_path',
            metavar='dir',
            default=None,
            help="Installation prefix where lib, bin and other top-level "
                 "folders are placed")

        self.cmd_opts.add_option(cmdoptions.build_dir())

        self.cmd_opts.add_option(cmdoptions.src())

        self.cmd_opts.add_option(
            '-U', '--upgrade',
            dest='upgrade',
            action='store_true',
            help='Upgrade all specified packages to the newest available '
                 'version. The handling of dependencies depends on the '
                 'upgrade-strategy used.'
        )

        self.cmd_opts.add_option(
            '--upgrade-strategy',
            dest='upgrade_strategy',
            default='only-if-needed',
            choices=['only-if-needed', 'eager'],
            help='Determines how dependency upgrading should be handled '
                 '[default: %default]. '
                 '"eager" - dependencies are upgraded regardless of '
                 'whether the currently installed version satisfies the '
                 'requirements of the upgraded package(s). '
                 '"only-if-needed" -  are upgraded only when they do not '
                 'satisfy the requirements of the upgraded package(s).'
        )

        self.cmd_opts.add_option(
            '--force-reinstall',
            dest='force_reinstall',
            action='store_true',
            help='Reinstall all packages even if they are already '
                 'up-to-date.')

        self.cmd_opts.add_option(
            '-I', '--ignore-installed',
            dest='ignore_installed',
            action='store_true',
            help='Ignore the installed packages, overwriting them. '
                 'This can break your system if the existing package '
                 'is of a different version or was installed '
                 'with a different package manager!'
        )

        self.cmd_opts.add_option(cmdoptions.ignore_requires_python())
        self.cmd_opts.add_option(cmdoptions.no_build_isolation())
        self.cmd_opts.add_option(cmdoptions.use_pep517())
        self.cmd_opts.add_option(cmdoptions.no_use_pep517())

        self.cmd_opts.add_option(cmdoptions.install_options())
        self.cmd_opts.add_option(cmdoptions.global_options())

        self.cmd_opts.add_option(
            "--compile",
            action="store_true",
            dest="compile",
            default=True,
            help="Compile Python source files to bytecode",
        )

        self.cmd_opts.add_option(
            "--no-compile",
            action="store_false",
            dest="compile",
            help="Do not compile Python source files to bytecode",
        )

        self.cmd_opts.add_option(
            "--no-warn-script-location",
            action="store_false",
            dest="warn_script_location",
            default=True,
            help="Do not warn when installing scripts outside PATH",
        )
        self.cmd_opts.add_option(
            "--no-warn-conflicts",
            action="store_false",
            dest="warn_about_conflicts",
            default=True,
            help="Do not warn about broken dependencies",
        )

        self.cmd_opts.add_option(cmdoptions.no_binary())
        self.cmd_opts.add_option(cmdoptions.only_binary())
        self.cmd_opts.add_option(cmdoptions.prefer_binary())
        self.cmd_opts.add_option(cmdoptions.require_hashes())
        self.cmd_opts.add_option(cmdoptions.progress_bar())

        index_opts = cmdoptions.make_option_group(
            cmdoptions.index_group,
            self.parser,
        )

        self.parser.insert_option_group(0, index_opts)
        self.parser.insert_option_group(0, self.cmd_opts)

    @with_cleanup
    def run(self, options, args):
        # type: (Values, List[str]) -> int
        if options.use_user_site and options.target_dir is not None:
            raise CommandError("Can not combine '--user' and '--target'")

        cmdoptions.check_install_build_global(options)
        upgrade_strategy = "to-satisfy-only"
        if options.upgrade:
            upgrade_strategy = options.upgrade_strategy

        cmdoptions.check_dist_restriction(options, check_target=True)

        install_options = options.install_options or []

        logger.debug("Using %s", get_pip_version())
        options.use_user_site = decide_user_install(
            options.use_user_site,
            prefix_path=options.prefix_path,
            target_dir=options.target_dir,
            root_path=options.root_path,
            isolated_mode=options.isolated_mode,
        )

        target_temp_dir = None  # type: Optional[TempDirectory]
        target_temp_dir_path = None  # type: Optional[str]
        if options.target_dir:
            options.ignore_installed = True
            options.target_dir = os.path.abspath(options.target_dir)
            if (os.path.exists(options.target_dir) and not
                    os.path.isdir(options.target_dir)):
                raise CommandError(
                    "Target path exists but is not a directory, will not "
                    "continue."
                )

            # Create a target directory for using with the target option
            target_temp_dir = TempDirectory(kind="target")
            target_temp_dir_path = target_temp_dir.path
            self.enter_context(target_temp_dir)

        global_options = options.global_options or []

        session = self.get_default_session(options)

        target_python = make_target_python(options)
        finder = self._build_package_finder(
            options=options,
            session=session,
            target_python=target_python,
            ignore_requires_python=options.ignore_requires_python,
        )
        wheel_cache = WheelCache(options.cache_dir, options.format_control)

        req_tracker = self.enter_context(get_requirement_tracker())

        directory = TempDirectory(
            delete=not options.no_clean,
            kind="install",
            globally_managed=True,
        )

        try:
            reqs = self.get_requirements(args, options, finder, session)

            reject_location_related_install_options(
                reqs, options.install_options
            )

            preparer = self.make_requirement_preparer(
                temp_build_dir=directory,
                options=options,
                req_tracker=req_tracker,
                session=session,
                finder=finder,
                use_user_site=options.use_user_site,
            )
            resolver = self.make_resolver(
                preparer=preparer,
                finder=finder,
                options=options,
                wheel_cache=wheel_cache,
                use_user_site=options.use_user_site,
                ignore_installed=options.ignore_installed,
                ignore_requires_python=options.ignore_requires_python,
                force_reinstall=options.force_reinstall,
                upgrade_strategy=upgrade_strategy,
                use_pep517=options.use_pep517,
            )

            self.trace_basic_info(finder)

            requirement_set = resolver.resolve(
                reqs, check_supported_wheels=not options.target_dir
            )

            try:
                pip_req = requirement_set.get_requirement("pip")
            except KeyError:
                modifying_pip = False
            else:
                # If we're not replacing an already installed pip,
                # we're not modifying it.
                modifying_pip = pip_req.satisfied_by is None
            protect_pip_from_modification_on_windows(
                modifying_pip=modifying_pip
            )

            check_binary_allowed = get_check_binary_allowed(
                finder.format_control
            )

            reqs_to_build = [
                r for r in requirement_set.requirements.values()
                if should_build_for_install_command(
                    r, check_binary_allowed
                )
            ]

            _, build_failures = build(
                reqs_to_build,
                wheel_cache=wheel_cache,
                verify=True,
                build_options=[],
                global_options=[],
            )

            # If we're using PEP 517, we cannot do a direct install
            # so we fail here.
            pep517_build_failure_names = [
                r.name   # type: ignore
                for r in build_failures if r.use_pep517
            ]  # type: List[str]
            if pep517_build_failure_names:
                raise InstallationError(
                    "Could not build wheels for {} which use"
                    " PEP 517 and cannot be installed directly".format(
                        ", ".join(pep517_build_failure_names)
                    )
                )

            # For now, we just warn about failures building legacy
            # requirements, as we'll fall through to a direct
            # install for those.
            for r in build_failures:
                if not r.use_pep517:
                    r.legacy_install_reason = 8368

            to_install = resolver.get_installation_order(
                requirement_set
            )

            # Check for conflicts in the package set we're installing.
            conflicts = None  # type: Optional[ConflictDetails]
            should_warn_about_conflicts = (
                not options.ignore_dependencies and
                options.warn_about_conflicts
            )
            if should_warn_about_conflicts:
                conflicts = self._determine_conflicts(to_install)

            # Don't warn about script install locations if
            # --target has been specified
            warn_script_location = options.warn_script_location
            if options.target_dir:
                warn_script_location = False

            installed = install_given_reqs(
                to_install,
                install_options,
                global_options,
                root=options.root_path,
                home=target_temp_dir_path,
                prefix=options.prefix_path,
                warn_script_location=warn_script_location,
                use_user_site=options.use_user_site,
                pycompile=options.compile,
            )

            lib_locations = get_lib_location_guesses(
                user=options.use_user_site,
                home=target_temp_dir_path,
                root=options.root_path,
                prefix=options.prefix_path,
                isolated=options.isolated_mode,
            )
            env = get_environment(lib_locations)

            installed.sort(key=operator.attrgetter('name'))
            items = []
            for result in installed:
                item = result.name
                try:
                    installed_dist = env.get_distribution(item)
                    if installed_dist is not None:
                        item = f"{item}-{installed_dist.version}"
                except Exception:
                    pass
                items.append(item)

            if conflicts is not None:
                self._warn_about_conflicts(
                    conflicts,
                    resolver_variant=self.determine_resolver_variant(options),
                )

            installed_desc = ' '.join(items)
            if installed_desc:
                write_output(
                    'Successfully installed %s', installed_desc,
                )
        except OSError as error:
            show_traceback = (self.verbosity >= 1)

            message = create_os_error_message(
                error, show_traceback, options.use_user_site,
            )
            logger.error(message, exc_info=show_traceback)  # noqa

            return ERROR

        if options.target_dir:
            assert target_temp_dir
            self._handle_target_dir(
                options.target_dir, target_temp_dir, options.upgrade
            )

        warn_if_run_as_root()
        return SUCCESS

    def _handle_target_dir(self, target_dir, target_temp_dir, upgrade):
        # type: (str, TempDirectory, bool) -> None
        ensure_dir(target_dir)

        # Checking both purelib and platlib directories for installed
        # packages to be moved to target directory
        lib_dir_list = []

        # Checking both purelib and platlib directories for installed
        # packages to be moved to target directory
        scheme = get_scheme('', home=target_temp_dir.path)
        purelib_dir = scheme.purelib
        platlib_dir = scheme.platlib
        data_dir = scheme.data

        if os.path.exists(purelib_dir):
            lib_dir_list.append(purelib_dir)
        if os.path.exists(platlib_dir) and platlib_dir != purelib_dir:
            lib_dir_list.append(platlib_dir)
        if os.path.exists(data_dir):
            lib_dir_list.append(data_dir)

        for lib_dir in lib_dir_list:
            for item in os.listdir(lib_dir):
                if lib_dir == data_dir:
                    ddir = os.path.join(data_dir, item)
                    if any(s.startswith(ddir) for s in lib_dir_list[:-1]):
                        continue
                target_item_dir = os.path.join(target_dir, item)
                if os.path.exists(target_item_dir):
                    if not upgrade:
                        logger.warning(
                            'Target directory %s already exists. Specify '
                            '--upgrade to force replacement.',
                            target_item_dir
                        )
                        continue
                    if os.path.islink(target_item_dir):
                        logger.warning(
                            'Target directory %s already exists and is '
                            'a link. pip will not automatically replace '
                            'links, please remove if replacement is '
                            'desired.',
                            target_item_dir
                        )
                        continue
                    if os.path.isdir(target_item_dir):
                        shutil.rmtree(target_item_dir)
                    else:
                        os.remove(target_item_dir)

                shutil.move(
                    os.path.join(lib_dir, item),
                    target_item_dir
                )

    def _determine_conflicts(self, to_install):
        # type: (List[InstallRequirement]) -> Optional[ConflictDetails]
        try:
            return check_install_conflicts(to_install)
        except Exception:
            logger.exception(
                "Error while checking for conflicts. Please file an issue on "
                "pip's issue tracker: https://github.com/pypa/pip/issues/new"
            )
            return None

    def _warn_about_conflicts(self, conflict_details, resolver_variant):
        # type: (ConflictDetails, str) -> None
        package_set, (missing, conflicting) = conflict_details
        if not missing and not conflicting:
            return

        parts = []  # type: List[str]
        if resolver_variant == "legacy":
            parts.append(
                "pip's legacy dependency resolver does not consider dependency "
                "conflicts when selecting packages. This behaviour is the "
                "source of the following dependency conflicts."
            )
        else:
            assert resolver_variant == "2020-resolver"
            parts.append(
                "pip's dependency resolver does not currently take into account "
                "all the packages that are installed. This behaviour is the "
                "source of the following dependency conflicts."
            )

        # NOTE: There is some duplication here, with commands/check.py
        for project_name in missing:
            version = package_set[project_name][0]
            for dependency in missing[project_name]:
                message = (
                    "{name} {version} requires {requirement}, "
                    "which is not installed."
                ).format(
                    name=project_name,
                    version=version,
                    requirement=dependency[1],
                )
                parts.append(message)

        for project_name in conflicting:
            version = package_set[project_name][0]
            for dep_name, dep_version, req in conflicting[project_name]:
                message = (
                    "{name} {version} requires {requirement}, but {you} have "
                    "{dep_name} {dep_version} which is incompatible."
                ).format(
                    name=project_name,
                    version=version,
                    requirement=req,
                    dep_name=dep_name,
                    dep_version=dep_version,
                    you=("you" if resolver_variant == "2020-resolver" else "you'll")
                )
                parts.append(message)

        logger.critical("\n".join(parts))


def get_lib_location_guesses(
        user=False,  # type: bool
        home=None,  # type: Optional[str]
        root=None,  # type: Optional[str]
        isolated=False,  # type: bool
        prefix=None  # type: Optional[str]
):
    # type:(...) -> List[str]
    scheme = get_scheme(
        '',
        user=user,
        home=home,
        root=root,
        isolated=isolated,
        prefix=prefix,
    )
    return [scheme.purelib, scheme.platlib]


def site_packages_writable(root, isolated):
    # type: (Optional[str], bool) -> bool
    return all(
        test_writable_dir(d) for d in set(
            get_lib_location_guesses(root=root, isolated=isolated))
    )


def decide_user_install(
    use_user_site,  # type: Optional[bool]
    prefix_path=None,  # type: Optional[str]
    target_dir=None,  # type: Optional[str]
    root_path=None,  # type: Optional[str]
    isolated_mode=False,  # type: bool
):
    # type: (...) -> bool
    """Determine whether to do a user install based on the input options.

    If use_user_site is False, no additional checks are done.
    If use_user_site is True, it is checked for compatibility with other
    options.
    If use_user_site is None, the default behaviour depends on the environment,
    which is provided by the other arguments.
    """
    # In some cases (config from tox), use_user_site can be set to an integer
    # rather than a bool, which 'use_user_site is False' wouldn't catch.
    if (use_user_site is not None) and (not use_user_site):
        logger.debug("Non-user install by explicit request")
        return False

    if use_user_site:
        if prefix_path:
            raise CommandError(
                "Can not combine '--user' and '--prefix' as they imply "
                "different installation locations"
            )
        if virtualenv_no_global():
            raise InstallationError(
                "Can not perform a '--user' install. User site-packages "
                "are not visible in this virtualenv."
            )
        logger.debug("User install by explicit request")
        return True

    # If we are here, user installs have not been explicitly requested/avoided
    assert use_user_site is None

    # user install incompatible with --prefix/--target
    if prefix_path or target_dir:
        logger.debug("Non-user install due to --prefix or --target option")
        return False

    # If user installs are not enabled, choose a non-user install
    if not site.ENABLE_USER_SITE:
        logger.debug("Non-user install because user site-packages disabled")
        return False

    # If we have permission for a non-user install, do that,
    # otherwise do a user install.
    if site_packages_writable(root=root_path, isolated=isolated_mode):
        logger.debug("Non-user install because site-packages writeable")
        return False

    logger.info("Defaulting to user installation because normal site-packages "
                "is not writeable")
    return True


def reject_location_related_install_options(requirements, options):
    # type: (List[InstallRequirement], Optional[List[str]]) -> None
    """If any location-changing --install-option arguments were passed for
    requirements or on the command-line, then show a deprecation warning.
    """
    def format_options(option_names):
        # type: (Iterable[str]) -> List[str]
        return ["--{}".format(name.replace("_", "-")) for name in option_names]

    offenders = []

    for requirement in requirements:
        install_options = requirement.install_options
        location_options = parse_distutils_args(install_options)
        if location_options:
            offenders.append(
                "{!r} from {}".format(
                    format_options(location_options.keys()), requirement
                )
            )

    if options:
        location_options = parse_distutils_args(options)
        if location_options:
            offenders.append(
                "{!r} from command line".format(
                    format_options(location_options.keys())
                )
            )

    if not offenders:
        return

    raise CommandError(
        "Location-changing options found in --install-option: {}."
        " This is unsupported, use pip-level options like --user,"
        " --prefix, --root, and --target instead.".format(
            "; ".join(offenders)
        )
    )


def create_os_error_message(error, show_traceback, using_user_site):
    # type: (OSError, bool, bool) -> str
    """Format an error message for an OSError

    It may occur anytime during the execution of the install command.
    """
    parts = []

    # Mention the error if we are not going to show a traceback
    parts.append("Could not install packages due to an OSError")
    if not show_traceback:
        parts.append(": ")
        parts.append(str(error))
    else:
        parts.append(".")

    # Spilt the error indication from a helper message (if any)
    parts[-1] += "\n"

    # Suggest useful actions to the user:
    #  (1) using user site-packages or (2) verifying the permissions
    if error.errno == errno.EACCES:
        user_option_part = "Consider using the `--user` option"
        permissions_part = "Check the permissions"

        if not running_under_virtualenv() and not using_user_site:
            parts.extend([
                user_option_part, " or ",
                permissions_part.lower(),
            ])
        else:
            parts.append(permissions_part)
        parts.append(".\n")

    return "".join(parts).strip() + "\n"
