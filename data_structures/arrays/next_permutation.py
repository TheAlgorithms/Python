"""
author: Aayush Soni
Given an array of integers nums, find the next permutation of nums.

Example: nums = [1, 2, 3, 4]
output: [1, 2, 4, 3]

Leetcode: https://leetcode.com/problems/next-permutation/
"""


def next_permutation(nums: list[int]) -> None:
    """
    :param nums: The list of integers for which the
        next permutation needs to be found.

    Example:
    >>> nums = [1, 2, 3]
    >>> next_permutation(nums)
    >>> nums
    [1, 3, 2]

    >>> nums = [3, 2, 1]
    >>> next_permutation(nums)
    >>> nums
    [1, 2, 3]

    >>> nums = [1, 3, 2, 4, 5, 6]
    >>> next_permutation(nums)
    >>> nums
    [1, 3, 2, 4, 6, 5]
    """

    nums_len = len(nums)
    # Find the pivot element.
    # A pivot is the first element from
    # the end of the sequence that doesn't follow
    # the property of non-increasing suffix.
    pivot_index = nums_len - 2

    while pivot_index >= 0:
        if nums[pivot_index] < nums[pivot_index + 1]:
            break
        pivot_index -= 1

    # Check if a pivot is not found.
    if pivot_index < 0:
        nums.reverse()

    # If a pivot is found.
    else:
        # Find the successor of the pivot in the suffix.
        successor_index = nums_len - 1
        while successor_index > pivot_index:
            if nums[successor_index] > nums[pivot_index]:
                break
            successor_index -= 1

        # Swap the pivot and the successor.
        nums[pivot_index], nums[successor_index] = (
            nums[successor_index],
            nums[pivot_index],
        )

        # Minimize the suffix part.
        start, end = pivot_index + 1, nums_len

        # Reverse the suffix.
        nums[start:end] = nums[start:end][::-1]


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    next_permutation(nums)
    print(nums)

    import doctest

    doctest.testmod()
