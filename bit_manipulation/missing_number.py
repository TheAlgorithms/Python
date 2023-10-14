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
    n = nums[-1]
    for i in range(nums[0], n + 1):
        if nums[i - nums[0]] != i:
            missing_number = i
            break

    return missing_number
