import numpy as np


def invert_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """
    Returns the inverse of a square matrix using NumPy.

    Parameters:
    matrix (list[list[float]]): A square matrix.

    Returns:
    list[list[float]]: Inverted matrix if invertible, else raises error.

    The exact floating-point representation returned by ``numpy.linalg.inv``
    can vary slightly across platforms and BLAS/LAPACK backends
    (e.g. ``0.6`` vs ``0.6000000000000001``), so the doctests below round the
    result to make the expected output deterministic.

    >>> [[round(x, 6) for x in row] for row in invert_matrix([[4.0, 7.0], [2.0, 6.0]])]
    [[0.6, -0.7], [-0.2, 0.4]]
    >>> [[round(x, 6) for x in row] for row in invert_matrix([[1.0, 0.0], [0.0, 2.0]])]
    [[1.0, 0.0], [0.0, 0.5]]
    >>> invert_matrix([[1.0, 2.0], [0.0, 0.0]])
    Traceback (most recent call last):
        ...
    ValueError: Matrix is not invertible
    """
    np_matrix = np.array(matrix)

    try:
        inv_matrix = np.linalg.inv(np_matrix)
    except np.linalg.LinAlgError:
        raise ValueError("Matrix is not invertible")

    return inv_matrix.tolist()


if __name__ == "__main__":
    mat = [[4.0, 7.0], [2.0, 6.0]]
    print("Original Matrix:")
    print(mat)
    print("Inverted Matrix:")
    print(invert_matrix(mat))
