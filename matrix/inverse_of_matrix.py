from __future__ import annotations

from decimal import Decimal

from numpy import array


def inverse_of_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """
    A matrix multiplied with its inverse gives the identity matrix.
    This function finds the inverse of a 2x2 and 3x3 matrix.
    If the determinant of a matrix is 0, its inverse does not exist.

    Sources for fixing inaccurate float arithmetic:
    https://stackoverflow.com/questions/6563058/how-do-i-use-accurate-float-arithmetic-in-python
    https://docs.python.org/3/library/decimal.html

    Doctests for 2x2
    >>> inverse_of_matrix([[2, 5], [2, 0]])
    [[0.0, 0.5], [0.2, -0.2]]
    >>> inverse_of_matrix([[2.5, 5], [1, 2]])
    Traceback (most recent call last):
        ...
    ValueError: This matrix has no inverse.
    >>> inverse_of_matrix([[12, -16], [-9, 0]])
    [[0.0, -0.1111111111111111], [-0.0625, -0.08333333333333333]]
    >>> inverse_of_matrix([[12, 3], [16, 8]])
    [[0.16666666666666666, -0.0625], [-0.3333333333333333, 0.25]]
    >>> inverse_of_matrix([[10, 5], [3, 2.5]])
    [[0.25, -0.5], [-0.3, 1.0]]

    Doctests for 3x3
    >>> inverse_of_matrix([[2, 5, 7], [2, 0, 1], [1, 2, 3]])
    [[2.0, 5.0, -4.0], [1.0, 1.0, -1.0], [-5.0, -12.0, 10.0]]
    >>> inverse_of_matrix([[1, 2, 2], [1, 2, 2], [3, 2, -1]])
    Traceback (most recent call last):
        ...
    ValueError: This matrix has no inverse.

    >>> inverse_of_matrix([[],[]])
    Traceback (most recent call last):
        ...
    ValueError: Please provide a matrix of size 2x2 or 3x3.

    >>> inverse_of_matrix([[1, 2], [3, 4], [5, 6]])
    Traceback (most recent call last):
        ...
    ValueError: Please provide a matrix of size 2x2 or 3x3.

    >>> inverse_of_matrix([[1, 2, 1], [0,3, 4]])
    Traceback (most recent call last):
        ...
    ValueError: Please provide a matrix of size 2x2 or 3x3.

    >>> inverse_of_matrix([[1, 2, 3], [7, 8, 9], [7, 8, 9]])
    Traceback (most recent call last):
        ...
    ValueError: This matrix has no inverse.

    >>> inverse_of_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    """

    d = Decimal

    # Check if the provided matrix has 2 rows and 2 columns
    # since this implementation only works for 2x2 matrices
    if len(matrix) == 2 and len(matrix[0]) == 2 and len(matrix[1]) == 2:
        # Calculate the determinant of the matrix
        determinant = float(
            d(matrix[0][0]) * d(matrix[1][1]) - d(matrix[1][0]) * d(matrix[0][1])
        )
        if determinant == 0:
            raise ValueError("This matrix has no inverse.")

        # Creates a copy of the matrix with swapped positions of the elements
        swapped_matrix = [[0.0, 0.0], [0.0, 0.0]]
        swapped_matrix[0][0], swapped_matrix[1][1] = matrix[1][1], matrix[0][0]
        swapped_matrix[1][0], swapped_matrix[0][1] = -matrix[1][0], -matrix[0][1]

        # Calculate the inverse of the matrix
        return [
            [(float(d(n)) / determinant) or 0.0 for n in row] for row in swapped_matrix
        ]
    elif (
        len(matrix) == 3
        and len(matrix[0]) == 3
        and len(matrix[1]) == 3
        and len(matrix[2]) == 3
    ):
        # Calculate the determinant of the matrix using Sarrus rule
        determinant = float(
            (
                (d(matrix[0][0]) * d(matrix[1][1]) * d(matrix[2][2]))
                + (d(matrix[0][1]) * d(matrix[1][2]) * d(matrix[2][0]))
                + (d(matrix[0][2]) * d(matrix[1][0]) * d(matrix[2][1]))
            )
            - (
                (d(matrix[0][2]) * d(matrix[1][1]) * d(matrix[2][0]))
                + (d(matrix[0][1]) * d(matrix[1][0]) * d(matrix[2][2]))
                + (d(matrix[0][0]) * d(matrix[1][2]) * d(matrix[2][1]))
            )
        )
        if determinant == 0:
            raise ValueError("This matrix has no inverse.")

        # Creating cofactor matrix
        cofactor_matrix = [
            [d(0.0), d(0.0), d(0.0)],
            [d(0.0), d(0.0), d(0.0)],
            [d(0.0), d(0.0), d(0.0)],
        ]
        cofactor_matrix[0][0] = (d(matrix[1][1]) * d(matrix[2][2])) - (
            d(matrix[1][2]) * d(matrix[2][1])
        )
        cofactor_matrix[0][1] = -(
            (d(matrix[1][0]) * d(matrix[2][2])) - (d(matrix[1][2]) * d(matrix[2][0]))
        )
        cofactor_matrix[0][2] = (d(matrix[1][0]) * d(matrix[2][1])) - (
            d(matrix[1][1]) * d(matrix[2][0])
        )
        cofactor_matrix[1][0] = -(
            (d(matrix[0][1]) * d(matrix[2][2])) - (d(matrix[0][2]) * d(matrix[2][1]))
        )
        cofactor_matrix[1][1] = (d(matrix[0][0]) * d(matrix[2][2])) - (
            d(matrix[0][2]) * d(matrix[2][0])
        )
        cofactor_matrix[1][2] = -(
            (d(matrix[0][0]) * d(matrix[2][1])) - (d(matrix[0][1]) * d(matrix[2][0]))
        )
        cofactor_matrix[2][0] = (d(matrix[0][1]) * d(matrix[1][2])) - (
            d(matrix[0][2]) * d(matrix[1][1])
        )
        cofactor_matrix[2][1] = -(
            (d(matrix[0][0]) * d(matrix[1][2])) - (d(matrix[0][2]) * d(matrix[1][0]))
        )
        cofactor_matrix[2][2] = (d(matrix[0][0]) * d(matrix[1][1])) - (
            d(matrix[0][1]) * d(matrix[1][0])
        )

        # Transpose the cofactor matrix (Adjoint matrix)
        adjoint_matrix = array(cofactor_matrix)
        for i in range(3):
            for j in range(3):
                adjoint_matrix[i][j] = cofactor_matrix[j][i]

        # Inverse of the matrix using the formula (1/determinant) * adjoint matrix
        inverse_matrix = array(cofactor_matrix)
        for i in range(3):
            for j in range(3):
                inverse_matrix[i][j] /= d(determinant)

        # Calculate the inverse of the matrix
        return [[float(d(n)) or 0.0 for n in row] for row in inverse_matrix]
    raise ValueError("Please provide a matrix of size 2x2 or 3x3.")
