def firstmissingpositive(nums):
    """
    Given an unsorted integer array nums, returns the smallest missing positive integer.

    The algorithm must run in O(n) time and use O(1) auxiliary space.

    Hints:
    - Try to place each number in its correct position, so that nums[i] equals i + 1.
    - Iterate through the array to find the first position where nums[i] != i + 1,
      indicating the missing positive integer.

    Args:
    - nums (List[int]): The input unsorted integer array.

    Returns:
    - int: The smallest missing positive integer.

    Examples:
    >>> firstmissingpositive([1, 2, 0])
    3

    >>> firstmissingpositive([3, 4, -1, 1])
    2

    >>> firstmissingpositive([7, 8, 9, 11, 12])
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
    print(firstmissingpositive(nums1))  # Output: 3

    nums2 = [3, 4, -1, 1]
    print(firstmissingpositive(nums2))  # Output: 2

    nums3 = [7, 8, 9, 11, 12]
    print(firstmissingpositive(nums3))  # Output: 1

    # Additional test
    nums4 = [2, 5, -10, 8, 4, 6, 1, 9]
    print(firstmissingpositive(nums4))  # Output: 3

    # Run the doctests
    doctest.testmod()
