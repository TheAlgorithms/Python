#!/usr/bin/env python3
from .number_theory.prime_numbers import next_prime


class HashTable:
    """
    Basic Hash Table example with open addressing and linear probing
    """

    def __init__(self, size_table, charge_factor=None, lim_charge=None):
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self._keys = {}

    def keys(self):
        return self._keys

    def balanced_factor(self):
        return sum(1 for slot in self.values if slot is not None) / (
            self.size_table * self.charge_factor
        )

    def hash_function(self, key):
        """
        >>> hashTable = HashTable(size_table=11)
        >>> hashTable.hash_function(111)
        1
        >>> hashTable.hash_function(17)
        6
        """
        return key % self.size_table

    def _step_by_step(self, step_ord):

        print(f"step {step_ord}")
        print([i for i in range(len(self.values))])
        print(self.values)

    def bulk_insert(self, values):
        """
        >>> hashTable = HashTable(size_table=10)
        >>> hashTable.bulk_insert([0,1,2,3,4,5,6,7,8,9])
        step 1
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, None, None, None, None, None, None, None, None, None]
        step 2
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, None, None, None, None, None, None, None, None]
        step 3
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 2, None, None, None, None, None, None, None]
        step 4
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 2, 3, None, None, None, None, None, None]
        step 5
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 2, 3, 4, None, None, None, None, None]
        step 6
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 2, 3, 4, 5, None, None, None, None]
        step 7
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 2, 3, 4, 5, 6, None, None, None]
        step 8
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 2, 3, 4, 5, 6, 7, None, None]
        step 9
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 2, 3, 4, 5, 6, 7, 8, None]
        step 10
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> hashTable = HashTable(size_table=10)
        >>> hashTable.bulk_insert([0,1,10,11,20,21])
        step 1
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, None, None, None, None, None, None, None, None, None]
        step 2
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, None, None, None, None, None, None, None, None]
        step 3
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 10, None, None, None, None, None, None, None]
        step 4
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 10, 11, None, None, None, None, None, None]
        step 5
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 10, 11, 20, None, None, None, None, None]
        step 6
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [0, 1, 10, 11, 20, 21, None, None, None, None]
        """
        i = 1
        for value in values:
            self.insert_data(value)
            self._step_by_step(i)
            i += 1

    def _set_value(self, key, data):
        """
        >>> hashTable = HashTable(10)
        >>> hashTable._set_value(0, 20)
        >>> hashTable.values[0]
        20
        >>> hashTable._keys[0]
        20
        """
        self.values[key] = data
        self._keys[key] = data

    def _collision_resolution(self, key, data=None):
        new_key = self.hash_function(key + 1)

        while self.values[new_key] is not None and self.values[new_key] != key:

            if self.values.count(None) > 0:
                new_key = self.hash_function(new_key + 1)
            else:
                new_key = None
                break

        return new_key

    def rehashing(self):
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self._keys.clear()
        self.values = [None] * self.size_table
        for value in survivor_values:
            self.insert_data(value)

    def insert_data(self, data):
        """
        >>> hashTable = HashTable(10)
        >>> hashTable.insert_data(43)
        >>> hashTable.values[3]
        43
        >>> hashTable._keys[3]
        43
        >>> hashTable.insert_data(43)
        >>> hashTable.values[3]
        43
        >>> hashTable._keys[3]
        43
        >>> hashTable.insert_data(23)
        >>> hashTable.values
        [None, None, None, 43, 23, None, None, None, None, None]
        >>> hashTable._keys
        {3: 43, 4: 23}
        >>> hashTable = HashTable(2)
        >>> hashTable.insert_data(0)
        >>> hashTable.values
        [0, None]
        >>> hashTable.insert_data(1)
        >>> hashTable.values
        [0, 1]
        >>> hashTable.insert_data(2)
        >>> hashTable.values
        [0, 1, 2, None, None]
        """
        key = self.hash_function(data)

        if self.values[key] is None:
            self._set_value(key, data)

        elif self.values[key] == data:
            pass

        else:
            collision_resolution = self._collision_resolution(key, data)
            if collision_resolution is not None:
                self._set_value(collision_resolution, data)
            else:
                self.rehashing()
                self.insert_data(data)
