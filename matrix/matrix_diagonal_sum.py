"""
Matrix Multiplication Algorithm

This function performs matrix multiplication on two valid matrices.
It follows the mathematical definition:
If A is an m×n matrix and B is an n×p matrix,
then their product C is an m×p matrix.

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

from typing import List


def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    if not _is_valid_matrix(A) or not _is_valid_matrix(B):
        raise ValueError("Invalid matrix structure")

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Incompatible matrix sizes")

    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def _is_valid_matrix(M: List[List[float]]) -> bool:
    if not isinstance(M, list) or not M:
        return False
    first_length = len(M[0])
    return all(isinstance(row, list) and len(row) == first_length for row in M)
