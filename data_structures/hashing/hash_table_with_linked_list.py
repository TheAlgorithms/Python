from collections import deque

from .hash_table import HashTable


class HashTableWithLinkedList(HashTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _set_value(self, key, data):
        """
        >>> hashTable = HashTableWithLinkedList(10)
        >>> hashTable._set_value(0, 20)
        >>> hashTable.values[0]
        deque([20])
        >>> hashTable._keys[0]
        deque([20])
        >>> hashTable._set_value(0, 40)
        >>> hashTable.values[0]
        deque([40, 20])
        >>> hashTable._keys[0]
        deque([40, 20])
        """
        self.values[key] = deque([]) if self.values[key] is None else self.values[key]
        self.values[key].appendleft(data)
        self._keys[key] = self.values[key]

    def balanced_factor(self):
        return (
            sum(self.charge_factor - len(slot) for slot in self.values)
            / self.size_table
            * self.charge_factor
        )

    def _collision_resolution(self, key):
        """
        >>> hashTable = HashTableWithLinkedList(3)
        >>> hashTable.bulk_insert([0, 1])
        step 1
        [0, 1, 2]
        [deque([0]), None, None]
        step 2
        [0, 1, 2]
        [deque([0]), deque([1]), None]
        >>> hashTable._collision_resolution(1)
        1
        >>> hashTable.insert_data(6)
        >>> hashTable.values
        [deque([6, 0]), deque([1]), None]
        >>> hashTable.insert_data(2)
        >>> hashTable.values
        [deque([6, 0]), deque([1]), deque([2])]
        >>> hashTable._collision_resolution(2)
        """
        if not (
            len(self.values[key]) == self.charge_factor and self.values.count(None) == 0
        ):
            return key
        return super()._collision_resolution(key)
