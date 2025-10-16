def gauss_seidel(
    coefficients: list[list[float]],
    rhs: list[float],
    tol: float = 1e-10,
    max_iter: int = 1000
) -> list[float]:
    """
    Solve the linear system Ax = b using the Gauss-Seidel iterative method.

    Args:
        coefficients (list[list[float]]): Coefficient matrix (n x n)
        rhs (list[float]): Right-hand side vector (n)
        tol (float): Convergence tolerance
        max_iter (int): Maximum number of iterations

    Returns:
        list[float]: Approximate solution vector

    Example:
        >>> A = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
        >>> b = [4, 7, 3]
        >>> gauss_seidel(A, b)
        [0.5, 1.0, 0.5]

    Wikipedia:
    https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method
    """
    n = len(coefficients)
    x = [0.0 for _ in range(n)]

    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_before = sum(coefficients[i][j] * x_new[j] for j in range(i))
            sum_after = sum(coefficients[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (rhs[i] - sum_before - sum_after) / coefficients[i][i]

        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new
        x = x_new

    return x
