"""
Question:
Given a binary array nums and an integer k, find the length of the longest subarray containing 1s after flipping at most k zeros.

Example:
Input: nums = [1,0,1,1,0,1], k = 1
Output: 4
Explanation:
Flip the first 0 at index 1 -> subarray [1,1,1,1] has length 4
"""

from typing import List


class LongestOnesAfterReplacement:
    def longest_ones(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer of sliding window
        max_len = 0  # Tracks maximum window length
        zeros_count = 0  # Count of zeros in current window

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1

            # Shrink window if zeros exceed k
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# Example dry run
if __name__ == "__main__":
    nums = [1, 0, 1, 1, 0, 1]
    k = 1
    solver = LongestOnesAfterReplacement()
    print("Longest Ones After Replacement:", solver.longest_ones(nums, k))
