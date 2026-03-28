"""
A Python implementation of the quick select algorithm, which is efficient for
calculating the value that would appear in the index of a list if it would be
sorted, even if it is not already sorted.
https://en.wikipedia.org/wiki/Quickselect

Time Complexity:
    Average: O(n)
    Worst:   O(n^2)
"""

import random
from typing import List, Optional, Tuple


def _partition(data: List[int], pivot: int) -> Tuple[List[int], List[int], List[int]]:
    """
    Partition the input list into three lists relative to a pivot.

    Args:
        data (List[int]): Input list.
        pivot (int): Pivot value.

    Returns:
        Tuple[List[int], List[int], List[int]]:
            Lists of elements less than, equal to, and greater than the pivot.
    """
    less, equal, greater = [], [], []
    for element in data:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater


def quick_select(items: List[int], index: int) -> Optional[int]:
    """
    Return the element that would appear at the given index if the list
    were sorted, without fully sorting the list.

    Args:
        items (List[int]): The unsorted input list.
        index (int): The zero-based target index in the sorted order.

    Returns:
        Optional[int]: The element at the given sorted index, or None for
        invalid input.

    Time Complexity:
        Average: O(n)
        Worst:   O(n^2)

    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 5)
    54
    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 1)
    4
    >>> quick_select([5, 4, 3, 2], 2)
    4
    >>> quick_select([3, 5, 7, 10, 2, 12], 3)
    7
    >>> quick_select([], 0) is None
    True
    """
    if not items:
        return None

    if not 0 <= index < len(items):
        return None

    pivot = random.choice(items)
    smaller, equal, greater = _partition(items, pivot)

    count = len(equal)
    m = len(smaller)

    # index is the pivot
    if m <= index < m + count:
        return pivot
    # must be in smaller
    elif m > index:
        return quick_select(smaller, index)
    # must be in greater
    else:
        return quick_select(greater, index - (m + count))


def median(items: List[int]) -> Optional[float]:
    """
    Find the median of an unsorted list using Quickselect.

    One common application of Quickselect is finding the median, which is
    the middle element (or average of the two middle elements) in a sorted
    dataset. It works efficiently on unsorted lists by partially sorting the
    data without fully sorting the entire list.

    Args:
        items (List[int]): The input list.

    Returns:
        Optional[float]: The median value, or None if the list is empty.

    >>> median([3, 2, 2, 9, 9])
    3
    >>> median([2, 2, 9, 9, 9, 3])
    6.0
    >>> median([]) is None
    True
    """
    if not items:
        return None

    mid, rem = divmod(len(items), 2)
    if rem != 0:
        return quick_select(items=items, index=mid)
    else:
        low_mid = quick_select(items=items, index=mid - 1)
        high_mid = quick_select(items=items, index=mid)
        return (low_mid + high_mid) / 2
