"""
Gaussian elimination method for solving a system of linear equations.
Gaussian elimination - https://en.wikipedia.org/wiki/Gaussian_elimination
"""

import numpy as np
from numpy import float64
from numpy.typing import NDArray


def retroactive_resolution(
    coefficients: NDArray[float64], vector: NDArray[float64]
) -> NDArray[float64]:
    """
    This function performs a retroactive linear system resolution
        for triangular matrix

    Examples:
        2x1 + 2x2 - 1x3 = 5         2x1 + 2x2 = -1
        0x1 - 2x2 - 1x3 = -7        0x1 - 2x2 = -1
        0x1 + 0x2 + 5x3 = 15
    >>> gaussian_elimination([[2, 2, -1], [0, -2, -1], [0, 0, 5]], [[5], [-7], [15]])
    array([[2.],
           [2.],
           [3.]])
    >>> gaussian_elimination([[2, 2], [0, -2]], [[-1], [-1]])
    array([[-1. ],
           [ 0.5]])
    """

    rows, columns = np.shape(coefficients)

    # Initialize solution vector x
    x: NDArray[float64] = np.zeros((rows, 1), dtype=float64)

    # Perform back substitution
    for row in reversed(range(rows)):
        total = np.dot(coefficients[row, row + 1 :], x[row + 1 :])
        x[row, 0] = (vector[row] - total[0]) / coefficients[row, row]

    return x


def gaussian_elimination(
    coefficients: NDArray[float64], vector: NDArray[float64]
) -> NDArray[float64]:
    """
    Perform Gaussian elimination on the system to reduce it to an upper triangular form,
    followed by retroactive linear system resolution to solve the system.

    Arguments:
        coefficients: Matrix of coefficients
        vector: Vector representing the right-hand side of the system

    Returns:
        Solution vector.

    Example:
    >>> gaussian_elimination(np.array([[1, -4, -2], [5, 2, -2], [1, -1, 0]], dtype=float64), np.array([[-2], [-3], [4]], dtype=float64))
    array([[ 2.3 ],
           [-1.7 ],
           [ 5.55]])
    """

    rows, columns = np.shape(coefficients)

    # Ensure the matrix is square
    if rows != columns:
        raise ValueError("Coefficient matrix must be square")

    # Augment the matrix with the vector
    augmented_mat: NDArray[float64] = np.concatenate((coefficients, vector), axis=1)
    augmented_mat = augmented_mat.astype(float64)

    # Perform Gaussian elimination (triangularization)
    for row in range(rows - 1):
        pivot = augmented_mat[row, row]

        # Check if the pivot is zero, and swap with a lower row if possible
        if np.isclose(pivot, 0):
            for swap_row in range(row + 1, rows):
                if not np.isclose(augmented_mat[swap_row, row], 0):
                    augmented_mat[[row, swap_row]] = augmented_mat[[swap_row, row]]
                    pivot = augmented_mat[row, row]
                    break
            else:
                raise ValueError(f"Matrix is singular at row {row}")

        # Eliminate entries below the pivot
        for col in range(row + 1, rows):
            factor = augmented_mat[col, row] / pivot
            augmented_mat[col, :] -= factor * augmented_mat[row, :]

    # Perform retroactive linear system resolution to get the solution
    x = retroactive_resolution(
        augmented_mat[:, 0:columns], augmented_mat[:, columns : columns + 1]
    )

    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()
