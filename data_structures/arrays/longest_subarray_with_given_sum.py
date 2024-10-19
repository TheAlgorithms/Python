"""
Author  : Akash Singh
Date    : October 19, 2024

This module finds the longest subarray with a given sum.
The algorithm uses a hash map to track cumulative sums and efficiently find subarrays.
"""

class LongestSubarrayWithGivenSum:
    def __init__(self, array: list[int]) -> None:
        self.array = array

    def find_longest_subarray(self, target_sum: int) -> int:
        """
        This function returns the length of the longest subarray
        that adds up to the target sum.

        Runtime: O(n)
        Space: O(n)

        >>> LongestSubarrayWithGivenSum([1, -1, 5, -2, 3]).find_longest_subarray(3)
        4
        >>> LongestSubarrayWithGivenSum([-2, -1, 2, 1]).find_longest_subarray(1)
        2
        >>> LongestSubarrayWithGivenSum([3, 1, 0, 1, 8, -2, 3]).find_longest_subarray(8)
        5
        >>> LongestSubarrayWithGivenSum([1, 2, 3]).find_longest_subarray(6)
        3
        >>> LongestSubarrayWithGivenSum([5, 1, -1, 5, -1, -2]).find_longest_subarray(4)
        3
        >>> LongestSubarrayWithGivenSum([2, 4, 6, 8]).find_longest_subarray(7)
        0
        """
        prefix_sum_map = {}
        longest_length = 0
        current_sum = 0

        for i, num in enumerate(self.array):
            current_sum += num

            if current_sum == target_sum:
                longest_length = i + 1  # If sum equals target from index 0

            if current_sum - target_sum in prefix_sum_map:
                longest_length = max(longest_length, i - prefix_sum_map[current_sum - target_sum])

            if current_sum not in prefix_sum_map:
                prefix_sum_map[current_sum] = i

        return longest_length


if __name__ == "__main__":
    import doctest
    doctest.testmod()
