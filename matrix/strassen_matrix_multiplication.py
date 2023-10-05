"""
In this problem, we want to multiply the matrix using Strassen's algorithm.

Article about it here:
https://www.interviewbit.com/blog/strassens-matrix-multiplication/
"""


import numpy as np
import numpy.typing as npt


def input_matrix(matrix: npt.ArrayLike, sizeOfMatrix: int) -> None:
    print("Enter matrix:")
    for i in range(sizeOfMatrix):
        for j in range(sizeOfMatrix):
            matrix[i][j] = int(input(f"Enter element [{i+1},{j+1}]: "))
    print()


def print_matrix(matrix: npt.ArrayLike, sizeOfMatrix: int) -> None:
    for i in range(sizeOfMatrix):
        for j in range(sizeOfMatrix):
            print(matrix[i][j], end=" ")
        print()
    print()


def strassen(matrixA: npt.ArrayLike, matrixB:npt.ArrayLike) -> np.ndarray:
    n = len(matrixA)
    if n == 1:
        return matrixA * matrixB

    c = np.zeros(shape=(n, n), dtype=np.int64)
    k = n // 2

    a11 = matrixA[:k, :k]
    a12 = matrixA[:k, k:]
    a21 = matrixA[k:, :k]
    a22 = matrixA[k:, k:]
    b11 = matrixB[:k, :k]
    b12 = matrixB[:k, k:]
    b21 = matrixB[k:, :k]
    b22 = matrixB[k:, k:]

    p1 = strassen(a11, b12 - b22)
    p2 = strassen(a11 + a12, b22)
    p3 = strassen(a21 + a22, b11)
    p4 = strassen(a22, b21 - b11)
    p5 = strassen(a11 + a22, b11 + b22)
    p6 = strassen(a12 - a22, b21 + b22)
    p7 = strassen(a11 - a21, b11 + b12)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c


if __name__ == "__main__":
    print(
        "Strassen's Matrix Multiplication Algorithm\n"
        "only works on square matrices whose dimension is a power of 2.\n"
        "So, please enter a valid dimension(size) of matrix.\n"
    )

    n = int(input("Enter size of matrix: "))
    a = np.zeros(shape=(n, n), dtype=np.int64)
    b = np.zeros(shape=(n, n), dtype=np.int64)

    input_matrix(a, n)
    print("Matrix A:")
    print_matrix(a, n)
    input_matrix(b, n)
    print("Matrix B:")
    print_matrix(b, n)

    c = strassen(a, b)
    print("Multiplication result:")
    print_matrix(c, n)
