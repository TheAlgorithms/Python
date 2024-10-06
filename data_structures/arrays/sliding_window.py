def max_sum_subarray(arr: list[int], k: int) -> int:
    """
    Finds the maximum sum of a subarray of size k.

    Args:
        arr (list[int]): List of integers.
        k (int): Size of the subarray.

    Returns:
        int: Maximum sum of a subarray of size k or 0 if no valid sum found.

    >>> max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
    9
    >>> max_sum_subarray([2, 3, 4, 1, 5], 2)
    7
    >>> max_sum_subarray([1, 2, 3], 5)
    0  # Example case where k is larger than the array
    """
    n = len(arr)
    if n < k:  # Edge case: if window size is larger than array size
        return 0  # Consider returning 0 instead of -1

    max_sum = float("-inf")
    window_sum = sum(arr[:k])  # Sum of the first window

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return int(max_sum) if max_sum != float("-inf") else 0
