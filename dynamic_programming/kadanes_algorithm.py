"""
Kadane's Algorithm
Find the maximum sum of a contiguous subarray.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_subarray_sum(arr: List[int]) -> int:
    """
    Find the maximum sum of a contiguous subarray.

    >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> max_subarray_sum([1])
    1
    >>> max_subarray_sum([5, 4, -1, 7, 8])
    23
    """
    if not arr:
        raise ValueError("Array must not be empty")

    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
