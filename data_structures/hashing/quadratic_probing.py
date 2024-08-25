#!/usr/bin/env python3

from .hash_table import HashTable


class QuadraticProbing(HashTable):
    """
    Basic Hash Table example with open addressing using Quadratic Probing
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _collision_resolution(self, key, data=None):  # noqa: ARG002
        """
        Quadratic probing is an open addressing scheme used for resolving
        collisions in hash table.

        It works by taking the original hash index and adding successive
        values of an arbitrary quadratic polynomial until open slot is found.

        Hash + 1², Hash + 2², Hash + 3² .... Hash + n²

        reference:
            - https://en.wikipedia.org/wiki/Quadratic_probing
        e.g:
        1. Create hash table with size 7
        >>> qp = QuadraticProbing(7)
        >>> qp.insert_data(90)
        >>> qp.insert_data(340)
        >>> qp.insert_data(24)
        >>> qp.insert_data(45)
        >>> qp.insert_data(99)
        >>> qp.insert_data(73)
        >>> qp.insert_data(7)
        >>> qp.keys()
        {11: 45, 14: 99, 7: 24, 0: 340, 5: 73, 6: 90, 8: 7}

        2. Create hash table with size 8
        >>> qp = QuadraticProbing(8)
        >>> qp.insert_data(0)
        >>> qp.insert_data(999)
        >>> qp.insert_data(111)
        >>> qp.keys()
        {0: 0, 7: 999, 3: 111}

        3. Try to add three data elements when the size is two
        >>> qp =  QuadraticProbing(2)
        >>> qp.insert_data(0)
        >>> qp.insert_data(999)
        >>> qp.insert_data(111)
        >>> qp.keys()
        {0: 0, 4: 999, 1: 111}

        4. Try to add three data elements when the size is one
        >>> qp =  QuadraticProbing(1)
        >>> qp.insert_data(0)
        >>> qp.insert_data(999)
        >>> qp.insert_data(111)
        >>> qp.keys()
        {4: 999, 1: 111}
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
