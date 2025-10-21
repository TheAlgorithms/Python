from collections import deque
from typing import List


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """
    Return a list of the maximum values in each sliding window of size k.

    This algorithm runs in O(n) time using a deque to keep track of useful elements.

    Parameters
    ----------
    nums : List[int]
        The input list of integers.
    k : int
        The window size.

    Returns
    -------
    List[int]
        A list containing the maximum of each sliding window.

    Examples
    --------
    >>> sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3)
    [3, 3, 5, 5, 6, 7]
    >>> sliding_window_maximum([9, 11], 2)
    [11]
    >>> sliding_window_maximum([4, -2], 1)
    [4, -2]
    >>> sliding_window_maximum([], 3)
    []
    >>> sliding_window_maximum([1,2,3], 0)
    []
    """
    if not nums or k <= 0:
        return []

    dq: deque[int] = deque()
    result: List[int] = []

    for i, num in enumerate(nums):
        # Remove indices that are out of the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller values as they are not useful
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Add the current max to the result once the window is of size k
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
