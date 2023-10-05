"""
In this problem, we want to multiply the matrix using Strassen's algorithm.

Article about it here:
https://www.interviewbit.com/blog/strassens-matrix-multiplication/
"""


import numpy as np
import numpy.typing as npt


def print_matrix(matrix: npt.ArrayLike) -> None:
    """
    >>> matrix_a = np.array([[5, 6], [7, 8]])
    >>> print_matrix(matrix_a)
    5 6
    7 8
    """
    size_of_matrix = len(matrix)
    for i in range(size_of_matrix):
        for j in range(size_of_matrix):
            if j == size_of_matrix - 1:
                print(matrix[i][j], end="")
                continue
            print(matrix[i][j], end=" ")
        print()


def strassen_multiplication(
    matrix_a: npt.ArrayLike, matrix_b: npt.ArrayLike
) -> np.ndarray:
    """
    >>> matrix_a = np.array([[1, 2], [3, 4]])
    >>> matrix_b = np.array([[5, 6], [7, 8]])
    >>> strassen_multiplication(matrix_a, matrix_b)
    array([[19, 22],
           [43, 50]])
    """
    n = len(matrix_a)
    if n == 1:
        return matrix_a * matrix_b

    c = np.zeros(shape=(n, n), dtype=np.int64)
    k = n // 2

    a11 = matrix_a[:k, :k]
    a12 = matrix_a[:k, k:]
    a21 = matrix_a[k:, :k]
    a22 = matrix_a[k:, k:]
    b11 = matrix_b[:k, :k]
    b12 = matrix_b[:k, k:]
    b21 = matrix_b[k:, :k]
    b22 = matrix_b[k:, k:]

    p1 = strassen_multiplication(a11, b12 - b22)
    p2 = strassen_multiplication(a11 + a12, b22)
    p3 = strassen_multiplication(a21 + a22, b11)
    p4 = strassen_multiplication(a22, b21 - b11)
    p5 = strassen_multiplication(a11 + a22, b11 + b22)
    p6 = strassen_multiplication(a12 - a22, b21 + b22)
    p7 = strassen_multiplication(a11 - a21, b11 + b12)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c


def main() -> None:
    """
    >>> main()
    Matrix A:
    1 2
    3 4
    Matrix B:
    5 6
    7 8
    Multiplication result:
    19 22
    43 50
    """
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])

    print("Matrix A:")
    print_matrix(matrix_a)

    print("Matrix B:")
    print_matrix(matrix_b)

    result_matrix = strassen_multiplication(matrix_a, matrix_b)
    print("Multiplication result:")
    print_matrix(result_matrix)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
