"""Quickselect to find the k-th smallest element (0-indexed)."""

from typing import MutableSequence


def quick_select(items: MutableSequence[int], k: int) -> int:
    if not 0 <= k < len(items):
        raise IndexError("k out of range")
    left, right = 0, len(items) - 1
    while True:
        pivot_index = _partition(items, left, right)
        if pivot_index == k:
            return items[pivot_index]
        if pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1


def _partition(items: MutableSequence[int], left: int, right: int) -> int:
    pivot = items[right]
    store = left
    for idx in range(left, right):
        if items[idx] <= pivot:
            items[store], items[idx] = items[idx], items[store]
            store += 1
    items[store], items[right] = items[right], items[store]
    return store
