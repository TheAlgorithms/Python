#!/usr/bin/env python3
"""
Power-of-two sized hash map (mask-based indexing).

Power-of-two tables often use a bitmask instead of modulo, but should mix the hash
so low bits are usable.

Reference (hash table sizing / open addressing context):
https://en.wikipedia.org/wiki/Hash_table
"""

from __future__ import annotations

from collections.abc import Iterator, MutableMapping
from dataclasses import dataclass
from typing import Generic, TypeVar

KEY = TypeVar("KEY")
VAL = TypeVar("VAL")


def _next_power_of_two(number: int) -> int:
    if number < 1:
        raise ValueError("number must be >= 1")
    return 1 << (number - 1).bit_length()


def _mix_hash(hash_value: int) -> int:
    # Simple avalanching to make low bits more useful.
    hash_value ^= hash_value >> 16
    hash_value *= 0x85EBCA6B
    hash_value &= 0xFFFFFFFFFFFFFFFF
    hash_value ^= hash_value >> 13
    hash_value *= 0xC2B2AE35
    hash_value &= 0xFFFFFFFFFFFFFFFF
    hash_value ^= hash_value >> 16
    return hash_value


@dataclass(slots=True)
class _Item(Generic[KEY, VAL]):  # noqa: UP046
    key: KEY
    val: VAL


class _DeletedItem(_Item):
    def __init__(self) -> None:
        super().__init__(None, None)

    def __bool__(self) -> bool:
        return False


_deleted = _DeletedItem()


class PowerOfTwoHashMap(MutableMapping[KEY, VAL]):
    """
    Open addressing with a power-of-two bucket count.

    >>> hm = PowerOfTwoHashMap(8)
    >>> hm["a"] = 1
    >>> hm["b"] = 2
    >>> hm["a"]
    1
    >>> len(hm)
    2
    >>> del hm["a"]
    >>> "a" in hm
    False
    """

    def __init__(
        self, initial_capacity: int = 8, capacity_factor: float = 0.75
    ) -> None:
        if not (0.0 < capacity_factor < 1.0):
            raise ValueError("capacity_factor must be between 0 and 1")
        cap = _next_power_of_two(max(1, initial_capacity))
        self._initial_capacity = cap
        self._buckets: list[_Item | None] = [None] * cap
        self._capacity_factor = capacity_factor
        self._len = 0

    def _mask(self) -> int:
        return len(self._buckets) - 1

    def _index(self, key: KEY) -> int:
        return _mix_hash(hash(key)) & self._mask()

    def _iterate(self, key: KEY) -> Iterator[int]:
        ind = self._index(key)
        for _ in range(len(self._buckets)):
            yield ind
            ind = (ind + 1) & self._mask()

    def _is_full(self) -> bool:
        return self._len >= int(len(self._buckets) * self._capacity_factor)

    def _resize(self, new_capacity: int) -> None:
        new_capacity = _next_power_of_two(new_capacity)
        old = self._buckets
        self._buckets = [None] * new_capacity
        self._len = 0
        for item in old:
            if item:
                self[item.key] = item.val

    def __setitem__(self, key: KEY, val: VAL) -> None:
        if self._is_full():
            self._resize(len(self._buckets) * 2)

        for ind in self._iterate(key):
            item = self._buckets[ind]
            if not item:
                self._buckets[ind] = _Item(key, val)
                self._len += 1
                return
            if item.key == key:
                item.val = val
                return

        self._resize(len(self._buckets) * 2)
        self[key] = val

    def __getitem__(self, key: KEY) -> VAL:
        for ind in self._iterate(key):
            item = self._buckets[ind]
            if item is None:
                break
            if item is _deleted:
                continue
            if item.key == key:
                return item.val
        raise KeyError(key)

    def __delitem__(self, key: KEY) -> None:
        for ind in self._iterate(key):
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
