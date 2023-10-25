from typing import List, Tuple, Union


def binary_search(
    array: List[int], lower_bound: int, upper_bound: int, value: int
) -> int:
    """
    Binary search in a sorted 1D array.
    Returns the index of the value if found, or -1 if not found.
    """
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1
    return -1


def search_2d_matrix(
    value: int, matrix: List[List[int]]
) -> Union[List[int], Tuple[int, int]]:
    """
    Search for a value in a sorted 2D matrix.
    Returns the index [row, col] of the value if found, or (-1, -1) if not found.
    """
    if not matrix or not matrix[0]:
        return (-1, -1)

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == value:
            return (row, col)
        elif matrix[row][col] < value:
            row += 1
        else:
            col -= 1

    return (-1, -1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
