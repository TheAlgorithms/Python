"""To find determinant of NxN Matrix i have used Row Reduction method
    you can see wikipedia of this Method
    https://en.wikipedia.org/wiki/Row_echelon_form"""

from __future__ import annotations

from copy import deepcopy


def determinant_of_nxn_matrix(matrix: list[list[float]]) -> float:
    """>>> determinant_of_nxn_matrix([[10, 5], [3, 2.5]])
        10.0
        >>> determinant_of_nxn_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
        -3.0
        >>> determinant_of_nxn_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 4]])
        15.0
        >>> determinant_of_nxn_matrix([[1, 2, 3, 7], [4, 5, 6, 6],
        [7, 8, 1, 5], [1, 2, 3, 4]])
        -72.0
        >>> determinant_of_nxn_matrix([[1, 2, 3, 7, 13], [4, 5, 6, 6, 90],
        [7, 8, 1, 5, 76],
        [1, 2, 3, 4, 12], [9, 6, 3, 7, 4]])
        19848.0
        >>> determinant_of_nxn_matrix([[1, 2,  3, 7,  13, 23],
        [4, 44, 6, 6,  90, 12],
        [7, 8,  1, 5,  6,  98], [1, 2,  3, 4,  12, 4],
        [9, 6,  3, 7,  4,  9], [2, 47, 8, 91, 36, 9]])
        -20981553.999999993"""
    
    size = int(len(matrix))
    matrix_copy = deepcopy(matrix)
    n = 0
    m = 1
    c1 = 1
    c2 = 0
    for k in range(1, (2 * (size - 1)) + 1):
        for i in range(c1, size):
            for j in range(0, size):
                if (matrix[c1 - 1][c2]) != 0:
                    matrix_copy[i][j] = matrix[i][j] - (
                        (matrix[m][n]) * ((matrix[c2][j]) / (matrix[c1 - 1][c2]))
                    )
            m = m + 1

        matrix = deepcopy(matrix_copy)
        n = n + 1
        m = n + 1
        c1 = c1 + 1
        c2 = c2 + 1

    determinant = float(1)
    for i in range(0, size):
        for j in range(0, size):
            if i == j:
                determinant = determinant * matrix[i][j]

    return determinant
