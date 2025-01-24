"""
A Python implementation of the quick select algorithm, which is efficient for
calculating the value that would appear in the index of a list if it would be
sorted, even if it is not already sorted
https://en.wikipedia.org/wiki/Quickselect
"""

import random


def _partition(data: list, pivot) -> tuple:
    """
    Three way partition the data into smaller, equal and greater lists,
    in relationship to the pivot
    :param data: The data to be sorted (a list)
    :param pivot: The value to partition the data on
    :return: Three list: smaller, equal and greater
    """
    less, equal, greater = [], [], []
    for element in data:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater


def quick_select(items: list, index: int):
    """
    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 5)
    54
    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 1)
    4
    >>> quick_select([5, 4, 3, 2], 2)
    4
    >>> quick_select([3, 5, 7, 10, 2, 12], 3)
    7
    """
    # index = len(items) // 2 when trying to find the median
    #   (value of index when items is sorted)

    # invalid input
    if index >= len(items) or index < 0:
        return None

    pivot = items[random.randint(0, len(items) - 1)]
    count = 0
    smaller, equal, larger = _partition(items, pivot)
    count = len(equal)
    m = len(smaller)

    # index is the pivot
    if m <= index < m + count:
        return pivot
    # must be in smaller
    elif m > index:
        return quick_select(smaller, index)
    # must be in larger
    else:
        return quick_select(larger, index - (m + count))
