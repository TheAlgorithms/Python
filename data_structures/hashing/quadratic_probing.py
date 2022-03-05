#!/usr/bin/env python3

from .hash_table import HashTable


class QuadraticProbing(HashTable):
    """
    Basic Hash Table example with open addressing using Quadratic Probing
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _collision_resolution(self, key, data=None):
        """
        >>> hashTable = QuadraticProbing(7)
        >>> hashTable.insert_data(0)
        >>> hashTable.values
        [0, None, None, None, None, None, None]
        >>> hashTable.insert_data(1)
        >>> hashTable.values
        [0, 1, None, None, None, None, None]
        >>> hashTable._collision_resolution(7)
        4
        >>> hashTable.insert_data(7)
        >>> hashTable.values
        [0, 1, None, None, 7, None, None]
        >>> hashTable.bulk_insert([2,3,5,6])
        step 1
        [0, 1, 2, 3, 4, 5, 6]
        [0, 1, 2, None, 7, None, None]
        step 2
        [0, 1, 2, 3, 4, 5, 6]
        [0, 1, 2, 3, 7, None, None]
        step 3
        [0, 1, 2, 3, 4, 5, 6]
        [0, 1, 2, 3, 7, 5, None]
        step 4
        [0, 1, 2, 3, 4, 5, 6]
        [0, 1, 2, 3, 7, 5, 6]
        >>> hashTable.balanced_factor()
        1.0
        >>> hashTable._collision_resolution(7)
        """
        i = 1
        new_key = self.hash_function(key + i * i)

        while self.values[new_key] is not None and self.values[new_key] != key:
            i += 1
            new_key = (
                self.hash_function(key + i * i)
                if not self.balanced_factor() >= self.lim_charge
                else None
            )

            if new_key is None:
                break

        return new_key
