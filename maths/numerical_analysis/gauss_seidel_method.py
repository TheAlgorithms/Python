def gauss_seidel(
    a: list[list[float]], b: list[float], tol: float = 1e-10, max_iter: int = 1000
) -> list[float]:
    """
    Solve the linear system Ax = b using the Gauss-Seidel iterative method.

    Args:
        a (list[list[float]]): Coefficient matrix (n x n)
        b (list[float]): Right-hand side vector (n)
        tol (float): Convergence tolerance
        max_iter (int): Maximum number of iterations

    Returns:
        list[float]: Approximate solution vector

    Example:
        >>> A = [[4,1,2],[3,5,1],[1,1,3]]
        >>> b = [4,7,3]
        >>> gauss_seidel(A, b)
        [0.5, 1.0, 0.5]

    Wikipedia : https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method
    """
    n = len(a)
    x = [0.0] * n
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(a[i][j] * x_new[j] for j in range(i))
            s2 = sum(a[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / a[i][i]
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new
        x = x_new
    return x
