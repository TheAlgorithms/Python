"""
Kadane's Algorithm: Given an array of integers, find the contiguous subarray
with the largest sum.

Example:
    [-2, 1, -3, 4, -1, 2, 1, -5, 4] --> 6 (subarray [4, -1, 2, 1])

Reference: https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""


def kadanes_algorithm(arr: list[int]) -> int:
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Parameters
    ----------
    arr: list[int], the input list of integers

    Returns
    -------
    int: the maximum subarray sum

    >>> kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> kadanes_algorithm([1])
    1
    >>> kadanes_algorithm([-1, -2, -3])
    -1
    >>> kadanes_algorithm([5, 4, -1, 7, 8])
    23
    >>> kadanes_algorithm([0, 0, 0])
    0
    >>> kadanes_algorithm([-2, -3, 4, -1, -2, 1, 5, -3])
    7
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Maximum subarray sum: {kadanes_algorithm(arr)}")
