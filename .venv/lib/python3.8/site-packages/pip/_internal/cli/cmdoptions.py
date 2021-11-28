"""
shared options and groups

The principle here is to define options once, but *not* instantiate them
globally. One reason being that options with action='append' can carry state
between parses. pip parses general options twice internally, and shouldn't
pass on state. To be consistent, all options will follow this design.
"""

# The following comment should be removed at some point in the future.
# mypy: strict-optional=False

import os
import textwrap
import warnings
from functools import partial
from optparse import SUPPRESS_HELP, Option, OptionGroup, OptionParser, Values
from textwrap import dedent
from typing import Any, Callable, Dict, Optional, Tuple

from pip._vendor.packaging.utils import canonicalize_name

from pip._internal.cli.parser import ConfigOptionParser
from pip._internal.cli.progress_bars import BAR_TYPES
from pip._internal.exceptions import CommandError
from pip._internal.locations import USER_CACHE_DIR, get_src_prefix
from pip._internal.models.format_control import FormatControl
from pip._internal.models.index import PyPI
from pip._internal.models.target_python import TargetPython
from pip._internal.utils.hashes import STRONG_HASHES
from pip._internal.utils.misc import strtobool


def raise_option_error(parser, option, msg):
    # type: (OptionParser, Option, str) -> None
    """
    Raise an option parsing error using parser.error().

    Args:
      parser: an OptionParser instance.
      option: an Option instance.
      msg: the error text.
    """
    msg = f"{option} error: {msg}"
    msg = textwrap.fill(" ".join(msg.split()))
    parser.error(msg)


def make_option_group(group, parser):
    # type: (Dict[str, Any], ConfigOptionParser) -> OptionGroup
    """
    Return an OptionGroup object
    group  -- assumed to be dict with 'name' and 'options' keys
    parser -- an optparse Parser
    """
    option_group = OptionGroup(parser, group["name"])
    for option in group["options"]:
        option_group.add_option(option())
    return option_group


def check_install_build_global(options, check_options=None):
    # type: (Values, Optional[Values]) -> None
    """Disable wheels if per-setup.py call options are set.

    :param options: The OptionParser options to update.
    :param check_options: The options to check, if not supplied defaults to
        options.
    """
    if check_options is None:
        check_options = options

    def getname(n):
        # type: (str) -> Optional[Any]
        return getattr(check_options, n, None)

    names = ["build_options", "global_options", "install_options"]
    if any(map(getname, names)):
        control = options.format_control
        control.disallow_binaries()
        warnings.warn(
            "Disabling all use of wheels due to the use of --build-option "
            "/ --global-option / --install-option.",
            stacklevel=2,
        )


def check_dist_restriction(options, check_target=False):
    # type: (Values, bool) -> None
    """Function for determining if custom platform options are allowed.

    :param options: The OptionParser options.
    :param check_target: Whether or not to check if --target is being used.
    """
    dist_restriction_set = any(
        [
            options.python_version,
            options.platforms,
            options.abis,
            options.implementation,
        ]
    )

    binary_only = FormatControl(set(), {":all:"})
    sdist_dependencies_allowed = (
        options.format_control != binary_only and not options.ignore_dependencies
    )

    # Installations or downloads using dist restrictions must not combine
    # source distributions and dist-specific wheels, as they are not
    # guaranteed to be locally compatible.
    if dist_restriction_set and sdist_dependencies_allowed:
        raise CommandError(
            "When restricting platform and interpreter constraints using "
            "--python-version, --platform, --abi, or --implementation, "
            "either --no-deps must be set, or --only-binary=:all: must be "
            "set and --no-binary must not be set (or must be set to "
            ":none:)."
        )

    if check_target:
        if dist_restriction_set and not options.target_dir:
            raise CommandError(
                "Can not use any platform or abi specific options unless "
                "installing via '--target'"
            )


def _path_option_check(option, opt, value):
    # type: (Option, str, str) -> str
    return os.path.expanduser(value)


def _package_name_option_check(option, opt, value):
    # type: (Option, str, str) -> str
    return canonicalize_name(value)


class PipOption(Option):
    TYPES = Option.TYPES + ("path", "package_name")
    TYPE_CHECKER = Option.TYPE_CHECKER.copy()
    TYPE_CHECKER["package_name"] = _package_name_option_check
    TYPE_CHECKER["path"] = _path_option_check


###########
# options #
###########

