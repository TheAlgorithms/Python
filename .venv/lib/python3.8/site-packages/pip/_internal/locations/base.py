import os
import site
import sys
import sysconfig
import typing

from pip._internal.utils import appdirs
from pip._internal.utils.virtualenv import running_under_virtualenv

# Application Directories
USER_CACHE_DIR = appdirs.user_cache_dir("pip")

# FIXME doesn't account for venv linked to global site-packages
site_packages = sysconfig.get_path("purelib")  # type: typing.Optional[str]


def get_major_minor_version():
    # type: () -> str
    """
    Return the major-minor version of the current Python as a string, e.g.
    "3.7" or "3.10".
    """
    return "{}.{}".format(*sys.version_info)


def get_src_prefix():
    # type: () -> str
    if running_under_virtualenv():
        src_prefix = os.path.join(sys.prefix, "src")
    else:
        # FIXME: keep src in cwd for now (it is not a temporary folder)
        try:
            src_prefix = os.path.join(os.getcwd(), "src")
        except OSError:
            # In case the current working directory has been renamed or deleted
            sys.exit("The folder you are executing pip from can no longer be found.")

    # under macOS + virtualenv sys.prefix is not properly resolved
    # it is something like /path/to/python/bin/..
    return os.path.abspath(src_prefix)


try:
    # Use getusersitepackages if this is present, as it ensures that the
    # value is initialised properly.
    user_site = site.getusersitepackages()  # type: typing.Optional[str]
except AttributeError:
    user_site = site.USER_SITE
