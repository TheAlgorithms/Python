"""
Jacobi Iteration Method - https://en.wikipedia.org/wiki/Jacobi_method
"""
from __future__ import annotations

import numpy as np
from numpy import float64
from numpy.typing import NDArray


# Method to find solution of system of linear equations
def jacobi_iteration_method(
    coefficient_matrix: NDArray[float64],
    constant_matrix: NDArray[float64],
    init_val: list[int],
    iterations: int,
) -> list[float]:
    """
    Jacobi Iteration Method:
    An iterative algorithm to determine the solutions of strictly diagonally dominant
    system of linear equations

    4x1 +  x2 +  x3 =  2
     x1 + 5x2 + 2x3 = -6
     x1 + 2x2 + 4x3 = -4

    x_init = [0.5, -0.5 , -0.5]

    Examples:

    >>> coefficient = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> constant = np.array([[2], [-6], [-4]])
    >>> init_val = [0.5, -0.5, -0.5]
    >>> iterations = 3
    >>> jacobi_iteration_method(coefficient, constant, init_val, iterations)
    [0.909375, -1.14375, -0.7484375]


    >>> coefficient = np.array([[4, 1, 1], [1, 5, 2]])
    >>> constant = np.array([[2], [-6], [-4]])
    >>> init_val = [0.5, -0.5, -0.5]
    >>> iterations = 3
    >>> jacobi_iteration_method(coefficient, constant, init_val, iterations)
    Traceback (most recent call last):
    ...
    ValueError: Coefficient matrix dimensions must be nxn but received 2x3

    >>> coefficient = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> constant = np.array([[2], [-6]])
    >>> init_val = [0.5, -0.5, -0.5]
    >>> iterations = 3
    >>> jacobi_iteration_method(coefficient, constant, init_val, iterations)
    Traceback (most recent call last):
    ...
    ValueError: Coefficient and constant matrices dimensions must be nxn and nx1 but
                received 3x3 and 2x1

    >>> coefficient = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> constant = np.array([[2], [-6], [-4]])
    >>> init_val = [0.5, -0.5]
    >>> iterations = 3
    >>> jacobi_iteration_method(coefficient, constant, init_val, iterations)
    Traceback (most recent call last):
    ...
    ValueError: Number of initial values must be equal to number of rows in coefficient
                matrix but received 2 and 3

    >>> coefficient = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> constant = np.array([[2], [-6], [-4]])
    >>> init_val = [0.5, -0.5, -0.5]
    >>> iterations = 0
    >>> jacobi_iteration_method(coefficient, constant, init_val, iterations)
    Traceback (most recent call last):
    ...
    ValueError: Iterations must be at least 1
    """

    rows1, cols1 = coefficient_matrix.shape
    rows2, cols2 = constant_matrix.shape

    if rows1 != cols1:
        raise ValueError(
            f"Coefficient matrix dimensions must be nxn but received {rows1}x{cols1}"
        )

    if cols2 != 1:
        raise ValueError(f"Constant matrix must be nx1 but received {rows2}x{cols2}")

    if rows1 != rows2:
        raise ValueError(
            f"""Coefficient and constant matrices dimensions must be nxn and nx1 but
            received {rows1}x{cols1} and {rows2}x{cols2}"""
        )

    if len(init_val) != rows1:
        raise ValueError(
            f"""Number of initial values must be equal to number of rows in coefficient
            matrix but received {len(init_val)} and {rows1}"""
        )

    if iterations <= 0:
        raise ValueError("Iterations must be at least 1")

    table: NDArray[float64] = np.concatenate(
        (coefficient_matrix, constant_matrix), axis=1
    )

    rows, cols = table.shape

    strictly_diagonally_dominant(table)

    # Iterates the whole matrix for given number of times
    for i in range(iterations):
        new_val = []
        for row in range(rows):
            temp = 0
            for col in range(cols):
                if col == row:
                    denom = table[row][col]
                elif col == cols - 1:
                    val = table[row][col]
                else:
                    temp += (-1) * table[row][col] * init_val[col]
            temp = (temp + val) / denom
            new_val.append(temp)
        init_val = new_val

    return [float(i) for i in new_val]


# Checks if the given matrix is strictly diagonally dominant
def strictly_diagonally_dominant(table: NDArray[float64]) -> bool:
    """
    >>> table = np.array([[4, 1, 1, 2], [1, 5, 2, -6], [1, 2, 4, -4]])
    >>> strictly_diagonally_dominant(table)
    True

    >>> table = np.array([[4, 1, 1, 2], [1, 5, 2, -6], [1, 2, 3, -4]])
    >>> strictly_diagonally_dominant(table)
    Traceback (most recent call last):
    ...
    ValueError: Coefficient matrix is not strictly diagonally dominant
    """

    rows, cols = table.shape

    is_diagonally_dominant = True

    for i in range(0, rows):
        total = 0
        for j in range(0, cols - 1):
            if i == j:
                continue
            else:
                total += table[i][j]

        if table[i][i] <= total:
            raise ValueError("Coefficient matrix is not strictly diagonally dominant")

    return is_diagonally_dominant


# Test Cases
if __name__ == "__main__":
    import doctest

    doctest.testmod()
