"""
Calculate the Maximum Sum Subarray using Kadane's Algorithm.
reference: https://en.wikipedia.org/wiki/Maximum_subarray_problem

Kadane's Algorithm solves the maximum sum subarray problem in O(n) time. Given an array
of integers, the goal is to find the contiguous subarray with the maximum sum.

For example, in the array [-2,1,-3,4,-1,2,1,-5,4], the maximum sum subarray is [4,-1,2,1],
with a sum of 6.

Example Input:
[-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Python doctests can be run with the following command:
python -m doctest -v kadanes_algorithm.py
"""


def kadanes_algorithm(arr: list[int]) -> int:
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Args:
        arr: A list of integers, both positive and negative.

    Returns:
        int: The maximum sum of any contiguous subarray.

    Examples:
        >>> kadanes_algorithm([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> kadanes_algorithm([1])
        1
        >>> kadanes_algorithm([-1,-2,-3,-4])
        -1
        >>> kadanes_algorithm([4,-1,2,1])
        6
        >>> kadanes_algorithm([0,0,0,0])
        0
        >>> kadanes_algorithm([5,-3,5])
        7
        >>> kadanes_algorithm([-2, -3, 4, -1, -2, 1, 5, -3])
        7
        >>> kadanes_algorithm([-1, 1])
        1
        >>> kadanes_algorithm([3.5, -2, 3])
        4.5
    """
    if not arr:
        return 0

    # Initialize the maximums
    max_current = max_global = arr[0]

    # Traverse the array, updating the max values
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current

    return max_global


if __name__ == "__main__":
    import doctest

    doctest.testmod()
