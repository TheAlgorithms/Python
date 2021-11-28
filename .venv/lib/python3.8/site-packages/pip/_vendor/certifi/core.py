# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem or its contents.
"""
import os


class _PipPatchedCertificate(Exception):
    pass


try:
    # Return a certificate file on disk for a standalone pip zipapp running in
    # an isolated build environment to use. Passing --cert to the standalone
    # pip does not work since requests calls where() unconditionally on import.
    _PIP_STANDALONE_CERT = os.environ.get("_PIP_STANDALONE_CERT")
    if _PIP_STANDALONE_CERT:
        def where():
            return _PIP_STANDALONE_CERT
        raise _PipPatchedCertificate()

    from importlib.resources import path as get_path, read_text

    _CACERT_CTX = None
    _CACERT_PATH = None

    def where():
        # This is slightly terrible, but we want to delay extracting the file
        # in cases where we're inside of a zipimport situation until someone
        # actually calls where(), but we don't want to re-extract the file
        # on every call of where(), so we'll do it once then store it in a
        # global variable.
        global _CACERT_CTX
        global _CACERT_PATH
        if _CACERT_PATH is None:
            # This is slightly janky, the importlib.resources API wants you to
            # manage the cleanup of this file, so it doesn't actually return a
            # path, it returns a context manager that will give you the path
            # when you enter it and will do any cleanup when you leave it. In
            # the common case of not needing a temporary file, it will just
            # return the file system location and the __exit__() is a no-op.
            #
            # We also have to hold onto the actual context manager, because
            # it will do the cleanup whenever it gets garbage collected, so
            # we will also store that at the global level as well.
            _CACERT_CTX = get_path("pip._vendor.certifi", "cacert.pem")
            _CACERT_PATH = str(_CACERT_CTX.__enter__())

        return _CACERT_PATH

except _PipPatchedCertificate:
    pass

except ImportError:
    # This fallback will work for Python versions prior to 3.7 that lack the
    # importlib.resources module but relies on the existing `where` function
    # so won't address issues with environments like PyOxidizer that don't set
    # __file__ on modules.
    def read_text(_module, _path, encoding="ascii"):
        with open(where(), "r", encoding=encoding) as data:
            return data.read()

    # If we don't have importlib.resources, then we will just do the old logic
    # of assuming we're on the filesystem and munge the path directly.
    def where():
        f = os.path.dirname(__file__)

        return os.path.join(f, "cacert.pem")


def contents():
    return read_text("certifi", "cacert.pem", encoding="ascii")
