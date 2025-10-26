"""
Optimized pure Python implementation of the merge sort algorithm.

Merge Sort is a divide-and-conquer algorithm that splits the input list into halves,
recursively sorts them, and merges the sorted halves.

Source: https://en.wikipedia.org/wiki/Merge_sort
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    """Defines minimal comparison operations required for sorting."""
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


def merge_sort(arr: Sequence[T]) -> list[T]:  # noqa: UP047
    """
    Sort a sequence in ascending order using merge sort.

    :param arr: Any sequence of comparable items.
    :return: A new sorted list.

    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> merge_sort(["b", "a", "c"])
    ['a', 'b', 'c']
    >>> merge_sort((3, 1, 2))
    [1, 2, 3]
    """
    n = len(arr)
    if n <= 1:
        return list(arr)

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list[T], right: list[T]) -> list[T]:
    """Merge two sorted lists efficiently using index pointers."""
    merged: list[T] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    try:
        user_input = input("Enter numbers separated by commas:\n").strip()
        numbers = [int(x) for x in user_input.split(",") if x.strip()]
        print("Sorted:", merge_sort(numbers))
    except ValueError:
        print("Invalid input. Please enter only comma-separated integers.")
