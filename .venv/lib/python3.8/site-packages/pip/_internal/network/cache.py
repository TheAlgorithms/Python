"""HTTP cache implementation.
"""

import os
from contextlib import contextmanager
from typing import Iterator, Optional

from pip._vendor.cachecontrol.cache import BaseCache
from pip._vendor.cachecontrol.caches import FileCache
from pip._vendor.requests.models import Response

from pip._internal.utils.filesystem import adjacent_tmp_file, replace
from pip._internal.utils.misc import ensure_dir


def is_from_cache(response):
    # type: (Response) -> bool
    return getattr(response, "from_cache", False)


@contextmanager
def suppressed_cache_errors():
    # type: () -> Iterator[None]
    """If we can't access the cache then we can just skip caching and process
    requests as if caching wasn't enabled.
    """
    try:
        yield
    except OSError:
        pass


class SafeFileCache(BaseCache):
    """
    A file based cache which is safe to use even when the target directory may
    not be accessible or writable.
    """

    def __init__(self, directory):
        # type: (str) -> None
        assert directory is not None, "Cache directory must not be None."
        super().__init__()
        self.directory = directory

    def _get_cache_path(self, name):
        # type: (str) -> str
        # From cachecontrol.caches.file_cache.FileCache._fn, brought into our
        # class for backwards-compatibility and to avoid using a non-public
        # method.
        hashed = FileCache.encode(name)
        parts = list(hashed[:5]) + [hashed]
        return os.path.join(self.directory, *parts)

    def get(self, key):
        # type: (str) -> Optional[bytes]
        path = self._get_cache_path(key)
        with suppressed_cache_errors():
            with open(path, 'rb') as f:
                return f.read()

    def set(self, key, value):
        # type: (str, bytes) -> None
        path = self._get_cache_path(key)
        with suppressed_cache_errors():
            ensure_dir(os.path.dirname(path))

            with adjacent_tmp_file(path) as f:
                f.write(value)

            replace(f.name, path)

    def delete(self, key):
        # type: (str) -> None
        path = self._get_cache_path(key)
        with suppressed_cache_errors():
            os.remove(path)
