from collections import deque
from typing import List


class SlidingWindowMaximum:
    """
    Problem:
    Given an integer array and a window_size, return the maximum value in each
    sliding window of that size.

    Example:
    >>> solver = SlidingWindowMaximum()
    >>> solver.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    [3, 3, 5, 5, 6, 7]
    """

    def max_sliding_window(self, nums: List[int], window_size: int) -> List[int]:
        if not nums:
            return []

        result = []
        window = deque()

        for i, num in enumerate(nums):
            while window and window[0] <= i - window_size:
                window.popleft()

            while window and nums[window[-1]] < num:
                window.pop()

            window.append(i)

            if i >= window_size - 1:
                result.append(nums[window[0]])

        return result


if __name__ == "__main__":
    solver = SlidingWindowMaximum()
    print(
        "Sliding Window Maximum:",
        solver.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3),
    )
