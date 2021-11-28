from __future__ import absolute_import, division, unicode_literals
from pip._vendor.six import text_type

from bisect import bisect_left

from ._base import Trie as ABCTrie


class Trie(ABCTrie):
    def __init__(self, data):
        if not all(isinstance(x, text_type) for x in data.keys()):
            raise TypeError("All keys must be strings")

        self._data = data
        self._keys = sorted(data.keys())
        self._cachestr = ""
        self._cachepoints = (0, len(data))

    def __contains__(self, key):
        return key in self._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def keys(self, prefix=None):
        if prefix is None or prefix == "" or not self._keys:
            return set(self._keys)

        if prefix.startswith(self._cachestr):
            lo, hi = self._cachepoints
            start = i = bisect_left(self._keys, prefix, lo, hi)
        else:
            start = i = bisect_left(self._keys, prefix)

        keys = set()
        if start == len(self._keys):
            return keys

        while self._keys[i].startswith(prefix):
            keys.add(self._keys[i])
            i += 1

        self._cachestr = prefix
        self._cachepoints = (start, i)

        return keys

    def has_keys_with_prefix(self, prefix):
        if prefix in self._data:
            return True

        if prefix.startswith(self._cachestr):
            lo, hi = self._cachepoints
            i = bisect_left(self._keys, prefix, lo, hi)
        else:
            i = bisect_left(self._keys, prefix)

        if i == len(self._keys):
            return False

        return self._keys[i].startswith(prefix)
