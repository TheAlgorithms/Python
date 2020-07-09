import sys
from abc import abstractmethod
from collections import deque


class LRUCache:
    """ Page Replacement Algorithm, Least Recently Used (LRU) Caching."""

    dq_store = object()  # Cache store of keys
    key_reference_map = object()  # References of the keys in cache
    _MAX_CAPACITY: int = 10  # Maximum capacity of cache

    @abstractmethod
    def __init__(self, n: int):
        """ Creates an empty store and map for the keys.
        The LRUCache is set the size n.
        """
        self.dq_store = deque()
        self.key_reference_map = set()
        if not n:
            LRUCache._MAX_CAPACITY = sys.maxsize
        elif n < 0:
            raise ValueError("n should be an integer greater than 0.")
        else:
            LRUCache._MAX_CAPACITY = n

    def refer(self, x):
        """
            Looks for a page in the cache store and adds reference to the set.
            Remove the least recently used key if the store is full.
            Update store to reflect recent access.
        """
        if x not in self.key_reference_map:
            if len(self.dq_store) == LRUCache._MAX_CAPACITY:
                last_element = self.dq_store.pop()
                self.key_reference_map.remove(last_element)
        else:
            index_remove = 0
            for idx, key in enumerate(self.dq_store):
                if key == x:
                    index_remove = idx
                    break
            self.dq_store.remove(index_remove)

        self.dq_store.appendleft(x)
        self.key_reference_map.add(x)

    def display(self):
        """
            Prints all the elements in the store.
        """
        for k in self.dq_store:
            print(k)


if __name__ == "__main__":
    lru_cache = LRUCache(4)
    lru_cache.refer(1)
    lru_cache.refer(2)
    lru_cache.refer(3)
    lru_cache.refer(1)
    lru_cache.refer(4)
    lru_cache.refer(5)
    lru_cache.display()
