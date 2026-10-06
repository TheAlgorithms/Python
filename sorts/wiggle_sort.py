"""
Wiggle Sort.

Given an unsorted array nums, reorder it such
that nums[0] < nums[1] > nums[2] < nums[3]....
For example:
if input numbers = [3, 5, 2, 1, 6, 4]
one possible Wiggle Sorted answer is [3, 5, 1, 6, 2, 4].
"""

from __future__ import annotations

from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...

    def __gt__(self, other: Any, /) -> bool: ...


def wiggle_sort[T: Comparable](nums: list[T]) -> list[T]:
    """
    Python implementation of wiggle sort.
    Reorders an array such that nums[0] <= nums[1] >= nums[2] <= nums[3]...

    Example:
    >>> wiggle_sort([0, 5, 3, 2, 2])
    [0, 5, 2, 3, 2]
    >>> wiggle_sort([])
    []
    >>> wiggle_sort([-2, -5, -45])
    [-5, -2, -45]
    >>> wiggle_sort([-2.1, -5.68, -45.11])
    [-5.68, -2.1, -45.11]
    >>> wiggle_sort(["d", "a", "c", "b"])
    ['a', 'd', 'b', 'c']
    >>> wiggle_sort([1, "a"])
    Traceback (most recent call last):
        ...
    TypeError: '>' not supported between instances of 'int' and 'str'
    """
    for i in range(1, len(nums)):
        if (i % 2 == 1 and nums[i - 1] > nums[i]) or (
            i % 2 == 0 and nums[i - 1] < nums[i]
        ):
            nums[i - 1], nums[i] = nums[i], nums[i - 1]

    return nums


if __name__ == "__main__":
    print("Enter the array elements:")
    array = list(map(int, input().split()))
    print("The unsorted array is:")
    print(array)
    print("Array after Wiggle sort:")
    print(wiggle_sort(array))
