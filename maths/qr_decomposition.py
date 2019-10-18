import numpy as np


def qr_householder(A):
    """Return a QR-decomposition of the matrix A using Householder reflection.

    The QR-decomposition decomposes the matrix A of shape (m, n) into an
    orthogonal matrix Q of shape (m, m) and an upper triangular matrix R of
    shape (m, n).  Note that the matrix A does not have to be square.  This
    method of decomposing A uses the Householder reflection, which is
    numerically stable and of complexity O(n^3).

    https://en.wikipedia.org/wiki/QR_decomposition#Using_Householder_reflections

    Arguments:
    A -- a numpy.ndarray of shape (m, n)

    Note: several optimizations can be made for numeric efficiency, but this is
    intended to demonstrate how it would be represented in a mathematics
    textbook.  In cases where efficiency is particularly important, an optimized
    version from BLAS should be used.

    >>> A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=float)
    >>> Q, R = qr_householder(A)

    >>> # check that the decomposition is correct
    >>> np.allclose(Q@R, A)
    True

    >>> # check that Q is orthogonal
    >>> np.allclose(Q@Q.T, np.eye(A.shape[0]))
    True
    >>> np.allclose(Q.T@Q, np.eye(A.shape[0]))
    True

    >>> # check that R is upper triangular
    >>> np.allclose(np.triu(R), R)
    True
    """
    m, n = A.shape
    t = min(m, n)
    Q = np.eye(m)
    R = A.copy()

    for k in range(t - 1):
        # select a column of modified matrix A':
        x = R[k:, [k]]
        # construct first basis vector
        e1 = np.zeros_like(x)
        e1[0] = 1.0
        # determine scaling factor
        alpha = np.linalg.norm(x)
        # construct vector v for Householder reflection
        v = x + np.sign(x[0])*alpha*e1
        v /= np.linalg.norm(v)

        # construct the Householder matrix
        Q_k = np.eye(m - k) - 2.0*v@v.T
        # pad with ones and zeros as necessary
        Q_k = np.block([[np.eye(k),            np.zeros((k, m - k))],
                        [np.zeros((m - k, k)), Q_k                 ]])

        Q = Q@Q_k.T
        R = Q_k@R

    return Q, R


if __name__ == "__main__":
    import doctest
    doctest.testmod()
