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

import random
from typing import Any


def partition(array: list, starting_index: int, ending_index: int) -> int:
    """
    Partition the array.
    Args:
        array: list of elements
        starting_index: starting index of the array
        ending_index: ending index of the array

    Returns:
        index of the pivot


    >>> arr = [-2, 3, -10, 11, 99, 100000, 100, -200]
    >>> partition(arr, 0, len(arr) - 1)
    0

    """
    pivot = array[ending_index]
    i = starting_index - 1
    for j in range(starting_index, ending_index):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[ending_index] = array[ending_index], array[i + 1]
    return i + 1


def randomized_partition(array: list, starting_index: int, ending_index: int) -> int:
    """
    Randomized partition of the array.
    Args:
        array: list of elements
        starting_index: starting index of the array
        ending_index: ending index of the array

    Returns:
        call to partition function


    >>> arr = [-2, 3, -10, 11, 99, 100000, 100, -200]
    >>> arr1 = randomized_partition(arr, 0, len(arr) - 1)
    >>> arr == arr1
    False

    """

    rand_idx = random.randint(starting_index, ending_index)
    array[rand_idx], array[ending_index] = array[ending_index], array[rand_idx]
    return partition(array, starting_index, ending_index)


def selection_sort(
    array: list, starting_index: int, ending_index: int, smallest_element: int
) -> list | None | Any:
    """
    Returns a list of sorted array elements using selection sort.
    Args:
        array: list of elements
        starting_index: starting index of the array
        ending_index: ending index of the array
        smallest_element: the ith smallest element of
                          the array A[p: r], where 1 ≤ i ≤ r-p+1

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

    if starting_index == ending_index:
        # 1 <= i <= r - p + 1 when p == r means that i == 1
        return array[starting_index]

    q = randomized_partition(array, starting_index, ending_index)

    k = q - starting_index + 1

    if smallest_element == k:
        return array[q]  # the pivot value is the answer
    elif smallest_element < k:
        return selection_sort(array, starting_index, q - 1, smallest_element)
    else:
        return selection_sort(array, q + 1, ending_index, smallest_element - k)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
