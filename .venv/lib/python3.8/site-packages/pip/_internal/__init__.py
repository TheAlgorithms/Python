from typing import List, Optional

import pip._internal.utils.inject_securetransport  # noqa


def main(args=None):
    # type: (Optional[List[str]]) -> int
    """This is preserved for old console scripts that may still be referencing
    it.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    """
    from pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)
