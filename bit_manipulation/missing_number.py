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
    number = nums[0]
    for i in range(n):
        if nums[i] != number:
            missing_number = number
            break
        number += 1
    return missing_number


# print(find_missing_number([0, 1, 3, 4]))
