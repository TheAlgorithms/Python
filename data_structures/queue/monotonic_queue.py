from __future__ import annotations

from collections import deque

arr = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3
expect = [3, 3, 5, 5, 6, 7]


def max_sliding_window(arr: list[float], window_size: int) -> list[float]:
    """
    Given an array of integers nums, there is a sliding window of size k which is moving
    from the very left of the array to the very right.
    Each time the sliding window of length window_size moves right by one position.
    Return the max sliding window.
    >>> max_sliding_window(arr, window_size) == expect
    True
    """
    max_val = []
    mono_queue: deque = deque()
    for i in range(len(arr)):
        # pop the element if the index is outside the window size k
        if mono_queue and i - mono_queue[0] >= window_size:
            mono_queue.popleft()
        # keep the queue monotonically decreasing
        # so that the max value is always on the top
        while mono_queue and arr[i] >= arr[mono_queue[-1]]:
            mono_queue.pop()
        mono_queue.append(i)
        # the maximum value is the first element in queue
        if i >= window_size - 1:
            max_val.append(arr[mono_queue[0]])
    return max_val


if __name__ == "__main__":
    from doctest import testmod

    testmod()
