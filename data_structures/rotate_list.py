"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1, 2, 3, 4, 5, 6, 7] and rotate_index = 3

Output: [5, 6, 7, 1, 2, 3, 4]

Explanation:
rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]
"""
def rotate(nums: [int], rotate_index: int) -> [int]:
    """
    >>> rotate([1, 2, 3, 4, 5, 6, 7], 3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> rotate([1, 2, 3, 4, 5, 6, 7], -3)
    Invalid input provided
    >>> rotate([1, 2, 3, 4, 5, 6, 7], 3.0)
    Invalid input provided
    >>> rotate("TheAlgorithms/Python", -6)
    Invalid input provided
    """
    if rotate_index < 0 or nums != list:
        return "Invalid input provided"
    elif rotate_index >= 0:
        nums[:] = nums[len(nums) - rotate_index:] + nums[:len(nums) - rotate_index]
        return nums
    else:
        return 'Invalid input provided'


if __name__ == "__main__":
    import doctest

    doctest.testmod()
