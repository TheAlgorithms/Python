"""
Wiggle Sort.

Given an unsorted array nums, reorder it such
that nums[0] < nums[1] > nums[2] < nums[3]....
For example:
if input numbers = [3, 5, 2, 1, 6, 4]
one possible Wiggle Sorted answer is [3, 5, 1, 6, 2, 4].
"""


def wiggle_sort(nums: list) -> list:
    """Perform Wiggle Sort.
    >>> arr = [3, 5, 2, 1, 6, 4]
    >>> wiggle_sort(arr)
    >>> arr
    [3, 5, 1, 6, 2, 4]
    """
    for i, j in enumerate(nums):
        if (i % 2 == 1) == (nums[i - 1] > j):
            nums[i - 1], nums[i] = j, nums[i - 1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Enter the array elements:\n")
    array = [int(x) for x in input().split()]
    print("The unsorted array is:\n")
    print(array)
    wiggle_sort(array)
    print("Array after Wiggle sort:\n")
    print(array)
