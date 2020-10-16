import numpy as np
from typing import Tuple


def rayleigh_quotient_iteration(
        input_matrix: np.array, vector: np.array, value: float,
        error_tol=1e-12, max_iterations=100) -> Tuple[float, np.array]:
    """
    https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration

    Rayleigh quotient iteration
    Find an approximate eigenvector and eigenvalue of the input matrix. Which
    eigenvalue, eigenvector pair is found depends on the vector and value
    input. Has very rapid convergence.

    >>> import numpy as np
    >>> input_matrix = np.array([
    ... [41,  4, 20],
    ... [ 4, 26, 30],
    ... [20, 30, 50]
    ... ])
    >>> vector = np.array([1, 1, 1])
    >>> value = 30
    >>> rayleigh_quotient_iteration(input_matrix, vector, value)
    (33.60344292195729, array([-0.86306005,  0.45012643,  0.22915836]))
    >>> value = 1
    >>> rayleigh_quotient_iteration(input_matrix, vector, value)
    (3.735693290153355, array([-0.23946876, -0.7641015 ,  0.59900218]))
    """

    N = len(input_matrix)

    error = error_tol + 1
    prev_eigenvalue = value
    while error > error_tol:
        # Construct the iterating matrix
        A = np.linalg.inv(input_matrix - np.eye(N) * value)
        # Construct new eigenvector
        vector = np.dot(A, vector)
        # Normalize new eigenvector
        vector = vector / np.linalg.norm(vector)

        # Construct better approximation for eigenvalue
        value = np.dot(np.conj(vector).T,
                       np.dot(input_matrix, vector))

        error = abs(value - prev_eigenvalue)
        prev_eigenvalue = value

    return value, vector
