"""
The Max-Min Problem is finding the maximum and minimum value in an array.

This is a divide and conquer approach to solve the Max-Min Problem.

For more information:
https://www.tutorialspoint.com/data_structures_algorithms/max_min_problem.htm
"""


class Pair:
    """
    Structure to store both maximum and minimum elements
    """

    def __init__(self) -> None:
        """
        Initializes the Pair object with maximum and minimum elements

        Args:
            None

        Returns:
            None

        >>> pair = Pair()
        >>> pair.max
        0
        >>> pair.min
        0
        """
        self.max = 0
        self.min = 0


def max_min_divide_conquer(arr: list, low: int, high: int) -> "Pair":
    """
    Returns the maximum and minimum elements in the array.

    Args:
        arr: A list of integers
        low: An integer representing the start index of the array
        high: An integer representing the end index of the array

    Returns:
        A Pair object containing the maximum and minimum elements in the array

    >>> arr = [1, 3, 4, 2, 8, 9, 7, 6, 5]
    >>> max_min_divide_conquer(arr, 0, len(arr) - 1).max
    9
    >>> max_min_divide_conquer(arr, 0, len(arr) - 1).min
    1
    >>> arr = [7]
    >>> max_min_divide_conquer(arr, 0, len(arr) - 1).max
    7
    >>> max_min_divide_conquer(arr, 0, len(arr) - 1).min
    7
    >>> arr = [7, 1]
    >>> max_min_divide_conquer(arr, 0, len(arr) - 1).max
    7
    >>> max_min_divide_conquer(arr, 0, len(arr) - 1).min
    1
    """
    result = Pair()

    # If only one element in the array
    if low == high:
        result.max = arr[low]
        result.min = arr[low]
        return result

    # If there are two elements in the array
    if high == low + 1:
        if arr[low] < arr[high]:
            result.min = arr[low]
            result.max = arr[high]
        else:
            result.min = arr[high]
            result.max = arr[low]
        return result

    # If there are more than two elements in the array
    mid = (low + high) // 2
    left = max_min_divide_conquer(arr, low, mid)
    right = max_min_divide_conquer(arr, mid + 1, high)

    # Compare and get the maximum of both parts
    result.max = max(left.max, right.max)

    # Compare and get the minimum of both parts
    result.min = min(left.min, right.min)

    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()
