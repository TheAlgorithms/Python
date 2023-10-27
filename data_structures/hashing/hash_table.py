#!/usr/bin/env python3
from .number_theory.prime_numbers import next_prime


class HashTable:
    """
    Basic Hash Table example with open addressing and linear probing
    """

    def __init__(
        self,
        size_table: int,
        charge_factor: int | None = None,
        lim_charge: float | None = None,
    ) -> None:
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self.__aux_list: list = []
        self._keys: dict = {}

    def keys(self):
        """
        The keys function returns a dictionary containing the key value pairs.
        key being the index number in hash table and value being the data value.

        Examples:
        1. creating HashTable with size 10 and inserting 3 elements
        >>> ht = HashTable(10)
        >>> ht.insert_data(10)
        >>> ht.insert_data(20)
        >>> ht.insert_data(30)
        >>> ht.keys()
        {0: 10, 1: 20, 2: 30}

        2. creating HashTable with size 5 and inserting 5 elements
        >>> ht = HashTable(5)
        >>> ht.insert_data(5)
        >>> ht.insert_data(4)
        >>> ht.insert_data(3)
        >>> ht.insert_data(2)
        >>> ht.insert_data(1)
        >>> ht.keys()
        {0: 5, 4: 4, 3: 3, 2: 2, 1: 1}
        """
        return self._keys

    def balanced_factor(self):
        return sum(1 for slot in self.values if slot is not None) / (
            self.size_table * self.charge_factor
        )

    def hash_function(self, key):
        """
        Generates hash for the given key value

        Examples:

        Creating HashTable with size 5
        >>> ht = HashTable(5)
        >>> ht.hash_function(10)
        0
        >>> ht.hash_function(20)
        0
        >>> ht.hash_function(4)
        4
        >>> ht.hash_function(18)
        3
        >>> ht.hash_function(-18)
        2
        >>> ht.hash_function(18.5)
        3.5
        >>> ht.hash_function(0)
        0
        >>> ht.hash_function(-0)
        0
        """
        return key % self.size_table

    def _step_by_step(self, step_ord):
        print(f"step {step_ord}")
        print(list(range(len(self.values))))
        print(self.values)

    def bulk_insert(self, values):
        """
        bulk_insert is used for entering more than one element at a time
        in the HashTable.

        Examples:
        1.
        >>> ht = HashTable(5)
        >>> ht.bulk_insert((10,20,30))
        step 1
        [0, 1, 2, 3, 4]
        [10, None, None, None, None]
        step 2
        [0, 1, 2, 3, 4]
        [10, 20, None, None, None]
        step 3
        [0, 1, 2, 3, 4]
        [10, 20, 30, None, None]

        2.
        >>> ht = HashTable(5)
        >>> ht.bulk_insert([5,4,3,2,1])
        step 1
        [0, 1, 2, 3, 4]
        [5, None, None, None, None]
        step 2
        [0, 1, 2, 3, 4]
        [5, None, None, None, 4]
        step 3
        [0, 1, 2, 3, 4]
        [5, None, None, 3, 4]
        step 4
        [0, 1, 2, 3, 4]
        [5, None, 2, 3, 4]
        step 5
        [0, 1, 2, 3, 4]
        [5, 1, 2, 3, 4]
        """
        i = 1
        self.__aux_list = values
        for value in values:
            self.insert_data(value)
            self._step_by_step(i)
            i += 1

    def _set_value(self, key, data):
        """
        _set_value functions allows to update value at a particular hash

        Examples:
        1. _set_value in HashTable of size 5
        >>> ht = HashTable(5)
        >>> ht.insert_data(10)
        >>> ht.insert_data(20)
        >>> ht.insert_data(30)
        >>> ht._set_value(0,15)
        >>> ht.keys()
        {0: 15, 1: 20, 2: 30}

        2. _set_value in HashTable of size 2
        >>> ht = HashTable(2)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht._set_value(3,15)
        >>> ht.keys()
        {3: 15, 2: 17, 4: 99}

        3. _set_value in HashTable when hash is not present
        >>> ht = HashTable(2)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht._set_value(0,15)
        >>> ht.keys()
        {3: 18, 2: 17, 4: 99, 0: 15}

        4. _set_value in HashTable when multiple hash are not present
        >>> ht = HashTable(2)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht._set_value(0,15)
        >>> ht._set_value(1,20)
        >>> ht.keys()
        {3: 18, 2: 17, 4: 99, 0: 15, 1: 20}
        """
        self.values[key] = data
        self._keys[key] = data

    def _collision_resolution(self, key, data=None):
        """
        This method is a type of open addressing which is used for handling collision.

        In this implementation the concept of linear probing has been used.

        The hash table is searched sequentially from the original location of the
        hash, if the new hash/location we get is already occupied we check for the next
        hash/location.

        references:
            - https://en.wikipedia.org/wiki/Linear_probing

        Examples:
        1. The collision will be with keys 18 & 99, so new hash will be created for 99
        >>> ht = HashTable(3)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht.keys()
        {2: 17, 0: 18, 1: 99}

        2. The collision will be with keys 17 & 101, so new hash
        will be created for 101
        >>> ht = HashTable(4)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht.insert_data(101)
        >>> ht.keys()
        {1: 17, 2: 18, 3: 99, 0: 101}

        2. The collision will be with all keys, so new hash will be created for all
        >>> ht = HashTable(1)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht.keys()
        {2: 17, 3: 18, 4: 99}

        3. Trying to insert float key in hash
        >>> ht = HashTable(1)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99.99)
        Traceback (most recent call last):
        ...
        TypeError: list indices must be integers or slices, not float
        """
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
        self.values = [None] * self.size_table  # hell's pointers D: don't DRY ;/
        for value in survivor_values:
            self.insert_data(value)

    def insert_data(self, data):
        """
        insert_data is used for inserting a single element at a time in the HashTable.

        Examples:

        >>> ht = HashTable(3)
        >>> ht.insert_data(5)
        >>> ht.keys()
        {2: 5}
        >>> ht = HashTable(5)
        >>> ht.insert_data(30)
        >>> ht.insert_data(50)
        >>> ht.keys()
        {0: 30, 1: 50}
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
