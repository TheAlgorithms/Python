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

Matrix = list[list[int]]


def add(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Add two square matrices of the same size.

    >>> add([[1,2],[3,4]], [[5,6],[7,8]])
    [[6, 8], [10, 12]]
    """
    n = len(matrix_a)
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(n)] for i in range(n)]


def subtract(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Subtract matrix_b from matrix_a.

    >>> sub([[5,6],[7,8]], [[1,2],[3,4]])
    [[4, 4], [4, 4]]
    """
    n = len(matrix_a)
    return [[matrix_a[i][j] - matrix_b[i][j] for j in range(n)] for i in range(n)]


def naive_multiplication(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Multiply two square matrices using the naive O(n^3) method.

    >>> naive_mul([[1,2],[3,4]], [[5,6],[7,8]])
    [[19, 22], [43, 50]]
    """
    n = len(matrix_a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        row_a = matrix_a[i]
        row_result = result[i]
        for k in range(n):
            a_ik = row_a[k]
            col_b = matrix_b[k]
            for j in range(n):
                row_result[j] += a_ik * col_b[j]
    return result


def next_power_of_two(n: int) -> int:
    """
    Return the next power of two greater than or equal to n.

    >>> next_power_of_two(5)
    8
    """
    power = 1
    while power < n:
        power <<= 1
    return power


def pad_matrix(matrix: Matrix, size: int) -> Matrix:
    """
    Pad a matrix with zeros to reach the given size.

    >>> pad_matrix([[1,2],[3,4]], 4)
    [[1, 2, 0, 0], [3, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    rows = len(matrix)
    cols = len(matrix[0])
    padded = [[0] * size for _ in range(size)]
    for i in range(rows):
        for j in range(cols):
            padded[i][j] = matrix[i][j]
    return padded


def unpad_matrix(matrix: Matrix, rows: int, cols: int) -> Matrix:
    """
    Remove padding from a matrix.

    >>> unpad_matrix([[1,2,0],[3,4,0],[0,0,0]], 2, 2)
    [[1, 2], [3, 4]]
    """
    return [row[:cols] for row in matrix[:rows]]


def split(matrix: Matrix) -> tuple:
    """
    Split a matrix into four quadrants (top-left, top-right, bottom-left, bottom-right).

    >>> split([[1,2],[3,4]])
    ([[1]], [[2]], [[3]], [[4]])
    """
    n = len(matrix)
    mid = n // 2
    top_left = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    top_right = [[matrix[i][j] for j in range(mid, n)] for i in range(mid)]
    bottom_left = [[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
    bottom_right = [[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return top_left, top_right, bottom_left, bottom_right


def join(c11: Matrix, c12: Matrix, c21: Matrix, c22: Matrix) -> Matrix:
    """
    Join four quadrants into a single matrix.

    >>> join([[1]], [[2]], [[3]], [[4]])
    [[1, 2], [3, 4]]
    """
    n2 = len(c11)
    n = n2 * 2
    result = [[0] * n for _ in range(n)]
    for i in range(n2):
        for j in range(n2):
            result[i][j] = c11[i][j]
            result[i][j + n2] = c12[i][j]
            result[i + n2][j] = c21[i][j]
            result[i + n2][j + n2] = c22[i][j]
    return result


def strassen(matrix_a: Matrix, matrix_b: Matrix, threshold: int = 64) -> Matrix:
    """
    Multiply two square matrices using Strassen's algorithm.
    Uses naive multiplication for matrices smaller than threshold.

    >>> strassen([[1,2],[3,4]], [[5,6],[7,8]])
    [[19, 22], [43, 50]]
    """
    assert len(matrix_a) == len(matrix_a[0]) == len(matrix_b) == len(matrix_b[0]), (
        "Only square matrices supported"
    )

    n_orig = len(matrix_a)
    if n_orig == 0:
        return []

    if (m := next_power_of_two(n_orig)) != n_orig:
        a_pad = pad_matrix(matrix_a, m)
        b_pad = pad_matrix(matrix_b, m)
    else:
        a_pad, b_pad = matrix_a, matrix_b

    c_pad = _strassen_recursive(a_pad, b_pad, threshold)
    return unpad_matrix(c_pad, n_orig, n_orig)


def _strassen_recursive(matrix_a: Matrix, matrix_b: Matrix, threshold: int) -> Matrix:
    n = len(matrix_a)
    if n <= threshold:
        return naive_multiplication(matrix_a, matrix_b)
    if n == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]

    a11, a12, a21, a22 = split(matrix_a)
    b11, b12, b21, b22 = split(matrix_b)

    m1 = _strassen_recursive(add(a11, a22), add(b11, b22), threshold)
    m2 = _strassen_recursive(add(a21, a22), b11, threshold)
    m3 = _strassen_recursive(a11, subtract(b12, b22), threshold)
    m4 = _strassen_recursive(a22, subtract(b21, b11), threshold)
    m5 = _strassen_recursive(add(a11, a12), b22, threshold)
    m6 = _strassen_recursive(subtract(a21, a11), add(b11, b12), threshold)
    m7 = _strassen_recursive(subtract(a12, a22), add(b21, b22), threshold)

    c11 = add(subtract(add(m1, m4), m5), m7)
    c12 = add(m3, m5)
    c21 = add(m2, m4)
    c22 = add(subtract(add(m1, m3), m2), m6)

    return join(c11, c12, c21, c22)


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    C = strassen(A, B, threshold=1)
    print("A * B =")
    for row in C:
        print(row)

    expected = naive_multiplication(A, B)
    assert expected == C, "Strassen result differs from naive multiplication!"
    print("Verified: result matches naive multiplication.")
