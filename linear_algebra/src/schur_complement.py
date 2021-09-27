import numpy as np


def schur_complement(
    a: np.ndarray, b: np.ndarray, c: np.ndarray, pseudo_inv: np.ndarray = None
) -> np.ndarray:
    """
    Schur complement of a symmetric matrix X given as a 2x2 block matrix
    consisting of matrices A, B and C.
    Matrix A must be quadratic and non-singular.
    In case A is singular, a pseudo-inverse may be provided using
    the pseudo_inv argument.

    Link to Wiki: https://en.wikipedia.org/wiki/Schur_complement
    See also Convex Optimization – Boyd and Vandenberghe, A.5.5
    >>> import numpy as np
    >>> a = np.array([[1, 2], [2, 1]])
    >>> b = np.array([[0, 3], [3, 0]])
    >>> c = np.array([[2, 1], [6, 3]])
    >>> schur_complement(a, b, c)
    array([[ 5., -5.],
           [ 0.,  6.]])
    """
    shape_a = np.shape(a)
    shape_b = np.shape(b)
    shape_c = np.shape(c)

    if shape_a[0] != shape_b[0]:
        raise ValueError(
            f"Expected the same number of rows for A and B. \
            Instead found A of size {shape_a} and B of size {shape_b}"
        )

    if shape_b[1] != shape_c[1]:
        raise ValueError(
            f"Expected the same number of columns for B and C. \
            Instead found B of size {shape_b} and C of size {shape_c}"
        )

    a_inv = pseudo_inv
    if a_inv is None:
        try:
            a_inv = np.linalg.inv(a)
        except np.linalg.LinAlgError:
            raise ValueError(
                "Input matrix A is not invertible. Cannot compute Schur complement."
            )

    return c - b.T @ a_inv @ b


def test_schur_complement():
    """
    >>> test_schur_complement()  # self running tests
    """
    a = np.array([[1, 2, 1], [2, 1, 2], [3, 2, 4]])
    b = np.array([[0, 3], [3, 0], [2, 3]])
    c = np.array([[2, 1], [6, 3]])

    s = schur_complement(a, b, c)

    input_matrix = np.block([[a, b], [b.T, c]])

    det_x = np.linalg.det(input_matrix)
    det_a = np.linalg.det(a)
    det_s = np.linalg.det(s)

    assert np.abs(det_x - det_a * det_s) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_schur_complement()
