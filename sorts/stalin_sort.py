from typing import TypeVar

"""
Stalin-sort is an esoteric sorting algorithm that removes items that are not in order.

Suitable only for totalitarian regimes.
"""

T = TypeVar("T", int, float)


def stalin_sort(comrades: list[T]) -> list[T]:
    """
    Sorts the list in-place using the Stalin-sort algorithm.

    :param comrades: A list of comrades to sort
    :return: The sorted list

    Time Complexity: O(n)

    Examples:
    >>> stalin_sort([0, 5, 3, 2, 2])
    [0, 5]
    >>> stalin_sort([])
    []
    >>> stalin_sort([-2, -5, -45])
    [-2]
    """
    i = 0
    while i < len(comrades) - 1:
        if comrades[i] > comrades[i + 1]:
            comrades.pop(i + 1)
        else:
            i += 1
    return comrades


if __name__ == "__main__":
    import doctest

    doctest.testmod()
