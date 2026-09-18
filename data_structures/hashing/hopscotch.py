#!/usr/bin/env python3
"""
Hopscotch hashing (open addressing with neighborhood invariants).

Reference: https://en.wikipedia.org/wiki/Hash_table#Hopscotch_hashing

This is an educational, single-threaded implementation.
"""

from __future__ import annotations

from collections.abc import Iterator, MutableMapping
from dataclasses import dataclass
from typing import Generic, TypeVar

KEY = TypeVar("KEY")
VAL = TypeVar("VAL")


@dataclass(slots=True)
class _Item(Generic[KEY, VAL]):  # noqa: UP046
    key: KEY
    val: VAL


class HopscotchHashMap(MutableMapping[KEY, VAL]):
    """
    Hopscotch hashing keeps each item within a fixed neighborhood (H)
    from its home bucket.

    >>> hs = HopscotchHashMap(initial_capacity=8, neighborhood_size=4)
    >>> hs["a"] = 1
    >>> hs["b"] = 2
    >>> hs["a"]
    1
    >>> len(hs)
    2
    """

    def __init__(
        self,
        initial_capacity: int = 8,
        neighborhood_size: int = 32,
        max_load: float = 0.85,
    ) -> None:
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be >= 1")
        if neighborhood_size < 2:
            raise ValueError("neighborhood_size must be >= 2")
        if not (0.0 < max_load < 1.0):
            raise ValueError("max_load must be between 0 and 1")

        self._H = neighborhood_size
        self._max_load = max_load
        self._buckets: list[_Item[KEY, VAL] | None] = [None] * initial_capacity
        # hop-info: bitmap for each bucket; bit i means an item exists at bucket+ i
        self._hop: list[int] = [0] * initial_capacity
        self._len = 0

    def _home(self, key: KEY) -> int:
        return hash(key) % len(self._buckets)

    def _is_full(self) -> bool:
        return self._len >= int(len(self._buckets) * self._max_load)

    def _resize(self, new_capacity: int) -> None:
        items = list(self.items())
        self._buckets = [None] * new_capacity
        self._hop = [0] * new_capacity
        self._len = 0
        for k, v in items:
            self[k] = v

    def _find_free(self, start: int) -> int:
        for dist in range(len(self._buckets)):
            idx = (start + dist) % len(self._buckets)
            if self._buckets[idx] is None:
                return idx
        return -1

    def _distance(self, home: int, idx: int) -> int:
        n = len(self._buckets)
        return (idx - home) % n

    def _try_relocate(self, home: int, free: int) -> int:
        """
        Try to move some existing item closer to its home so that `free` moves into
        the neighborhood of `home`.

        Returns the new free index if relocation succeeded, else -1.
        """
        n = len(self._buckets)

        while self._distance(home, free) >= self._H:
            moved = False
            # Search backward within H-1 positions from free.
            for back in range(self._H - 1, 0, -1):
                cand = (free - back) % n
                cand_hop = self._hop[cand]
                # Find an item in cand's neighborhood to move into free.
                for off in range(self._H - 1, -1, -1):
                    if (cand_hop >> off) & 1:
                        from_idx = (cand + off) % n
                        # from_idx item will move to free only if it stays within
                        #  cand neighborhood.
                        if self._distance(cand, free) < self._H:
                            self._buckets[free] = self._buckets[from_idx]
                            self._buckets[from_idx] = None

                            # Update hop bitmaps
                            self._hop[cand] &= ~(1 << off)
                            new_off = self._distance(cand, free)
                            self._hop[cand] |= 1 << new_off

                            free = from_idx
                            moved = True
                            break
                if moved:
                    break

            if not moved:
                return -1

        return free

    def __setitem__(self, key: KEY, val: VAL) -> None:
        if self._is_full():
            self._resize(len(self._buckets) * 2)

        home = self._home(key)

        # Update if already present in neighborhood.
        hop = self._hop[home]
        for off in range(self._H):
            if (hop >> off) & 1:
                idx = (home + off) % len(self._buckets)
                item = self._buckets[idx]
                if item is not None and item.key == key:
                    item.val = val
                    return

        free = self._find_free(home)
        if free == -1:
            self._resize(len(self._buckets) * 2)
            self[key] = val
            return

        free = self._try_relocate(home, free)
        if free == -1:
            # Relocation failed; grow and retry.
            self._resize(len(self._buckets) * 2)
            self[key] = val
            return

        off = self._distance(home, free)
        if off >= self._H:
            # Should not happen due to _try_relocate, but keep safe.
            self._resize(len(self._buckets) * 2)
            self[key] = val
            return

        self._buckets[free] = _Item(key, val)
        self._hop[home] |= 1 << off
        self._len += 1

    def __getitem__(self, key: KEY) -> VAL:
        home = self._home(key)
        hop = self._hop[home]
        for off in range(self._H):
            if (hop >> off) & 1:
                idx = (home + off) % len(self._buckets)
                item = self._buckets[idx]
                if item is not None and item.key == key:
                    return item.val
        raise KeyError(key)

    def __delitem__(self, key: KEY) -> None:
        home = self._home(key)
        hop = self._hop[home]
        for off in range(self._H):
            if (hop >> off) & 1:
                idx = (home + off) % len(self._buckets)
                item = self._buckets[idx]
                if item is not None and item.key == key:
                    self._buckets[idx] = None
                    self._hop[home] &= ~(1 << off)
                    self._len -= 1
                    return
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
