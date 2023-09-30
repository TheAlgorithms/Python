"""
Author  : Bama Charan Chhandogi
Date    : October 1, 2023

Kadane's algorithm is a popular algorithm for finding the
maximum subarray sum in a given array of numbers.

"""

from typing import List


def kadanes_algorithm(arr: List[int]) -> int:
    """
    Kadane's Algorithm for finding the maximum subarray sum.

    Args:
        arr (List[int]): A list of numbers.

    Returns:
        int: The maximum subarray sum.
    """
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


# Run doctest to test the function with the examples in the docstring
if __name__ == "__main__":
    import doctest

    doctest.testmod()
