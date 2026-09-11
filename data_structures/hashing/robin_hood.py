#!/usr/bin/env python3
"""
Robin Hood hashing (open addressing with probe-sequence-length balancing).

Reference: https://en.wikipedia.org/wiki/Hash_table#Robin_Hood_hashing
"""

from __future__ import annotations

from collections.abc import Iterator, MutableMapping
from dataclasses import dataclass
from typing import Generic, TypeVar

KEY = TypeVar("KEY")
VAL = TypeVar("VAL")


@dataclass(slots=True)
class _Entry(Generic[KEY, VAL]):  # noqa: UP046
    key: KEY
    val: VAL
    psl: int  # probe sequence length (distance from home)


class RobinHoodHashMap(MutableMapping[KEY, VAL]):
    """
    Robin Hood hashing reduces variance by swapping when the incoming item has
    a larger probe distance than the resident.

    Deletion uses backward-shift deletion (no tombstones), keeping lookups fast.

    >>> rh = RobinHoodHashMap()
    >>> rh["a"] = 1
    >>> rh["b"] = 2
    >>> rh["a"]
    1
    >>> del rh["a"]
    >>> "a" in rh
    False
    """

    def __init__(self, initial_capacity: int = 8, max_load: float = 0.75) -> None:
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be >= 1")
        if not (0.0 < max_load < 1.0):
            raise ValueError("max_load must be between 0 and 1")

        self._buckets: list[_Entry[KEY, VAL] | None] = [None] * initial_capacity
        self._max_load = max_load
        self._len = 0

    def _home(self, key: KEY) -> int:
        return hash(key) % len(self._buckets)

    def _is_full(self) -> bool:
        return self._len >= int(len(self._buckets) * self._max_load)

    def _resize(self, new_capacity: int) -> None:
        old_items = list(self.items())
        self._buckets = [None] * new_capacity
        self._len = 0
        for k, v in old_items:
            self[k] = v

    def __setitem__(self, key: KEY, val: VAL) -> None:
        if self._is_full():
            self._resize(len(self._buckets) * 2)

        idx = self._home(key)
        entry = _Entry(key, val, 0)

        for _ in range(len(self._buckets)):
            cur = self._buckets[idx]
            if cur is None:
                self._buckets[idx] = entry
                self._len += 1
                return

            if cur.key == key:
                cur.val = val
                return

            # Robin Hood rule: if incoming is "poorer" (larger psl), swap.
            if entry.psl > cur.psl:
                self._buckets[idx], entry = entry, cur

            idx = (idx + 1) % len(self._buckets)
            entry = _Entry(entry.key, entry.val, entry.psl + 1)

        # Safety: should not happen with resizing policy.
        self._resize(len(self._buckets) * 2)
        self[key] = val

    def __getitem__(self, key: KEY) -> VAL:
        idx = self._home(key)
        psl = 0

        for _ in range(len(self._buckets)):
            cur = self._buckets[idx]
            if cur is None:
                break
            # Early exit: if current resident is "richer" than our search distance,
            # the key cannot appear further in the cluster.
            if cur.psl < psl:
                break
            if cur.key == key:
                return cur.val
            idx = (idx + 1) % len(self._buckets)
            psl += 1  # noqa: SIM113

        raise KeyError(key)

    def _delete_at(self, idx: int) -> None:
        # Backward-shift deletion.
        self._buckets[idx] = None
        self._len -= 1

        nxt = (idx + 1) % len(self._buckets)
        while True:
            cur = self._buckets[nxt]
            if cur is None or cur.psl == 0:
                break
            # Shift back by one.
            self._buckets[idx] = _Entry(cur.key, cur.val, cur.psl - 1)
            self._buckets[nxt] = None
            idx = nxt
            nxt = (nxt + 1) % len(self._buckets)

    def __delitem__(self, key: KEY) -> None:
        idx = self._home(key)
        psl = 0

        for _ in range(len(self._buckets)):
            cur = self._buckets[idx]
            if cur is None:
                break
            if cur.psl < psl:
                break
            if cur.key == key:
                self._delete_at(idx)
                return
            idx = (idx + 1) % len(self._buckets)
            psl += 1  # noqa: SIM113

        raise KeyError(key)

    def __iter__(self) -> Iterator[KEY]:
        for item in self._buckets:
            if item is not None:
                yield item.key

    def __len__(self) -> int:
        return self._len


if __name__ == "__main__":
    import doctest

    doctest.testmod()
