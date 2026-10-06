"""
A pure Python implementation of the Stalin sort algorithm.

For doctests run the following command:
    python3 -m doctest -v stalin_sort.py

For manual testing run:
    python3 stalin_sort.py
"""

from typing import Any, Protocol


class Comparable(Protocol):
    def __ge__(self, other: Any, /) -> bool: ...


def stalin_sort[T: Comparable](sequence: list[T]) -> list[T]:
    """Sort a list of mutually comparable items using the Stalin sort algorithm.

    Iterates through the sequence and retains elements that are greater than
    or equal to the last retained element, discarding any out-of-order items.

    Reference: https://medium.com/@kaweendra/the-ultimate-sorting-algorithm-6513d6968420

    Complexity Analysis:
        - Time Complexity: O(n) where n is the number of elements in the list.
        - Space Complexity: O(n) auxiliary space for the output list.

    Examples:
    >>> stalin_sort([4, 3, 5, 2, 1, 7])
    [4, 5, 7]
    >>> stalin_sort([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> stalin_sort([4, 5, 5, 2, 3])
    [4, 5, 5]
    >>> stalin_sort([6, 11, 12, 4, 1, 5])
    [6, 11, 12]
    >>> stalin_sort([5, 0, 4, 3])
    [5]
    >>> stalin_sort([5, 4, 3, 2, 1])
    [5]
    >>> stalin_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> stalin_sort([1, 2, 8, 7, 6])
    [1, 2, 8]
    >>> stalin_sort([])
    []
    >>> stalin_sort([7])
    [7]
    >>> stalin_sort([2.5, -1.0, 0.0, 3.2])
    [2.5, 3.2]
    >>> stalin_sort(["d", "a", "e", "c", "f"])
    ['d', 'e', 'f']
    >>> stalin_sort([1, "a"])
    Traceback (most recent call last):
        ...
    TypeError: '>=' not supported between instances of 'str' and 'int'
    """
    if not sequence:
        return []

    result = [sequence[0]]
    for element in sequence[1:]:
        if element >= result[-1]:
            result.append(element)

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
