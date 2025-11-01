"""
A pure Python implementation of the quick sort algorithm

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""
from __future__ import annotations

from random import randrange


def quick_sort(collection: list) -> list:
    """A pure Python implementation of quicksort algorithm using in-place sorting.

    :param collection: a mutable collection of comparable items
    :return: the same collection ordered in ascending order

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> quick_sort([])
    []

    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    # Call the helper function to sort in-place
    _quick_sort(collection, 0, len(collection) - 1)
    return collection


def _quick_sort(collection: list, low: int, high: int) -> None:
    """Helper function that performs in-place quicksort.

    :param collection: the list to sort
    :param low: starting index of the partition
    :param high: ending index of the partition
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = _partition(collection, low, high)
        # Recursively sort elements before and after partition
        _quick_sort(collection, low, pivot_index - 1)
        _quick_sort(collection, pivot_index + 1, high)


def _partition(collection: list, low: int, high: int) -> int:
    """In-place partitioning using Lomuto partition scheme.

    :param collection: the list to partition
    :param low: starting index of the partition
    :param high: ending index of the partition
    :return: the final pivot index after partitioning
    """
  # Randomly select a pivot index and swap with the last element
    pivot_index = randrange(low, high + 1)
    
    # Use a temporary variable for the swap to keep lines short
    temp_pivot = collection[pivot_index]
    collection[pivot_index] = collection[high]
    collection[high] = temp_pivot

    pivot = collection[high]

    # Index of smaller element (elements <= pivot will be moved to left of this)
    i = low - 1

    # Traverse through all elements and move smaller elements to the left
    for j in range(low, high):
        if collection[j] <= pivot:
            i += 1
            collection[i], collection[j] = collection[j], collection[i]

    # Place pivot in its correct position
    collection[i + 1], collection[high] = collection[high], collection[i + 1]
    return i + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
