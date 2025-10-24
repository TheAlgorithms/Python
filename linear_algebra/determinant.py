"""
Matrix determinant calculation using various methods.

The determinant is a scalar value that characterizes a square matrix.
It provides important information about the matrix, such as whether it's invertible.

Reference: https://en.wikipedia.org/wiki/Determinant
"""

import numpy as np
from numpy import float64
from numpy.typing import NDArray


def determinant_recursive(matrix: NDArray[float64]) -> float:
    """
    Calculate the determinant of a square matrix
    using recursive cofactor expansion.
    This method is suitable for
    small matrices but becomes inefficient for large matrices.
    Parameters:
        matrix (NDArray[float64]): A square matrix
    Returns:
        float: The determinant of the matrix
    Raises:
        ValueError: If the matrix is not square
    Examples:
    >>> import numpy as np
    >>> matrix = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=float)
    >>> determinant_recursive(matrix)
    -2.0

    >>> matrix = np.array([[5.0]], dtype=float)
    >>> determinant_recursive(matrix)
    5.0
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")

    n = matrix.shape[0]

    # Base cases
    if n == 1:
        return float(matrix[0, 0])

    if n == 2:
        return float(matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0])

    # Recursive case: cofactor expansion along the first row
    det = 0.0
    for col in range(n):
        # Create submatrix by removing row 0 and column col
        submatrix = np.delete(np.delete(matrix, 0, axis=0), col, axis=1)

        # Calculate cofactor
        cofactor = ((-1) ** col) * matrix[0, col] * determinant_recursive(submatrix)
        det += cofactor

    return det


def determinant_lu(matrix: NDArray[float64]) -> float:
    """
    Calculate the determinant using LU decomposition.
    This method is more efficient for larger matrices
    than recursive expansion.
    Parameters:
        matrix (NDArray[float64]): A square matrix
    Returns:
        float: The determinant of the matrix
    Raises:
        ValueError: If the matrix is not square
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")

    n = matrix.shape[0]

    # Create a copy to avoid modifying the original matrix
    A = matrix.astype(float64, copy=True)

    # Keep track of row swaps for sign adjustment
    swap_count = 0

    # Forward elimination to get upper triangular matrix
    for i in range(n):
        # Find pivot
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k, i]) > abs(A[max_row, i]):
                max_row = k

        # Swap rows if needed
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            swap_count += 1

        # Check for singular matrix
        if abs(A[i, i]) < 1e-14:
            return 0.0

        # Eliminate below pivot
        for k in range(i + 1, n):
            factor = A[k, i] / A[i, i]
            for j in range(i, n):
                A[k, j] -= factor * A[i, j]

    # Calculate determinant as product of diagonal elements
    det = 1.0
    for i in range(n):
        det *= A[i, i]

    # Adjust sign based on number of row swaps
    if swap_count % 2 == 1:
        det = -det

    return det


def determinant(matrix: NDArray[float64]) -> float:
    """
    Calculate the determinant of a square matrix using
    the most appropriate method.
    Uses recursive expansion for small matrices (≤3x3)
    and LU decomposition for larger ones.
    Parameters:
        matrix (NDArray[float64]): A square matrix
    Returns:
        float: The determinant of the matrix
    Examples:
    >>> import numpy as np
    >>> matrix = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=float)
    >>> determinant(matrix)
    -2.0
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")

    n = matrix.shape[0]

    # Use recursive method for small matrices, LU decomposition for larger ones
    if n <= 3:
        return determinant_recursive(matrix)
    else:
        return determinant_lu(matrix)


def test_determinant() -> None:
    """
    Test function for matrix determinant calculation.

    >>> test_determinant()  # self running tests
    """
    # Test 1: 2x2 matrix
    matrix_2x2 = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=float)
    det_2x2 = determinant(matrix_2x2)
    assert abs(det_2x2 - (-2.0)) < 1e-10, "2x2 determinant calculation failed"

    # Test 2: 3x3 matrix
    matrix_3x3 = np.array(
        [[2.0, -3.0, 1.0], [2.0, 0.0, -1.0], [1.0, 4.0, 5.0]], dtype=float
    )
    det_3x3 = determinant(matrix_3x3)
    assert abs(det_3x3 - 49.0) < 1e-10, "3x3 determinant calculation failed"

    # Test 3: Singular matrix
    singular_matrix = np.array([[1.0, 2.0], [2.0, 4.0]], dtype=float)
    det_singular = determinant(singular_matrix)
    assert abs(det_singular) < 1e-10, "Singular matrix should have zero determinant"

    # Test 4: Identity matrix
    identity_3x3 = np.eye(3, dtype=float)
    det_identity = determinant(identity_3x3)
    assert abs(det_identity - 1.0) < 1e-10, "Identity matrix should have determinant 1"

    # Test 5: Compare recursive and LU methods
    test_matrix = np.array(
        [[1.0, 2.0, 3.0], [0.0, 1.0, 4.0], [5.0, 6.0, 0.0]], dtype=float
    )
    det_recursive = determinant_recursive(test_matrix)
    det_lu = determinant_lu(test_matrix)
    assert abs(det_recursive - det_lu) < 1e-10, (
        "Recursive and LU methods should give same result"
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_determinant()
