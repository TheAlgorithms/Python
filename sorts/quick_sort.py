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
    """
    if len(collection) < 2:
        return collection

    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    lesser_partition, greater_partition = partition(collection, pivot)

    return [*quick_sort(lesser_partition), pivot, *quick_sort(greater_partition)]


def partition(collection: list, pivot) -> tuple[list, list]:
    """Partition the collection into two lists: elements less
    than or equal to the pivot, and elements greater than the pivot.
    :param collection: a mutable collection of comparable items
    :param pivot: the pivot element
    :return: two lists representing the lesser and greater partitions
    """
    lesser_partition = [item for item in collection if item <= pivot]
    greater_partition = [item for item in collection if item > pivot]

    return lesser_partition, greater_partition


def get_user_input() -> list:
    """Get user input and convert it into a list of integers.

    :return: a list of integers provided by the user
    """
    user_input = input("Enter numbers separated by a comma:\n").strip()
    return [int(item) for item in user_input.split(",")]


if __name__ == "__main__":
    unsorted = get_user_input()
    print(quick_sort(unsorted))
