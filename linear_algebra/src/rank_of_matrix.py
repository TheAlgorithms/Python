"""
Calculate the rank of a matrix.

See: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
"""


def rank_of_matrix(matrix: list[list[int | float]]) -> int:
    """
    Finds the rank of a matrix.

    Args:
        `matrix`: The matrix as a list of lists.

    Returns:
        The rank of the matrix.

    Example:

    >>> matrix1 = [[1, 2, 3],
    ...            [4, 5, 6],
    ...            [7, 8, 9]]
    >>> rank_of_matrix(matrix1)
    2
    >>> matrix2 = [[1, 0, 0],
    ...            [0, 1, 0],
    ...            [0, 0, 0]]
    >>> rank_of_matrix(matrix2)
    2
    >>> matrix3 = [[1, 2, 3, 4],
    ...            [5, 6, 7, 8],
    ...            [9, 10, 11, 12]]
    >>> rank_of_matrix(matrix3)
    2
    >>> rank_of_matrix([[2,3,-1,-1],
    ...                [1,-1,-2,4],
    ...                [3,1,3,-2],
    ...                [6,3,0,-7]])
    4
    >>> rank_of_matrix([[2,1,-3,-6],
    ...                [3,-3,1,2],
    ...                [1,1,1,2]])
    3
    >>> rank_of_matrix([[2,-1,0],
    ...                [1,3,4],
    ...                [4,1,-3]])
    3
    >>> rank_of_matrix([[3,2,1],
    ...                [-6,-4,-2]])
    1
    >>> rank_of_matrix([[],[]])
    0
    >>> rank_of_matrix([[1]])
    1
    >>> rank_of_matrix([[]])
    0
    """

    rows = len(matrix)
    columns = len(matrix[0])
    rank = min(rows, columns)

    for row in range(rank):
        # Check if diagonal element is not zero
        if matrix[row][row] != 0:
            # Eliminate all the elements below the diagonal
            for col in range(row + 1, rows):
                multiplier = matrix[col][row] / matrix[row][row]
                for i in range(row, columns):
                    matrix[col][i] -= multiplier * matrix[row][i]
        else:
            # Find a non-zero diagonal element to swap rows
            reduce = True
            for i in range(row + 1, rows):
                if matrix[i][row] != 0:
                    matrix[row], matrix[i] = matrix[i], matrix[row]
                    reduce = False
                    break
            if reduce:
                rank -= 1
                for i in range(rows):
                    matrix[i][row] = matrix[i][rank]

            # Reduce the row pointer by one to stay on the same row
            row -= 1

    return rank


if __name__ == "__main__":
    import doctest

    doctest.testmod()
