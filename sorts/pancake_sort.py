"""
This is a pure Python implementation of the pancake sort algorithm

For doctests run following command:
python3 -m doctest -v pancake_sort.py
or
python -m doctest -v pancake_sort.py
For manual testing run:
python pancake_sort.py
"""

from collections.abc import Sequence
from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def pancake_sort[T: Comparable](arr: Sequence[T]) -> list[T]:
    """Sort Array with Pancake Sort.

    :param arr: some ordered collection with heterogeneous comparable items
    inside
    :return: the same collection ordered by ascending

    Examples:
    >>> pancake_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> pancake_sort([])
    []
    >>> pancake_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> pancake_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> pancake_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> pancake_sort(collection) == sorted(collection)
    True
    """
    arr = list(arr)
    cur = len(arr)
    while cur > 1:
        # Find the maximum number in arr
        mi = arr.index(max(arr[0:cur]))
        # Reverse from 0 to mi
        arr = arr[mi::-1] + arr[mi + 1 : len(arr)]
        # Reverse whole list
        arr = arr[cur - 1 :: -1] + arr[cur : len(arr)]
        cur -= 1
    return arr


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(pancake_sort(unsorted))
