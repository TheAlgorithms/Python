"""Array Traversal.

This module contains functions for common array traversal operations,
including finding maximum, minimum, and sum of elements.
"""


def find_max(arr: list[int | float]) -> int | float:
    """
    Find the maximum element in an array.

    Args:
        arr: List of numbers

    Returns:
        The maximum value in the array

    Raises:
        ValueError: If the array is empty

    Examples:
        >>> find_max([1, 5, 3, 9, 2])
        9
        >>> find_max([-1, -5, -3])
        -1
        >>> find_max([42])
        42
        >>> find_max([1.5, 2.7, 1.2])
        2.7
        >>> find_max([])
        Traceback (most recent call last):
            ...
        ValueError: Array cannot be empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    return max(arr)


def find_min(arr: list[int | float]) -> int | float:
    """
    Find the minimum element in an array.

    Args:
        arr: List of numbers

    Returns:
        The minimum value in the array

    Raises:
        ValueError: If the array is empty

    Examples:
        >>> find_min([1, 5, 3, 9, 2])
        1
        >>> find_min([-1, -5, -3])
        -5
        >>> find_min([42])
        42
        >>> find_min([])
        Traceback (most recent call last):
            ...
        ValueError: Array cannot be empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    return min(arr)


def array_sum(arr: list[int | float]) -> int | float:
    """
    Calculate the sum of all elements in an array.

    Args:
        arr: List of numbers

    Returns:
        The sum of all values in the array

    Examples:
        >>> array_sum([1, 2, 3, 4, 5])
        15
        >>> array_sum([-1, 1, -2, 2])
        0
        >>> array_sum([1.5, 2.5, 3.0])
        7.0
        >>> array_sum([])
        0
    """
    return sum(arr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
