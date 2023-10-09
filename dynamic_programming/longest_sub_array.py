"""
Author  : Yvonne

This is a pure Python implementation of Dynamic Programming solution to the
    longest_sub_array problem.

The problem is  :
Given an array, to find the longest and continuous sub array and get the max sum of the
    sub array in the given array.
"""


def longest_sub_array(arr: list):
    """
    Find the longest continuous subarray with the maximum sum within a given list of integers.

    Args:
    arr (list): A list of integers.

    Returns:
    A Integer which is the max subarray sum in the whole array.

    Examples:
    >>> longest_sub_array([1, 2, 3, 2, 5])
    13

    >>> longest_sub_array([5, -4, 3, -2, 1])
    5

    >>> longest_sub_array([1, 2, 3, -2, 5])
    9

    >>> longest_sub_array([10, 20, -30, 40, 50])
    90

    >>> longest_sub_array([])
    0
    """

    max_so_far = arr[0]
    max_ending_here = arr[0]
    max_len = 1
    curr_len = 1

    for i in range(1, len(arr)):
        if max_ending_here < 0:
            max_ending_here = arr[i]
            curr_len = 1
        else:
            max_ending_here += arr[i]
            curr_len += 1
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            max_len = curr_len
        elif max_ending_here == max_so_far:
            max_len = max(max_len, curr_len)

    return max_len


if __name__ == "__main__":
    import doctest

    doctest.testmod()
