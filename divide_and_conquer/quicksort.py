from __future__ import annotations


def quick_sort(array: list) -> list:
    """Returns a list of sorted array elements using quick sort.

    >>> from random import shuffle
    >>> array = [-2, 3, -10, 11, 99, 100000, 100, -200]
    >>> shuffle(array)
    >>> quick_sort(array)
    [-200, -10, -2, 3, 11, 99, 100, 100000]

    >>> shuffle(array)
    >>> quick_sort(array)
    [-200, -10, -2, 3, 11, 99, 100, 100000]

    >>> array = [-200]
    >>> quick_sort(array)
    [-200]

    >>> array = [-2, 3, -10, 11, 99, 100000, 100, -200]
    >>> shuffle(array)
    >>> sorted(array) == quick_sort(array)
    True

    >>> array = [-2]
    >>> quick_sort(array)
    [-2]

    >>> array = []
    >>> quick_sort(array)
    []

    >>> array = [10000000, 1, -1111111111, 101111111112, 9000002]
    >>> sorted(array) == quick_sort(array)
    True
    """
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# Refer this for more info https://www.geeksforgeeks.org/quick-sort/
