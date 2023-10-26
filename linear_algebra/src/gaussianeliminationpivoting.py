import numpy as np
def custom_pivoting(matrix: np.ndarray, n: int, i: int) -> int:
    """
    Selects the index of the minimum absolute 
    value in the i-th column of a matrix.

    Parameters:
    - matrix (np.ndarray): The input matrix.
    - n (int): The size of the matrix.
    - i (int): The column index.

    Returns:
    - int: The index of the minimum absolute value in the 
    i-th column.

    Example:
    >>> a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
    dtype=float)
    >>> custom_pivoting(a_matrix, 3, 1)
    0
    """
    min_index = i
    for index in range(i + 1, n):
        if abs(matrix[index][i]) < abs(matrix[min_index][i]):
            min_index = index
    return min_index


def custom_gauss_elimination_pivoting(
    coeff_matrix: list, const_vector: list, n: int
) -> list:
    """
    Solves a system of linear equations 
    using Gaussian elimination with partial pivoting.

    Parameters:
    - coeff_matrix (list): The coefficient matrix.
    - const_vector (list): The constant vector.
    - n (int): The size of the system.

    Returns:
    - list: The solution vector.

    Example:
    >>> a_matrix = [[2, 3, 4], [1, -2, 3], [3, 4, 5]]
    >>> b_vector = [20, 9, 11]
    >>> custom_gauss_elimination_pivoting(a_matrix, b_vector, 3)
    [1.0, 2.0, 3.0]
    """
    result = []
    for i in range(n - 1):
        new_index = custom_pivoting(coeff_matrix, n, i)
        coeff_matrix[i], coeff_matrix[new_index] = (
            coeff_matrix[new_index],
            coeff_matrix[i],
        )
        const_vector[i], const_vector[new_index] = (
            const_vector[new_index],
            const_vector[i],
        )
        pivot = coeff_matrix[i][i]
        for j in range(i + 1, n):
            m = -1 * coeff_matrix[j][i] / pivot
            for k in range(n):
                coeff_matrix[j][k] += m * coeff_matrix[i][k]
            const_vector[j] += m * const_vector[i]

    for p in range(n - 1, -1, -1):
        result.append(const_vector[p] / coeff_matrix[p][p])
        for q in range(p - 1, -1, -1):
            const_vector[q] = const_vector[q] - result[n - p - 1] * coeff_matrix[q][p]
    return result


# Example usage:
# n_size = 3
# a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
# b_vector = np.array([10, 11, 12], dtype=float)

# solution = custom_gauss_elimination_pivoting(a_matrix, b_vector, n_size)
# print("Solution:", solution)


# URL that points to Wikipedia or another similar explanation.
# >>>>>>URL:https://courses.engr.illinois.edu/cs357/su2013/lectures/lecture07.pdf<<<<<#
