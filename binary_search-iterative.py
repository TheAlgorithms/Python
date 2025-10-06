"""
https://en.wikipedia.org/wiki/Binary_search_algorithm

Binary Search Algorithm (Iterative)
-----------------------------------
Binary search is a search algorithm that finds the position of a target value
within a sorted array. It compares the target value to the middle element of the
array; if they are unequal, the half in which the target cannot lie is eliminated,
and the search continues on the remaining half until it is successful.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


def binary_search_iterative(arr: List[int], target: int) -> int:
    """
    Perform binary search on a sorted list to find the index of the target element.

    Args:
        arr (List[int]): Sorted list of integers.
        target (int): The element to search for.

    Returns:
        int: The index of `target` in `arr`, or -1 if not found.

    Examples:
        >>> binary_search_iterative([1, 3, 5, 7, 9], 7)
        3
        >>> binary_search_iterative([1, 3, 5, 7, 9], 2)
        -1
        >>> binary_search_iterative([], 5)
        -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
