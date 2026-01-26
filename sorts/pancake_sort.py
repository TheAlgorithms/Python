"""Pancake Sort Algorithm Implementation.

This module provides a pure Python implementation of the Pancake Sort algorithm.
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

from typing import Any


def pancake_sort(arr: list[Any]) -> list[Any]:
    """Sort an array using the Pancake Sort algorithm.

    Pancake sort works by finding the maximum unsorted element, flipping it to
    the top of the array, then flipping the entire unsorted portion to move the
    maximum to its correct position at the end.

    Args:
        arr: A list of comparable items to be sorted.

    Returns:
        The input list sorted in ascending order.

    Time Complexity:
        O(n^2) where n is the length of the array.
        - We iterate n times (once for each position)
        - Each iteration involves finding max O(n) and up to 2 flips O(n)

    Space Complexity:
        O(1) - sorting is done in-place with only constant extra space.

    Examples:
        >>> pancake_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> pancake_sort([])
        []
        >>> pancake_sort([-2, -5, -45])
        [-45, -5, -2]
        >>> pancake_sort([1])
        [1]
        >>> pancake_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
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

    user_input = input("Enter numbers separated by comma: ").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"Unsorted: {unsorted}")
    print(f"Sorted: {pancake_sort(unsorted)}")
