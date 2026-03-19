"""
A pure Python implementation of the quick sort algorithm

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""

from __future__ import annotations

from typing import Any


def quick_sort(collection: list[Any]) -> list[Any]:
    """A pure Python implementation of quicksort algorithm.

    This implementation does not mutate the original collection. It uses
    median-of-three pivot selection for improved performance on sorted or
    nearly-sorted inputs.

    :param collection: a mutable collection of comparable items
    :return: a new list with the same elements ordered in ascending order

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    >>> quick_sort([1])
    [1]
    >>> quick_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> quick_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> quick_sort([3, 3, 3, 3])
    [3, 3, 3, 3]
    >>> quick_sort(['d', 'a', 'b', 'e', 'c'])
    ['a', 'b', 'c', 'd', 'e']
    >>> quick_sort([1.1, 0.5, 3.3, 2.2])
    [0.5, 1.1, 2.2, 3.3]
    >>> original = [3, 1, 2]
    >>> sorted_list = quick_sort(original)
    >>> original
    [3, 1, 2]
    >>> sorted_list
    [1, 2, 3]
    >>> import random
    >>> collection_arg = random.sample(range(-50, 50), 100)
    >>> quick_sort(collection_arg) == sorted(collection_arg)
    True
    """
    # Base case: if the collection has 0 or 1 elements, it is already sorted
    if len(collection) < 2:
        return collection

    # Use median-of-three pivot selection for better worst-case performance.
    # Compare the first, middle, and last elements and pick the median value.
    first = collection[0]
    middle = collection[len(collection) // 2]
    last = collection[-1]
    pivot = sorted((first, middle, last))[1]

    # Partition elements into three groups without mutating the original list
    lesser = [item for item in collection if item < pivot]
    equal = [item for item in collection if item == pivot]
    greater = [item for item in collection if item > pivot]

    # Recursively sort the lesser and greater groups, and combine with equal
    return [*quick_sort(lesser), *equal, *quick_sort(greater)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Get user input and convert it into a list of integers
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]

    # Print the result of sorting the user-provided list
    print(quick_sort(unsorted))
