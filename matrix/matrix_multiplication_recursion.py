# @Author  : ojas-wani
# @File    : matrix_multiplication_recursion.py
# @Date    : 10/06/2023


"""
Perform matrix multiplication using a recursive algorithm.
https://en.wikipedia.org/wiki/Matrix_multiplication
"""
# type Matrix = list[list[int]]  # psf/black currenttly fails on this line
Matrix = list[list[int]]

matrix_1_to_4 = [
    [1, 2],
    [3, 4],
]

matrix_5_to_8 = [
    [5, 6],
    [7, 8],
]

matrix_5_to_9_high = [
    [5, 6],
    [7, 8],
    [9],
]

matrix_5_to_9_wide = [
    [5, 6],
    [7, 8, 9],
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
matrices = (
    matrix_1_to_4,
    matrix_5_to_8,
    matrix_5_to_9_high,
    matrix_5_to_9_wide,
    matrix_count_up,
    matrix_unordered,
)


def is_square(matrix: Matrix) -> bool:
    """
    >>> is_square([])
    True
    >>> is_square(matrix_1_to_4)
    True
    >>> is_square(matrix_5_to_9_high)
    False
    """
    len_matrix = len(matrix)
    return all(len(row) == len_matrix for row in matrix)


def matrix_multiply(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    >>> matrix_multiply(matrix_1_to_4, matrix_5_to_8)
    [[19, 22], [43, 50]]
    """
    return [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_b)]
        for row in matrix_a
    ]


def matrix_multiply_recursive(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    :param matrix_a: A square Matrix.
    :param matrix_b: Another square Matrix with the same dimensions as matrix_a.
    :return: Result of matrix_a * matrix_b.
    :raises ValueError: If the matrices cannot be multiplied.

    >>> matrix_multiply_recursive([], [])
    []
    >>> matrix_multiply_recursive(matrix_1_to_4, matrix_5_to_8)
    [[19, 22], [43, 50]]
    >>> matrix_multiply_recursive(matrix_count_up, matrix_unordered)
    [[37, 61, 74, 61], [105, 165, 166, 129], [173, 269, 258, 197], [241, 373, 350, 265]]
    >>> matrix_multiply_recursive(matrix_1_to_4, matrix_5_to_9_wide)
    Traceback (most recent call last):
        ...
    ValueError: Invalid matrix dimensions
    >>> matrix_multiply_recursive(matrix_1_to_4, matrix_5_to_9_high)
    Traceback (most recent call last):
        ...
    ValueError: Invalid matrix dimensions
    >>> matrix_multiply_recursive(matrix_1_to_4, matrix_count_up)
    Traceback (most recent call last):
        ...
    ValueError: Invalid matrix dimensions
    """
    if not matrix_a or not matrix_b:
        return []
    if not all(
        (len(matrix_a) == len(matrix_b), is_square(matrix_a), is_square(matrix_b))
    ):
        raise ValueError("Invalid matrix dimensions")

    # Initialize the result matrix with zeros
    result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    # Recursive multiplication of matrices
    def multiply(
        i_loop: int,
        j_loop: int,
        k_loop: int,
        matrix_a: Matrix,
        matrix_b: Matrix,
        result: Matrix,
    ) -> None:
        """
        :param matrix_a: A square Matrix.
        :param matrix_b: Another square Matrix with the same dimensions as matrix_a.
        :param result: Result matrix
        :param i: Index used for iteration during multiplication.
        :param j: Index used for iteration during multiplication.
        :param k: Index used for iteration during multiplication.
        >>> 0 > 1  # Doctests in inner functions are never run
        True
        """
        if i_loop >= len(matrix_a):
            return
        if j_loop >= len(matrix_b[0]):
            return multiply(i_loop + 1, 0, 0, matrix_a, matrix_b, result)
        if k_loop >= len(matrix_b):
            return multiply(i_loop, j_loop + 1, 0, matrix_a, matrix_b, result)
        result[i_loop][j_loop] += matrix_a[i_loop][k_loop] * matrix_b[k_loop][j_loop]
        return multiply(i_loop, j_loop, k_loop + 1, matrix_a, matrix_b, result)

    # Perform the recursive matrix multiplication
    multiply(0, 0, 0, matrix_a, matrix_b, result)
    return result


if __name__ == "__main__":
    from doctest import testmod

    failure_count, test_count = testmod()
    if not failure_count:
        matrix_a = matrices[0]
        for matrix_b in matrices[1:]:
            print("Multiplying:")
            for row in matrix_a:
                print(row)
            print("By:")
            for row in matrix_b:
                print(row)
            print("Result:")
            try:
                result = matrix_multiply_recursive(matrix_a, matrix_b)
                for row in result:
                    print(row)
                assert result == matrix_multiply(matrix_a, matrix_b)
            except ValueError as e:
                print(f"{e!r}")
            print()
            matrix_a = matrix_b

    print("Benchmark:")
    from functools import partial
    from timeit import timeit

    mytimeit = partial(timeit, globals=globals(), number=100_000)
    for func in ("matrix_multiply", "matrix_multiply_recursive"):
        print(f"{func:>25}(): {mytimeit(f'{func}(matrix_count_up, matrix_unordered)')}")
