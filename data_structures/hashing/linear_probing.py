#!/usr/bin/env python3
"""
Linear Probing Hash Table Implementation with Collision Resolution.
Reference: https://en.wikipedia.org/wiki/Linear_probing
"""

from typing import Any

from .hash_table import HashTable


class LinearProbing(HashTable):
    """
    Hash Table with Linear Probing collision resolution.

    Hash function: h(k, i) = (h(k) + i) % m
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def _collision_resolution(self, key: int, data: Any = None) -> int | None:
        """
        Resolve collisions by probing sequentially.

        Examples:
        >>> lp = LinearProbing(5)
        >>> lp.insert_data(10)  # hash(10) -> 0
        >>> lp.insert_data(15)  # hash(15) -> 0 (Collision) -> Probe 1
        >>> lp.keys()
        {0: 10, 1: 15}

        >>> lp = LinearProbing(2)
        >>> lp.insert_data(1); lp.insert_data(2); lp.insert_data(3) # Resizes
        >>> len(lp.keys())
        3
        """
        i = 1
        # Initial probe is already occupied, start from next slot
        new_key = (key + 1) % self.size_table

        while self.values[new_key] is not None and self.values[new_key] != data:
            # Check load factor to avoid filling table completely
            if self.balanced_factor() >= self.lim_charge:
                return None  # Trigger rehashing in parent

            new_key = (new_key + 1) % self.size_table
            i += 1

            # Safety break: Avoid infinite loop if table is full but
            #  lim_charge logic fails
            if i > self.size_table:
                return None

        return new_key


if __name__ == "__main__":
    import doctest

    doctest.testmod()
