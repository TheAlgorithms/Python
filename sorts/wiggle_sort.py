"""
Wiggle Sort.

Given an unsorted array nums, reorder it such
that nums[0] < nums[1] > nums[2] < nums[3]....
For example:
if input numbers = [3, 5, 2, 1, 6, 4]
one possible Wiggle Sorted answer is [3, 5, 1, 6, 2, 4].
"""


def wiggle_sort(nums: list) -> list:
    """
    Python implementation of wiggle.
    Example:
    >>> wiggle_sort([0, 5, 3, 2, 2])
    [0, 5, 2, 3, 2]
    >>> wiggle_sort([])
    []
    >>> wiggle_sort([-2, -5, -45])
    [-45, -2, -5]
    >>> wiggle_sort([-2.1, -5.68, -45.11])
    [-45.11, -2.1, -5.68]
    """
    for i, _ in enumerate(nums):
        if (i % 2 == 1) == (nums[i - 1] > nums[i]):
            nums[i - 1], nums[i] = nums[i], nums[i - 1]

    return nums


if __name__ == "__main__":
    print("Enter the array elements:")
    array = list(map(int, input().split()))
    print("The unsorted array is:")
    print(array)
    print("Array after Wiggle sort:")
    print(wiggle_sort(array))
