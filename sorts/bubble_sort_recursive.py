"""
A pure Python implementation of the recursive bubble sort algorithm.
"""

from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def bubble_sort_recursive[T: Comparable](collection: list[T]) -> list[T]:
    """
    Sorts a list of comparable items using the recursive Bubble Sort algorithm.

    >>> bubble_sort_recursive([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
    >>> bubble_sort_recursive([])
    []
    >>> bubble_sort_recursive([1])
    [1]
    >>> bubble_sort_recursive([3, 3, 2, 1])
    [1, 2, 3, 3]
    >>> bubble_sort_recursive([-1, 5, 0, -2])
    [-2, -1, 0, 5]
    >>> bubble_sort_recursive(["banana", "apple", "cherry"])
    ['apple', 'banana', 'cherry']
    >>> bubble_sort_recursive([3.14, 1.5, 2.7])
    [1.5, 2.7, 3.14]
    >>> bubble_sort_recursive([1, "two"])  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: ...
    """
    length = len(collection)
    if length <= 1:
        return collection

    swapped = False
    for i in range(length - 1):
        if collection[i + 1] < collection[i]:
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
            swapped = True

    if not swapped:
        return collection

    return [*bubble_sort_recursive(collection[:-1]), collection[-1]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
