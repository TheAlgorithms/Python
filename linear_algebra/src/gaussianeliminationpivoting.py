import numpy as np

def custom_pivoting(a: np.ndarray, n: int, i: int) -> int:
    """
    Selects the index of the minimum absolute value in the i-th column of a matrix.

    Parameters:
    - a (np.ndarray): The input matrix.
    - n (int): The size of the matrix.
    - i (int): The column index.

    Returns:
    - int: The index of the minimum absolute value in the i-th column.

    Example:
    >> a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
    >> custom_pivoting(a_matrix, 3, 1)
    0
    """    
    min_index = i
    for index in range(i + 1, n):
        if abs(a[index][i]) < abs(a[min_index][i]):
            min_index = index
    return min_index

def custom_gauss_elimination_pivoting(a: list, b: list, n: int) -> list:
    """
    Solves a system of linear equations using Gaussian elimination with partial pivoting.

    Parameters:
    - a (list): The coefficient matrix.
    - b (list): The constant vector.
    - n (int): The size of the system.

    Returns:
    - list: The solution vector.

    Example:
    >>a_matrix = [[2, 3, 4], [1, -2, 3], [3, 4, 5]]
    >> b_vector = [20, 9, 11]
    >> custom_gauss_elimination_pivoting(a_matrix, b_vector, 3)
    [1.0, 2.0, 3.0]
    """
    result = []
    for i in range(n - 1):
        new_index = custom_pivoting(a, n, i)
        a[i], a[new_index] = a[new_index], a[i]
        b[i], b[new_index] = b[new_index], b[i]
        pivot = a[i][i]
        for j in range(i + 1, n):
            m = -1 * a[j][i] / pivot
            for k in range(0, n):
                a[j][k] += m * a[i][k]
            b[j] += m * b[i]

    for p in range(n - 1, -1, -1):
        result.append(b[p] / a[p][p])
        for q in range(p - 1, -1, -1):
            b[q] = b[q] - result[n - p - 1] * a[q][p]
    return result




# Example usage:
# n_size = 3
# a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
# b_vector = np.array([10, 11, 12], dtype=float)

# solution = custom_gauss_elimination_pivoting(a_matrix, b_vector, n_size)
# print("Solution:", solution)


#URL that points to Wikipedia or another similar explanation.
#>>>>>>URL:https://courses.engr.illinois.edu/cs357/su2013/lectures/lecture07.pdf<<<<<#
