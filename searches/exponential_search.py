#!/usr/bin/env python3

"""
Pure Python implementation of exponential search algorithm

For more information, see the Wikipedia page:
https://en.wikipedia.org/wiki/Exponential_search

For doctests run the following command:
python3 -m doctest -v exponential_search.py

For manual testing run:
python3 exponential_search.py
"""

from __future__ import annotations


def binary_search_by_recursion(
    sorted_collection: list[int], item: int, left: int = 0, right: int = -1
) -> int:
    """Pure implementation of binary search algorithm in Python using recursion

    Be careful: the collection must be ascending sorted otherwise, the result will be
    unpredictable.

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :param left: starting index for the search
    :param right: ending index for the search
    :return: index of the found item or -1 if the item is not found

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
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    if right < left:
        return -1

    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint + 1, right)


def exponential_search(sorted_collection: list[int], item: int) -> int:
    """
    Pure implementation of an exponential search algorithm in Python.
    For more information, refer to:
    https://en.wikipedia.org/wiki/Exponential_search

    Be careful: the collection must be ascending sorted, otherwise the result will be
    unpredictable.

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found

    The time complexity of this algorithm is O(log i) where i is the index of the item.

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
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")

    if sorted_collection[0] == item:
        return 0

    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2

    left = bound // 2
    right = min(bound, len(sorted_collection) - 1)
    return binary_search_by_recursion(sorted_collection, item, left, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Manual testing
    user_input = input("Enter numbers separated by commas: ").strip()
    collection = sorted(int(item) for item in user_input.split(","))
    target = int(input("Enter a number to search for: "))
    result = exponential_search(sorted_collection=collection, item=target)
    if result == -1:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at index {result} in {collection}.")
