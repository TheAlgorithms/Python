# The following comment should be removed at some point in the future.
# mypy: strict-optional=False

import contextlib
import errno
import getpass
import hashlib
import io
import logging
import os
import posixpath
import shutil
import stat
import sys
import urllib.parse
from io import StringIO
from itertools import filterfalse, tee, zip_longest
from types import TracebackType
from typing import (
    Any,
    AnyStr,
    BinaryIO,
    Callable,
    Container,
    ContextManager,
    Iterable,
    Iterator,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    cast,
)

from pip._vendor.pkg_resources import Distribution
from pip._vendor.tenacity import retry, stop_after_delay, wait_fixed

from pip import __version__
from pip._internal.exceptions import CommandError
from pip._internal.locations import get_major_minor_version, site_packages, user_site
from pip._internal.utils.compat import WINDOWS, stdlib_pkgs
from pip._internal.utils.virtualenv import (
    running_under_virtualenv,
    virtualenv_no_global,
)

__all__ = [
    "rmtree",
    "display_path",
    "backup_dir",
    "ask",
    "splitext",
    "format_size",
    "is_installable_dir",
    "normalize_path",
    "renames",
    "get_prog",
    "captured_stdout",
    "ensure_dir",
    "remove_auth_from_url",
]


logger = logging.getLogger(__name__)

T = TypeVar("T")
ExcInfo = Tuple[Type[BaseException], BaseException, TracebackType]
VersionInfo = Tuple[int, int, int]
NetlocTuple = Tuple[str, Tuple[Optional[str], Optional[str]]]


def get_pip_version():
    # type: () -> str
    pip_pkg_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    pip_pkg_dir = os.path.abspath(pip_pkg_dir)

    return "pip {} from {} (python {})".format(
        __version__,
        pip_pkg_dir,
        get_major_minor_version(),
    )


def normalize_version_info(py_version_info):
    # type: (Tuple[int, ...]) -> Tuple[int, int, int]
    """
    Convert a tuple of ints representing a Python version to one of length
    three.

    :param py_version_info: a tuple of ints representing a Python version,
        or None to specify no version. The tuple can have any length.

    :return: a tuple of length three if `py_version_info` is non-None.
        Otherwise, return `py_version_info` unchanged (i.e. None).
    """
    if len(py_version_info) < 3:
        py_version_info += (3 - len(py_version_info)) * (0,)
    elif len(py_version_info) > 3:
        py_version_info = py_version_info[:3]

    return cast("VersionInfo", py_version_info)


def ensure_dir(path):
    # type: (AnyStr) -> None
    """os.path.makedirs without EEXIST."""
    try:
        os.makedirs(path)
    except OSError as e:
        # Windows can raise spurious ENOTEMPTY errors. See #6426.
        if e.errno != errno.EEXIST and e.errno != errno.ENOTEMPTY:
            raise


def get_prog():
    # type: () -> str
    try:
        prog = os.path.basename(sys.argv[0])
        if prog in ("__main__.py", "-c"):
            return f"{sys.executable} -m pip"
        else:
            return prog
    except (AttributeError, TypeError, IndexError):
        pass
    return "pip"


# Retry every half second for up to 3 seconds
# Tenacity raises RetryError by default, explictly raise the original exception
@retry(reraise=True, stop=stop_after_delay(3), wait=wait_fixed(0.5))
def rmtree(dir, ignore_errors=False):
    # type: (AnyStr, bool) -> None
    shutil.rmtree(dir, ignore_errors=ignore_errors, onerror=rmtree_errorhandler)


def rmtree_errorhandler(func, path, exc_info):
    # type: (Callable[..., Any], str, ExcInfo) -> None
    """On Windows, the files in .svn are read-only, so when rmtree() tries to
    remove them, an exception is thrown.  We catch that here, remove the
    read-only attribute, and hopefully continue without problems."""
    try:
        has_attr_readonly = not (os.stat(path).st_mode & stat.S_IWRITE)
    except OSError:
        # it's equivalent to os.path.exists
        return

    if has_attr_readonly:
        # convert to read/write
        os.chmod(path, stat.S_IWRITE)
        # use the original function to repeat the operation
        func(path)
        return
    else:
        raise


def display_path(path):
    # type: (str) -> str
    """Gives the display value for a given path, making it relative to cwd
    if possible."""
    path = os.path.normcase(os.path.abspath(path))
    if path.startswith(os.getcwd() + os.path.sep):
        path = "." + path[len(os.getcwd()) :]
    return path


