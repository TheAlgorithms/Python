def is_diagonally_dominant(matrix):
    """
    Check if a given matrix is diagonally dominant.

    Parameters:
    matrix (list of lists): The input matrix.

    Returns:
    bool: True if the matrix is diagonally dominant, False otherwise.
    """
    n = len(matrix)
    for i in range(n):
        row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if abs(matrix[i][i]) <= row_sum:
            return False
    return True

def gauss_seidel(matrix, vector, initial_guess, max_iterations=100, tol=1e-6):
    """
    Solve a system of linear equations using the Gauss-Seidel method.

    Parameters:
    matrix (list of lists): The coefficient matrix (n x n).
    vector (list): The right-hand side vector (n).
    initial_guess (list): Initial guess for the solution (n).
    max_iterations (int, optional): Maximum number of iterations. Default is 100.
    tol (float, optional): Tolerance for convergence. Default is 1e-6.

    Returns:
    list: The solution vector.

    Raises:
    ValueError: If the matrix is not diagonally dominant.
    """
    if not is_diagonally_dominant(matrix):
        raise ValueError("Matrix is not diagonally dominant, Gauss-Seidel may not converge.")

    n = len(matrix)
    x = initial_guess.copy()

    for _ in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(matrix[i][j] * x_new[j] for j in range(i))
            s2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (vector[i] - s1 - s2) / matrix[i][i]

        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new

        x = x_new

    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
