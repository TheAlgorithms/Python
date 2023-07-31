from __future__ import annotations

import sys
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class LRUCache(Generic[T]):
    """
    Page Replacement Algorithm, Least Recently Used (LRU) Caching.

    >>> lru_cache: LRUCache[str | int] = LRUCache(4)
    >>> lru_cache.refer("A")
    >>> lru_cache.refer(2)
    >>> lru_cache.refer(3)

    >>> lru_cache
    LRUCache(4) => [3, 2, 'A']

    >>> lru_cache.refer("A")
    >>> lru_cache
    LRUCache(4) => ['A', 3, 2]

    >>> lru_cache.refer(4)
    >>> lru_cache.refer(5)
    >>> lru_cache
    LRUCache(4) => [5, 4, 'A', 3]

    """

    dq_store: deque[T]  # Cache store of keys
    key_reference: set[T]  # References of the keys in cache
    _MAX_CAPACITY: int = 10  # Maximum capacity of cache

    def __init__(self, n: int) -> None:
        """Creates an empty store and map for the keys.
        The LRUCache is set the size n.
        """
        self.dq_store = deque()
        self.key_reference = set()
        if not n:
            LRUCache._MAX_CAPACITY = sys.maxsize
        elif n < 0:
            raise ValueError("n should be an integer greater than 0.")
        else:
            LRUCache._MAX_CAPACITY = n

    def refer(self, x: T) -> None:
        """
        Looks for a page in the cache store and adds reference to the set.
        Remove the least recently used key if the store is full.
        Update store to reflect recent access.
        """
        if x not in self.key_reference:
            if len(self.dq_store) == LRUCache._MAX_CAPACITY:
                last_element = self.dq_store.pop()
                self.key_reference.remove(last_element)
        else:
            self.dq_store.remove(x)

        self.dq_store.appendleft(x)
        self.key_reference.add(x)

    def display(self) -> None:
        """
        Prints all the elements in the store.
        """
        for k in self.dq_store:
            print(k)

    def __repr__(self) -> str:
        return f"LRUCache({self._MAX_CAPACITY}) => {list(self.dq_store)}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    lru_cache: LRUCache[str | int] = LRUCache(4)
    lru_cache.refer("A")
    lru_cache.refer(2)
    lru_cache.refer(3)
    lru_cache.refer("A")
    lru_cache.refer(4)
    lru_cache.refer(5)
    lru_cache.display()

    print(lru_cache)
    assert str(lru_cache) == "LRUCache(4) => [5, 4, 'A', 3]"
