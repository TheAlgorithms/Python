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
        return self._keys

    def balanced_factor(self):
        return sum(1 for slot in self.values if slot is not None) / (
            self.size_table * self.charge_factor
        )

    def hash_function(self, key):
        return key % self.size_table

    def _step_by_step(self, step_ord):

        print(f"step {step_ord}")
        print(list(range(len(self.values))))
        print(self.values)

    def bulk_insert(self, values):
        i = 1
        self.__aux_list = values
        for value in values:
            self.insert_data(value)
            self._step_by_step(i)
            i += 1

    def _set_value(self, key, data):
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
        self.values = [None] * self.size_table  # hell's pointers D: don't DRY ;/
        for value in survivor_values:
            self.insert_data(value)

    def insert_data(self, data):
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
