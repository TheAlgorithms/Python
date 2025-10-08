"""
Kadane's Algorithm implementation in Python.

Finds the maximum sum of a contiguous subarray within
a one-dimensional array of numbers.

Source:
https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""


def kadane(arr: list[int]) -> tuple[int, list[int]]:
    """
    Returns the maximum sum of a contiguous subarray and the subarray itself.

    Parameters
    ----------
    arr : list
        List of integers (can be positive, negative, or zero).

    Returns
    -------
    tuple
        Maximum subarray sum and the corresponding subarray.

    Examples
    --------
    >>> kadane([-2,1,-3,4,-1,2,1,-5,4])
    (6, [4, -1, 2, 1])

    >>> kadane([1,2,3,4])
    (10, [1, 2, 3, 4])

    >>> kadane([-1,-2,-3])
    (-1, [-1])
    """
    if not arr:
        raise ValueError("Input array cannot be empty")

    max_current = max_global = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > max_current + arr[i]:
            max_current = arr[i]
            s = i
        else:
            max_current += arr[i]

        if max_current > max_global:
            max_global = max_current
            start = s
            end = i

    return max_global, arr[start:end+1]


# Doctest runner
if __name__ == "__main__":
    import doctest
    doctest.testmod()
