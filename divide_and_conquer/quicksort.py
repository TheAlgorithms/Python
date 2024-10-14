from __future__ import annotations


def quicksort(array: list) -> list:
    """
    Returns a sorted list using the quicksort algorithm.

    Quicksort uses a divide-and-conquer approach to sort the elements
    by selecting a pivot and partitioning the array.

    >>> quicksort([-2, 3, -10, 11, 99, 100000, 100, -200])
    [-200, -10, -2, 3, 11, 99, 100, 100000]

    >>> quicksort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    >>> quicksort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> quicksort([-200])
    [-200]

    >>> quicksort([])
    []

    >>> quicksort([10000000, 1, -1111111111, 101111111112, 9000002])
    [-1111111111, 1, 9000002, 10000000, 101111111112]

    >>> quicksort([2, 1])
    [1, 2]
    """
    if len(array) <= 1:
        return array

    pivot = array[-1]  # Choose the last element as the pivot
    left = [x for x in array[:-1] if x <= pivot]
    right = [x for x in array[:-1] if x > pivot]

    return [*quicksort(left), pivot, *quicksort(right)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
