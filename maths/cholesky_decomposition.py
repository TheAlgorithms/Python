import numpy as np


# ruff: noqa: N803,N806
def cholesky_decomposition(A: np.ndarray) -> np.ndarray:
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

    assert A.shape[0] == A.shape[1], f"A is not square, {A.shape=}"

    n = A.shape[0]
    L = np.tril(A)

    for i in range(n):
        for j in range(i + 1):
            L[i, j] -= np.sum(L[i, :j] * L[j, :j])

            if i == j:
                if L[i, i] <= 0:
                    raise ValueError("Matrix A is not positive definite")

                L[i, i] = np.sqrt(L[i, i])
            else:
                L[i, j] /= L[j, j]

    return L


def solve_cholesky(L: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """Given a Cholesky decomposition L L^T = A of a matrix A, solve the
    system of equations A X = Y where B is either a matrix or a vector.

    >>> L = np.array([[2, 0], [3, 4]], dtype=float)
    >>> Y = np.array([[22, 54], [81, 193]], dtype=float)
    >>> X = solve_cholesky(L, Y)
    >>> np.allclose(X, np.array([[1, 3], [3, 7]], dtype=float))
    True
    """

    assert L.shape[0] == L.shape[1], f"L is not square, {L.shape=}"
    assert np.allclose(np.tril(L), L), "L is not lower triangular"

    # Handle vector case by reshaping to matrix and then flattening again
    if len(Y.shape) == 1:
        return solve_cholesky(L, Y.reshape(-1, 1)).ravel()

    n = Y.shape[0]

    # Solve L W = B for W
    W = Y.copy()
    for i in range(n):
        for j in range(i):
            W[i] -= L[i, j] * W[j]

        W[i] /= L[i, i]

    # Solve L^T X = W for X
    X = W
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            X[i] -= L[j, i] * X[j]

        X[i] /= L[i, i]

    return X


if __name__ == "__main__":
    import doctest

    doctest.testmod()
