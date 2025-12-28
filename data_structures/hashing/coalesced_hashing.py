#!/usr/bin/env python3
"""
Coalesced hashing (hybrid of open addressing + chaining inside the table).

Reference: [https://en.wikipedia.org/wiki/Hash_table#Coalesced_hashing](https://en.wikipedia.org/wiki/Hash_table#Coalesced_hashing)
"""

from __future__ import annotations

from collections.abc import Iterator, MutableMapping
from dataclasses import dataclass
from typing import Generic, TypeVar

KEY = TypeVar("KEY")
VAL = TypeVar("VAL")


@dataclass(slots=True)
class _Node(Generic[KEY, VAL]):  # noqa: UP046
    key: KEY
    val: VAL
    next: int  # -1 means end of chain


class CoalescedHashMap(MutableMapping[KEY, VAL]):
    """
    Coalesced hashing stores the chain pointers inside the array.

    This implementation uses:
    - Primary area: all indices, chaining occurs via `next` pointers.
    - Free slot choice: highest-index free slot (easy to explain + deterministic).

    >>> ch = CoalescedHashMap(5)
    >>> ch["a"] = 1
    >>> ch["b"] = 2
    >>> ch["a"]
    1
    >>> len(ch)
    2
    """

    def __init__(self, capacity: int = 8, capacity_factor: float = 0.8) -> None:
        if capacity < 1:
            raise ValueError("capacity must be >= 1")
        if not (0.0 < capacity_factor < 1.0):
            raise ValueError("capacity_factor must be between 0 and 1")

        self._capacity_factor = capacity_factor
        self._table: list[_Node[KEY, VAL] | None] = [None] * capacity
        self._len = 0

    def _home(self, key: KEY) -> int:
        return hash(key) % len(self._table)

    def _is_full(self) -> bool:
        return self._len >= int(len(self._table) * self._capacity_factor)

    def _find_free_from_end(self) -> int:
        for i in range(len(self._table) - 1, -1, -1):
            if self._table[i] is None:
                return i
        return -1

    def _resize(self, new_capacity: int) -> None:
        old_items = list(self.items())
        self._table = [None] * new_capacity
        self._len = 0
        for k, v in old_items:
            self[k] = v

    def __setitem__(self, key: KEY, val: VAL) -> None:
        if self._is_full():
            self._resize(len(self._table) * 2)

        home = self._home(key)
        node = self._table[home]

        if node is None:
            self._table[home] = _Node(key, val, -1)
            self._len += 1
            return

        # Search chain for update.
        cur = home
        while True:
            # Explicitly type the current node to satisfy mypy
            current_node = self._table[cur]
            if current_node is None:
                # Should not happen if logic is correct, but handles None safety
                break

            if current_node.key == key:
                current_node.val = val
                return
            if current_node.next == -1:
                break
            cur = current_node.next

        # Insert new node at a free slot and link it.
        free = self._find_free_from_end()
        if free == -1:
            self._resize(len(self._table) * 2)
            self[key] = val
            return

        self._table[free] = _Node(key, val, -1)

        # Link the previous end of chain to the new free slot
        # We re-fetch the node at 'cur' to be safe
        if (tail_node := self._table[cur]) is not None:
            tail_node.next = free
        self._len += 1

    def __getitem__(self, key: KEY) -> VAL:
        home = self._home(key)
        cur = home
        while cur != -1:
            node = self._table[cur]
            if node is None:
                break
            if node.key == key:
                return node.val
            cur = node.next
        raise KeyError(key)

    def __delitem__(self, key: KEY) -> None:
        home = self._home(key)
        prev = -1
        cur = home

        while cur != -1:
            node = self._table[cur]
            if node is None:
                break
            if node.key == key:
                # If deleting head: copy next node into home if exists
                #  (keeps chains valid).
                if prev == -1:
                    if node.next == -1:
                        self._table[cur] = None
                    else:
                        nxt = node.next
                        next_node = self._table[nxt]
                        # Must assert next_node is not None for mypy
                        if next_node is not None:
                            self._table[cur] = _Node(
                                next_node.key,
                                next_node.val,
                                next_node.next,
                            )
                            self._table[nxt] = None
                else:
                    # Update previous node's next pointer
                    prev_node = self._table[prev]
                    if prev_node is not None:
                        prev_node.next = node.next
                    self._table[cur] = None
                self._len -= 1
                return
            prev, cur = cur, node.next

        raise KeyError(key)

    def __iter__(self) -> Iterator[KEY]:
        for node in self._table:
            if node is not None:
                yield node.key

    def __len__(self) -> int:
        return self._len


if __name__ == "__main__":
    import doctest

    doctest.testmod()
