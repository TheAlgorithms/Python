"""
The Tribonacci matrix is a matrix A such that the following
description holds:

       |      T(n)         T(n+1)        T(n+2)  |
 A^n = | T(n+2)-T(n+1) T(n+3)-T(n+2) T(n+3)-T(n) |
       |     T(n+1)        T(n+2)        T(n+3)  |

where T(n) is the n-th tribonacci number. The following matrix
has the previous property:

     | 0  0  1 |
 A = | 1  0  1 |
     | 0  1  1 |

We can use the matrix A, in order to compute the n-th
tribonacci number by getting the n-3 power of A, and the
A[3][3] entry will have the number that we're looking for.
"""

from typing import List

Matrix = List[List[int]]


def matrix_multiplication(matrix_1: Matrix, matrix_2: Matrix) -> Matrix:
    """
    Multiply two given matrices.

    Examples:
    >>> matrix_multiplication([[0,0,1],[1,0,1],[0,1,1]],[[0,0,1],[1,0,1],[0,1,1]])
    [[0, 1, 1], [0, 1, 2], [1, 1, 2]]
    """
    result_matrix = []

    for i in range(len(matrix_1)):
        row = []

        for j in range(len(matrix_2[i])):
            entry = 0

            for k in range(len(matrix_2)):
                entry += matrix_1[i][k] * matrix_2[k][j]

            row.append(entry)
        result_matrix.append(row)
    return result_matrix


def nth_tribonacci_matrix(n: int) -> int:
    """
    Get the (n-3) power of the Tribonacci matrix, in order to get the
    n-th tribonacci number.

    Examples:
    >>> nth_tribonacci_matrix(1)
    0
    >>> nth_tribonacci_matrix(2)
    0
    >>> nth_tribonacci_matrix(3)
    1
    >>> nth_tribonacci_matrix(50)
    1697490356184
    """
    if n <= 2:
        return 0

    res_matrix = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]
    tribonacci_matrix = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]

    for _ in range(0, n - 4):
        res_matrix = matrix_multiplication(res_matrix, tribonacci_matrix)

    return res_matrix[2][2]


def nth_tribonacci_bruteforce(n: int) -> int:
    """
    Compute the nth tribonacci number by brute-force, meaning
    it will follow the description of the sequence given by:
    T(1) = 0, T(2) = 0, T(3) = 1, T(n) = T(n-1) + T(n-2) + T(n-3)

    Examples:
    >>> nth_tribonacci_bruteforce(1)
    0
    >>> nth_tribonacci_bruteforce(2)
    0
    >>> nth_tribonacci_bruteforce(3)
    1
    >>> nth_tribonacci_bruteforce(50)
    1697490356184
    """
    if n < 1:
        return n
    elif n <= 2:
        return 0

    trib1 = 0
    trib2 = 0
    trib3 = 1

    for _ in range(3, n):
        trib1, trib2, trib3 = trib2, trib3, trib1 + trib2 + trib3

    return trib3


def main() -> None:
    amount = 50
    brute_force = [str(nth_tribonacci_bruteforce(x)) for x in range(1, amount + 1)]
    matrix = [str(nth_tribonacci_matrix(x)) for x in range(1, amount + 1)]
    print("First {} numbers of the tribonacci sequence.".format(amount))
    print("Computation by brute-force: {}".format(",".join(brute_force)))
    print("Computation by matrix exponentiation: {}".format(",".join(matrix)))


if __name__ == "__main__":
    main()
