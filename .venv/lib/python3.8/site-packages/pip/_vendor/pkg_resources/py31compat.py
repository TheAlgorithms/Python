import os
import errno
import sys

from pip._vendor import six


def _makedirs_31(path, exist_ok=False):
    try:
        os.makedirs(path)
    except OSError as exc:
        if not exist_ok or exc.errno != errno.EEXIST:
            raise


# rely on compatibility behavior until mode considerations
#  and exists_ok considerations are disentangled.
# See https://github.com/pypa/setuptools/pull/1083#issuecomment-315168663
needs_makedirs = (
    six.PY2 or
    (3, 4) <= sys.version_info < (3, 4, 1)
)
makedirs = _makedirs_31 if needs_makedirs else os.makedirs
