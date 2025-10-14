"""
Strassen's Matrix Multiplication Algorithm (Descriptive Version)
---------------------------------------------------------------
An optimized divide-and-conquer algorithm for matrix multiplication that
reduces the number of multiplications from 8 (in the naive approach)
to 7 per recursion step.

This results in a time complexity of approximately O(n^2.807),
which is faster than the standard O(n^3) algorithm for large matrices.

Reference:
https://en.wikipedia.org/wiki/Strassen_algorithm
"""

Matrix = list[list[int]]


def add_matrices(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Add two square matrices of the same size.
    """
    size = len(matrix_a)
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(size)] for i in range(size)]


def subtract_matrices(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Subtract matrix_b from matrix_a.
    """
    size = len(matrix_a)
    return [[matrix_a[i][j] - matrix_b[i][j] for j in range(size)] for i in range(size)]


def multiply_matrices_naive(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Multiply two square matrices using the naive O(n^3) method.
    """
    size = len(matrix_a)
    result_matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for k in range(size):
            for j in range(size):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix


def get_next_power_of_two(n: int) -> int:
    """
    Return the next power of two greater than or equal to n.
    """
    power = 1
    while power < n:
        power <<= 1
    return power


def pad_matrix_to_size(matrix: Matrix, target_size: int) -> Matrix:
    """
    Pad a matrix with zeros to reach the given target size.
    """
    rows, cols = len(matrix), len(matrix[0])
    padded_matrix = [[0] * target_size for _ in range(target_size)]
    for i in range(rows):
        for j in range(cols):
            padded_matrix[i][j] = matrix[i][j]
    return padded_matrix


def remove_matrix_padding(
    matrix: Matrix, original_rows: int, original_cols: int
) -> Matrix:
    """
    Remove zero padding from a matrix to restore its original size.
    """
    return [row[:original_cols] for row in matrix[:original_rows]]


def split_matrix_into_quadrants(
    matrix: Matrix,
) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    """
    Split a matrix into four equal quadrants:
    top-left, top-right, bottom-left, bottom-right.
    """
    size = len(matrix)
    mid = size // 2
    top_left = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    top_right = [[matrix[i][j] for j in range(mid, size)] for i in range(mid)]
    bottom_left = [[matrix[i][j] for j in range(mid)] for i in range(mid, size)]
    bottom_right = [[matrix[i][j] for j in range(mid, size)] for i in range(mid, size)]
    return top_left, top_right, bottom_left, bottom_right


def join_matrix_quadrants(
    top_left: Matrix, top_right: Matrix, bottom_left: Matrix, bottom_right: Matrix
) -> Matrix:
    """
    Join four quadrants into a single square matrix.
    """
    quadrant_size = len(top_left)
    full_size = quadrant_size * 2
    combined_matrix = [[0] * full_size for _ in range(full_size)]

    for i in range(quadrant_size):
        for j in range(quadrant_size):
            combined_matrix[i][j] = top_left[i][j]
            combined_matrix[i][j + quadrant_size] = top_right[i][j]
            combined_matrix[i + quadrant_size][j] = bottom_left[i][j]
            combined_matrix[i + quadrant_size][j + quadrant_size] = bottom_right[i][j]
    return combined_matrix


def strassen_matrix_multiplication(
    matrix_a: Matrix, matrix_b: Matrix, threshold: int = 64
) -> Matrix:
    """
    Multiply two square matrices using Strassen's algorithm.
    Uses naive multiplication for matrices smaller than the threshold.
    """
    assert len(matrix_a) == len(matrix_a[0]) == len(matrix_b) == len(matrix_b[0]), (
        "Strassen's algorithm supports only square matrices."
    )

    original_size = len(matrix_a)
    if original_size == 0:
        return []

    # Pad matrices to next power of two for even splitting
    if (padded_size := get_next_power_of_two(original_size)) != original_size:
        matrix_a = pad_matrix_to_size(matrix_a, padded_size)
        matrix_b = pad_matrix_to_size(matrix_b, padded_size)

    result_padded = _strassen_recursive_multiply(matrix_a, matrix_b, threshold)
    return remove_matrix_padding(result_padded, original_size, original_size)


def _strassen_recursive_multiply(
    matrix_a: Matrix, matrix_b: Matrix, threshold: int
) -> Matrix:
    """
    Recursive implementation of Strassen's algorithm.
    """
    size = len(matrix_a)

    # Base case: use naive multiplication for small matrices
    if size <= threshold:
        return multiply_matrices_naive(matrix_a, matrix_b)

    if size == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]

    # Split matrices into quadrants
    a11, a12, a21, a22 = split_matrix_into_quadrants(matrix_a)
    b11, b12, b21, b22 = split_matrix_into_quadrants(matrix_b)

    # Compute the 7 Strassen products
    p1 = _strassen_recursive_multiply(
        add_matrices(a11, a22), add_matrices(b11, b22), threshold
    )
    p2 = _strassen_recursive_multiply(add_matrices(a21, a22), b11, threshold)
    p3 = _strassen_recursive_multiply(a11, subtract_matrices(b12, b22), threshold)
    p4 = _strassen_recursive_multiply(a22, subtract_matrices(b21, b11), threshold)
    p5 = _strassen_recursive_multiply(add_matrices(a11, a12), b22, threshold)
    p6 = _strassen_recursive_multiply(
        subtract_matrices(a21, a11), add_matrices(b11, b12), threshold
    )
    p7 = _strassen_recursive_multiply(
        subtract_matrices(a12, a22), add_matrices(b21, b22), threshold
    )

    # Combine partial results into final quadrants
    c11 = add_matrices(subtract_matrices(add_matrices(p1, p4), p5), p7)
    c12 = add_matrices(p3, p5)
    c21 = add_matrices(p2, p4)
    c22 = add_matrices(subtract_matrices(add_matrices(p1, p3), p2), p6)

    return join_matrix_quadrants(c11, c12, c21, c22)


if __name__ == "__main__":
    matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    result_matrix = strassen_matrix_multiplication(matrix_A, matrix_B, threshold=1)
    print("A × B =")
    for row in result_matrix:
        print(row)

    expected_matrix = multiply_matrices_naive(matrix_A, matrix_B)
    assert expected_matrix == result_matrix, (
        "Strassen result differs from naive multiplication!"
    )
    print("Verified: result matches naive multiplication.")
