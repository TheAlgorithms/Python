"""
Return the minimum element of an array using the
divide-and-conquer algorithm for selection sort.
Like quick sort algorithm it partitions the input array recursively.
But unlike quicksort,
which recursively processes both sides of the partition,
this algorithm works on only one side of the partition.
The expected running time of this selection sort algorithm is 0(n),
assuming that the elements are distinct.
It returns the ith smallest element of the array A[p: r], where 1 ≤ i ≤ r-p+1.
(From Introduction to Algorithms, Fourth Edition, Cormen, 2022: Chapter 9.2)
"""
from __future__ import annotations
from typing import Any
import random


def partition(array, p, r) -> int:
    """
    Partition the array.
    Args:
        array: list of elements
        p: starting index of the array
        r: ending index of the array

    Returns:
        index of the pivot

    """
    pivot = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def randomized_partition(array, p, r) -> int:
    """
    Randomized partition of the array.
    Args:
        array: list of elements
        p: starting index of the array
        r: ending index of the array

    Returns:
        call to partition function

    """

    rand_idx = random.randint(p, r)
    array[rand_idx], array[r] = array[r], array[rand_idx]
    return partition(array, p, r)


def selection_sort(array: list, p: int, r: int, i: int) -> list | None | Any:
    """
    Returns a list of sorted array elements using selection sort.
    Args:
        array: list of elements
        p: starting index of the array
        r: ending index of the array
        i: the ith smallest element of the array A[p: r], where 1 ≤ i ≤ r-p+1

    Returns:
        sorted array

    >>> from random import shuffle
    >>> arr = [-2, 3, -10, 11, 99, 100000, 100, -200]
    >>> shuffle(arr)
    >>> selection_sort(arr, 0, len(arr) - 1, 1)
    -200

    >>> shuffle(arr)
    >>> selection_sort(arr, 0, len(arr) - 1, 1)
    -200

    >>> arr = [-200]
    >>> selection_sort(arr, 0, len(arr) - 1, 1)
    -200

    >>> arr = [-2]
    >>> selection_sort(arr, 0, len(arr) - 1, 1)
    -2

    >>> arr = []
    >>> selection_sort(arr, 0, len(arr) - 1, 1)
    []
    """

    if array is None or len(array) == 0:
        return array

    if p == r:
        return array[p]  # 1 <= i <= r - p + 1 when p == r means that i == 1

    q = randomized_partition(array, p, r)

    k = q - p + 1

    if i == k:
        return array[q]  # the pivot value is the answer
    elif i < k:
        return selection_sort(array, p, q - 1, i)
    else:
        return selection_sort(array, q + 1, r, i - k)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
