"""
Pure Python implementation of Recursive Binary Search.

Binary Search is a divide-and-conquer algorithm that works on sorted lists.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar


T = TypeVar("T")


def binary_search_recursive(
    arr: Sequence[T],
    target: T,
    left: int = 0,
    right: int | None = None,
) -> int:
    """
    Perform recursive binary search on a sorted sequence.

    :param arr: A sorted sequence of comparable elements
    :param target: The element to search for
    :param left: Left boundary of the search interval
    :param right: Right boundary of the search interval
    :return: Index of target if found, otherwise -1

    >>> binary_search_recursive([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search_recursive([1, 2, 3, 4, 5], 1)
    0
    >>> binary_search_recursive([1, 2, 3, 4, 5], 5)
    4
    >>> binary_search_recursive([1, 2, 3, 4, 5], 6)
    -1
    >>> binary_search_recursive([], 10)
    -1
    >>> binary_search_recursive([2, 4, 6, 8], 6)
    2
    """

    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    return binary_search_recursive(arr, target, mid + 1, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
