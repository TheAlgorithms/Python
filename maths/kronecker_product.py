"""
Kronecker Product of Two Matrices
Implementation with type hints, doctests, and detailed Big-O complexity analysis.
Reference: https://en.wikipedia.org/wiki/Kronecker_product
"""

from __future__ import annotations


def kronecker_product(
    matrix_a: list[list[float | int]], matrix_b: list[list[float | int]]
) -> list[list[float | int]]:
    """
    Computes the Kronecker product (tensor product) of two matrices A and B.

    If A is an m-by-n matrix and B is a p-by-q matrix, then the Kronecker product
    A (x) B is the (m*p)-by-(n*q) block matrix.

    Time Complexity: O(m * n * p * q) where A is m x n and B is p x q.
    Space Complexity: O(m * n * p * q) for the output block matrix.

    >>> kronecker_product([[1, 2], [3, 4]], [[0, 5], [6, 7]])
    [[0, 5, 0, 10], [6, 7, 12, 14], [0, 15, 0, 20], [18, 21, 24, 28]]

    >>> kronecker_product([[1, -1]], [[2], [3]])
    [[2, -2], [3, -3]]

    >>> kronecker_product([[1]], [[5, 6], [7, 8]])
    [[5, 6], [7, 8]]

    >>> kronecker_product([], [[1, 2]])
    []

    >>> kronecker_product([[1, 2]], [])
    []
    """
    if not matrix_a or not matrix_b:
        return []

    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a == 0 or cols_b == 0:
        return []

    result_rows = rows_a * rows_b
    result_cols = cols_a * cols_b
    result: list[list[float | int]] = [
        [0 for _ in range(result_cols)] for _ in range(result_rows)
    ]

    for i in range(rows_a):
        for j in range(cols_a):
            for k in range(rows_b):
                for l_idx in range(cols_b):
                    row_idx = i * rows_b + k
                    col_idx = j * cols_b + l_idx
                    result[row_idx][col_idx] = matrix_a[i][j] * matrix_b[k][l_idx]

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
