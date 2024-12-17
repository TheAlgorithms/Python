import numpy as np


def lanczos(a: np.ndarray) -> tuple[list[float], list[float]]:
    """
    Implements the Lanczos algorithm for a symmetric matrix.

    Parameters:
    -----------
    matrix : numpy.ndarray
        Symmetric matrix of size (n, n).

    Returns:
    --------
    alpha : [float]
        List of diagonal elements of the resulting tridiagonal matrix.
    beta : [float]
        List of off-diagonal elements of the resulting tridiagonal matrix.
    """
    n = a.shape[0]
    v = np.zeros((n, n))
    rng = np.random.default_rng()
    v[:, 0] = rng.standard_normal(n)
    v[:, 0] /= np.linalg.norm(v[:, 0])
    alpha: list[float] = []
    beta: list[float] = []
    for j in range(n):
        w = np.dot(a, v[:, j])
        alpha.append(np.dot(w, v[:, j]))
        if j == n - 1:
            break
        w -= alpha[j] * v[:, j]
        if j > 0:
            w -= beta[j - 1] * v[:, j - 1]
        beta.append(np.linalg.norm(w))
        v[:, j + 1] = w / beta[j]
    return alpha, beta
