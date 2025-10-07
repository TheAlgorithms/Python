"""
Find the maximum subarray sum (Kadane's Algorithm).
"""


def max_subarray(nums: list[int]) -> int:
    """
    Find the contiguous subarray with the largest sum.

    Args:
        nums: List of integers.

    Returns:
        Maximum sum of subarray.

    Examples:
        >>> max_subarray([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> max_subarray([1])
        1
        >>> max_subarray([5,4,-1,7,8])
        23
    """
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