help_ = partial(
    Option,
    "-h",
    "--help",
    dest="help",
    action="help",
    help="Show help.",
)  # type: Callable[..., Option]

isolated_mode = partial(
    Option,
    "--isolated",
    dest="isolated_mode",
    action="store_true",
    default=False,
    help=(
        "Run pip in an isolated mode, ignoring environment variables and user "
        "configuration."
    ),
)  # type: Callable[..., Option]

require_virtualenv = partial(
    Option,
    # Run only if inside a virtualenv, bail if not.
    "--require-virtualenv",
    "--require-venv",
    dest="require_venv",
    action="store_true",
    default=False,
    help=SUPPRESS_HELP,
)  # type: Callable[..., Option]

verbose = partial(
    Option,
    "-v",
    "--verbose",
    dest="verbose",
    action="count",
    default=0,
    help="Give more output. Option is additive, and can be used up to 3 times.",
)  # type: Callable[..., Option]

no_color = partial(
    Option,
    "--no-color",
    dest="no_color",
    action="store_true",
    default=False,
    help="Suppress colored output.",
)  # type: Callable[..., Option]

version = partial(
    Option,
    "-V",
    "--version",
    dest="version",
    action="store_true",
    help="Show version and exit.",
)  # type: Callable[..., Option]

quiet = partial(
    Option,
    "-q",
    "--quiet",
    dest="quiet",
    action="count",
    default=0,
    help=(
        "Give less output. Option is additive, and can be used up to 3"
        " times (corresponding to WARNING, ERROR, and CRITICAL logging"
        " levels)."
    ),
)  # type: Callable[..., Option]

progress_bar = partial(
    Option,
    "--progress-bar",
    dest="progress_bar",
    type="choice",
    choices=list(BAR_TYPES.keys()),
    default="on",
    help=(
        "Specify type of progress to be displayed ["
        + "|".join(BAR_TYPES.keys())
        + "] (default: %default)"
    ),
)  # type: Callable[..., Option]

log = partial(
    PipOption,
    "--log",
    "--log-file",
    "--local-log",
    dest="log",
    metavar="path",
    type="path",
    help="Path to a verbose appending log.",
)  # type: Callable[..., Option]

no_input = partial(
    Option,
    # Don't ask for input
    "--no-input",
    dest="no_input",
    action="store_true",
    default=False,
    help="Disable prompting for input.",
)  # type: Callable[..., Option]

proxy = partial(
    Option,
    "--proxy",
    dest="proxy",
    type="str",
    default="",
    help="Specify a proxy in the form [user:passwd@]proxy.server:port.",
)  # type: Callable[..., Option]

retries = partial(
    Option,
    "--retries",
    dest="retries",
    type="int",
    default=5,
    help="Maximum number of retries each connection should attempt "
    "(default %default times).",
)  # type: Callable[..., Option]

timeout = partial(
    Option,
    "--timeout",
    "--default-timeout",
    metavar="sec",
    dest="timeout",
    type="float",
    default=15,
    help="Set the socket timeout (default %default seconds).",
)  # type: Callable[..., Option]


def exists_action():
    # type: () -> Option
    return Option(
        # Option when path already exist
        "--exists-action",
        dest="exists_action",
        type="choice",
        choices=["s", "i", "w", "b", "a"],
        default=[],
        action="append",
        metavar="action",
        help="Default action when a path already exists: "
        "(s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.",
    )


cert = partial(
    PipOption,
    "--cert",
    dest="cert",
    type="path",
    metavar="path",
    help=(
        "Path to PEM-encoded CA certificate bundle. "
        "If provided, overrides the default. "
        "See 'SSL Certificate Verification' in pip documentation "
        "for more information."
    ),
)  # type: Callable[..., Option]

client_cert = partial(
    PipOption,
    "--client-cert",
    dest="client_cert",
    type="path",
    default=None,
    metavar="path",
    help="Path to SSL client certificate, a single file containing the "
    "private key and the certificate in PEM format.",
)  # type: Callable[..., Option]

index_url = partial(
    Option,
    "-i",
    "--index-url",
    "--pypi-url",
    dest="index_url",
    metavar="URL",
    default=PyPI.simple_url,
    help="Base URL of the Python Package Index (default %default). "
    "This should point to a repository compliant with PEP 503 "
    "(the simple repository API) or a local directory laid out "
    "in the same format.",
)  # type: Callable[..., Option]


