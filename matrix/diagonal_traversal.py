from typing import List


def find_diagonal_order(mat: List[List[int]]) -> List[int]:
    """
    Returns the elements of the matrix in diagonal order.

    :param mat: A 2D list representing the matrix.
    :return: A list of elements in diagonal order.
    :raises ValueError: If the matrix is empty or rows have different lengths.

    >>> find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 4, 7, 5, 3, 6, 8, 9]

    Example:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Algorithm:
        Step 1. Initialize variables to track the current row and column.
        Step 2. Iterate through the elements of the matrix in a
                manner that alternates between moving diagonally up
                and down.
    """
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])

    # Check for uniformity of row lengths
    for row in mat:
        if len(row) != n:
            raise ValueError("All rows must have the same number of columns.")

    result = []
    row, col = 0, 0

    for _ in range(m * n):
        result.append(mat[row][col])

        # Determine the direction of traversal
        if (row + col) % 2 == 0:  # moving up
            if col == n - 1:  # hit the right boundary
                row += 1
            elif row == 0:  # hit the top boundary
                col += 1
            else:  # move up diagonally
                row -= 1
                col += 1
        else:  # moving down
            if row == m - 1:  # hit the bottom boundary
                col += 1
            elif col == 0:  # hit the left boundary
                row += 1
            else:  # move down diagonally
                row += 1
                col -= 1

    return result


# Driver code
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(find_diagonal_order(matrix))
