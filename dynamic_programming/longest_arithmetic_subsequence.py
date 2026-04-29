"""
Longest Arithmetic Subsequence Problem: Given an array nums of integers,
return the length of the longest arithmetic subsequence in nums.

Note that:
- A subsequence is an array that can be derived from another array by
deleting some or no elements without changing the order of the remaining elements.
- A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value
(for 0 <= i < seq.length - 1).
"""


def longest_arithmetic_subsequence(nums: list[int]) -> int:
    """
    Finds the length of the longest arithmetic subsequence in a given array of integers.

    Parameters
    ----------
    nums : list[int]
        The input array of integers.

    Returns
    -------
    int
        The length of the longest arithmetic subsequence.

    Examples
    --------
    >>> longest_arithmetic_subsequence([3, 6, 9, 12])
    4
    >>> longest_arithmetic_subsequence([9, 4, 7, 2, 10])
    3
    >>> longest_arithmetic_subsequence([20, 1, 15, 3, 10, 5, 8])
    4
    >>> longest_arithmetic_subsequence([])  # Empty array
    0
    >>> longest_arithmetic_subsequence(None)  # Null array
    Traceback (most recent call last):
        ...
    ValueError: Input array cannot be None
    """
    if nums is None:
        raise ValueError("Input array cannot be None")

    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return 1

    dp: list[dict[int, int]] = [{} for _ in range(len(nums))]
    max_length = 2

    for i in range(len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            max_length = max(max_length, dp[i][diff])

    return max_length


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # test cases
    test_cases = [
        ([3, 6, 9, 12], 4),
        ([3, 6, 9, 12, 15], 5),
        ([1, 7, 10, 13, 14, 19], 4),
        ([1, 2, 3, 4], 4),
        ([], 0),
        ([10], 1),
        ([9, 4, 7, 2, 10], 3),
        ([1, 2, 2, 2, 2, 5], 4),
    ]

    for nums, expected_length in test_cases:
        result = longest_arithmetic_subsequence(nums)
        print(f"Test case {nums}: Expected {expected_length}, Got {result}")
        assert result == expected_length, f"Test failed for input {nums}"
