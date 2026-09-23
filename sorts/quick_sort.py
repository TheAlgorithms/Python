"""
A pure Python implementation of the quick sort algorithm

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""

from __future__ import annotations

from random import randrange
from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def quick_sort[T: Comparable](collection: list[T]) -> list[T]:
    """A pure Python implementation of quicksort algorithm.

    :param collection: a mutable collection of comparable items
    :return: the same collection ordered in ascending order

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    >>> quick_sort(["z", "a", "m", "b"])
    ['a', 'b', 'm', 'z']
    >>> quick_sort([3.14, -1.0, 2.71])
    [-1.0, 2.71, 3.14]
    >>> quick_sort([0, 5, 3, 2, 2]) == sorted([0, 5, 3, 2, 2])
    True
    >>> quick_sort(["z", "a", "m"]) == sorted(["z", "a", "m"])
    True
    """
    if len(collection) < 2:
        return collection
    pivot_index = randrange(len(collection))
    pivot = collection[pivot_index]
    lesser = [item for item in collection if item < pivot]
    equal = [item for item in collection if item == pivot]
    greater = [item for item in collection if item > pivot]
    return [*quick_sort(lesser), *equal, *quick_sort(greater)]


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))
