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
    xor_list = nums[0]
    xor_range = 1

    for i in range(1, len(nums)):
        xor_list ^= nums[i]

    for i in range(2, len(nums) + 2):
        xor_range ^= i

    missing_number = xor_list ^ xor_range

    return missing_number