def backup_dir(dir, ext=".bak"):
    # type: (str, str) -> str
    """Figure out the name of a directory to back up the given dir to
    (adding .bak, .bak2, etc)"""
    n = 1
    extension = ext
    while os.path.exists(dir + extension):
        n += 1
        extension = ext + str(n)
    return dir + extension


def ask_path_exists(message, options):
    # type: (str, Iterable[str]) -> str
    for action in os.environ.get("PIP_EXISTS_ACTION", "").split():
        if action in options:
            return action
    return ask(message, options)


def _check_no_input(message):
    # type: (str) -> None
    """Raise an error if no input is allowed."""
    if os.environ.get("PIP_NO_INPUT"):
        raise Exception(
            f"No input was expected ($PIP_NO_INPUT set); question: {message}"
        )


def ask(message, options):
    # type: (str, Iterable[str]) -> str
    """Ask the message interactively, with the given possible responses"""
    while 1:
        _check_no_input(message)
        response = input(message)
        response = response.strip().lower()
        if response not in options:
            print(
                "Your response ({!r}) was not one of the expected responses: "
                "{}".format(response, ", ".join(options))
            )
        else:
            return response


def ask_input(message):
    # type: (str) -> str
    """Ask for input interactively."""
    _check_no_input(message)
    return input(message)


def ask_password(message):
    # type: (str) -> str
    """Ask for a password interactively."""
    _check_no_input(message)
    return getpass.getpass(message)


def strtobool(val):
    # type: (str) -> int
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1
    elif val in ("n", "no", "f", "false", "off", "0"):
        return 0
    else:
        raise ValueError(f"invalid truth value {val!r}")


def format_size(bytes):
    # type: (float) -> str
    if bytes > 1000 * 1000:
        return "{:.1f} MB".format(bytes / 1000.0 / 1000)
    elif bytes > 10 * 1000:
        return "{} kB".format(int(bytes / 1000))
    elif bytes > 1000:
        return "{:.1f} kB".format(bytes / 1000.0)
    else:
        return "{} bytes".format(int(bytes))


def tabulate(rows):
    # type: (Iterable[Iterable[Any]]) -> Tuple[List[str], List[int]]
    """Return a list of formatted rows and a list of column sizes.

    For example::

    >>> tabulate([['foobar', 2000], [0xdeadbeef]])
    (['foobar     2000', '3735928559'], [10, 4])
    """
    rows = [tuple(map(str, row)) for row in rows]
    sizes = [max(map(len, col)) for col in zip_longest(*rows, fillvalue="")]
    table = [" ".join(map(str.ljust, row, sizes)).rstrip() for row in rows]
    return table, sizes


def is_installable_dir(path):
    # type: (str) -> bool
    """Is path is a directory containing setup.py or pyproject.toml?"""
    if not os.path.isdir(path):
        return False
    setup_py = os.path.join(path, "setup.py")
    if os.path.isfile(setup_py):
        return True
    pyproject_toml = os.path.join(path, "pyproject.toml")
    if os.path.isfile(pyproject_toml):
        return True
    return False


def read_chunks(file, size=io.DEFAULT_BUFFER_SIZE):
    # type: (BinaryIO, int) -> Iterator[bytes]
    """Yield pieces of data from a file-like object until EOF."""
    while True:
        chunk = file.read(size)
        if not chunk:
            break
        yield chunk


def normalize_path(path, resolve_symlinks=True):
    # type: (str, bool) -> str
    """
    Convert a path to its canonical, case-normalized, absolute version.

    """
    path = os.path.expanduser(path)
    if resolve_symlinks:
        path = os.path.realpath(path)
    else:
        path = os.path.abspath(path)
    return os.path.normcase(path)


def splitext(path):
    # type: (str) -> Tuple[str, str]
    """Like os.path.splitext, but take off .tar too"""
    base, ext = posixpath.splitext(path)
    if base.lower().endswith(".tar"):
        ext = base[-4:] + ext
        base = base[:-4]
    return base, ext


def renames(old, new):
    # type: (str, str) -> None
    """Like os.renames(), but handles renaming across devices."""
    # Implementation borrowed from os.renames().
    head, tail = os.path.split(new)
    if head and tail and not os.path.exists(head):
        os.makedirs(head)

    shutil.move(old, new)

    head, tail = os.path.split(old)
    if head and tail:
        try:
            os.removedirs(head)
        except OSError:
            pass


