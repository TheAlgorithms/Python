"""
Implementation of Strassen's matrix multiplication algorithm.
https://en.wikipedia.org/wiki/Strassen_algorithm

This is a divide-and-conquer algorithm that is asymptotically faster
than the standard O(n^3) matrix multiplication for large matrices.

Note: In Python, due to the overhead of recursion and list slicing,
this implementation will be *slower* than the iterative version
for small or medium-sized matrices (like 4x4).
"""

# type Matrix = list[list[int]]  # psf/black currently fails on this line
Matrix = list[list[int]]

# --- Test Matrices (reused from other files) ---
matrix_1_to_4 = [
    [1, 2],
    [3, 4],
]

matrix_5_to_8 = [
    [5, 6],
    [7, 8],
]

matrix_count_up = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

matrix_unordered = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1],
    [2, 6, 10, 14],
]

matrix_non_square = [
    [1, 2, 3],
    [4, 5, 6],
]


# --- Helper function from matrix_multiplication_recursion.py ---
def is_square(matrix: Matrix) -> bool:
    """
    Checks if a matrix is square.
    >>> is_square(matrix_1_to_4)
    True
    >>> is_square(matrix_non_square)
    False
    """
    len_matrix = len(matrix)
    return all(len(row) == len_matrix for row in matrix)


# --- Helper function for benchmarking ---
def matrix_multiply(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Standard iterative matrix multiplication for comparison.
    >>> matrix_multiply(matrix_1_to_4, matrix_5_to_8)
    [[19, 22], [43, 50]]
    """
    return [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_b)]
        for row in matrix_a
    ]


# --- Helper functions for Strassen's Algorithm ---


def matrix_add(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Adds two matrices element-wise.
    >>> matrix_add(matrix_1_to_4, matrix_5_to_8)
    [[6, 8], [10, 12]]
    """
    return [
        [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
        for i in range(len(matrix_a))
    ]


def matrix_subtract(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Subtracts matrix_b from matrix_a element-wise.
    >>> matrix_subtract(matrix_5_to_8, matrix_1_to_4)
    [[4, 4], [4, 4]]
    """
    return [
        [matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a[0]))]
        for i in range(len(matrix_a))
    ]


def split_matrix(matrix: Matrix) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    """
    Splits a given matrix into four equal quadrants.
    >>> a, b, c, d = split_matrix(matrix_count_up)
    >>> a
    [[1, 2], [5, 6]]
    >>> b
    [[3, 4], [7, 8]]
    >>> c
    [[9, 10], [13, 14]]
    >>> d
    [[11, 12], [15, 16]]
    """
    n = len(matrix) // 2
    a11 = [row[:n] for row in matrix[:n]]
    a12 = [row[n:] for row in matrix[:n]]
    a21 = [row[:n] for row in matrix[n:]]
    a22 = [row[n:] for row in matrix[n:]]
    return a11, a12, a21, a22


def combine_matrices(
    c11: Matrix, c12: Matrix, c21: Matrix, c22: Matrix
) -> Matrix:
    """
    Combines four quadrants into a single matrix.
    >>> a, b, c, d = split_matrix(matrix_count_up)
    >>> combine_matrices(a, b, c, d) == matrix_count_up
    True
    """
    n = len(c11)
    result = []
    for i in range(n):
        result.append(c11[i] + c12[i])
    for i in range(n):
        result.append(c21[i] + c22[i])
    return result


def pad_matrix(matrix: Matrix, target_size: int) -> Matrix:
    """Pads a matrix with zeros to reach the target_size."""
    n = len(matrix)
    if n == target_size:
        return matrix

    padded_matrix = [[0] * target_size for _ in range(target_size)]
    for i in range(n):
        for j in range(len(matrix[i])):
            padded_matrix[i][j] = matrix[i][j]
    return padded_matrix


def unpad_matrix(matrix: Matrix, original_size: int) -> Matrix:
    """Removes padding to return to the original_size."""
    if len(matrix) == original_size:
        return matrix
    return [row[:original_size] for row in matrix[:original_size]]


# --- Main Strassen Function ---


def strassen(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    :param matrix_a: A square Matrix.
    :param matrix_b: Another square Matrix with the same dimensions as matrix_a.
    :return: Result of matrix_a * matrix_b.
    :raises ValueError: If the matrices cannot be multiplied.

    >>> strassen([], [])
    []
    >>> strassen(matrix_1_to_4, matrix_5_to_8)
    [[19, 22], [43, 50]]
    >>> strassen(matrix_count_up, matrix_unordered)
    [[37, 61, 74, 61], [105, 165, 166, 129], [173, 269, 258, 197], [241, 373, 350, 265]]
    >>> strassen(matrix_1_to_4, matrix_non_square)
    Traceback (most recent call last):
        ...
    ValueError: Matrices must be square and of the same dimensions
    >>> strassen(matrix_1_to_4, matrix_count_up)
    Traceback (most recent call last):
        ...
    ValueError: Matrices must be square and of the same dimensions
    """
    if not matrix_a or not matrix_b:
        return []

    if not (
        len(matrix_a) == len(matrix_b)
        and is_square(matrix_a)
        and is_square(matrix_b)
    ):
        raise ValueError("Matrices must be square and of the same dimensions")

    original_size = len(matrix_a)

    # Base case
    if original_size == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]

    # Pad matrix to the next power of 2
    n = original_size
    if n & (n - 1) != 0:
        next_power_of_2 = 1 << n.bit_length()
        a = pad_matrix(matrix_a, next_power_of_2)
        b = pad_matrix(matrix_b, next_power_of_2)
        n = next_power_of_2
    else:
        a = matrix_a
        b = matrix_b

    # Split matrices into quadrants
    a11, a12, a21, a22 = split_matrix(a)
    b11, b12, b21, b22 = split_matrix(b)

    # Calculate the 7 Strassen products recursively
    p1 = strassen(a11, matrix_subtract(b12, b22))
    p2 = strassen(matrix_add(a11, a12), b22)
    p3 = strassen(matrix_add(a21, a22), b11)
    p4 = strassen(a22, matrix_subtract(b21, b11))
    p5 = strassen(matrix_add(a11, a22), matrix_add(b11, b22))
    p6 = strassen(matrix_subtract(a12, a22), matrix_add(b21, b22))
    p7 = strassen(matrix_subtract(a11, a21), matrix_add(b11, b12))

    # Calculate result quadrants
    c11 = matrix_add(matrix_subtract(matrix_add(p5, p4), p2), p6)
    c12 = matrix_add(p1, p2)
    c21 = matrix_add(p3, p4)
    c22 = matrix_subtract(matrix_subtract(matrix_add(p5, p1), p3), p7)

    # Combine result quadrants
    result = combine_matrices(c11, c12, c21, c22)

    # Unpad the result to match original dimensions
    return unpad_matrix(result, original_size)


if __name__ == "__main__":
    from doctest import testmod

    failure_count, test_count = testmod()
    if not failure_count:
        print("\nBenchmark (Note: Strassen has high overhead in Python):")
        from functools import partial
        from timeit import timeit

        # Run fewer iterations as Strassen is slower for small matrices in Python
        mytimeit = partial(timeit, globals=globals(), number=10_0DENIED)
        for func in ("matrix_multiply", "strassen"):
            print(
                f"{func:>25}(): "
                f"{mytimeit(f'{func}(matrix_count_up, matrix_unordered)')}"
            )
