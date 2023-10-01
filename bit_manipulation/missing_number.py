def find_missing_number(nums):
    """
    Finds the missing number in a list of consecutive integers.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        int: The missing number.

    Example:
        >>> find_missing_number([0, 1, 3, 4])
        2
    """
    n = len(nums)
    missing_number = n

    for i in range(n):
        missing_number ^= i ^ nums[i]

    return missing_number
