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
    """Return a new list containing the sorted elements of the collection
    using the Quick Sort algorithm.

    :param collection: a list of comparable items
    :return: a new list sorted in ascending order

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """

    # Base case: if list has 0 or 1 element it is already sorted
    if len(collection) < 2:
        return collection.copy()

    # Select a random pivot
    pivot_index = randrange(len(collection))
    pivot = collection[pivot_index]

    # Partition the elements
    lesser = [
        item for index, item in enumerate(collection)
        if item <= pivot and index != pivot_index
    ]
    greater = [item for item in collection if item > pivot]

    # Recursively sort both partitions
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    # Get user input and convert it into a list of integers
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]

    # Print the sorted result
    print(quick_sort(unsorted))