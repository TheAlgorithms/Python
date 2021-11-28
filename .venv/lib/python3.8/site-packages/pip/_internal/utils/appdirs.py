"""
This code wraps the vendored appdirs module to so the return values are
compatible for the current pip code base.

The intention is to rewrite current usages gradually, keeping the tests pass,
and eventually drop this after all usages are changed.
"""

import os
from typing import List

from pip._vendor import appdirs as _appdirs


def user_cache_dir(appname):
    # type: (str) -> str
    return _appdirs.user_cache_dir(appname, appauthor=False)


def user_config_dir(appname, roaming=True):
    # type: (str, bool) -> str
    path = _appdirs.user_config_dir(appname, appauthor=False, roaming=roaming)
    if _appdirs.system == "darwin" and not os.path.isdir(path):
        path = os.path.expanduser("~/.config/")
        if appname:
            path = os.path.join(path, appname)
    return path


# for the discussion regarding site_config_dir locations
# see <https://github.com/pypa/pip/issues/1733>
def site_config_dirs(appname):
    # type: (str) -> List[str]
    dirval = _appdirs.site_config_dir(appname, appauthor=False, multipath=True)
    if _appdirs.system not in ["win32", "darwin"]:
        # always look in /etc directly as well
        return dirval.split(os.pathsep) + ["/etc"]
    return [dirval]
