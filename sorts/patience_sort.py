from __future__ import annotations

from bisect import bisect_left
from functools import total_ordering
from heapq import merge
from typing import Protocol

"""
A pure Python implementation of the patience sort algorithm

For more information: https://en.wikipedia.org/wiki/Patience_sorting

This algorithm is based on the card game patience

For doctests run following command:
python3 -m doctest -v patience_sort.py

For manual testing run:
python3 patience_sort.py
"""


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


@total_ordering
class Stack[T: Comparable](list[T]):
    def __lt__(self, other: Stack[T]) -> bool:
        return self[-1] < other[-1]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Stack):
            return NotImplemented
        return self[-1] == other[-1]


def patience_sort[T: Comparable](collection: list[T]) -> list[T]:
    """A pure implementation of patience sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> patience_sort([1, 9, 5, 21, 17, 6])
    [1, 5, 6, 9, 17, 21]

    >>> patience_sort([])
    []

    >>> patience_sort([-3, -17, -48])
    [-48, -17, -3]

    >>> patience_sort(['d', 'a', 'b', 'e']) == sorted(['d', 'a', 'b', 'e'])
    True

    >>> patience_sort([3.3, 1.1, 2.2])
    [1.1, 2.2, 3.3]

    >>> patience_sort([1, "a"])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    stacks: list[Stack] = []
    # sort into stacks
    for element in collection:
        new_stacks = Stack([element])
        i = bisect_left(stacks, new_stacks)
        if i != len(stacks):
            stacks[i].append(element)
        else:
            stacks.append(new_stacks)

    # use a heap-based merge to merge stack efficiently
    collection[:] = merge(*(reversed(stack) for stack in stacks))
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(patience_sort(unsorted))
