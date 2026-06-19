"""
Median of Two Sorted Arrays

Problem: Given two sorted arrays nums1 and nums2 of sizes m and n,
return the median of the two sorted arrays.

This implementation uses a partition-based divide-and-conquer approach
to achieve optimal time complexity.

Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)

Reference: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from __future__ import annotations


def find_median_sorted_arrays(
    nums1: list[int | float], nums2: list[int | float]
) -> float:
    """
    Find the median of two sorted arrays using binary search.

    The algorithm works by partitioning both arrays such that:
    - All elements on the left side are smaller than elements on the right side
    - The left side has the same number of elements as the right side (or one more)

    Args:
        nums1: First sorted array
        nums2: Second sorted array

    Returns:
        The median of the two sorted arrays as a float

    Raises:
        ValueError: If both input arrays are empty

    Examples:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0
        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5
        >>> find_median_sorted_arrays([], [1])
        1.0
        >>> find_median_sorted_arrays([2], [])
        2.0
        >>> find_median_sorted_arrays([1, 2, 3, 4, 5], [6, 7, 8])
        4.5
        >>> find_median_sorted_arrays([1.5, 2.5], [2.0, 3.0])
        2.25
        >>> find_median_sorted_arrays([1, 1, 1], [1, 1, 1])
        1.0
        >>> find_median_sorted_arrays([-5, -3, -1], [0, 2, 4])
        -0.5
        >>> find_median_sorted_arrays([1], [2, 3, 4, 5, 6])
        3.5
        >>> find_median_sorted_arrays([], [])
        Traceback (most recent call last):
            ...
        ValueError: Both input arrays are empty
    """
    if not nums1 and not nums2:
        raise ValueError("Both input arrays are empty")

    # Ensure nums1 is the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total_left = (m + n + 1) // 2  # Number of elements on the left side

    left, right = 0, m

    while left <= right:
        # Partition indices for nums1 and nums2
        i = (left + right) // 2  # Partition index for nums1
        j = total_left - i  # Partition index for nums2

        # Get the boundary elements around the partitions
        nums1_left_max = nums1[i - 1] if i > 0 else float("-inf")
        nums1_right_min = nums1[i] if i < m else float("inf")

        nums2_left_max = nums2[j - 1] if j > 0 else float("-inf")
        nums2_right_min = nums2[j] if j < n else float("inf")

        # Check if we found the correct partition
        if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
            # Correct partition found
            if (m + n) % 2 == 1:
                # Odd total length: median is the max of left side
                return float(max(nums1_left_max, nums2_left_max))
            else:
                # Even total length: median is average of max(left) and min(right)
                left_max = max(nums1_left_max, nums2_left_max)
                right_min = min(nums1_right_min, nums2_right_min)
                return (left_max + right_min) / 2.0
        elif nums1_left_max > nums2_right_min:
            # We are too far right in nums1, move left
            right = i - 1
        else:
            # We are too far left in nums1, move right
            left = i + 1

    # This should not be reached if inputs are valid sorted arrays
    raise ValueError("Input arrays are not sorted or some unexpected error occurred")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