def extra_index_url():
    # type: () -> Option
    return Option(
        "--extra-index-url",
        dest="extra_index_urls",
        metavar="URL",
        action="append",
        default=[],
        help="Extra URLs of package indexes to use in addition to "
        "--index-url. Should follow the same rules as "
        "--index-url.",
    )


no_index = partial(
    Option,
    "--no-index",
    dest="no_index",
    action="store_true",
    default=False,
    help="Ignore package index (only looking at --find-links URLs instead).",
)  # type: Callable[..., Option]


def find_links():
    # type: () -> Option
    return Option(
        "-f",
        "--find-links",
        dest="find_links",
        action="append",
        default=[],
        metavar="url",
        help="If a URL or path to an html file, then parse for links to "
        "archives such as sdist (.tar.gz) or wheel (.whl) files. "
        "If a local path or file:// URL that's a directory,  "
        "then look for archives in the directory listing. "
        "Links to VCS project URLs are not supported.",
    )


def trusted_host():
    # type: () -> Option
    return Option(
        "--trusted-host",
        dest="trusted_hosts",
        action="append",
        metavar="HOSTNAME",
        default=[],
        help="Mark this host or host:port pair as trusted, even though it "
        "does not have valid or any HTTPS.",
    )


def constraints():
    # type: () -> Option
    return Option(
        "-c",
        "--constraint",
        dest="constraints",
        action="append",
        default=[],
        metavar="file",
        help="Constrain versions using the given constraints file. "
        "This option can be used multiple times.",
    )


def requirements():
    # type: () -> Option
    return Option(
        "-r",
        "--requirement",
        dest="requirements",
        action="append",
        default=[],
        metavar="file",
        help="Install from the given requirements file. "
        "This option can be used multiple times.",
    )


def editable():
    # type: () -> Option
    return Option(
        "-e",
        "--editable",
        dest="editables",
        action="append",
        default=[],
        metavar="path/url",
        help=(
            "Install a project in editable mode (i.e. setuptools "
            '"develop mode") from a local project path or a VCS url.'
        ),
    )


def _handle_src(option, opt_str, value, parser):
    # type: (Option, str, str, OptionParser) -> None
    value = os.path.abspath(value)
    setattr(parser.values, option.dest, value)


src = partial(
    PipOption,
    "--src",
    "--source",
    "--source-dir",
    "--source-directory",
    dest="src_dir",
    type="path",
    metavar="dir",
    default=get_src_prefix(),
    action="callback",
    callback=_handle_src,
    help="Directory to check out editable projects into. "
    'The default in a virtualenv is "<venv path>/src". '
    'The default for global installs is "<current dir>/src".',
)  # type: Callable[..., Option]


def _get_format_control(values, option):
    # type: (Values, Option) -> Any
    """Get a format_control object."""
    return getattr(values, option.dest)


def _handle_no_binary(option, opt_str, value, parser):
    # type: (Option, str, str, OptionParser) -> None
    existing = _get_format_control(parser.values, option)
    FormatControl.handle_mutual_excludes(
        value,
        existing.no_binary,
        existing.only_binary,
    )


def _handle_only_binary(option, opt_str, value, parser):
    # type: (Option, str, str, OptionParser) -> None
    existing = _get_format_control(parser.values, option)
    FormatControl.handle_mutual_excludes(
        value,
        existing.only_binary,
        existing.no_binary,
    )


def no_binary():
    # type: () -> Option
    format_control = FormatControl(set(), set())
    return Option(
        "--no-binary",
        dest="format_control",
        action="callback",
        callback=_handle_no_binary,
        type="str",
        default=format_control,
        help="Do not use binary packages. Can be supplied multiple times, and "
        'each time adds to the existing value. Accepts either ":all:" to '
        'disable all binary packages, ":none:" to empty the set (notice '
        "the colons), or one or more package names with commas between "
        "them (no colons). Note that some packages are tricky to compile "
        "and may fail to install when this option is used on them.",
    )


def only_binary():
    # type: () -> Option
    format_control = FormatControl(set(), set())
    return Option(
        "--only-binary",
        dest="format_control",
        action="callback",
        callback=_handle_only_binary,
        type="str",
        default=format_control,
        help="Do not use source packages. Can be supplied multiple times, and "
        'each time adds to the existing value. Accepts either ":all:" to '
        'disable all source packages, ":none:" to empty the set, or one '
        "or more package names with commas between them. Packages "
        "without binary distributions will fail to install when this "
        "option is used on them.",
    )


