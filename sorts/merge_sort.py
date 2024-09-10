"""
Merge Sort Algorithm
====================

This module implements the Merge Sort algorithm with three variations:
1. Recursive Merge Sort
2. Iterative Merge Sort
3. Merge Insertion Sort

Usage:
    - Run this module directly for manual testing.
    - Use doctests to verify correctness.

Example:
    python merge_sort.py
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Perform merge sort on a list of integers.

    Args:
        arr: A list of integers.

    Returns:
        A sorted list of integers.

    Example:
        >>> merge_sort([8, 3, 5, 6])
        [3, 5, 6, 8]
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def iterative_merge_sort(arr: List[int]) -> List[int]:
    """
    Perform iterative merge sort on a list of integers.

    Args:
        arr: A list of integers.

    Returns:
        A sorted list of integers.

    Example:
        >>> iterative_merge_sort([8, 3, 5, 6])
        [3, 5, 6, 8]
    """
    if len(arr) <= 1:
        return arr

    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i : i + width]
            right = arr[i + width : i + 2 * width]
            merged = merge(left, right)
            arr[i : i + len(merged)] = merged
        width *= 2

    return arr


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists into a single sorted list.

    Args:
        left: A sorted list of integers.
        right: A sorted list of integers.

    Returns:
        A merged and sorted list of integers.

    Example:
        >>> merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_insertion_sort(arr: List[int]) -> List[int]:
    """
    Perform merge insertion sort on a list of integers.

    Args:
        arr: A list of integers.

    Returns:
        A sorted list of integers.

    Example:
        >>> merge_insertion_sort([8, 3, 5, 6])
        [3, 5, 6, 8]
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_insertion_sort(left)
    right = merge_insertion_sort(right)

    return merge(left, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
