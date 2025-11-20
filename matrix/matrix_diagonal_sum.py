"""
Matrix Multiplication Algorithm

This function performs matrix multiplication on two valid matrices.
It follows the mathematical definition:
If a is an m x n matrix and b is an n x p matrix,
then their product c is an m x p matrix.

Raises:
    ValueError: if matrices have invalid structure or incompatible sizes.

Sources:
    https://en.wikipedia.org/wiki/Matrix_multiplication

Examples:
    >>> A = [[1, 2], [3, 4]]
    >>> B = [[5, 6], [7, 8]]
    >>> matrix_multiply(A, B)
    [[19, 22], [43, 50]]

    >>> matrix_multiply([[1, 2, 3]], [[4], [5], [6]])
    [[32]]

    # Invalid structure
    >>> matrix_multiply([[1, 2], [3]], [[1, 2]])
    Traceback (most recent call last):
    ...
    ValueError: Invalid matrix structure

    # Incompatible sizes
    >>> matrix_multiply([[1, 2]], [[1, 2]])
    Traceback (most recent call last):
    ...
    ValueError: Incompatible matrix sizes
"""


def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    if not _is_valid_matrix(a) or not _is_valid_matrix(b):
        raise ValueError("Invalid matrix structure")

    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError("Incompatible matrix sizes")

    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


def _is_valid_matrix(m: list[list[float]]) -> bool:
    if not isinstance(m, list) or not m:
        return False
    first_length = len(m[0])
    return all(isinstance(row, list) and len(row) == first_length for row in m)
