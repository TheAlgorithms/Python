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

    x: NDArray[float64] = np.zeros((rows, 1), dtype=float)
    for row in reversed(range(rows)):
        total = np.dot(coefficients[row, row + 1 :], x[row + 1 :])
        x[row, 0] = (vector[row] - total) / coefficients[row, row]

    return x


def gaussian_elimination(
    coefficients: NDArray[float64], vector: NDArray[float64]
) -> NDArray[float64]:
    """
    This function performs Gaussian elimination method

    Examples:
        1x1 - 4x2 - 2x3 = -2        1x1 + 2x2 = 5
        5x1 + 2x2 - 2x3 = -3        5x1 + 2x2 = 5
        1x1 - 1x2 + 0x3 = 4
    >>> gaussian_elimination([[1, -4, -2], [5, 2, -2], [1, -1, 0]], [[-2], [-3], [4]])
    array([[ 2.3 ],
           [-1.7 ],
           [ 5.55]])
    >>> gaussian_elimination([[1, 2], [5, 2]], [[5], [5]])
    array([[0. ],
           [2.5]])
    """
    # coefficients must to be a square matrix so we need to check first
    rows, columns = np.shape(coefficients)
    if rows != columns:
        return np.array((), dtype=float)

    # augmented matrix
    augmented_mat: NDArray[float64] = np.concatenate((coefficients, vector), axis=1)
    augmented_mat = augmented_mat.astype("float64")

    # scale the matrix leaving it triangular

    # factor - taken elements from 'augmented_mat' by row slice: row + 1: columns,
    # with 'row' column number, divided by the selected 'diagonal_element'.
    # [:, np.newaxis] - array is converted to two dimensions to use vector multiplication.

    # product of factor and the row selected from augmented_mat[row, :] is subtracted from
    # the value of the selected 'rows: row + 1: columns' and all columns:
    # augmented_mat[row + 1: columns, :]

    for row in range(rows - 1):
        diagonal_element = augmented_mat[row, row]
        factor = (augmented_mat[row + 1: columns, row] / diagonal_element)[:, np.newaxis]
        augmented_mat[row + 1: columns, :] -= factor * augmented_mat[row, :]

    x = retroactive_resolution(
        augmented_mat[:, 0:columns], augmented_mat[:, columns : columns + 1]
    )

    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()
