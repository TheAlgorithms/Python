"""
In linear algebra, a QR decomposition, also known as a QR factorization or QU factorization,
is a decomposition of a matrix A into a product A = QR
of an orthonormal matrix Q and an upper triangular matrix R.
QR decomposition is often used to solve the linear least squares (LLS) problem
and is the basis for a particular eigenvalue algorithm, the QR algorithm.

This algorithm will simply attempt to perform QR decomposition on any square matrix.

Reference: https://en.wikipedia.org/wiki/QR_decomposition
"""

from __future__ import annotations
import numpy as np
from scipy.linalg import qr

def qr_decomposition(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Perform QR decomposition on a given matrix and raises an error if in
    m×n matrix A if m is smaller than n or m,n is less than 2

    >>> A = np.array([[1, 2, 3], [4, 5, 9], [7, 8, 15]])
    >>> Q,R = qr_decomposition(A)
    >>> Q
    array([[-0.17,  0.9 ,  0.41],
           [-0.51,  0.28, -0.82],
           [-0.85, -0.35,  0.41]])
    >>> R
    array([[-17.75,  -9.63,  -8.11],
           [  0.  ,   0.41,  -0.41],
           [  0.  ,   0.  ,   0.  ]])
    >>> A = np.array([[1, 2], [4, 5], [7, 8]])
    >>> Q,R = qr_decomposition(A)
    >>> Q
    array([[-0.21,  0.89,  0.41],
           [-0.52,  0.25, -0.82],
           [-0.83, -0.38,  0.41]])
    >>> R
    array([[-9.64, -8.09],
           [ 0.  , -0.76],
           [ 0.  ,  0.  ]])
    >>> A = np.array([[1, 2, 3], [4, 5, 6]])
    >>> Q,R = qr_decomposition(A)
    Traceback (most recent call last):
        ...
    ValueError: row size should be greater than column size
    >>> A = np.array([[1], [4]])
    >>> Q,R = qr_decomposition(A)
    Traceback (most recent call last):
        ...
    ValueError: row size and column size should be greater than 2
    >>> A = np.array([[1,4]])
    >>> Q,R = qr_decomposition(A)
    Traceback (most recent call last):
        ...
    ValueError: row size should be greater than column size
    """


    rows, columns = np.shape(A)
    if rows < columns:
        msg = (
            "row size should be greater than column size"
        )
        raise ValueError(msg)
    if rows < 2 or columns < 2:
        msg = (
            "row size and column size should be greater than 2"
        )
        raise ValueError(msg)
    # Perform QR decomposition with pivoting
    # Q: Orthogonal matrix
    # R: Upper triangular matrix
    # P: Pivot indices (permutation vector)

    Q, R, P = qr(A, pivoting=True)

    # Note: The bottom row of R is all zeros because the matrix is rank-deficient.
    # Verification: A[:, P] should equal Q @ R
    AP = A[:, P]
    if(np.allclose(AP, Q @ R)):
        return np.round(Q,2), np.round(R,2)
    else:
        msg = (
            "No matrix found which decompose given matrix"
        )
        raise ValueError(msg)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
