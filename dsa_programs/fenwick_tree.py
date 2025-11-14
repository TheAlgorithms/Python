"""Fenwick tree (Binary Indexed Tree) for prefix sums."""

from typing import Iterable, List


class FenwickTree:
    def __init__(self, data: Iterable[int]):
        values = list(data)
        self._size = len(values)
        self._tree: List[int] = [0] * (self._size + 1)
        for idx, value in enumerate(values, start=1):
            self._internal_update(idx, value)

    def update(self, index: int, delta: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError("Index out of range")
        self._internal_update(index + 1, delta)

    def prefix_sum(self, index: int) -> int:
        if index < 0:
            return 0
        if index >= self._size:
            index = self._size - 1
        idx = index + 1
        result = 0
        while idx > 0:
            result += self._tree[idx]
            idx -= idx & -idx
        return result

    def range_sum(self, left: int, right: int) -> int:
        if left > right:
            return 0
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def _internal_update(self, index: int, delta: int) -> None:
        while index <= self._size:
            self._tree[index] += delta
            index += index & -index
