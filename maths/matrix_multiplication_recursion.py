# @Author  : ojas-wani
# @File    : matrix_multiplication_recursion.py
# @Date    : 10/06/2023


"""
Introduction:

This Python script demonstrates matrix multiplication using a recursive algorithm. 
Matrix multiplication is a fundamental operation in linear algebra and computer science.
"""


def matrix_multiply_recursive(matrix_A: list, matrix_B: list):
    """
    :param matrix_A: Input matrices.
    :param matrix_B: Input matrices where length of matrices is 
                    as same as number of columns matrix_A.

    """

    # Check if matrices can be multiplied
    if len(matrix_A[0]) != len(matrix_B):
        raise ValueError("Invalid matrix dimensions")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix_B[0]))]
              for _ in range(len(matrix_A))]

    # Recursive multiplication of matrices
    def multiply(i, j, k, matrix_A, matrix_B, result):
        """
        :param matrix_A: Input matrices.
        :param matrix_B: Input matrices where length of matrices is 
                    as same as number of columns matrix_A.
        :param result: Result matrix
        :param i: Indices used for iteration during multiplication.
        :param j: Indices used for iteration during multiplication.
        :param k: Indices used for iteration during multiplication.
        """

        if i >= len(matrix_A):
            return
        if j >= len(matrix_B[0]):
            return multiply(matrix_A, matrix_B, result, i + 1, 0, 0)
        if k >= len(matrix_B):
            return multiply(matrix_A, matrix_B, result, i, j + 1, 0)
        result[i][j] += matrix_A[i][k] * matrix_B[k][j]
        multiply(matrix_A, matrix_B, result, i, j, k + 1)

    # Perform matrix multiplication
    multiply(matrix_A, matrix_B, result, 0, 0, 0)
    return result


if __name__ == "__main__":

    # Input matrixes
    matrix_A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [13, 14, 15, 16]
    ]
    matrix_B = [
        [5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1],
        [2, 6, 10, 14]
    ]

    result_matrix = matrix_multiply_recursive(matrix_A, matrix_B)
    for row in result_matrix:
        print(row)
