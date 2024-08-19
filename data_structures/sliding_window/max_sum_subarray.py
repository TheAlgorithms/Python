from typing import List


def max_sum_subarray(array: List[int], subarray_length: int) -> int:
    """
    Finds the maximum sum of a subarray of length k within the given array.[https://www.geeksforgeeks.org/window-sliding-technique/]

    Args:
    arr (list): The input array.
    k (int): The length of the subarray.

    Returns:
    int: The maximum sum of a subarray of length k.

    Examples:
    >>> max_sum_subarray([1, 2, 3, 4, 5], 2)
    9
    >>> max_sum_subarray([1, 2, 3, 4, 5], 3)
    12
    >>> max_sum_subarray([1, 2, 3, 4, 5], 6)
    Invalid input: k is larger than the array size
    >>> max_sum_subarray([], 1)
    Invalid input: k is larger than the array size
    """
    n = len(arr)
    if n < k or k <= 0:
        print("Invalid input: k is larger than the array size or non-positive")
        return None

    # Calculate the sum of the first window of size k
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window from start to end of the array
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
