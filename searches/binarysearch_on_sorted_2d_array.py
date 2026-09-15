#!/usr/bin/env python3


def binary_search_2d(matrix: list[list[int]], target: int) -> tuple[int, int]:
    """
    Searches for a target value in a 2D sorted array.

    The matrix is sorted such that each row is in ascending order, and the
    first element of each row is greater than the last element of the previous row.

    Args:
        matrix: A 2D list of integers sorted in ascending order.
        target: The integer value to search for.

    Returns:
        A tuple (row_index, col_index) if found, otherwise (-1, -1).

    Raises:
        ValueError: If matrix is empty or not rectangular.

    >>> binary_search_2d([[1, 3, 5], [7, 9, 11], [12, 13, 15]], 9)
    (1, 1)
    >>> binary_search_2d([[1, 3, 5], [7, 9, 11], [12, 13, 15]], 4)
    (-1, -1)
    >>> binary_search_2d([], 1)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: matrix must not be empty
    >>> binary_search_2d([[1, 2], [3, 4, 5]], 3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: matrix must be rectangular
    """
    if not matrix or not matrix[0]:
        raise ValueError("matrix must not be empty")

    rows = len(matrix)
    cols = len(matrix[0])

    for row in matrix:
        if len(row) != cols:
            raise ValueError("matrix must be rectangular")

    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return mid // cols, mid % cols
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    matrix = [[1, 3, 5], [7, 9, 11], [12, 13, 15]]
    target = 9
    result = binary_search_2d(matrix, target)
    if result == (-1, -1):
        print(f"{target} was not found in the matrix.")
    else:
        print(f"{target} was found at position {result} in the matrix.")
