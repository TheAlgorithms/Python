from distutils.errors import DistutilsArgError
from distutils.fancy_getopt import FancyGetopt
from typing import Dict, List

_options = [
    ("exec-prefix=", None, ""),
    ("home=", None, ""),
    ("install-base=", None, ""),
    ("install-data=", None, ""),
    ("install-headers=", None, ""),
    ("install-lib=", None, ""),
    ("install-platlib=", None, ""),
    ("install-purelib=", None, ""),
    ("install-scripts=", None, ""),
    ("prefix=", None, ""),
    ("root=", None, ""),
    ("user", None, ""),
]


# typeshed doesn't permit Tuple[str, None, str], see python/typeshed#3469.
_distutils_getopt = FancyGetopt(_options)  # type: ignore


def parse_distutils_args(args):
    # type: (List[str]) -> Dict[str, str]
    """Parse provided arguments, returning an object that has the
    matched arguments.

    Any unknown arguments are ignored.
    """
    result = {}
    for arg in args:
        try:
            _, match = _distutils_getopt.getopt(args=[arg])
        except DistutilsArgError:
            # We don't care about any other options, which here may be
            # considered unrecognized since our option list is not
            # exhaustive.
            pass
        else:
            result.update(match.__dict__)
    return result
