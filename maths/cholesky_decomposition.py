import numpy as np


def cholesky_decomposition(a: np.ndarray) -> np.ndarray:
    """Return a Cholesky decomposition of the matrix A.

    The Cholesky decomposition decomposes the square, positive definite matrix A
    into a lower triangular matrix L such that A = L L^T.

    https://en.wikipedia.org/wiki/Cholesky_decomposition

    Arguments:
    A -- a numpy.ndarray of shape (n, n)

    >>> A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=float)
    >>> L = cholesky_decomposition(A)
    >>> np.allclose(L, np.array([[2, 0, 0], [6, 1, 0], [-8, 5, 3]]))
    True

    >>> # check that the decomposition is correct
    >>> np.allclose(L @ L.T, A)
    True

    >>> # check that L is lower triangular
    >>> np.allclose(np.tril(L), L)
    True

    The Cholesky decomposition can be used to solve the system of equations A x = y.

    >>> x_true = np.array([1, 2, 3], dtype=float)
    >>> y = A @ x_true
    >>> x = solve_cholesky(L, y)
    >>> np.allclose(x, x_true)
    True

    It can also be used to solve multiple equations A X = Y simultaneously.

    >>> X_true = np.random.rand(3, 3)
    >>> Y = A @ X_true
    >>> X = solve_cholesky(L, Y)
    >>> np.allclose(X, X_true)
    True
    """
    assert a.shape[0] == a.shape[1]
    n = a.shape[0]
    lo = np.tril(a)

    for i in range(n):
        for j in range(i):
            lo[i, j] = (lo[i, j] - np.sum(lo[i, :j] * lo[j, :j])) / lo[j, j]

        s = lo[i, i] - np.sum(lo[i, :i] * lo[i, :i])

        if s <= 0:
            raise ValueError("Matrix A is not positive definite")

        lo[i, i] = np.sqrt(s)

    return lo


def solve_cholesky(lo: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Given a Cholesky decomposition L L^T = A of a matrix A, solve the
    system of equations A X = Y where B is either a matrix or a vector.

    >>> L = np.array([[2, 0], [3, 4]], dtype=float)
    >>> Y = np.array([[22, 54], [81, 193]], dtype=float)
    >>> X = solve_cholesky(L, Y)
    >>> np.allclose(X, np.array([[1, 3], [3, 7]], dtype=float))
    True
    """

    # Handle vector case by reshaping to matrix and then flattening again
    if len(y.shape) == 1:
        return solve_cholesky(lo, y.reshape(-1, 1)).ravel()

    n, m = y.shape

    # Backsubstitute L X = B
    x = y.copy()
    for i in range(n):
        for j in range(i):
            x[i, :] -= lo[i, j] * x[j, :]

        for k in range(m):
            x[i, k] /= lo[i, i]

    # Backsubstitute L^T
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            x[i, :] -= lo[j, i] * x[j, :]

        for k in range(m):
            x[i, k] /= lo[i, i]

    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()
