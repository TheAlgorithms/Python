"""
Shell Sort Algorithm
--------------------

Issue: #13887
Implements the Shell Sort algorithm which is a generalization of insertion sort.
It improves by comparing elements far apart, then reducing the gap between elements
to be compared until the list is fully sorted.

Time Complexity:
    Worst case: O(n^2)
    Best case:  O(n log n)
    Average:    O(n^(3/2))

Space Complexity: O(1)
"""

from __future__ import annotations


def shell_sort(arr: list[int]) -> list[int]:
    """
    Sorts the given list using Shell Sort and returns the sorted list.

    >>> shell_sort([5, 2, 9, 1])
    [1, 2, 5, 9]
    >>> shell_sort([])
    []
    >>> shell_sort([3])
    [3]
    >>> shell_sort([1, 2, 3])
    [1, 2, 3]
    >>> shell_sort([4, 3, 3, 1])
    [1, 3, 3, 4]
    """
    n = len(arr)
    gap = n // 2

    # Keep reducing the gap until it becomes 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr
