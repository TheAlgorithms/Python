"""
Basic HashSet implementation using open addressing and linear probing
"""


class HashSet:
    def __init__(
        self,
        initial_size: int,
        charge_factor: int | None = None,
        lim_charge: float | None = None,
    ) -> None:
        self.size_table = initial_size
        self.values = [None] * self.size_table
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self._keys: dict = {}

    def keys(self) -> list:
        """
        >>> hashset = HashSet(2)
        >>> hashset.add(10)
        >>> hashset.keys()
        [10]

        """
        return list(self._keys.values())

    def add(self, value):
        self.insert_data(value)

    def contains(self, value) -> bool:
        key = self.hash_function(value)
        return key in self._keys

    def remove(self, value):
        key = self.hash_function(value)
        if key in self._keys:
            self._set_value(key, None)
            del self._keys[key]

    def balanced_factor(self):
        return sum(1 for slot in self.values if slot is not None) / (
            self.size_table * self.charge_factor
        )

    def hash_function(self, key):
        return key % self.size_table

    def _set_value(self, key, data):
        self.values[key] = data
        if data is not None:
            self._keys[key] = data

    def _collision_resolution(self, key):
        new_key = self.hash_function(key + 1)
        while self.values[new_key] is not None and self.values[new_key] != key:
            if self.values.count(None) > 0:
                new_key = self.hash_function(new_key + 1)
            else:
                new_key = None
                break

        return new_key

    def rehashing(self):
        new_size = self.size_table * 2
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = new_size
        self._keys.clear()
        self.values = [None] * self.size_table
        for value in survivor_values:
            self.insert_data(value)

    def insert_data(self, data):
        key = self.hash_function(data)

        if self.values[key] is None:
            self._set_value(key, data)

        elif self.values[key] == data:
            pass

        else:
            collision_resolution = self._collision_resolution(key)
            if collision_resolution is not None:
                self._set_value(collision_resolution, data)
            else:
                self.rehashing()
                self.insert_data(data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
