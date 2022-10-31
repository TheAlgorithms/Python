#!/usr/bin/env python3
"""
Hashing is a technique that  uses a hash function that converts a given  number
or any other key to a smaller number and uses the small number as the index in a table called a hash table.

Hash Function:
A function that converts a given big number to a small practical integer value.
The mapped integer value is used as an index in the hash table.

Quadratic Probing:
Quadratic probing is an open-addressing scheme where we look for the i^2th slot in the i’th iteration
if the given hash value x collides in the hash table.

The logic is

For the loop of the array, running from 0 to array length, given x is an element of the array
1 - Check if the slot hash(x) % SizeofHashtable is full, then we try (hash(x) + 1*1) % SizeofHashtable.
2 - then check if (hash(x) + 1*1) % SizeofHashtable is also full, then we try (hash(x) + 2*2) % SizeofHashtable.
3 - then check If (hash(x) + 2*2) % SizeofHashtable is also full, then we try (hash(x) + 3*3) % SizeofHashtable.
...
This process is repeated for all the values of i until an empty slot is found.
"""
from .hash_table import HashTable


class QuadraticProbing(HashTable):
    """
    Basic Hash Table example with open addressing using Quadratic Probing
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _collision_resolution(self, key, data=None):
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