def is_local(path):
    # type: (str) -> bool
    """
    Return True if path is within sys.prefix, if we're running in a virtualenv.

    If we're not in a virtualenv, all paths are considered "local."

    Caution: this function assumes the head of path has been normalized
    with normalize_path.
    """
    if not running_under_virtualenv():
        return True
    return path.startswith(normalize_path(sys.prefix))


def dist_is_local(dist):
    # type: (Distribution) -> bool
    """
    Return True if given Distribution object is installed locally
    (i.e. within current virtualenv).

    Always True if we're not in a virtualenv.

    """
    return is_local(dist_location(dist))


def dist_in_usersite(dist):
    # type: (Distribution) -> bool
    """
    Return True if given Distribution is installed in user site.
    """
    return dist_location(dist).startswith(normalize_path(user_site))


def dist_in_site_packages(dist):
    # type: (Distribution) -> bool
    """
    Return True if given Distribution is installed in
    sysconfig.get_python_lib().
    """
    return dist_location(dist).startswith(normalize_path(site_packages))


def dist_is_editable(dist):
    # type: (Distribution) -> bool
    """
    Return True if given Distribution is an editable install.
    """
    for path_item in sys.path:
        egg_link = os.path.join(path_item, dist.project_name + ".egg-link")
        if os.path.isfile(egg_link):
            return True
    return False


def get_installed_distributions(
    local_only=True,  # type: bool
    skip=stdlib_pkgs,  # type: Container[str]
    include_editables=True,  # type: bool
    editables_only=False,  # type: bool
    user_only=False,  # type: bool
    paths=None,  # type: Optional[List[str]]
):
    # type: (...) -> List[Distribution]
    """Return a list of installed Distribution objects.

    Left for compatibility until direct pkg_resources uses are refactored out.
    """
    from pip._internal.metadata import get_default_environment, get_environment
    from pip._internal.metadata.pkg_resources import Distribution as _Dist

    if paths is None:
        env = get_default_environment()
    else:
        env = get_environment(paths)
    dists = env.iter_installed_distributions(
        local_only=local_only,
        skip=skip,
        include_editables=include_editables,
        editables_only=editables_only,
        user_only=user_only,
    )
    return [cast(_Dist, dist)._dist for dist in dists]


def get_distribution(req_name):
    # type: (str) -> Optional[Distribution]
    """Given a requirement name, return the installed Distribution object.

    This searches from *all* distributions available in the environment, to
    match the behavior of ``pkg_resources.get_distribution()``.

    Left for compatibility until direct pkg_resources uses are refactored out.
    """
    from pip._internal.metadata import get_default_environment
    from pip._internal.metadata.pkg_resources import Distribution as _Dist

    dist = get_default_environment().get_distribution(req_name)
    if dist is None:
        return None
    return cast(_Dist, dist)._dist


def egg_link_path(dist):
    # type: (Distribution) -> Optional[str]
    """
    Return the path for the .egg-link file if it exists, otherwise, None.

    There's 3 scenarios:
    1) not in a virtualenv
       try to find in site.USER_SITE, then site_packages
    2) in a no-global virtualenv
       try to find in site_packages
    3) in a yes-global virtualenv
       try to find in site_packages, then site.USER_SITE
       (don't look in global location)

    For #1 and #3, there could be odd cases, where there's an egg-link in 2
    locations.

    This method will just return the first one found.
    """
    sites = []
    if running_under_virtualenv():
        sites.append(site_packages)
        if not virtualenv_no_global() and user_site:
            sites.append(user_site)
    else:
        if user_site:
            sites.append(user_site)
        sites.append(site_packages)

    for site in sites:
        egglink = os.path.join(site, dist.project_name) + ".egg-link"
        if os.path.isfile(egglink):
            return egglink
    return None


def dist_location(dist):
    # type: (Distribution) -> str
    """
    Get the site-packages location of this distribution. Generally
    this is dist.location, except in the case of develop-installed
    packages, where dist.location is the source code location, and we
    want to know where the egg-link file is.

    The returned location is normalized (in particular, with symlinks removed).
    """
    egg_link = egg_link_path(dist)
    if egg_link:
        return normalize_path(egg_link)
    return normalize_path(dist.location)


def write_output(msg, *args):
    # type: (Any, Any) -> None
    logger.info(msg, *args)


