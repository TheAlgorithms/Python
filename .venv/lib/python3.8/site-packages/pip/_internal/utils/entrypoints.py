import sys
from typing import List, Optional

from pip._internal.cli.main import main


def _wrapper(args=None):
    # type: (Optional[List[str]]) -> int
    """Central wrapper for all old entrypoints.

    Historically pip has had several entrypoints defined. Because of issues
    arising from PATH, sys.path, multiple Pythons, their interactions, and most
    of them having a pip installed, users suffer every time an entrypoint gets
    moved.

    To alleviate this pain, and provide a mechanism for warning users and
    directing them to an appropriate place for help, we now define all of
    our old entrypoints as wrappers for the current one.
    """
    sys.stderr.write(
        "WARNING: pip is being invoked by an old script wrapper. This will "
        "fail in a future version of pip.\n"
        "Please see https://github.com/pypa/pip/issues/5599 for advice on "
        "fixing the underlying issue.\n"
        "To avoid this problem you can invoke Python with '-m pip' instead of "
        "running pip directly.\n"
    )
    return main(args)
