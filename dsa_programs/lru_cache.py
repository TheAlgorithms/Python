"""Least Recently Used cache built on top of OrderedDict."""

from collections import OrderedDict
from typing import Generic, MutableMapping, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self._store: MutableMapping[K, V] = OrderedDict()

    def get(self, key: K) -> Optional[V]:
        if key not in self._store:
            return None
        value = self._store.pop(key)
        self._store[key] = value
        return value

    def put(self, key: K, value: V) -> None:
        if key in self._store:
            self._store.pop(key)
        elif len(self._store) >= self.capacity:
            self._store.popitem(last=False)
        self._store[key] = value

    def __len__(self) -> int:
        return len(self._store)
