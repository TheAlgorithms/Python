def binary_search_2d(matrix: list[list[int]], target: int) -> tuple[int, int]:
    """
    Searches for a target value in a 2D sorted array.

    The matrix is sorted such that each row is in ascending order, and the
    first element of each row is greater than the last element of the previous row.

    :param matrix: A 2D list of integers sorted in ascending order.
    :param target: The integer value to search for.
    :return: A tuple (row_index, col_index) if found, otherwise (-1, -1).

    Examples:
    >>> binary_search_2d([[1, 3, 5], [7, 9, 11], [12, 13, 15]], 9)
    (1, 1)
    >>> binary_search_2d([[1, 3, 5], [7, 9, 11], [12, 13, 15]], 4)
    (-1, -1)
    """
    if not matrix or not matrix[0]:
        return -1, -1

    rows, cols = len(matrix), len(matrix[0])
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