class StreamWrapper(StringIO):
    orig_stream = None  # type: TextIO

    @classmethod
    def from_stream(cls, orig_stream):
        # type: (TextIO) -> StreamWrapper
        cls.orig_stream = orig_stream
        return cls()

    # compileall.compile_dir() needs stdout.encoding to print to stdout
    # https://github.com/python/mypy/issues/4125
    @property
    def encoding(self):  # type: ignore
        return self.orig_stream.encoding


@contextlib.contextmanager
def captured_output(stream_name):
    # type: (str) -> Iterator[StreamWrapper]
    """Return a context manager used by captured_stdout/stdin/stderr
    that temporarily replaces the sys stream *stream_name* with a StringIO.

    Taken from Lib/support/__init__.py in the CPython repo.
    """
    orig_stdout = getattr(sys, stream_name)
    setattr(sys, stream_name, StreamWrapper.from_stream(orig_stdout))
    try:
        yield getattr(sys, stream_name)
    finally:
        setattr(sys, stream_name, orig_stdout)


def captured_stdout():
    # type: () -> ContextManager[StreamWrapper]
    """Capture the output of sys.stdout:

       with captured_stdout() as stdout:
           print('hello')
       self.assertEqual(stdout.getvalue(), 'hello\n')

    Taken from Lib/support/__init__.py in the CPython repo.
    """
    return captured_output("stdout")


def captured_stderr():
    # type: () -> ContextManager[StreamWrapper]
    """
    See captured_stdout().
    """
    return captured_output("stderr")


# Simulates an enum
def enum(*sequential, **named):
    # type: (*Any, **Any) -> Type[Any]
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = {value: key for key, value in enums.items()}
    enums["reverse_mapping"] = reverse
    return type("Enum", (), enums)


def build_netloc(host, port):
    # type: (str, Optional[int]) -> str
    """
    Build a netloc from a host-port pair
    """
    if port is None:
        return host
    if ":" in host:
        # Only wrap host with square brackets when it is IPv6
        host = f"[{host}]"
    return f"{host}:{port}"


def build_url_from_netloc(netloc, scheme="https"):
    # type: (str, str) -> str
    """
    Build a full URL from a netloc.
    """
    if netloc.count(":") >= 2 and "@" not in netloc and "[" not in netloc:
        # It must be a bare IPv6 address, so wrap it with brackets.
        netloc = f"[{netloc}]"
    return f"{scheme}://{netloc}"


def parse_netloc(netloc):
    # type: (str) -> Tuple[str, Optional[int]]
    """
    Return the host-port pair from a netloc.
    """
    url = build_url_from_netloc(netloc)
    parsed = urllib.parse.urlparse(url)
    return parsed.hostname, parsed.port


def split_auth_from_netloc(netloc):
    # type: (str) -> NetlocTuple
    """
    Parse out and remove the auth information from a netloc.

    Returns: (netloc, (username, password)).
    """
    if "@" not in netloc:
        return netloc, (None, None)

    # Split from the right because that's how urllib.parse.urlsplit()
    # behaves if more than one @ is present (which can be checked using
    # the password attribute of urlsplit()'s return value).
    auth, netloc = netloc.rsplit("@", 1)
    pw = None  # type: Optional[str]
    if ":" in auth:
        # Split from the left because that's how urllib.parse.urlsplit()
        # behaves if more than one : is present (which again can be checked
        # using the password attribute of the return value)
        user, pw = auth.split(":", 1)
    else:
        user, pw = auth, None

    user = urllib.parse.unquote(user)
    if pw is not None:
        pw = urllib.parse.unquote(pw)

    return netloc, (user, pw)


def redact_netloc(netloc):
    # type: (str) -> str
    """
    Replace the sensitive data in a netloc with "****", if it exists.

    For example:
        - "user:pass@example.com" returns "user:****@example.com"
        - "accesstoken@example.com" returns "****@example.com"
    """
    netloc, (user, password) = split_auth_from_netloc(netloc)
    if user is None:
        return netloc
    if password is None:
        user = "****"
        password = ""
    else:
        user = urllib.parse.quote(user)
        password = ":****"
    return "{user}{password}@{netloc}".format(
        user=user, password=password, netloc=netloc
    )


