"""
This is a pure Python implementation of the pancake sort algorithm.

Pancake sort works by repeatedly finding the maximum element in the unsorted
portion and flipping the subarray from the beginning to that position, then
flipping the entire unsorted portion to move the maximum to its correct position.

For doctests run following command:
python3 -m doctest -v pancake_sort.py
or
python -m doctest -v pancake_sort.py

For manual testing run:
python pancake_sort.py
"""

from collections.abc import Collection
from typing import Any


def pancake_sort(arr: list) -> list:
    """Sort a list using Pancake Sort.

    Args:
        arr: A list of comparable items.

    Returns:
        A new list with items ordered in ascending order.

    Examples:
    >>> pancake_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> pancake_sort([])
    []
    >>> pancake_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    if not arr:
        return []

    result = arr.copy()
    cur = len(result)

    while cur > 1:
        # Find the index of the maximum number in the unsorted portion
        max_index = result[:cur].index(max(result[:cur]))

        # Flip from 0 to max_index to move max to the front
        result[: max_index + 1] = result[: max_index + 1][::-1]

        # Flip from 0 to cur-1 to move max to its correct position
        result[:cur] = result[:cur][::-1]

        cur -= 1

    return result


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(pancake_sort(unsorted))
