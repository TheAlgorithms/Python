import numpy as np


def cholesky_decomposition(matrix: np.ndarray) -> np.ndarray:
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

    The Cholesky decomposition can be used to solve the linear system A x = y.

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

    assert (
        matrix.shape[0] == matrix.shape[1]
    ), f"Input matrix is not square, {matrix.shape=}"
    assert np.allclose(matrix, matrix.T), "Input matrix must be symmetric"

    n = matrix.shape[0]
    lower_triangle = np.tril(matrix)

    for i in range(n):
        for j in range(i + 1):
            lower_triangle[i, j] -= np.sum(
                lower_triangle[i, :j] * lower_triangle[j, :j]
            )

            if i == j:
                if lower_triangle[i, i] <= 0:
                    raise ValueError("Matrix A is not positive definite")

                lower_triangle[i, i] = np.sqrt(lower_triangle[i, i])
            else:
                lower_triangle[i, j] /= lower_triangle[j, j]

    return lower_triangle


def solve_cholesky(
    lower_triangle: np.ndarray,
    right_hand_side: np.ndarray,
) -> np.ndarray:
    """Given a Cholesky decomposition L L^T = A of a matrix A, solve the
    system of equations A X = Y where the right-hand side Y is either
    a matrix or a vector.

    >>> L = np.array([[2, 0], [3, 4]], dtype=float)
    >>> Y = np.array([[22, 54], [81, 193]], dtype=float)
    >>> X = solve_cholesky(L, Y)
    >>> np.allclose(X, np.array([[1, 3], [3, 7]], dtype=float))
    True
    """

    assert (
        lower_triangle.shape[0] == lower_triangle.shape[1]
    ), f"Matrix L is not square, {lower_triangle.shape=}"
    assert np.allclose(
        np.tril(lower_triangle), lower_triangle
    ), "Matrix L is not lower triangular"

    # Handle vector case by reshaping to matrix and then flattening again
    if len(right_hand_side.shape) == 1:
        return solve_cholesky(lower_triangle, right_hand_side.reshape(-1, 1)).ravel()

    n = right_hand_side.shape[0]

    # Solve L W = Y for W
    w = right_hand_side.copy()
    for i in range(n):
        for j in range(i):
            w[i] -= lower_triangle[i, j] * w[j]

        w[i] /= lower_triangle[i, i]

    # Solve L^T X = W for X
    x = w
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            x[i] -= lower_triangle[j, i] * x[j]

        x[i] /= lower_triangle[i, i]

    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()
