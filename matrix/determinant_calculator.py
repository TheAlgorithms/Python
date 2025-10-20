# Wikipedia URL- https://en.wikipedia.org/wiki/Determinant

def get_minor(matrix: list[list[int] | list[float]], row: int, col: int) -> list[list[int] | list[float]]:
    """
    Returns the minor matrix obtained by removing the specified row and column.

    Parameters
    ----------
    matrix : list[list[int] | list[float]]
        The original square matrix.
    row : int
        The row to remove.
    col : int
        The column to remove.

    Returns
    -------
    list[list[int] | list[float]]
        Minor matrix.
    """
    return [r[:col] + r[col+1:] for i, r in enumerate(matrix) if i != row]


def determinant_manual(matrix: list[list[int] | list[float]]) -> int | float:
    """
    Calculates the determinant of a square matrix using cofactor expansion.

    Parameters
    ----------
    matrix : list[list[int] | list[float]]
        A square matrix.

    Returns
    -------
    int | float
        Determinant of the matrix.

    Examples
    --------
    >>> determinant_manual([[1,2],[3,4]])
    -2
    >>> determinant_manual([[2]])
    2
    >>> determinant_manual([[1,2,3],[4,5,6],[7,8,9]])
    0
    """
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for j in range(n):
        minor = get_minor(matrix, 0, j)
        cofactor = (-1) ** j * determinant_manual(minor)
        det += matrix[0][j] * cofactor
    return det


if __name__ == "__main__":
    # Simple demo
    matrix_demo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"The determinant is: {determinant_manual(matrix_demo)}")
