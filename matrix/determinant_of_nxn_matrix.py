"""To find determinant of NxN Matrix i have used Row Reduction method
    you can see wikipedia of this Method
    https://en.wikipedia.org/wiki/Row_echelon_form"""

from __future__ import annotations

from copy import deepcopy


def determinant_of_nxn_matrix(a: list[list[float]]) -> float:
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
    
    N = int(len(a))
    a_copy = deepcopy(a)
    n = 0
    m = 1
    c1 = 1
    c2 = 0
    for k in range(1, (2 * (N - 1)) + 1):
        for i in range(c1, N):
            for j in range(0, N):
                if (a[c1 - 1][c2]) != 0:
                    a_copy[i][j] = a[i][j] - (
                        (a[m][n]) * ((a[c2][j]) / (a[c1 - 1][c2]))
                    )
            m = m + 1

        a = deepcopy(a_copy)
        n = n + 1
        m = n + 1
        c1 = c1 + 1
        c2 = c2 + 1

    determinant = float(1)
    for i in range(0, N):
        for j in range(0, N):
            if i == j:
                determinant = determinant * a[i][j]

    return determinant
