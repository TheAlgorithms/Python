"""
Strassen's Matrix Multiplication Algorithm
------------------------------------------
An optimized divide-and-conquer algorithm for matrix multiplication that
reduces the number of multiplications from 8 (in the naive approach)
to 7 per recursion step.

This results in a time complexity of approximately O(n^2.807),
which is faster than the standard O(n^3) algorithm for large matrices.

Reference:
https://en.wikipedia.org/wiki/Strassen_algorithm
"""


from typing import List

Matrix = List[List[int]]

def add(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def naive_mul(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        ai = A[i]
        ci = C[i]
        for k in range(n):
            a_ik = ai[k]
            bk = B[k]
            for j in range(n):
                ci[j] += a_ik * bk[j]
    return C

def next_power_of_two(n: int) -> int:
    p = 1
    while p < n:
        p <<= 1
    return p

def pad_matrix(A: Matrix, size: int) -> Matrix:
    n = len(A)
    padded = [[0]*size for _ in range(size)]
    for i in range(n):
        for j in range(len(A[0])):
            padded[i][j] = A[i][j]
    return padded

def unpad_matrix(A: Matrix, rows: int, cols: int) -> Matrix:
    return [row[:cols] for row in A[:rows]]

def split(A: Matrix) -> tuple:
    n = len(A)
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return A11, A12, A21, A22

def join(C11: Matrix, C12: Matrix, C21: Matrix, C22: Matrix) -> Matrix:
    n2 = len(C11)
    n = n2 * 2
    C = [[0]*n for _ in range(n)]
    for i in range(n2):
        for j in range(n2):
            C[i][j] = C11[i][j]
            C[i][j + n2] = C12[i][j]
            C[i + n2][j] = C21[i][j]
            C[i + n2][j + n2] = C22[i][j]
    return C

def strassen(A: Matrix, B: Matrix, threshold: int = 64) -> Matrix:
    """
    Multiply square matrices A and B using Strassen algorithm.
    threshold: below this size, uses naive multiplication (tweakable).
    """
    assert len(A) == len(A[0]) == len(B) == len(B[0]), "Only square matrices supported in this implementation"

    n_orig = len(A)
    if n_orig == 0:
        return []

    m = next_power_of_two(n_orig)
    if m != n_orig:
        A_pad = pad_matrix(A, m)
        B_pad = pad_matrix(B, m)
    else:
        A_pad, B_pad = A, B

    C_pad = _strassen_recursive(A_pad, B_pad, threshold)

    C = unpad_matrix(C_pad, n_orig, n_orig)
    return C

def _strassen_recursive(A: Matrix, B: Matrix, threshold: int) -> Matrix:
    n = len(A)
    if n <= threshold:
        return naive_mul(A, B)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    M1 = _strassen_recursive(add(A11, A22), add(B11, B22), threshold)
    M2 = _strassen_recursive(add(A21, A22), B11, threshold)
    M3 = _strassen_recursive(A11, sub(B12, B22), threshold)
    M4 = _strassen_recursive(A22, sub(B21, B11), threshold)
    M5 = _strassen_recursive(add(A11, A12), B22, threshold)
    M6 = _strassen_recursive(sub(A21, A11), add(B11, B12), threshold)
    M7 = _strassen_recursive(sub(A12, A22), add(B21, B22), threshold)

    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    return join(C11, C12, C21, C22)

if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    C = strassen(A, B, threshold=1)
    print("A * B =")
    for row in C:
        print(row)

    # verify against naive
    expected = naive_mul(A, B)
    assert C == expected, "Strassen result differs from naive multiplication!"
    print("Verified: result matches naive multiplication.")