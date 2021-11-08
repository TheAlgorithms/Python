"""
This implementation of LRU Cache uses the in-built Python dictionary (dict) which from
Python 3.6 onward maintain the insertion order of keys and ensures O(1) operations on
insert, delete and access. https://docs.python.org/3/library/stdtypes.html#typesmapping
"""
from typing import Any, Hashable


class LRUCache(dict):
    def __init__(self, capacity: int) -> None:
        """
        Initialize an LRU Cache with given capacity.
        capacity : int -> the capacity of the LRU Cache
        >>> cache = LRUCache(2)
        >>> cache
        {}
        """
        self.remaining: int = capacity

    def get(self, key: Hashable) -> Any:
        """
        This method returns the value associated with the key.
        key : A hashable object that is mapped to a value in the LRU cache.
        return -> Any object that has been stored as a value in the LRU cache.

        >>> cache = LRUCache(2)
        >>> cache.put(1,1)
        >>> cache.get(1)
        1
        >>> cache.get(2)
        Traceback (most recent call last):
        ...
        KeyError: '2 not found.'
        """
        if key not in self:
            raise KeyError(f"{key} not found.")
        val = self.pop(key)  # Pop the key-value and re-insert to maintain the order
        self[key] = val
        return val

    def put(self, key: Hashable, value: Any) -> None:
        """
        This method puts the value associated with the key provided in the LRU cache.
        key : A hashable object that is mapped to a value in the LRU cache.
        value: Any object that is to be associated with the key in the LRU cache.
        >>> cache = LRUCache(2)
        >>> cache.put(3,3)
        >>> cache
        {3: 3}
        >>> cache.put(2,2)
        >>> cache
        {3: 3, 2: 2}
        """
        # To pop the last value inside of the LRU cache
        if key in self:
            self.pop(key)
            self[key] = value
            return

        if self.remaining > 0:
            self.remaining -= 1
        # To pop the least recently used item from the dictionary
        else:
            self.pop(next(iter(self)))
        self[key] = value


def main() -> None:
    """Example test case with LRU_Cache of size 2
    >>> main()
    1
    Key=2 not found in cache
    Key=1 not found in cache
    3
    4
    """
    cache = LRUCache(2)  # Creates an LRU cache with size 2
    cache.put(1, 1)  # cache = {1:1}
    cache.put(2, 2)  # cache = {1:1, 2:2}
    try:
        print(cache.get(1))  # Prints 1
    except KeyError:
        print("Key not found in cache")
    cache.put(
        3, 3
    )  # cache = {1:1, 3:3} key=2 is evicted because it wasn't used recently
    try:
        print(cache.get(2))
    except KeyError:
        print("Key=2 not found in cache")  # Prints key not found
    cache.put(
        4, 4
    )  # cache = {4:4, 3:3} key=1 is evicted because it wasn't used recently
    try:
        print(cache.get(1))
    except KeyError:
        print("Key=1 not found in cache")  # Prints key not found
    try:
        print(cache.get(3))  # Prints value 3
    except KeyError:
        print("Key not found in cache")

    try:
        print(cache.get(4))  # Prints value 4
    except KeyError:
        print("Key not found in cache")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
