"""
Pure Python implementation of the sentinel linear search algorithm.

For doctests run the following command:
python3 -m doctest -v sentinel_linear_search.py
"""

from typing import Any


def sentinel_linear_search(sequence: list[Any], target: Any) -> int | None:
    """Pure implementation of sentinel linear search algorithm in Python.

    :param sequence: list of comparable items
    :param target: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 0)
    0
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 15)
    4
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 5)
    1
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 6) is None
    True
    >>> sentinel_linear_search([], 1) is None
    True
    >>> sentinel_linear_search([-10, -5, 0, 5, 10], -5)
    1
    >>> sentinel_linear_search([1, 2, 2, 3], 2)
    1
    >>> sentinel_linear_search(["apple", "banana", "cherry"], "banana")
    1
    >>> sentinel_linear_search(["apple", "banana", "cherry"], "durian") is None
    True
    >>> sentinel_linear_search([42], 42)
    0
    >>> sentinel_linear_search([42], 0) is None
    True
    """
    sequence.append(target)

    index = 0
    while sequence[index] != target:
        index += 1

    sequence.pop()

    if index == len(sequence):
        return None

    return index


if __name__ == "__main__":
    import doctest

    doctest.testmod()
