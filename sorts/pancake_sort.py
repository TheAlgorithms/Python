# sorts/pancake_sort.py
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
from typing import TypeVar

T = TypeVar("T")


def pancake_sort(arr: Sequence[T]) -> list[T]:
    """Sort Array with Pancake Sort.

    :param arr: Collection containing comparable items
    :return: Collection ordered in ascending order of items

    Examples:
    >>> pancake_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> pancake_sort([])
    []
    >>> pancake_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> pancake_sort(["banana", "apple", "orange"])
    ['apple', 'banana', 'orange']

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    cur = len(arr)

    while cur > 1:
        # Find the maximum item in the unsorted portion.
        maximum = max(arr[:cur])
        mi = arr.index(maximum)

        # Move the maximum item to the front.
        arr = arr[mi::-1] + arr[mi + 1 :]

        # Move the maximum item to its final position.
        arr = arr[cur - 1 :: -1] + arr[cur:]

        cur -= 1

    return list(arr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{pancake_sort(unsorted) = }")
