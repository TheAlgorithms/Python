"""
https://en.wikipedia.org/wiki/Shellsort#Pseudocode
"""

from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def shell_sort(collection: list[T]) -> list[T]:
    """Pure implementation of shell sort algorithm in Python.

    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending

    Examples:
    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> shell_sort(["c", "a", "b"])
    ['a', 'b', 'c']
    >>> shell_sort([2.5, -1.0, 0.0])
    [-1.0, 0.0, 2.5]
    >>> shell_sort([0, 5, 3, 2, 2]) == sorted([0, 5, 3, 2, 2])
    True
    >>> shell_sort(["c", "a", "b"]) == sorted(["c", "a", "b"])
    True
    """
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(collection)):
            insert_value = collection[i]
            j = i
            while j >= gap and insert_value < collection[j - gap]:
                collection[j] = collection[j - gap]
                j -= gap
            if j != i:
                collection[j] = insert_value
    return collection


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(shell_sort(unsorted))
