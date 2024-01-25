def first_missing_positive(nums: list[int]) -> int:
    """
    Given an unsorted integer array nums, returns the smallest missing positive integer.

    The algorithm must run in O(n) time and use O(1) auxiliary space.

    Hints:
    - Try to place each number in its correct position, so that nums[i] equals i + 1.
    - Iterate through the array to find the first position where nums[i] != i + 1,
      indicating the missing positive integer.

    :param nums: The input unsorted integer array.
    :return: The smallest missing positive integer.

    Examples:
    >>> first_missing_positive([1, 2, 0])
    3

    >>> first_missing_positive([3, 4, -1, 1])
    2

    >>> first_missing_positive([7, 8, 9, 11, 12])
    1

    >>> first_missing_positive([])
    1

    >>> first_missing_positive([0])
    1

    >>> first_missing_positive([1])
    2

    >>> first_missing_positive([0.9, 1.5, -2.3, 3.0, 2.7])
    1

    >>> first_missing_positive([-1, -2, -3])
    1

    >>> first_missing_positive([1.5, -2.3, 3.0, 2.7])
    1

    >>> first_missing_positive("ABC")
    Traceback (most recent call last):
    ...
    TypeError: Input must be a list of numbers
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of numbers")

    # Filter out non-positive numbers and fractional parts
    nums = [int(x) for x in nums if x > 0 and x == int(x)]

    n = len(nums)

    # Move each number to its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find the first missing positive integer
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all integers from 1 to n are present, return n + 1
    return n + 1


# Run the doctests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
