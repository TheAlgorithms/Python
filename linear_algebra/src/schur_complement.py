import numpy as np


def schur_complement(
    A: np.ndarray, B: np.ndarray, C: np.ndarray, pseudo_inv: np.ndarray = None
) -> np.ndarray:
    """
    Schur complement of a symmetric matrix X given as a 2x2 block matrix
    consisting of matrices A, B and C.
    Matrix A must be quadratic and non-singular.
    In case A is singular, a pseudo-inverse may be provided using
    the pseudo_inv argument.
    >>> import numpy as np
    >>> A = np.array([[1, 2], [2, 1]])
    >>> B = np.array([[0, 3], [3, 0]])
    >>> C = np.array([[2, 1], [6, 3]])
    >>> schur_complement(A, B, C)
    array([[ 5., -5.],
           [ 0.,  6.]])
    """
    shape_A = np.shape(A)
    shape_B = np.shape(B)
    shape_C = np.shape(C)

    if shape_A[0] != shape_B[0]:
        raise ValueError(
            f"Expected the same number of rows for A and B. \
            Instead found A of size {shape_A} and B of size {shape_B}"
        )

    if shape_B[1] != shape_C[1]:
        raise ValueError(
            f"Expected the same number of columns for B and C. \
            Instead found B of size {shape_B} and C of size {shape_C}"
        )

    A_inv = pseudo_inv
    if A_inv is None:
        try:
            A_inv = np.linalg.inv(A)
        except np.linalg.LinAlgError:
            raise ValueError(
                "Input matrix A is not invertible. Cannot compute Schur complement."
            )

    return C - B.T @ A_inv @ B


def test_schur_complement():
    """
    >>> test_schur_complement()  # self running tests
    """
    A = np.array([[1, 2, 1], [2, 1, 2], [3, 2, 4]])
    B = np.array([[0, 3], [3, 0], [2, 3]])
    C = np.array([[2, 1], [6, 3]])

    S = schur_complement(A, B, C)

    input_matrix = np.block([[A, B], [B.T, C]])

    det_X = np.linalg.det(input_matrix)
    det_A = np.linalg.det(A)
    det_S = np.linalg.det(S)

    assert np.abs(det_X - det_A * det_S) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_schur_complement()
