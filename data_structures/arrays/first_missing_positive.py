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
    """
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

    # Add more tests if needed
    nums1 = [1, 2, 0]
    print(first_missing_positive(nums1))  # Output: 3

    nums2 = [3, 4, -1, 1]
    print(first_missing_positive(nums2))  # Output: 2

    nums3 = [7, 8, 9, 11, 12]
    print(first_missing_positive(nums3))  # Output: 1

    # Additional test
    nums4 = [2, 5, -10, 8, 4, 6, 1, 9]
    print(first_missing_positive(nums4))  # Output: 3

    # Run the doctests
    doctest.testmod()
