import random

"""
A python implementation of the quick select algorithm, which is efficient for calculating the value that would appear in the index of a list if it would be sorted, even if it is not already sorted
https://en.wikipedia.org/wiki/Quickselect
"""


def _partition(data, pivot):
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


def quickSelect(list, k):
    # k = len(list) // 2 when trying to find the median (index that value would be when list is sorted)

    # invalid input
    if k >= len(list) or k < 0:
        return None

    smaller = []
    larger = []
    pivot = random.randint(0, len(list) - 1)
    pivot = list[pivot]
    count = 0
    smaller, equal, larger = _partition(list, pivot)
    count = len(equal)
    m = len(smaller)

    # k is the pivot
    if m <= k < m + count:
        return pivot
    # must be in smaller
    elif m > k:
        return quickSelect(smaller, k)
    # must be in larger
    else:
        return quickSelect(larger, k - (m + count))
