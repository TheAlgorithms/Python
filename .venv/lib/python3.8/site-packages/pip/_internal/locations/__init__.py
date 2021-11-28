import logging
import pathlib
import sys
import sysconfig
from typing import List, Optional

from pip._internal.models.scheme import SCHEME_KEYS, Scheme

from . import _distutils, _sysconfig
from .base import (
    USER_CACHE_DIR,
    get_major_minor_version,
    get_src_prefix,
    site_packages,
    user_site,
)

__all__ = [
    "USER_CACHE_DIR",
    "get_bin_prefix",
    "get_bin_user",
    "get_major_minor_version",
    "get_platlib",
    "get_prefixed_libs",
    "get_purelib",
    "get_scheme",
    "get_src_prefix",
    "site_packages",
    "user_site",
]


logger = logging.getLogger(__name__)


def _default_base(*, user: bool) -> str:
    if user:
        base = sysconfig.get_config_var("userbase")
    else:
        base = sysconfig.get_config_var("base")
    assert base is not None
    return base


def _warn_if_mismatch(old: pathlib.Path, new: pathlib.Path, *, key: str) -> bool:
    if old == new:
        return False
    issue_url = "https://github.com/pypa/pip/issues/9617"
    message = (
        "Value for %s does not match. Please report this to <%s>"
        "\ndistutils: %s"
        "\nsysconfig: %s"
    )
    logger.debug(message, key, issue_url, old, new)
    return True


def _log_context(
    *,
    user: bool = False,
    home: Optional[str] = None,
    root: Optional[str] = None,
    prefix: Optional[str] = None,
) -> None:
    message = (
        "Additional context:" "\nuser = %r" "\nhome = %r" "\nroot = %r" "\nprefix = %r"
    )
    logger.debug(message, user, home, root, prefix)


def get_scheme(
    dist_name,  # type: str
    user=False,  # type: bool
    home=None,  # type: Optional[str]
    root=None,  # type: Optional[str]
    isolated=False,  # type: bool
    prefix=None,  # type: Optional[str]
):
    # type: (...) -> Scheme
    old = _distutils.get_scheme(
        dist_name,
        user=user,
        home=home,
        root=root,
        isolated=isolated,
        prefix=prefix,
    )
    new = _sysconfig.get_scheme(
        dist_name,
        user=user,
        home=home,
        root=root,
        isolated=isolated,
        prefix=prefix,
    )

    base = prefix or home or _default_base(user=user)
    warned = []
    for k in SCHEME_KEYS:
        # Extra join because distutils can return relative paths.
        old_v = pathlib.Path(base, getattr(old, k))
        new_v = pathlib.Path(getattr(new, k))

        # distutils incorrectly put PyPy packages under ``site-packages/python``
        # in the ``posix_home`` scheme, but PyPy devs said they expect the
        # directory name to be ``pypy`` instead. So we treat this as a bug fix
        # and not warn about it. See bpo-43307 and python/cpython#24628.
        skip_pypy_special_case = (
            sys.implementation.name == "pypy"
            and home is not None
            and k in ("platlib", "purelib")
            and old_v.parent == new_v.parent
            and old_v.name == "python"
            and new_v.name == "pypy"
        )
        if skip_pypy_special_case:
            continue

        warned.append(_warn_if_mismatch(old_v, new_v, key=f"scheme.{k}"))

    if any(warned):
        _log_context(user=user, home=home, root=root, prefix=prefix)

    return old


def get_bin_prefix():
    # type: () -> str
    old = _distutils.get_bin_prefix()
    new = _sysconfig.get_bin_prefix()
    if _warn_if_mismatch(pathlib.Path(old), pathlib.Path(new), key="bin_prefix"):
        _log_context()
    return old


def get_bin_user():
    # type: () -> str
    return _sysconfig.get_scheme("", user=True).scripts


def get_purelib():
    # type: () -> str
    """Return the default pure-Python lib location."""
    old = _distutils.get_purelib()
    new = _sysconfig.get_purelib()
    if _warn_if_mismatch(pathlib.Path(old), pathlib.Path(new), key="purelib"):
        _log_context()
    return old


def get_platlib():
    # type: () -> str
    """Return the default platform-shared lib location."""
    old = _distutils.get_platlib()
    new = _sysconfig.get_platlib()
    if _warn_if_mismatch(pathlib.Path(old), pathlib.Path(new), key="platlib"):
        _log_context()
    return old


def get_prefixed_libs(prefix):
    # type: (str) -> List[str]
    """Return the lib locations under ``prefix``."""
    old_pure, old_plat = _distutils.get_prefixed_libs(prefix)
    new_pure, new_plat = _sysconfig.get_prefixed_libs(prefix)

    warned = [
        _warn_if_mismatch(
            pathlib.Path(old_pure),
            pathlib.Path(new_pure),
            key="prefixed-purelib",
        ),
        _warn_if_mismatch(
            pathlib.Path(old_plat),
            pathlib.Path(new_plat),
            key="prefixed-platlib",
        ),
    ]
    if any(warned):
        _log_context(prefix=prefix)

    if old_pure == old_plat:
        return [old_pure]
    return [old_pure, old_plat]
