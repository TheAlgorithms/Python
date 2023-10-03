from __future__ import annotations


def merge(left_half: list, right_half: list) -> list:
    """Merge two sorted lists into a single sorted list."""
    # Your existing code...


def merge_sort(array: list) -> list:
    """Sorts an array using the merge sort algorithm.

    Args:
        array (list): The unsorted list.

    Returns:
        list: A sorted list.

    Examples:
        >>> merge_sort([3, 2, 1])
        [1, 2, 3]
    """
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]

    return merge(merge_sort(left_half), merge_sort(right_half))
