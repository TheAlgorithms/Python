def find_missing_number(nums: list[int]) -> int:
    """
    Finds the missing number in a list of consecutive integers.

    Args:
        nums: A list of integers.

    Returns:
        The missing number.

    Example:
        >>> find_missing_number([0, 1, 3, 4])
        2
    """
    n = len(nums)
    total_sum = (n * (n + 1)) // 2  # Sum of consecutive integers formula
    actual_sum = sum(nums)
    missing_number = total_sum - actual_sum
    return missing_number
