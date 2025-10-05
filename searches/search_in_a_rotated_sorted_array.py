def search_in_rotated_sorted_array(nums: list[int], target: int) -> int:
    """
    Search for a target value in a rotated sorted array.

    This function implements a modified binary search to find the index of a target
    value in an array that was originally sorted in ascending order but then rotated
    at some pivot point unknown to you beforehand.

    Args:
        nums: A list of integers that is sorted in ascending order and then rotated
              at some pivot point. Example: [4, 5, 6, 7, 0, 1, 2]
        target: The integer value to search for in the array.

    Returns:
        int: The index of target in nums if found, otherwise -1.

    Raises:
        ValueError: If nums is empty.

    Examples:
        >>> search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3)
        -1
        >>> search_in_rotated_sorted_array([1], 0)
        -1
        >>> search_in_rotated_sorted_array([1], 1)
        0
        >>> search_in_rotated_sorted_array([], 1)
        Traceback (most recent call last):
            ...
        ValueError: nums cannot be empty
    """
    if not nums:
        raise ValueError("nums cannot be empty")

    left_index, right_index = 0, len(nums) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        if nums[middle_index] == target:
            return middle_index

        # Check if left half is sorted array
        if nums[left_index] <= nums[middle_index]:
            # Target is in the sorted left half
            if nums[left_index] <= target < nums[middle_index]:
                right_index = middle_index - 1
            # If target is not in sorted part searching in other part
            else:
                left_index = middle_index + 1
        # Right half is sorted
        elif nums[middle_index] < target <= nums[right_index]:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Additional test cases
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
        ([1], 1),
        ([3, 1], 1),
        ([3, 1], 3),
    ]

    for nums, target in test_cases:
        result = search_in_rotated_sorted_array(nums, target)
        print(f"search_in_rotated_sorted_array({nums}, {target}) = {result}")
