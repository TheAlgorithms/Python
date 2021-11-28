"""Utilities for providing backward compatibility."""
from pip._vendor import six


def get_exc_info_from_future(future):
    """
    Get an exc_info value from a Future.

    Given a a Future instance, retrieve an exc_info value suitable for passing
    in as the exc_info parameter to logging.Logger.log() and related methods.

    On Python 2, this will be a (type, value, traceback) triple.
    On Python 3, this will be an exception instance (with embedded traceback).

    If there was no exception, None is returned on both versions of Python.
    """
    if six.PY3:
        return future.exception()
    else:
        ex, tb = future.exception_info()
        if ex is None:
            return None
        return type(ex), ex, tb
