import logging
import os
import shutil
from optparse import Values
from typing import List

from pip._internal.cache import WheelCache
from pip._internal.cli import cmdoptions
from pip._internal.cli.req_command import RequirementCommand, with_cleanup
from pip._internal.cli.status_codes import SUCCESS
from pip._internal.exceptions import CommandError
from pip._internal.req.req_install import InstallRequirement
from pip._internal.req.req_tracker import get_requirement_tracker
from pip._internal.utils.misc import ensure_dir, normalize_path
from pip._internal.utils.temp_dir import TempDirectory
from pip._internal.wheel_builder import build, should_build_for_wheel_command

logger = logging.getLogger(__name__)


class WheelCommand(RequirementCommand):
    """
    Build Wheel archives for your requirements and dependencies.

    Wheel is a built-package format, and offers the advantage of not
    recompiling your software during every install. For more details, see the
    wheel docs: https://wheel.readthedocs.io/en/latest/

    Requirements: setuptools>=0.8, and wheel.

    'pip wheel' uses the bdist_wheel setuptools extension from the wheel
    package to build individual wheels.

    """

    usage = """
      %prog [options] <requirement specifier> ...
      %prog [options] -r <requirements file> ...
      %prog [options] [-e] <vcs project url> ...
      %prog [options] [-e] <local project path> ...
      %prog [options] <archive url/path> ..."""

    def add_options(self):
        # type: () -> None

        self.cmd_opts.add_option(
            '-w', '--wheel-dir',
            dest='wheel_dir',
            metavar='dir',
            default=os.curdir,
            help=("Build wheels into <dir>, where the default is the "
                  "current working directory."),
        )
        self.cmd_opts.add_option(cmdoptions.no_binary())
        self.cmd_opts.add_option(cmdoptions.only_binary())
        self.cmd_opts.add_option(cmdoptions.prefer_binary())
        self.cmd_opts.add_option(cmdoptions.no_build_isolation())
        self.cmd_opts.add_option(cmdoptions.use_pep517())
        self.cmd_opts.add_option(cmdoptions.no_use_pep517())
        self.cmd_opts.add_option(cmdoptions.constraints())
        self.cmd_opts.add_option(cmdoptions.editable())
        self.cmd_opts.add_option(cmdoptions.requirements())
        self.cmd_opts.add_option(cmdoptions.src())
        self.cmd_opts.add_option(cmdoptions.ignore_requires_python())
        self.cmd_opts.add_option(cmdoptions.no_deps())
        self.cmd_opts.add_option(cmdoptions.build_dir())
        self.cmd_opts.add_option(cmdoptions.progress_bar())

        self.cmd_opts.add_option(
            '--no-verify',
            dest='no_verify',
            action='store_true',
            default=False,
            help="Don't verify if built wheel is valid.",
        )

        self.cmd_opts.add_option(cmdoptions.build_options())
        self.cmd_opts.add_option(cmdoptions.global_options())

        self.cmd_opts.add_option(
            '--pre',
            action='store_true',
            default=False,
            help=("Include pre-release and development versions. By default, "
                  "pip only finds stable versions."),
        )

        self.cmd_opts.add_option(cmdoptions.require_hashes())

        index_opts = cmdoptions.make_option_group(
            cmdoptions.index_group,
            self.parser,
        )

        self.parser.insert_option_group(0, index_opts)
        self.parser.insert_option_group(0, self.cmd_opts)

    @with_cleanup
    def run(self, options, args):
        # type: (Values, List[str]) -> int
        cmdoptions.check_install_build_global(options)

        session = self.get_default_session(options)

        finder = self._build_package_finder(options, session)
        wheel_cache = WheelCache(options.cache_dir, options.format_control)

        options.wheel_dir = normalize_path(options.wheel_dir)
        ensure_dir(options.wheel_dir)

        req_tracker = self.enter_context(get_requirement_tracker())

        directory = TempDirectory(
            delete=not options.no_clean,
            kind="wheel",
            globally_managed=True,
        )

        reqs = self.get_requirements(args, options, finder, session)

        preparer = self.make_requirement_preparer(
            temp_build_dir=directory,
            options=options,
            req_tracker=req_tracker,
            session=session,
            finder=finder,
            download_dir=options.wheel_dir,
            use_user_site=False,
        )

        resolver = self.make_resolver(
            preparer=preparer,
            finder=finder,
            options=options,
            wheel_cache=wheel_cache,
            ignore_requires_python=options.ignore_requires_python,
            use_pep517=options.use_pep517,
        )

        self.trace_basic_info(finder)

        requirement_set = resolver.resolve(
            reqs, check_supported_wheels=True
        )

        reqs_to_build = []  # type: List[InstallRequirement]
        for req in requirement_set.requirements.values():
            if req.is_wheel:
                preparer.save_linked_requirement(req)
            elif should_build_for_wheel_command(req):
                reqs_to_build.append(req)

        # build wheels
        build_successes, build_failures = build(
            reqs_to_build,
            wheel_cache=wheel_cache,
            verify=(not options.no_verify),
            build_options=options.build_options or [],
            global_options=options.global_options or [],
        )
        for req in build_successes:
            assert req.link and req.link.is_wheel
            assert req.local_file_path
            # copy from cache to target directory
            try:
                shutil.copy(req.local_file_path, options.wheel_dir)
            except OSError as e:
                logger.warning(
                    "Building wheel for %s failed: %s",
                    req.name, e,
                )
                build_failures.append(req)
        if len(build_failures) != 0:
            raise CommandError(
                "Failed to build one or more wheels"
            )

        return SUCCESS
