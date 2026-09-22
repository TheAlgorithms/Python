"""
A recursive implementation of the insertion sort algorithm
"""

from __future__ import annotations

from collections.abc import MutableSequence
from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def rec_insertion_sort[T](collection: MutableSequence[T], n: int) -> None:
    """
    Given a collection of comparable elements and its length, sorts the
    collection in place in ascending order.

    :param collection: A mutable collection of comparable elements
    :param n: The length of collection

    >>> col = [1, 2, 1]
    >>> rec_insertion_sort(col, len(col))
    >>> col
    [1, 1, 2]

    >>> col = [2, 1, 0, -1, -2]
    >>> rec_insertion_sort(col, len(col))
    >>> col
    [-2, -1, 0, 1, 2]

    >>> col = [1]
    >>> rec_insertion_sort(col, len(col))
    >>> col
    [1]

    >>> col = ['d', 'a', 'b', 'e', 'c']
    >>> rec_insertion_sort(col, len(col))
    >>> col
    ['a', 'b', 'c', 'd', 'e']
    """
    # Checks if the entire collection has been sorted
    if len(collection) <= 1 or n <= 1:
        return

    insert_next(collection, n - 1)
    rec_insertion_sort(collection, n - 1)


def insert_next[T](collection: MutableSequence[T], index: int) -> None:
    """
    Inserts the '(index-1)th' element into place

    >>> col = [3, 2, 4, 2]
    >>> insert_next(col, 1)
    >>> col
    [2, 3, 4, 2]

    >>> col = [3, 2, 3]
    >>> insert_next(col, 2)
    >>> col
    [3, 2, 3]

    >>> col = []
    >>> insert_next(col, 1)
    >>> col
    []
    """
    # Checks order between adjacent elements
    if index >= len(collection) or collection[index - 1] <= collection[index]:
        return

    # Swaps adjacent elements since they are not in ascending order
    collection[index - 1], collection[index] = (
        collection[index],
        collection[index - 1],
    )

    insert_next(collection, index + 1)


if __name__ == "__main__":
    numbers = input("Enter integers separated by spaces: ")
    number_list: list[int] = [int(num) for num in numbers.split()]
    rec_insertion_sort(number_list, len(number_list))
    print(number_list)
