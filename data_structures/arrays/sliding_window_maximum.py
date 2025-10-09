"""
Question:
Given an integer array nums and an integer k, return the maximum value in each sliding window of size k.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window positions and max values:
[1,3,-1] -> max = 3
[3,-1,-3] -> max = 3
[-1,-3,5] -> max = 5
[-3,5,3] -> max = 5
[5,3,6] -> max = 6
[3,6,7] -> max = 7
"""

from collections import deque
from typing import List


class SlidingWindowMaximum:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []  # Stores max of each window
        window = deque()  # Stores indices of elements in current window

        for i, num in enumerate(nums):
            # Remove indices of elements outside current window
            while window and window[0] <= i - k:
                window.popleft()

            # Remove indices of elements smaller than current num
            while window and nums[window[-1]] < num:
                window.pop()

            window.append(i)

            # Add the max for this window to result
            if i >= k - 1:
                result.append(nums[window[0]])

        return result


# Example dry run
if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    solver = SlidingWindowMaximum()
    print("Sliding Window Maximum:", solver.max_sliding_window(nums, k))