platforms = partial(
    Option,
    "--platform",
    dest="platforms",
    metavar="platform",
    action="append",
    default=None,
    help=(
        "Only use wheels compatible with <platform>. Defaults to the "
        "platform of the running system. Use this option multiple times to "
        "specify multiple platforms supported by the target interpreter."
    ),
)  # type: Callable[..., Option]


# This was made a separate function for unit-testing purposes.
def _convert_python_version(value):
    # type: (str) -> Tuple[Tuple[int, ...], Optional[str]]
    """
    Convert a version string like "3", "37", or "3.7.3" into a tuple of ints.

    :return: A 2-tuple (version_info, error_msg), where `error_msg` is
        non-None if and only if there was a parsing error.
    """
    if not value:
        # The empty string is the same as not providing a value.
        return (None, None)

    parts = value.split(".")
    if len(parts) > 3:
        return ((), "at most three version parts are allowed")

    if len(parts) == 1:
        # Then we are in the case of "3" or "37".
        value = parts[0]
        if len(value) > 1:
            parts = [value[0], value[1:]]

    try:
        version_info = tuple(int(part) for part in parts)
    except ValueError:
        return ((), "each version part must be an integer")

    return (version_info, None)


def _handle_python_version(option, opt_str, value, parser):
    # type: (Option, str, str, OptionParser) -> None
    """
    Handle a provided --python-version value.
    """
    version_info, error_msg = _convert_python_version(value)
    if error_msg is not None:
        msg = "invalid --python-version value: {!r}: {}".format(
            value,
            error_msg,
        )
        raise_option_error(parser, option=option, msg=msg)

    parser.values.python_version = version_info


python_version = partial(
    Option,
    "--python-version",
    dest="python_version",
    metavar="python_version",
    action="callback",
    callback=_handle_python_version,
    type="str",
    default=None,
    help=dedent(
        """\
    The Python interpreter version to use for wheel and "Requires-Python"
    compatibility checks. Defaults to a version derived from the running
    interpreter. The version can be specified using up to three dot-separated
    integers (e.g. "3" for 3.0.0, "3.7" for 3.7.0, or "3.7.3"). A major-minor
    version can also be given as a string without dots (e.g. "37" for 3.7.0).
    """
    ),
)  # type: Callable[..., Option]


implementation = partial(
    Option,
    "--implementation",
    dest="implementation",
    metavar="implementation",
    default=None,
    help=(
        "Only use wheels compatible with Python "
        "implementation <implementation>, e.g. 'pp', 'jy', 'cp', "
        " or 'ip'. If not specified, then the current "
        "interpreter implementation is used.  Use 'py' to force "
        "implementation-agnostic wheels."
    ),
)  # type: Callable[..., Option]


abis = partial(
    Option,
    "--abi",
    dest="abis",
    metavar="abi",
    action="append",
    default=None,
    help=(
        "Only use wheels compatible with Python abi <abi>, e.g. 'pypy_41'. "
        "If not specified, then the current interpreter abi tag is used. "
        "Use this option multiple times to specify multiple abis supported "
        "by the target interpreter. Generally you will need to specify "
        "--implementation, --platform, and --python-version when using this "
        "option."
    ),
)  # type: Callable[..., Option]


def add_target_python_options(cmd_opts):
    # type: (OptionGroup) -> None
    cmd_opts.add_option(platforms())
    cmd_opts.add_option(python_version())
    cmd_opts.add_option(implementation())
    cmd_opts.add_option(abis())


def make_target_python(options):
    # type: (Values) -> TargetPython
    target_python = TargetPython(
        platforms=options.platforms,
        py_version_info=options.python_version,
        abis=options.abis,
        implementation=options.implementation,
    )

    return target_python


def prefer_binary():
    # type: () -> Option
    return Option(
        "--prefer-binary",
        dest="prefer_binary",
        action="store_true",
        default=False,
        help="Prefer older binary packages over newer source packages.",
    )


cache_dir = partial(
    PipOption,
    "--cache-dir",
    dest="cache_dir",
    default=USER_CACHE_DIR,
    metavar="dir",
    type="path",
    help="Store the cache data in <dir>.",
)  # type: Callable[..., Option]


