"""
In linear algebra, a QR decomposition, also known as a QR factorization
or Q factorization,
is a decomposition of a matrix a into a product matrix_a = QR
of an orthonormal matrix Q and an upper triangular matrix R.
QR decomposition is often used to solve the linear least squares (LLS) problem
and is the basis for a particular eigenvalue algorithm, the QR algorithm.

This algorithm will simply attempt to perform QR decomposition on any square matrix.

Reference: https://en.wikipedia.org/wiki/QR_decomposition
"""

import numpy as np
from __future__ import annotations
from scipy.linalg import qr


def qr_decomposition(matrix_a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Perform QR decomposition on a given matrix and raises an error if in
    rowXcolumn matrix a if row is smaller than column or row,column is less than 2

    >>> matrix_a = np.array([[1, 2, 3], [4, 5, 9], [7, 8, 15]])
    >>> (matrix_q,matrix_r) = qr_decomposition(matrix_a)
    >>> matrix_q
    array([[-0.17,  0.9 ,  0.41],
           [-0.51,  0.28, -0.82],
           [-0.85, -0.35,  0.41]])
    >>> matrix_r
    array([[-17.75,  -9.63,  -8.11],
           [  0.  ,   0.41,  -0.41],
           [  0.  ,   0.  ,   0.  ]])
    >>> matrix_a = np.array([[1, 2], [4, 5], [7, 8]])
    >>> (matrix_q,matrix_r) = qr_decomposition(matrix_a)
    >>> matrix_q
    array([[-0.21,  0.89,  0.41],
           [-0.52,  0.25, -0.82],
           [-0.83, -0.38,  0.41]])
    >>> matrix_r
    array([[-9.64, -8.09],
           [ 0.  , -0.76],
           [ 0.  ,  0.  ]])
    >>> matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
    >>> (matrix_q,matrix_r) = qr_decomposition(matrix_a)
    Traceback (most recent call last):
        ...
    ValueError: row size should be greater than column size
    >>> matrix_a = np.array([[1], [4]])
    >>> (matrix_q,matrix_r) = qr_decomposition(matrix_a)
    Traceback (most recent call last):
        ...
    ValueError: row size and column size should be greater than 2
    >>> matrix_a = np.array([[1,4]])
    >>> (matrix_q,matrix_r) = qr_decomposition(matrix_a)
    Traceback (most recent call last):
        ...
    ValueError: row size should be greater than column size
    """

    rows, columns = np.shape(matrix_a)
    if rows < columns:
        msg = "row size should be greater than column size"
        raise ValueError(msg)
    if rows < 2 or columns < 2:
        msg = "row size and column size should be greater than 2"
        raise ValueError(msg)
    # Perform QR decomposition with pivoting
    # matrix_q: Orthogonal matrix
    # matrix_r: Upper triangular matrix
    # pivot: Pivot indices (permutation vector)

    matrix_q, matrix_r, pivot = qr(matrix_a, pivoting=True)

    # Verification: matrix_a[:, pivot] should equal matrix_q @ matrix_r
    permute_matrix = matrix_a[:, pivot]
    if np.allclose(permute_matrix, matrix_q @ matrix_r):
        return np.round(matrix_q, 2), np.round(matrix_r, 2)
    else:
        msg = "No matrix found which decompose given matrix"
        raise ValueError(msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
