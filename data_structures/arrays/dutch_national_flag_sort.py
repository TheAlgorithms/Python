"""
Implements the Dutch National Flag algorithm to sort an array of 0s, 1s, and 2s
in-place. Includes error handling for invalid values and examples in the docstring.

This algorithm runs in O(n) time and O(1) space using three pointers.
See: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""

from __future__ import annotations


def dutch_flag_sort(arr: list[int]) -> None:
    """
    Sorts an array of 0s, 1s, and 2s in-place.

    Args:
        arr: List containing only 0, 1, or 2.

    Returns:
        None

    Raises:
        ValueError: If array contains values other than 0, 1, or 2.

    Examples:
        >>> arr = [2, 0, 2, 1, 1, 0]
        >>> dutch_flag_sort(arr)
        >>> arr
        [0, 0, 1, 1, 2, 2]

        >>> arr = [2, 0, 1]
        >>> dutch_flag_sort(arr)
        >>> arr
        [0, 1, 2]

        >>> arr = []
        >>> dutch_flag_sort(arr)
        >>> arr
        []

        >>> arr = [1]
        >>> dutch_flag_sort(arr)
        >>> arr
        [1]

        >>> arr = [0, 0, 0]
        >>> dutch_flag_sort(arr)
        >>> arr
        [0, 0, 0]

        >>> arr = [3]
        >>> dutch_flag_sort(arr)
        Traceback (most recent call last):
        ...
        ValueError: Array contains invalid value: 3

        >>> arr = [-1, 0, 1]
        >>> dutch_flag_sort(arr)
        Traceback (most recent call last):
        ...
        ValueError: Array contains invalid value: -1

        >>> arr = [2, 0, '1']
        >>> dutch_flag_sort(arr)
        Traceback (most recent call last):
        ...
        ValueError: Array contains invalid value: 1
    """
    if not arr:
        return

    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        value = arr[mid]
        if value == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif value == 1:
            mid += 1
        elif value == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            msg = f"Array contains invalid value: {value}"
            raise ValueError(msg)


if __name__ == "__main__":
    examples = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [],
        [1],
        [0, 0, 0],
        [2, 2, 2],
        [1, 1, 1],
        [0, 1, 2, 0, 1, 2],
        [2, 1, 0, 2, 1, 0],
    ]

    for test_arr in examples:
        arr = test_arr.copy()
        print(f"Before: {arr}")
        dutch_flag_sort(arr)
        print(f"After : {arr}\n")
