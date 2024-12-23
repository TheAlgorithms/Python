class KadaneAlgorithm:
    """
    Kadane's Algorithm to find the maximum sum
    of a contiguous subarray in a given array.

    Time Complexity: O(n)
    Space Complexity: O(1)

    The function works efficiently with both positive and negative integers.

    Usage:
    >>> kadane = KadaneAlgorithm()
    >>> kadane.max_subarray_sum([1, 2, 3, -2, 5])
    9
    >>> kadane.max_subarray_sum([-1, -2, -3, -4])
    -1
    >>> kadane.max_subarray_sum([1, 2, 3, 4])
    10
    >>> kadane.max_subarray_sum([10, -10, 20, -5, 10])
    25
    """

    def __init__(self):
        pass

    def max_subarray_sum(self, arr: list[int]) -> int:
        """
        This function finds the maximum sum of a
        contiguous subarray using Kadane's Algorithm.

        :param arr: List of integers.
        :return: Maximum sum of a contiguous subarray.

        Raises:
            ValueError: If the input array is empty.

        >>> kadane = KadaneAlgorithm()
        >>> kadane.max_subarray_sum([1, 2, 3, -2, 5])
        9
        >>> kadane.max_subarray_sum([-1, -2, -3, -4])
        -1
        >>> kadane.max_subarray_sum([1, 2, 3, 4])
        10
        >>> kadane.max_subarray_sum([10, -10, 20, -5, 10])
        25
        """
        if not arr:
            raise ValueError("Input array cannot be empty.")

        max_sum = current_sum = arr[0]

        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
