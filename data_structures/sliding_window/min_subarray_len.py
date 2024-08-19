from typing import List


def min_subarray_len(target_sum: int, numbers: List[int]) -> int:
    """
    Finds the minimal length of a contiguous subarray of which the sum is at least the target.[https://www.geeksforgeeks.org/window-sliding-technique/]


    Args:
    target (int): The target sum.
    nums (list): The list of positive integers.

    Returns:
    int: The minimal length of a contiguous subarray with a sum at least equal to the target, or 0 if no such subarray exists.

    Examples:
    >>> min_subarray_len(7, [2,3,1,2,4,3])
    2
    >>> min_subarray_len(4, [1,4,4])
    1
    >>> min_subarray_len(11, [1,1,1,1,1,1,1,1])
    0
    >>> min_subarray_len(15, [5,1,3,5,10,7,4,9,2,8])
    2
    """
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float("inf")

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float("inf") else 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
