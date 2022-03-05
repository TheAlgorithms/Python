#!/usr/bin/env python3
from .hash_table import HashTable
from .number_theory.prime_numbers import check_prime, next_prime


class DoubleHash(HashTable):
    """
    Hash Table example with open addressing and Double Hash
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _hash_function_2(self, value, data):
        """
        >>> hashTable = DoubleHash(3)
        >>> hashTable._hash_function_2(1, 4) # next_prime_gt = 3, return 3 - (4 % 3) = 2
        2
        >>> hashTable = DoubleHash(5)
        >>> hashTable._hash_function_2(3, 8) # next_prime(3) = 3, return 3 - (8 % 3) = 1
        1
        """
        next_prime_gt = (
            next_prime(value % self.size_table)
            if not check_prime(value % self.size_table)
            else value % self.size_table
        )  # gt = bigger than
        return next_prime_gt - (data % next_prime_gt)

    def _hash_double_function(self, key, data, increment):
        """
        >>> hashTable = DoubleHash(3)
        >>> hashTable._hash_double_function(1, 4, 1)
        2
        >>> hashTable._hash_double_function(1, 4, 2)
        1
        >>> hashTable = DoubleHash(5)
        >>> hashTable._hash_double_function(3, 8, 1)
        1
        >>> hashTable._hash_double_function(3, 8, 4)
        4
        """
        return (increment * self._hash_function_2(key, data)) % self.size_table

    def _collision_resolution(self, key, data=None):
        """
        >>> hashTable = DoubleHash(7)
        >>> hashTable.insert_data(0)
        >>> hashTable.values
        [0, None, None, None, None, None, None]
        >>> hashTable.insert_data(1)
        >>> hashTable.values
        [0, 1, None, None, None, None, None]
        >>> hashTable.insert_data(7)
        >>> hashTable.values
        [7, 1, None, None, None, None, None]
        >>> _ = hashTable.bulk_insert([1,2,3,4,5,6])
        step 1
        [0, 1, 2, 3, 4, 5, 6]
        [7, 1, None, None, None, None, None]
        step 2
        [0, 1, 2, 3, 4, 5, 6]
        [7, 1, 2, None, None, None, None]
        step 3
        [0, 1, 2, 3, 4, 5, 6]
        [7, 1, 2, 3, None, None, None]
        step 4
        [0, 1, 2, 3, 4, 5, 6]
        [7, 1, 2, 3, 4, None, None]
        step 5
        [0, 1, 2, 3, 4, 5, 6]
        [7, 1, 2, 3, 4, 5, None]
        step 6
        [0, 1, 2, 3, 4, 5, 6]
        [7, 1, 2, 3, 4, 5, 6]
        >>> hashTable.balanced_factor()
        1.0
        >>> hashTable._collision_resolution(3, 8)
        """
        i = 1
        new_key = self.hash_function(data)

        while self.values[new_key] is not None and self.values[new_key] != key:
            new_key = (
                self._hash_double_function(key, data, i)
                if not self.balanced_factor() >= self.lim_charge
                else None
            )
            if new_key is None:
                break
            else:
                i += 1

        return new_key
