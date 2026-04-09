#!/usr/bin/env python3

"""
Pure Python implementations of binary search algorithms

For doctests run the following command:
python3 -m doctest -v binary_search.py

For manual testing run:
python3 binary_search.py
"""

import bisect
from itertools import pairwise


def bisect_left(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> int:
    """
    Locates the first element in a sorted array that is larger or equal to a given
    value.

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item to bisect
    :param lo: lowest index to consider (as in sorted_collection[lo:hi])
    :param hi: past the highest index to consider (as in sorted_collection[lo:hi])
    :return: index i such that all values in sorted_collection[lo:i] are < item and all
        values in sorted_collection[i:hi] are >= item.

    Examples:
    >>> bisect_left([0, 5, 7, 10, 15], 0)
    0
    >>> bisect_left([0, 5, 7, 10, 15], 6)
    2
    >>> bisect_left([0, 5, 7, 10, 15], 20)
    5
    >>> bisect_left([0, 5, 7, 10, 15], 15, 1, 3)
    3
    >>> bisect_left([0, 5, 7, 10, 15], 6, 2)
    2
    """
    if hi < 0:
        hi = len(sorted_collection)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if sorted_collection[mid] < item:
            lo = mid + 1
        else:
            hi = mid

    return lo


def bisect_right(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> int:
    """
    Locates the first element in a sorted array that is larger than a given value.

    Examples:
    >>> bisect_right([0, 5, 7, 10, 15], 0)
    1
    >>> bisect_right([0, 5, 7, 10, 15], 15)
    5
    >>> bisect_right([0, 5, 7, 10, 15], 6)
    2
    >>> bisect_right([0, 5, 7, 10, 15], 15, 1, 3)
    3
    >>> bisect_right([0, 5, 7, 10, 15], 6, 2)
    2
    """
    if hi < 0:
        hi = len(sorted_collection)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if sorted_collection[mid] <= item:
            lo = mid + 1
        else:
            hi = mid

    return lo


def insort_left(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> None:
    """
    Inserts a given value into a sorted array before other values with the same value.

    Examples:
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 6)
    >>> sorted_collection
    [0, 5, 6, 7, 10, 15]
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 20)
    >>> sorted_collection
    [0, 5, 7, 10, 15, 20]
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 15, 1, 3)
    >>> sorted_collection
    [0, 5, 7, 15, 10, 15]
    """
    sorted_collection.insert(bisect_left(sorted_collection, item, lo, hi), item)


def insort_right(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> None:
    """
    Inserts a given value into a sorted array after other values with the same value.

    Examples:
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 6)
    >>> sorted_collection
    [0, 5, 6, 7, 10, 15]
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 20)
    >>> sorted_collection
    [0, 5, 7, 10, 15, 20]
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 15, 1, 3)
    >>> sorted_collection
    [0, 5, 7, 15, 10, 15]
    """
    sorted_collection.insert(bisect_right(sorted_collection, item, lo, hi), item)


def binary_search(sorted_collection: list[int], item: int) -> int:
    """Pure implementation of a binary search algorithm in Python.

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search([0, 5, 7, 10, 15], 6)
    -1
    """
    if any(a > b for a, b in pairwise(sorted_collection)):
        raise ValueError("sorted_collection must be sorted in ascending order")

    left = 0
    right = len(sorted_collection) - 1
    result = -1

    while left <= right:
        midpoint = left + (right - left) // 2
        if sorted_collection[midpoint] == item:
            result = midpoint
            right = midpoint - 1  # Logic for first occurrence
        elif item < sorted_collection[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return result


def binary_search_std_lib(sorted_collection: list[int], item: int) -> int:
    """Binary search using stdlib.

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)
    -1
    """
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return -1


def binary_search_with_duplicates(sorted_collection: list[int], item: int) -> list[int]:
    """Returns a list of all indexes where the target occurs.

    Examples:
    >>> binary_search_with_duplicates([0, 5, 7, 10, 15], 0)
    [0]
    >>> binary_search_with_duplicates([0, 5, 7, 10, 15], 15)
    [4]
    >>> binary_search_with_duplicates([1, 2, 2, 2, 3], 2)
    [1, 2, 3]
    >>> binary_search_with_duplicates([1, 2, 2, 2, 3], 4)
    []
    """
    left = bisect_left(sorted_collection, item)
    right = bisect_right(sorted_collection, item)

    if left == len(sorted_collection) or sorted_collection[left] != item:
        return []
    return list(range(left, right))


def binary_search_by_recursion(
    sorted_collection: list[int], item: int, left: int = 0, right: int = -1
) -> int:
    """Recursive binary search.

    Examples:
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 0, 0, 4)
    0
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 15, 0, 4)
    4
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 5, 0, 4)
    1
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 6, 0, 4)
    -1
    """
    if right < 0:
        right = len(sorted_collection) - 1

    if right < left:
        return -1

    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        if midpoint > left:
            res = binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)
            return res if res != -1 else midpoint
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint + 1, right)


def exponential_search(sorted_collection: list[int], item: int) -> int:
    """Exponential search algorithm.

    Examples:
    >>> exponential_search([0, 5, 7, 10, 15], 0)
    0
    >>> exponential_search([0, 5, 7, 10, 15], 15)
    4
    >>> exponential_search([0, 5, 7, 10, 15], 5)
    1
    >>> exponential_search([0, 5, 7, 10, 15], 6)
    -1
    """
    if not sorted_collection:
        return -1
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2
    left = bound // 2
    right = min(bound, len(sorted_collection) - 1)
    return binary_search_by_recursion(sorted_collection, item, left, right)


searches = (
    binary_search_std_lib,
    binary_search,
    exponential_search,
    binary_search_by_recursion,
)


if __name__ == "__main__":
    import doctest
    doctest.testmod()