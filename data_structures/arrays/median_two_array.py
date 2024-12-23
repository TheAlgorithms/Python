def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays.

    This implementation uses binary search to achieve an optimal solution in O(log(min(m, n))) time.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        The median of the two sorted arrays.

    Raises:
        ValueError: If both input arrays are empty.

    Examples:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0

        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5

        >>> find_median_sorted_arrays([0, 0], [0, 0])
        0.0

        >>> find_median_sorted_arrays([], [])
        Traceback (most recent last):
            ...
        ValueError: Both input arrays are empty.

        >>> find_median_sorted_arrays([], [1])
        1.0

        >>> find_median_sorted_arrays([-1000], [1000])
        0.0

        >>> find_median_sorted_arrays([-1.1, -2.2], [-3.3, -4.4])
        -2.75
    """
    if not nums1 and not nums2:
        raise ValueError("Both input arrays are empty.")

    # Insert 1: Ensure the smaller array is nums1
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1

        # Handle edges of the arrays with infinities
        max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float("inf") if partition1 == m else nums1[partition1]

        max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float("inf") if partition2 == n else nums2[partition2]

        # Insert 2: Debugging: Log partition indices and elements (useful for large arrays)
        # print(f"partition1: {partition1}, partition2: {partition2}")
        # print(f"max_left1: {max_left1}, min_right1: {min_right1}")
        # print(f"max_left2: {max_left2}, min_right2: {min_right2}")

        # Check if we have found the correct partition
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 1:
                return max(max_left1, max_left2)
            else:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
        elif max_left1 > min_right2:
            high = partition1 - 1
        else:
            low = partition1 + 1

    # Insert 3: Remove redundant exception, already handled at the beginning
    # raise ValueError("Input arrays are not sorted.")  # This line is no longer necessary.


def merge_sorted_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Merge two sorted arrays into a single sorted array in O(m + n) time.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        A new sorted array containing all elements of nums1 and nums2.

    Examples:
        >>> merge_sorted_arrays([1, 3], [2])
        [1, 2, 3]

        >>> merge_sorted_arrays([1, 2], [3, 4])
        [1, 2, 3, 4]

        >>> merge_sorted_arrays([0, 0], [0, 0])
        [0, 0, 0, 0]

        >>> merge_sorted_arrays([], [1])
        [1]

        >>> merge_sorted_arrays([], [])
        []
    """
    # Insert 4: Edge case: If one array is empty, just return the other array
    if not nums1:
        return nums2
    if not nums2:
        return nums1

    i, j = 0, 0
    merged = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Insert 5: Append remaining elements from either nums1 or nums2
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    return merged


def is_sorted(nums: list[int]) -> bool:
    """
    Helper function to check if the array is sorted.

    Args:
        nums: The array to check.

    Returns:
        True if the array is sorted, False otherwise.
    """
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
