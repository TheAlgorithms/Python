from __future__ import annotations

from .double_ended_queue import Deque

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
    queue = Deque()
    for i in range(len(arr)):
        # pop the element if the index is outside the window size k
        if queue and i - queue._front.val >= window_size:
            queue.popleft()
        # keep the queue monotonically decreasing
        # so that the max value is always on the top
        while queue and arr[i] >= arr[queue._back.val]:
            queue.pop()
        queue.append(i)
        # the maximum value is the first element in queue
        if i >= window_size - 1:
            max_val.append(arr[queue._front.val])
    return max_val


if __name__ == "__main__":
    from doctest import testmod

    testmod()