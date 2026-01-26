from collections import deque


def sliding_window_maximum(nums: list[int], window_size: int) -> list[int]:
    """
    Return a list of the maximum values in each sliding window of the given size.
    This algorithm runs in O(n) time using a deque to keep track of useful elements.

    Parameters
    ----------
    nums : list[int]
        The input list of integers.
    window_size : int
        The size of the sliding window.

    Returns
    -------
    list[int]
        A list containing the maximum of each sliding window.

    Examples
    --------
    >>> sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
    [3, 3, 5, 5, 6, 7]
    >>> sliding_window_maximum([9, 11], 2)
    [11]
    >>> sliding_window_maximum([4, -2], 1)
    [4, -2]
    >>> sliding_window_maximum([], 3)
    []
    >>> sliding_window_maximum([1, 2, 3], 0)
    []

    Reference
    ---------
    https://en.wikipedia.org/wiki/Sliding_window_protocol
    """
    if not nums or window_size <= 0:
        return []

    dq: deque[int] = deque()
    result: list[int] = []

    for i, num in enumerate(nums):
        # Remove indices that are out of the current window
        while dq and dq[0] <= i - window_size:
            dq.popleft()

        # Remove smaller values as they are not useful
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Add the current max to the result once the window is of size window_size
        if i >= window_size - 1:
            result.append(nums[dq[0]])

    return result
