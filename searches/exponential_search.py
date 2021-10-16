#!/usr/bin/env python3

"""
This is pure Python implementation of exponential search algorithms

For doctests run following command:
python3 -m doctest -v exponential_search.py

For manual testing run:
python3 exponential_search.py
"""


def binary_search(sequence: list, left: int, right: int, target: int) -> int:
    """
    This is a recursive python implementation of binary search intended
    to be used in conjunction with the following exponential sort algorithm

    :param sequence: A sequence of comparable items sorted ascendingly
    :param left: The left bound of the section of the sequence being searched
    :param right: The right bound of the section of the sequence being searched
    :param target: item value to search
    :return: index of found item or None if item is not found

    Example:
    >>> binary_search([1,2,3,4,5], 0, 4, 3)
    2
    >>> binary_search([1,2,3,4,5], 0, 4, 6)
    -1
    """
    if left > right:
        return -1

    mid = (left + right) // 2

    if sequence[mid] == target:
        return mid
    if sequence[mid] > target:
        return binary_search(sequence, left, mid - 1, target)
    return binary_search(sequence, mid + 1, right, target)


def exponential_search(sequence: list, target: int) -> int:
    """
    This is a python implementation of the exponential search algorithm

    Make sure that the sequence being searched is sorted ascendingly or
    the algorithm may not work as expected.

    https://en.wikipedia.org/wiki/Exponential_search

    :param sequence: A sequence of comparable items sorted ascendingly
    :param target: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> exponential_search([1, 2, 3, 4, 5], 3)
    2
    >>> exponential_search([0, 5, 7, 10, 15], 15)
    4
    >>> exponential_search(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'], "J")
    9
    >>> exponential_search([0, 1, 2, 3, 4], 10)
    -1
    """
    if sequence[0] == target:
        return 0

    i = 1
    while i < len(sequence) and sequence[i] <= target:
        i *= 2

    return binary_search(sequence, i // 2, min(i, len(sequence) - 1), target)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]

    target = int(input("Enter a single number to be found in the list:\n").strip())
    result = exponential_search(sequence, target)
    if result == -1:
        print(f"{target} was not found in {sequence}")
    else:
        print(f"exponential_search({sequence}, {target}) = {result}")
