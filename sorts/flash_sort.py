"""
Flashsort is a distribution sorting algorithm showing linear
computational complexity O(n) for uniformly distributed
data sets and relatively little additional memory requirement.

Wikipedia: https://en.wikipedia.org/wiki/Flashsort
"""

import math
from collections.abc import Iterable


def bucket_index(
    value: float, min_value: float, max_value: float, swap_index_m: float
) -> float:
    """
    This function returns the bucket index
    Args:
        value: float value
        min_value: minimum array value
        max_value: maximum array value
        swap_index_m: initial swap index
    Returns:
        Float value for bucket index
    Examples:
    >>> bucket_index(10, 1, 20, 2)
    0
    """
    return math.floor(
        (swap_index_m * (value - min_value)) / (max_value - min_value + 1)
    )


def swap_index(
    b_id: int,
    lb: Iterable,
    array: Iterable,
    min_value: float,
    max_value: float,
    swap_index_m: float,
) -> int:
    """
    This function returns the bucket index
    Args:
        b_id: integer index
        lb: temporary list
        array: original unsorted list
        min_value: minimum array value
        max_value: maximum array value
        swap_index_m: initial swap index
    Returns:
        New swap index
    Example:
    >>> swap_index(1, [3, 5, 8], [15, 13, 24, 7, 18, 3, 22, 9], 3, 24, 3)
    3
    """

    for ind in range(lb[b_id - 1], lb[b_id]):
        if bucket_index(array[ind], min_value, max_value, swap_index_m) != b_id:
            break

    return ind


def rearrange(
    i1: int,
    i2: int,
    original_b: int,
    unsorted: Iterable,
    min_value: float,
    max_value: float,
    swap_index_m: float,
    lb: Iterable,
) -> None:
    for i in range(i1, i2):
        b_id = bucket_index(unsorted[i], min_value, max_value, swap_index_m)
        while b_id != original_b:
            s_ind = swap_index(b_id, lb, unsorted, min_value, max_value, swap_index_m)
            unsorted[i], unsorted[s_ind] = unsorted[s_ind], unsorted[i]
            b_id = bucket_index(unsorted[i], min_value, max_value, swap_index_m)


def insertion_sort(unsorted: Iterable) -> Iterable:
    """
    This function is used to insert sort an unsorted
    iterable as a list or a set
    Args:
        unsorted: Iterable object
    Returns:
        Iterable object insert sorted
    Examples:
    >>> insertion_sort([10, 2, 3, 1])
    [1, 2, 3, 10]
    """

    for i in range(1, len(unsorted)):
        key = unsorted[i]
        j = i - 1

        while j >= 0 and key < unsorted[j]:
            unsorted[j + 1] = unsorted[j]
            j -= 1

        unsorted[j + 1] = key

    return unsorted


def flash_sort(unsorted: Iterable) -> Iterable:
    """
    This function is used to flash sort an unsorted
    iterable as a list or a set
    Args:
        unsorted: Iterable object
    Returns:
        Iterable object flash sorted
    Examples:
    >>> flash_sort([15, 13, 24, 7, 18, 3, 22, 9])
    [3, 7, 9, 13, 15, 18, 22, 24]
    """

    # Store length of array and first split point
    n = len(unsorted)
    m = max(math.floor(0.45 * n), 1)

    # Find minimum and maximum values from array
    min_value, max_value = unsorted[0], unsorted[0]
    for i in range(1, n):
        if unsorted[i] > max_value:
            max_value = unsorted[i]
        if unsorted[i] < min_value:
            min_value = unsorted[i]

    if min_value == max_value:
        return

    # Separate elements in each class
    l = [0] * m
    for value in unsorted:
        l[bucket_index(value, min_value, max_value, m)] += 1

    for i in range(1, m):
        l[i] = l[i - 1] + l[i]

    # Rearrange the elements
    for b in range(m - 1):
        if b == 0:
            rearrange(b, l[b], b, unsorted, min_value, max_value, m, l)
        else:
            rearrange(l[b - 1], l[b], b, unsorted, min_value, max_value, m, l)

    # Sort each bucket
    for i in range(m):
        if i == 0:
            unsorted[i : l[i]] = insertion_sort(unsorted[i : l[i]])
        else:
            unsorted[l[i - 1] : l[i]] = insertion_sort(unsorted[l[i - 1] : l[i]])

    return unsorted


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted_array = user_input.split(",")
    print(flash_sort(unsorted_array))
