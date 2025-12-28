#!/usr/bin/env python3
"""
FNV-1a hashing + a small educational hash map.

FNV-1a is a fast, non-cryptographic hash often used for hashing bytes/strings.
Reference: https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
"""

from __future__ import annotations

from collections.abc import Iterator, MutableMapping
from dataclasses import dataclass
from typing import TypeVar

KEY = TypeVar("KEY")
VAL = TypeVar("VAL")


def fnv1a_32(data: bytes) -> int:
    """
    Compute 32-bit FNV-1a over bytes.

    >>> fnv1a_32(b"")
    2166136261
    >>> fnv1a_32(b"a")  # deterministic
    3826002220
    """
    h = 0x811C9DC5  # offset basis
    for b in data:
        h ^= b
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h


def fnv1a_64(data: bytes) -> int:
    """
    Compute 64-bit FNV-1a over bytes.

    >>> fnv1a_64(b"")
    14695981039346656037
    """
    h = 0xCBF29CE484222325  # offset basis
    for b in data:
        h ^= b
        h = (h * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
    return h


@dataclass(slots=True)
class _Item[KEY, VAL]:
    key: KEY
    val: VAL


class _DeletedItem(_Item):
    def __init__(self) -> None:
        super().__init__(None, None)

    def __bool__(self) -> bool:
        return False


_deleted = _DeletedItem()


class FNVHashMap(MutableMapping[KEY, VAL]):
    """
    Hash map using FNV-1a for string/bytes keys and Python's hash otherwise.

    >>> hm = FNVHashMap()
    >>> hm["hello"] = 1
    >>> hm[b"hello"] = 2
    >>> hm["hello"]
    1
    >>> hm[b"hello"]
    2
    >>> "missing" in hm
    False
    """

    def __init__(
        self, initial_block_size: int = 8, capacity_factor: float = 0.75
    ) -> None:
        if initial_block_size < 1:
            raise ValueError("initial_block_size must be >= 1")
        if not (0.0 < capacity_factor < 1.0):
            raise ValueError("capacity_factor must be between 0 and 1")

        self._initial_block_size = initial_block_size
        self._buckets: list[_Item | None] = [None] * initial_block_size
        self._capacity_factor = capacity_factor
        self._len = 0

    def _hash_key(self, key: KEY) -> int:
        if isinstance(key, bytes):
            return fnv1a_32(key)
        if isinstance(key, str):
            return fnv1a_32(key.encode("utf-8"))
        return hash(key)

    def _get_bucket_index(self, key: KEY) -> int:
        return self._hash_key(key) % len(self._buckets)

    def _iterate_buckets(self, key: KEY) -> Iterator[int]:
        ind = self._get_bucket_index(key)
        for _ in range(len(self._buckets)):
            yield ind
            ind = (ind + 1) % len(self._buckets)

    def _is_full(self) -> bool:
        return self._len >= int(len(self._buckets) * self._capacity_factor)

    def _resize(self, new_size: int) -> None:
        old = self._buckets
        self._buckets = [None] * new_size
        self._len = 0
        for item in old:
            if item:
                self[item.key] = item.val

    def __setitem__(self, key: KEY, val: VAL) -> None:
        if self._is_full():
            self._resize(len(self._buckets) * 2)

        for ind in self._iterate_buckets(key):
            stored = self._buckets[ind]
            if not stored:
                self._buckets[ind] = _Item(key, val)
                self._len += 1
                return
            if stored.key == key:
                stored.val = val
                return

        # Extremely unlikely due to resize policy, but safe.
        self._resize(len(self._buckets) * 2)
        self[key] = val

    def __getitem__(self, key: KEY) -> VAL:
        for ind in self._iterate_buckets(key):
            item = self._buckets[ind]
            if item is None:
                break
            if item is _deleted:
                continue
            if item.key == key:
                return item.val
        raise KeyError(key)

    def __delitem__(self, key: KEY) -> None:
        for ind in self._iterate_buckets(key):
            item = self._buckets[ind]
            if item is None:
                break
            if item is _deleted:
                continue
            if item.key == key:
                self._buckets[ind] = _deleted
                self._len -= 1
                return
        raise KeyError(key)

    def __iter__(self) -> Iterator[KEY]:
        yield from (item.key for item in self._buckets if item)

    def __len__(self) -> int:
        return self._len

    def __repr__(self) -> str:
        parts = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"FNVHashMap({parts})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
