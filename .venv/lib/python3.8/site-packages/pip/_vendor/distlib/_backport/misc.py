# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 The Python Software Foundation.
# See LICENSE.txt and CONTRIBUTORS.txt.
#
"""Backports for individual classes and functions."""

import os
import sys

__all__ = ['cache_from_source', 'callable', 'fsencode']


try:
    from imp import cache_from_source
except ImportError:
    def cache_from_source(py_file, debug=__debug__):
        ext = debug and 'c' or 'o'
        return py_file + ext


try:
    callable = callable
except NameError:
    from collections import Callable

    def callable(obj):
        return isinstance(obj, Callable)


try:
    fsencode = os.fsencode
except AttributeError:
    def fsencode(filename):
        if isinstance(filename, bytes):
            return filename
        elif isinstance(filename, str):
            return filename.encode(sys.getfilesystemencoding())
        else:
            raise TypeError("expect bytes or str, not %s" %
                            type(filename).__name__)
