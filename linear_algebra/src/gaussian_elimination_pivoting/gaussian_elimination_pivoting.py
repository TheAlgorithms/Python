import sys
import time

import numpy as np


def solve_linear_system(matrix: np.ndarray) -> np.ndarray:
    """
    Solves a linear system of equations using
    Gaussian elimination with partial pivoting.

    Args:
    - matrix (np.ndarray): Coefficient matrix
    with the last column representing the constants.

    Returns:
    - np.ndarray: Solution vector.

    Raises:
    - sys.exit: If the matrix is not correct
    (i.e., singular).

    Example:
    >>> A = np.array([[2, 1, -1], [-3, -1, 2]
    , [-2, 1, 2]], dtype=float)
    >>> B = np.array([8, -11, -3], dtype=float)
    >>> solution = solve_linear_system(np.column_stack((A, B)))
    >>> np.allclose(solution, np.array([2., 3., -1.]))
    True
    """
    start = time.process_time()
    ab = np.copy(matrix)
    num_of_rows = ab.shape[0]
    num_of_columns = ab.shape[1] - 1
    x_lst: List[Union[int, float]] = []

    # Lead element search
    for column_num in range(num_of_rows):
        for i in range(column_num, num_of_columns):
            if abs(ab[i][column_num]) > abs(ab[column_num][column_num]):
                ab[[column_num, i]] = ab[[i, column_num]]
                if ab[column_num, column_num] == 0.0:
                    raise sys.exit("Matrix is not correct")
            else:
                pass
        if column_num != 0:
            for i in range(column_num, num_of_rows):
                ab[i, :] -= (
                    ab[i, column_num - 1]
                    / ab[column_num - 1, column_num - 1]
                    * ab[column_num - 1, :]
                )

    # Upper triangular matrix
    for column_num in range(num_of_rows):
        for i in range(column_num, num_of_columns):
            if abs(ab[i][column_num]) > abs(ab[column_num][column_num]):
                ab[[column_num, i]] = ab[[i, column_num]]
                if ab[column_num, column_num] == 0.0:
                    raise sys.exit("Matrix is not correct")
            else:
                pass
        if column_num != 0:
            for i in range(column_num, num_of_rows):
                ab[i, :] -= (
                    ab[i, column_num - 1]
                    / ab[column_num - 1, column_num - 1]
                    * ab[column_num - 1, :]
                )

    # Find x vector
    column_num = num_of_rows
    while column_num != 0:
        column_num -= 1
        line_of_x = ab[column_num, num_of_rows]
        if column_num + 1 != num_of_rows:
            for y in range(1, num_of_rows - column_num):
                line_of_x += -ab[column_num, num_of_rows - y] * x_lst[y - 1]
        x = line_of_x / ab[column_num, column_num]
        x_lst.append(x)

    stop = time.process_time()

    # Return the solution vector
    return np.asarray(x_lst)

if __name__ == "__main__":
    vectorofxalpha = foo(matrixab)


    """Cond(A)"""
    modifiedb = np.copy(B)
    modifiedb[np.argmax(abs(B))] = B[np.argmax(abs(B))] / 100 * 101

    matrixab[:, matrixab.shape[1] - 1] = modifiedb
    print()
    print("Cond(A) check: ")
    vectorofxbeta = foo(matrixab)

    deltab = modifiedb - B
    deltax = vectorofxalpha - vectorofxbeta
    print(" ")
    conda = abs(np.sum(deltax) / np.sum(vectorofxalpha)) * (np.sum(B) / np.sum(deltab))
    print(f"Cond(A) =< {conda:0.6f}")


# Example usage:
# n_size = 3
# a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
# b_vector = np.array([10, 11, 12], dtype=float)

# solution = custom_gauss_elimination_pivoting(a_matrix, b_vector, n_size)
# print("Solution:", solution)


# URL that points to Wikipedia or another similar explanation.
# >>>>>>URL:https://courses.engr.illinois.edu/cs357/su2013/lectures/lecture07.pdf<<<<<#
