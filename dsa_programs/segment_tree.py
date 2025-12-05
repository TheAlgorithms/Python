"""Segment tree supporting range-sum queries and point updates."""

from typing import Iterable, List


class SegmentTree:
    def __init__(self, data: Iterable[int]):
        values = list(data)
        if not values:
            raise ValueError("Segment tree requires at least one value")
        self._size = len(values)
        self._tree: List[int] = [0] * (2 * self._size)
        self._tree[self._size : 2 * self._size] = values
        for idx in range(self._size - 1, 0, -1):
            self._tree[idx] = self._tree[2 * idx] + self._tree[2 * idx + 1]

    def update(self, index: int, value: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError("Index out of range")
        pos = index + self._size
        self._tree[pos] = value
        pos //= 2
        while pos >= 1:
            self._tree[pos] = self._tree[2 * pos] + self._tree[2 * pos + 1]
            pos //= 2

    def range_sum(self, left: int, right: int) -> int:
        if not (0 <= left <= right < self._size):
            raise IndexError("Invalid range")
        left += self._size
        right += self._size
        total = 0
        while left <= right:
            if left % 2 == 1:
                total += self._tree[left]
                left += 1
            if right % 2 == 0:
                total += self._tree[right]
                right -= 1
            left //= 2
            right //= 2
        return total
