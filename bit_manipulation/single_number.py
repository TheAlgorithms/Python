def single_number(nums: list[int]) -> int:
    """
    Find the single number in an array where every other number appears twice.

    Args:
        nums: List of integers where every integer appears twice except for one.

    Returns:
        The single integer that appears once.

    Example:
    >>> single_number([4, 1, 2, 1, 2])
    4
    >>> single_number([2, 2, 1])
    1
    >>> single_number([1])
    1
    """
    result = 0
    for num in nums:
        result ^= num  # Applying XOR operation
    return result


if __name__ == "__main__":
    # Test cases
    print(single_number([4, 1, 2, 1, 2]))  # Output: 4
    print(single_number([2, 2, 1]))  # Output: 1
    print(single_number([1]))  # Output: 1
    print(single_number([5, 3, 5, 7, 3]))  # Output: 7
