"""Iterative binary search on a sorted sequence."""

from typing import Sequence


def binary_search(items: Sequence[int], target: int) -> int:
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        value = items[mid]
        if value == target:
            return mid
        if value < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
