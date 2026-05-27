"""
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m + n)).

Examples:
    Example 1:
        Input: nums1 = [1, 3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1, 2, 3] and median is 2.

    Example 2:
        Input: nums1 = [1, 2], nums2 = [3, 4]
        Output: 2.50000
        Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.

Constraints:
    * nums1.length == m
    * nums2.length == n
    * 0 <= m <= 1000
    * 0 <= n <= 1000
    * 1 <= m + n <= 2000
    * -10^6 <= nums1[i], nums2[i] <= 10^6

Implementation: Divide and Conquer (Binary Search on partitions).
Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
"""

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Find the median of two sorted arrays using binary search on partitions.

    Args:
        nums1 (List[int]): First sorted array
        nums2 (List[int]): Second sorted array

    Returns:
        float: Median of the two arrays
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    # Binary search for the partition in nums1
    while left <= right:
        i = (left + right) // 2  # Partition in nums1
        j = (m + n + 1) // 2 - i  # Partition in nums2

        # Edge cases for partitions
        left1 = float("-inf") if i == 0 else nums1[i - 1]
        right1 = float("inf") if i == m else nums1[i]
        left2 = float("-inf") if j == 0 else nums2[j - 1]
        right2 = float("inf") if j == n else nums2[j]

        # Check if this partition is correct
        if left1 <= right2 and left2 <= right1:
            # Correct partition found
            if (m + n) % 2 == 0:
                # Even length: average of max(lefts) and min(rights)
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                # Odd length: max of lefts
                return max(left1, left2)
        elif left1 > right2:
            # Move partition left in nums1
            right = i - 1
        else:
            # Move partition right in nums1
            left = i + 1

    # Should not reach here if inputs are valid
    raise ValueError("Input arrays are not sorted or invalid")


# Optional: Add simple tests
if __name__ == "__main__":
    assert abs(find_median_sorted_arrays([1, 3], [2]) - 2.0) < 1e-5
    assert abs(find_median_sorted_arrays([1, 2], [3, 4]) - 2.5) < 1e-5
    print("All tests passed!")
