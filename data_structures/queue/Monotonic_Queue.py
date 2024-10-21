"""
A Monotonic Queue is a data structure that supports efficient insertion, deletion,
and retrieval of elements in a specific order, typically in increasing or decreasing order.
"""

from collections import deque


class MonotonicQueue:
    def __init__(self):
        self.deque = deque()

    def push(self, value):
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def max(self):
        return self.deque[0]

    def pop(self, value):
        if self.deque and self.deque[0] == value:
            self.deque.popleft()


def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []
    if k >= len(nums):
        return [max(nums)]
    if k == 1:
        return nums

    q = MonotonicQueue()
    result = []
    for i in range(len(nums)):
        if i < k - 1:
            q.push(nums[i])
        else:
            q.push(nums[i])
            result.append(q.max())
            q.pop(nums[i - k + 1])
    return result


# Test cases
print(sliding_window_max([], 3))  # Edge case: Empty list
print(sliding_window_max([1, 2], 3))  # Edge case: k > len(nums)
print(sliding_window_max([1, 3, 2, 5, 4], 1))  # Edge case: k == 1
print(sliding_window_max([1, 3, 2, 5, 4], 5))  # Edge case: k == len(nums)
print(sliding_window_max([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 3))  # Normal case
