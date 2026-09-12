"""
A pure Python implementation of the quick sort algorithm

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""

from __future__ import annotations

from random import randrange
from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


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
    >>> quick_sort(["banana", "apple", "cherry"])
    ['apple', 'banana', 'cherry']
    >>> quick_sort([3.14, 1.5, 2.7])
    [1.5, 2.7, 3.14]
    >>> quick_sort([1, "two"])  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: '<' not supported between instances of ...
    """
    # Base case: if the collection has 0 or 1 elements, it is already sorted
    if len(collection) < 2:
        return collection

    # Randomly select a pivot index and remove the pivot element
    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    # Partition the remaining elements using the less-than comparison
    lesser = [item for item in collection if item < pivot]
    greater = [item for item in collection if not item < pivot]

    # Recursively sort the lesser and greater groups, and combine with the pivot
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    # Get user input and convert it into a list of integers
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]

    # Print the result of sorting the user-provided list
    print(quick_sort(unsorted))
