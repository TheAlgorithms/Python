"""
This is a pure Python implementation of the bogosort algorithm,
also known as permutation sort, stupid sort, slowsort, shotgun sort, or monkey sort.
Bogosort generates random permutations until it guesses the correct one.

More info on: https://en.wikipedia.org/wiki/Bogosort

For doctests run following command:
python -m doctest -v bogo_sort.py
or
python3 -m doctest -v bogo_sort.py
For manual testing run:
python bogo_sort.py
"""

import random
from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def bogo_sort[T: Comparable](collection: list[T]) -> list[T]:
    """Pure implementation of the bogosort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> bogo_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bogo_sort([])
    []
    >>> bogo_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> bogo_sort(["c", "a", "b"])
    ['a', 'b', 'c']
    >>> bogo_sort([2.5, -1.0, 0.0])
    [-1.0, 0.0, 2.5]
    >>> bogo_sort([1, "a"])
    Traceback (most recent call last):
    ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """

    def is_sorted[T: Comparable](collection: list[T]) -> bool:
        for i in range(len(collection) - 1):
            if collection[i + 1] < collection[i]:
                return False
        return True

    while not is_sorted(collection):
        random.shuffle(collection)
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(bogo_sort(unsorted))
