import numpy as np


def lanczos(A: np.ndarray) -> ([float], [float]):
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
    n = A.shape[0]
    V = np.zeros((n, n))
    V[:, 0] = np.random.randn(n)
    V[:, 0] /= np.linalg.norm(V[:, 0])
    alpha = []
    beta = []
    for j in range(n):
        w = np.dot(A, V[:, j])
        alpha.append(np.dot(w, V[:, j]))
        if j == n - 1:
            break
        w -= alpha[j] * V[:, j]
        if j > 0:
            w -= beta[j - 1] * V[:, j - 1]
        beta.append(np.linalg.norm(w))
        V[:, j + 1] = w / beta[j]
    return alpha, beta