def _transform_url(url, transform_netloc):
    # type: (str, Callable[[str], Tuple[Any, ...]]) -> Tuple[str, NetlocTuple]
    """Transform and replace netloc in a url.

    transform_netloc is a function taking the netloc and returning a
    tuple. The first element of this tuple is the new netloc. The
    entire tuple is returned.

    Returns a tuple containing the transformed url as item 0 and the
    original tuple returned by transform_netloc as item 1.
    """
    purl = urllib.parse.urlsplit(url)
    netloc_tuple = transform_netloc(purl.netloc)
    # stripped url
    url_pieces = (purl.scheme, netloc_tuple[0], purl.path, purl.query, purl.fragment)
    surl = urllib.parse.urlunsplit(url_pieces)
    return surl, cast("NetlocTuple", netloc_tuple)


def _get_netloc(netloc):
    # type: (str) -> NetlocTuple
    return split_auth_from_netloc(netloc)


def _redact_netloc(netloc):
    # type: (str) -> Tuple[str,]
    return (redact_netloc(netloc),)


def split_auth_netloc_from_url(url):
    # type: (str) -> Tuple[str, str, Tuple[str, str]]
    """
    Parse a url into separate netloc, auth, and url with no auth.

    Returns: (url_without_auth, netloc, (username, password))
    """
    url_without_auth, (netloc, auth) = _transform_url(url, _get_netloc)
    return url_without_auth, netloc, auth


def remove_auth_from_url(url):
    # type: (str) -> str
    """Return a copy of url with 'username:password@' removed."""
    # username/pass params are passed to subversion through flags
    # and are not recognized in the url.
    return _transform_url(url, _get_netloc)[0]


def redact_auth_from_url(url):
    # type: (str) -> str
    """Replace the password in a given url with ****."""
    return _transform_url(url, _redact_netloc)[0]


class HiddenText:
    def __init__(
        self,
        secret,  # type: str
        redacted,  # type: str
    ):
        # type: (...) -> None
        self.secret = secret
        self.redacted = redacted

    def __repr__(self):
        # type: (...) -> str
        return "<HiddenText {!r}>".format(str(self))

    def __str__(self):
        # type: (...) -> str
        return self.redacted

    # This is useful for testing.
    def __eq__(self, other):
        # type: (Any) -> bool
        if type(self) != type(other):
            return False

        # The string being used for redaction doesn't also have to match,
        # just the raw, original string.
        return self.secret == other.secret


def hide_value(value):
    # type: (str) -> HiddenText
    return HiddenText(value, redacted="****")


def hide_url(url):
    # type: (str) -> HiddenText
    redacted = redact_auth_from_url(url)
    return HiddenText(url, redacted=redacted)


def protect_pip_from_modification_on_windows(modifying_pip):
    # type: (bool) -> None
    """Protection of pip.exe from modification on Windows

    On Windows, any operation modifying pip should be run as:
        python -m pip ...
    """
    pip_names = [
        "pip.exe",
        "pip{}.exe".format(sys.version_info[0]),
        "pip{}.{}.exe".format(*sys.version_info[:2]),
    ]

    # See https://github.com/pypa/pip/issues/1299 for more discussion
    should_show_use_python_msg = (
        modifying_pip and WINDOWS and os.path.basename(sys.argv[0]) in pip_names
    )

    if should_show_use_python_msg:
        new_command = [sys.executable, "-m", "pip"] + sys.argv[1:]
        raise CommandError(
            "To modify pip, please run the following command:\n{}".format(
                " ".join(new_command)
            )
        )


def is_console_interactive():
    # type: () -> bool
    """Is this console interactive?"""
    return sys.stdin is not None and sys.stdin.isatty()


def hash_file(path, blocksize=1 << 20):
    # type: (str, int) -> Tuple[Any, int]
    """Return (hash, length) for path using hashlib.sha256()"""

    h = hashlib.sha256()
    length = 0
    with open(path, "rb") as f:
        for block in read_chunks(f, size=blocksize):
            length += len(block)
            h.update(block)
    return h, length


def is_wheel_installed():
    # type: () -> bool
    """
    Return whether the wheel package is installed.
    """
    try:
        import wheel  # noqa: F401
    except ImportError:
        return False

    return True


def pairwise(iterable):
    # type: (Iterable[Any]) -> Iterator[Tuple[Any, Any]]
    """
    Return paired elements.

    For example:
        s -> (s0, s1), (s2, s3), (s4, s5), ...
    """
    iterable = iter(iterable)
    return zip_longest(iterable, iterable)


def partition(
    pred,  # type: Callable[[T], bool]
    iterable,  # type: Iterable[T]
):
    # type: (...) -> Tuple[Iterable[T], Iterable[T]]
    """
    Use a predicate to partition entries into false entries and true entries,
    like

        partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    """
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)
