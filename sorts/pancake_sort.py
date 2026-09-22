"""Pancake Sort Algorithm Implementation.

A pure Python implementation of the Pancake Sort algorithm.
Pancake sort is a sorting algorithm that sorts an array by repeatedly flipping
subsections of the array, similar to how you might sort a stack of pancakes
by inserting a spatula and flipping the top portion.

The algorithm works by finding the maximum element, flipping it to the top,
then flipping it down to its correct position. This process is repeated for
the remaining unsorted portion.

Time Complexity: O(n^2) - We perform n iterations, each with up to 2 flips
Space Complexity: O(1) - In-place sorting, only uses a constant amount of extra space

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

    Time Complexity: (O(n^2))
    Space Complexity: (O(n))

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
        # Find the index of maximum element in arr[0:cur]
        max_index = arr.index(max(arr[:cur]))
        # Move maximum element to end of current unsorted portion:
        # 1. Flip to bring max to the beginning
        arr[: max_index + 1] = reversed(arr[: max_index + 1])
        # 2. Flip to send max to position cur-1
        arr[:cur] = reversed(arr[:cur])
        cur -= 1
    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{unsorted = }, {pancake_sort(unsorted) = }")
