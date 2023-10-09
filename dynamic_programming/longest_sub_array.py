"""
Author  : Yvonne

This is a pure Python implementation of Dynamic Programming solution to the
    longest_sub_array problem.

The problem is  :
Given an array, to find the longest and continuous sub array and get the max sum of the
    sub array in the given array.
"""


def longest_subarray(arr: list):
    """
    Find the longest continuous subarray with the maximum sum.

    Args:
    arr (list): A list of integers.

    Returns:
    A Integer which is the max subarray sum in the whole array.

    Examples:
    >>> longest_subarray([1, 2, 3, 2, 5])
    13

    >>> longest_subarray([5, -4, 3, -2, 1])
    5

    >>> longest_subarray([1, 2, 3, -2, 5])
    9

    >>> longest_subarray([10, 20, -30, 40, 50])
    90

    >>> longest_subarray([])
    0
    """

    if not arr:
        return 0

    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > (current_sum + arr[i]):
            current_sum = arr[i]
        else:
            current_sum += arr[i]

        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