def _handle_no_cache_dir(option, opt, value, parser):
    # type: (Option, str, str, OptionParser) -> None
    """
    Process a value provided for the --no-cache-dir option.

    This is an optparse.Option callback for the --no-cache-dir option.
    """
    # The value argument will be None if --no-cache-dir is passed via the
    # command-line, since the option doesn't accept arguments.  However,
    # the value can be non-None if the option is triggered e.g. by an
    # environment variable, like PIP_NO_CACHE_DIR=true.
    if value is not None:
        # Then parse the string value to get argument error-checking.
        try:
            strtobool(value)
        except ValueError as exc:
            raise_option_error(parser, option=option, msg=str(exc))

    # Originally, setting PIP_NO_CACHE_DIR to a value that strtobool()
    # converted to 0 (like "false" or "no") caused cache_dir to be disabled
    # rather than enabled (logic would say the latter).  Thus, we disable
    # the cache directory not just on values that parse to True, but (for
    # backwards compatibility reasons) also on values that parse to False.
    # In other words, always set it to False if the option is provided in
    # some (valid) form.
    parser.values.cache_dir = False


no_cache = partial(
    Option,
    "--no-cache-dir",
    dest="cache_dir",
    action="callback",
    callback=_handle_no_cache_dir,
    help="Disable the cache.",
)  # type: Callable[..., Option]

no_deps = partial(
    Option,
    "--no-deps",
    "--no-dependencies",
    dest="ignore_dependencies",
    action="store_true",
    default=False,
    help="Don't install package dependencies.",
)  # type: Callable[..., Option]

build_dir = partial(
    PipOption,
    "-b",
    "--build",
    "--build-dir",
    "--build-directory",
    dest="build_dir",
    type="path",
    metavar="dir",
    help=SUPPRESS_HELP,
)  # type: Callable[..., Option]

ignore_requires_python = partial(
    Option,
    "--ignore-requires-python",
    dest="ignore_requires_python",
    action="store_true",
    help="Ignore the Requires-Python information.",
)  # type: Callable[..., Option]

no_build_isolation = partial(
    Option,
    "--no-build-isolation",
    dest="build_isolation",
    action="store_false",
    default=True,
    help="Disable isolation when building a modern source distribution. "
    "Build dependencies specified by PEP 518 must be already installed "
    "if this option is used.",
)  # type: Callable[..., Option]


def _handle_no_use_pep517(option, opt, value, parser):
    # type: (Option, str, str, OptionParser) -> None
    """
    Process a value provided for the --no-use-pep517 option.

    This is an optparse.Option callback for the no_use_pep517 option.
    """
    # Since --no-use-pep517 doesn't accept arguments, the value argument
    # will be None if --no-use-pep517 is passed via the command-line.
    # However, the value can be non-None if the option is triggered e.g.
    # by an environment variable, for example "PIP_NO_USE_PEP517=true".
    if value is not None:
        msg = """A value was passed for --no-use-pep517,
        probably using either the PIP_NO_USE_PEP517 environment variable
        or the "no-use-pep517" config file option. Use an appropriate value
        of the PIP_USE_PEP517 environment variable or the "use-pep517"
        config file option instead.
        """
        raise_option_error(parser, option=option, msg=msg)

    # Otherwise, --no-use-pep517 was passed via the command-line.
    parser.values.use_pep517 = False


use_pep517 = partial(
    Option,
    "--use-pep517",
    dest="use_pep517",
    action="store_true",
    default=None,
    help="Use PEP 517 for building source distributions "
    "(use --no-use-pep517 to force legacy behaviour).",
)  # type: Any

no_use_pep517 = partial(
    Option,
    "--no-use-pep517",
    dest="use_pep517",
    action="callback",
    callback=_handle_no_use_pep517,
    default=None,
    help=SUPPRESS_HELP,
)  # type: Any

install_options = partial(
    Option,
    "--install-option",
    dest="install_options",
    action="append",
    metavar="options",
    help="Extra arguments to be supplied to the setup.py install "
    'command (use like --install-option="--install-scripts=/usr/local/'
    'bin"). Use multiple --install-option options to pass multiple '
    "options to setup.py install. If you are using an option with a "
    "directory path, be sure to use absolute path.",
)  # type: Callable[..., Option]

build_options = partial(
    Option,
    "--build-option",
    dest="build_options",
    metavar="options",
    action="append",
    help="Extra arguments to be supplied to 'setup.py bdist_wheel'.",
)  # type: Callable[..., Option]

global_options = partial(
    Option,
    "--global-option",
    dest="global_options",
    action="append",
    metavar="options",
    help="Extra global options to be supplied to the setup.py "
    "call before the install or bdist_wheel command.",
)  # type: Callable[..., Option]

