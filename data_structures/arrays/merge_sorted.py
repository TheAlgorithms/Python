def merge_sorted_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Merge two sorted arrays into one sorted array.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        A single merged and sorted array.

    Examples:
        >>> merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]

        >>> merge_sorted_arrays([1, 2], [])
        [1, 2]

        >>> merge_sorted_arrays([], [3, 4])
        [3, 4]

        >>> merge_sorted_arrays([], [])
        []

        >>> merge_sorted_arrays([0, 0], [0, 0])
        [0, 0, 0, 0]

        >>> merge_sorted_arrays([-5, -3, -1], [-2, -2])
        [-5, -3, -2, -2, -1]
    """
    # If one array is empty, simply return the other.
    if not nums1:
        return nums2
    if not nums2:
        return nums1

    # Two-pointer approach to merge both sorted arrays.
    i, j = 0, 0
    merged = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Append remaining elements if any.
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    return merged


if __name__ == "__main__":
    import doctest

    doctest.testmod()
