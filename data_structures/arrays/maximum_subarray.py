"""
Kadane's Algorithm is an efficient method to find the maximum
sum of a contiguous subarray within a one-dimensional array of
numbers. It maintains two key values as we traverse the array:
the current maximum sum ending at the current index and the
global maximum sum found so far.
"""

# Advantages
"""
- Efficiency: Runs in linear time, `O(n)`.
- Simplicity: Straightforward to implement and understand.
- Versatility: Easily adaptable to related problems.
"""

# Time Complexity
"""
- Time Complexity: `O(n)` - processes each element once.
- Space Complexity: `O(1)` - uses a fixed amount of extra space.
"""

"""
Find the Maximum Subarray Sum using Kadane's Algorithm.
Reference: https://leetcode.com/problems/maximum-subarray/

Python doctest can be run with the following command:
python -m doctest -v maximum_subarray.py

Given an integer array nums, this function returns
the maximum sum of a contiguous subarray.

A subarray is a contiguous part of an array.

Example Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
"""

def max_subarray_sum(nums: list[int]) -> int:
    """
    Find the maximum subarray sum using Kadane's Algorithm.

    Args:
        nums (list[int]): The input array of integers.

    Returns:
        int: The maximum subarray sum.

    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> max_subarray_sum([1])
        1
        >>> max_subarray_sum([5, 4, -1, 7, 8])
        23
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
    """
    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global


if __name__ == "__main__":
    import doctest

    doctest.testmod()