no_clean = partial(
    Option,
    "--no-clean",
    action="store_true",
    default=False,
    help="Don't clean up build directories.",
)  # type: Callable[..., Option]

pre = partial(
    Option,
    "--pre",
    action="store_true",
    default=False,
    help="Include pre-release and development versions. By default, "
    "pip only finds stable versions.",
)  # type: Callable[..., Option]

disable_pip_version_check = partial(
    Option,
    "--disable-pip-version-check",
    dest="disable_pip_version_check",
    action="store_true",
    default=False,
    help="Don't periodically check PyPI to determine whether a new version "
    "of pip is available for download. Implied with --no-index.",
)  # type: Callable[..., Option]


def _handle_merge_hash(option, opt_str, value, parser):
    # type: (Option, str, str, OptionParser) -> None
    """Given a value spelled "algo:digest", append the digest to a list
    pointed to in a dict by the algo name."""
    if not parser.values.hashes:
        parser.values.hashes = {}
    try:
        algo, digest = value.split(":", 1)
    except ValueError:
        parser.error(
            "Arguments to {} must be a hash name "  # noqa
            "followed by a value, like --hash=sha256:"
            "abcde...".format(opt_str)
        )
    if algo not in STRONG_HASHES:
        parser.error(
            "Allowed hash algorithms for {} are {}.".format(  # noqa
                opt_str, ", ".join(STRONG_HASHES)
            )
        )
    parser.values.hashes.setdefault(algo, []).append(digest)


hash = partial(
    Option,
    "--hash",
    # Hash values eventually end up in InstallRequirement.hashes due to
    # __dict__ copying in process_line().
    dest="hashes",
    action="callback",
    callback=_handle_merge_hash,
    type="string",
    help="Verify that the package's archive matches this "
    "hash before installing. Example: --hash=sha256:abcdef...",
)  # type: Callable[..., Option]


require_hashes = partial(
    Option,
    "--require-hashes",
    dest="require_hashes",
    action="store_true",
    default=False,
    help="Require a hash to check each requirement against, for "
    "repeatable installs. This option is implied when any package in a "
    "requirements file has a --hash option.",
)  # type: Callable[..., Option]


list_path = partial(
    PipOption,
    "--path",
    dest="path",
    type="path",
    action="append",
    help="Restrict to the specified installation path for listing "
    "packages (can be used multiple times).",
)  # type: Callable[..., Option]


def check_list_path_option(options):
    # type: (Values) -> None
    if options.path and (options.user or options.local):
        raise CommandError("Cannot combine '--path' with '--user' or '--local'")


list_exclude = partial(
    PipOption,
    "--exclude",
    dest="excludes",
    action="append",
    metavar="package",
    type="package_name",
    help="Exclude specified package from the output",
)  # type: Callable[..., Option]


no_python_version_warning = partial(
    Option,
    "--no-python-version-warning",
    dest="no_python_version_warning",
    action="store_true",
    default=False,
    help="Silence deprecation warnings for upcoming unsupported Pythons.",
)  # type: Callable[..., Option]


use_new_feature = partial(
    Option,
    "--use-feature",
    dest="features_enabled",
    metavar="feature",
    action="append",
    default=[],
    choices=["2020-resolver", "fast-deps", "in-tree-build"],
    help="Enable new functionality, that may be backward incompatible.",
)  # type: Callable[..., Option]

use_deprecated_feature = partial(
    Option,
    "--use-deprecated",
    dest="deprecated_features_enabled",
    metavar="feature",
    action="append",
    default=[],
    choices=["legacy-resolver"],
    help=("Enable deprecated functionality, that will be removed in the future."),
)  # type: Callable[..., Option]


##########
# groups #
##########

general_group = {
    "name": "General Options",
    "options": [
        help_,
        isolated_mode,
        require_virtualenv,
        verbose,
        version,
        quiet,
        log,
        no_input,
        proxy,
        retries,
        timeout,
        exists_action,
        trusted_host,
        cert,
        client_cert,
        cache_dir,
        no_cache,
        disable_pip_version_check,
        no_color,
        no_python_version_warning,
        use_new_feature,
        use_deprecated_feature,
    ],
}  # type: Dict[str, Any]

index_group = {
    "name": "Package Index Options",
    "options": [
        index_url,
        extra_index_url,
        no_index,
        find_links,
    ],
}  # type: Dict[str, Any]
