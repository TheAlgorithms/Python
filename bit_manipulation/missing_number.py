def find_missing_number(nums: list[int]) -> int:
    """
    Finds the missing number in a list of consecutive integers.

    Args:
        nums: A list of integers.

    Returns:
        The missing number.

    Example:
        >>> find_missing_number([1, 3, 4, 5, 6])
        2
    """
    n = len(nums)
    expected_sum = (n + 1) * (nums[0] + nums[-1]) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum
