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
        >>> find_missing_number([4, 3, 1, 0])
        2
        >>> find_missing_number([-2, 0, 1, 3, 4])
        Traceback (most recent call last):
        ...
        ValueError: negative values not supported
    """
    n = len(nums)
    missing_number = n

    for i in range(n):
        if nums[i] < 0:
            raise ValueError("negative values not supported")
        missing_number ^= i ^ nums[i]

    return missing_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
