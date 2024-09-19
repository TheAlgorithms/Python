"""
Fixed-Size Sliding Window Algorithm

This module contains an implementation of the fixed-size
sliding window algorithm with doctests.

Examples:
    >>> max_sum_subarray([1, 2, 3, 4, 5], 3)
    12

    >>> max_sum_subarray([2, 1, 5, 1, 3, 2], 4)
    11
"""


def max_sum_subarray(arr: list[int], k: int) -> int:
    """
    Find the maximum sum of any subarray of size `k`.

    Args:
        arr: The input array of integers.
        k: The size of the subarray.

    Returns:
        The maximum sum of a subarray of size `k`.

    Raises:
        ValueError: If the length of the array is less than `k`.

    Examples:
        >>> max_sum_subarray([1, 2, 3, 4, 5], 3)
        12

        >>> max_sum_subarray([2, 1, 5, 1, 3, 2], 4)
        11

        >>> max_sum_subarray([1, 2], 3)
        Traceback (most recent call last):
            ...
        ValueError: Array length must be at least as large as the window size.
    """
    if len(arr) < k:
        raise ValueError("Array length must be at least as large as the window size.")

    max_sum = float("-inf")
    window_sum = sum(arr[:k])
    max_sum = max(max_sum, window_sum)

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
