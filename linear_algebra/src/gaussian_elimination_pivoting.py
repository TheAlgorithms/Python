import numpy as np

def custom_pivoting(matrix: np.ndarray, num_rows: int, column_index: int) -> int:
    """
    Selects the index of the minimum absolute
    value in the specified column of a matrix.

    Parameters:
    - matrix (np.ndarray): The input matrix.
    - num_rows (int): The number of rows in the matrix.
    - column_index (int): The index of the column.

    Returns:
    - int: The index of the minimum absolute value in the specified column.

    Example:
    >>> a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
    >>> custom_pivoting(a_matrix, 3, 1)
    0
    """
    min_index = column_index
    for index in range(column_index + 1, num_rows):
        if abs(matrix[index][column_index]) < abs(matrix[min_index][column_index]):
            min_index = index
    return min_index

def custom_gauss_elimination_pivoting(
    matrix: list, const_vector: list, num_equations: int
) -> list:
    """
        Solves a system of linear equations using Gaussian
    elimination with partial pivoting.
        Parameters:
        - coeff_matrix (list): The coefficient matrix.
        - const_vector (list): The constant vector.
        - num_equations (int): The number of equations in the system.
        Returns:
        - list: The solution vector.
        Example:
        >>> a_matrix = [[2, 3, 4], [1, -2, 3], [3, 4, 5]]
        >>> b_vector = [20, 9, 11]
        >>> custom_gauss_elimination_pivoting(a_matrix, b_vector, 3)
        [1.0, 2.0, 3.0]
    """
    result = []
    for i in range(num_equations - 1):
        new_index = custom_pivoting(matrix, num_equations, i)
        matrix[i], matrix[new_index] = matrix[new_index], matrix[i]
        const_vector[i], const_vector[new_index] = (
            const_vector[new_index],
            const_vector[i],
        )
        pivot = matrix[i][i]
        for j in range(i + 1, num_equations):
            m = -1 * matrix[j][i] / pivot
            for k in range(num_equations):
                matrix[j][k] += m * matrix[i][k]
            const_vector[j] += m * const_vector[i]
    for row_index in range(num_equations - 1, -1, -1):
        result.append(const_vector[row_index] / matrix[row_index][row_index])
        for q in range(row_index - 1, -1, -1):
            const_vector[q] = (
                const_vector[q]
                - result[num_equations - row_index - 1] * matrix[q][row_index]
            )
    return result


# Example usage:
# n_size = 3
# a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
# b_vector = np.array([10, 11, 12], dtype=float)

# solution = custom_gauss_elimination_pivoting(a_matrix, b_vector, n_size)
# print("Solution:", solution)


# URL that points to Wikipedia or another similar explanation.
# >>>>>>URL:https://courses.engr.illinois.edu/cs357/su2013/lectures/lecture07.pdf<<<<<#