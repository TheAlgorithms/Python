import numpy as np
from typing import Tuple, Union
import numpy.typing as npt


def power_iteration(
    input_matrix: npt.NDArray[Union[np.float64, np.complex128]],
    vector: npt.NDArray[Union[np.float64, np.complex128]],
    error_tol: float = 1e-12,
    max_iterations: int = 100,
) -> Tuple[float, npt.NDArray[Union[np.float64, np.complex128]]]:
    """
    Power Iteration.
    Find the largest eigenvalue and corresponding eigenvector
    of matrix input_matrix given a random vector in the same space.
    Works as long as vector has a component of the largest eigenvector.
    input_matrix must be either real or Hermitian.

    Input:
    input_matrix: Input matrix whose largest eigenvalue we will find.
    A square numpy array. Shape: (N, N).
    vector: Random initial vector in the same space as the matrix.
    Numpy array. Shape: (N,) or (N,1).

    Output:
    largest_eigenvalue: Largest eigenvalue of the matrix.
    largest_eigenvector: Eigenvector corresponding to largest eigenvalue.

    Example:
    >>> import numpy as np
    >>> input_matrix = np.array([
    ... [41, 4, 20],
    ... [4, 26, 30],
    ... [20, 30, 50]
    ... ])
    >>> vector = np.array([41, 4, 20])
    >>> power_iteration(input_matrix, vector)
    (79.66086378788381, array([0.44472726, 0.46209842, 0.76725662]))
    """
    # Ensure matrix is square.
    N, M = np.shape(input_matrix)
    assert N == M, "Input matrix must be square."
    # Ensure proper dimensionality.
    assert N == np.shape(vector)[0], "Vector must be compatible with matrix dimensions."
    # Ensure inputs are either both complex or both real
    assert np.iscomplexobj(input_matrix) == np.iscomplexobj(
        vector
    ), "Both inputs must be either real or complex."

    is_complex = np.iscomplexobj(input_matrix)
    if is_complex:
        # Ensure complex input_matrix is Hermitian (A == A*)
        assert np.array_equal(
            input_matrix, input_matrix.conj().T
        ), "Input matrix must be Hermitian if complex."

    convergence = False
    lambda_previous = 0.0
    iterations = 0
    error = float("inf")

    while not convergence:
        # Multiply matrix by the vector.
        w = np.dot(input_matrix, vector)
        # Normalize the resulting output vector.
        vector = w / np.linalg.norm(w)
        # Find the Rayleigh quotient (faster since we know vector is normalized).
        vector_h = vector.conj().T if is_complex else vector.T
        lambda_ = np.dot(vector_h, np.dot(input_matrix, vector))

        # Check convergence.
        error = np.abs(lambda_ - lambda_previous) / np.abs(lambda_)
        iterations += 1

        if error <= error_tol or iterations >= max_iterations:
            convergence = True

        lambda_previous = lambda_

    # Ensure lambda_ is real if the matrix is complex.
    if is_complex:
        lambda_ = np.real(lambda_)

    return float(lambda_), vector


def test_power_iteration() -> None:
    """
    Test function for power_iteration.
    Runs tests on real and complex matrices using the power_iteration function.
    """
    real_input_matrix = np.array([[41, 4, 20], [4, 26, 30], [20, 30, 50]])
    real_vector = np.array([41, 4, 20])
    complex_input_matrix = real_input_matrix.astype(np.complex128)
    imag_matrix = np.triu(1j * complex_input_matrix, 1)
    complex_input_matrix += imag_matrix
    complex_input_matrix += -1 * imag_matrix.T
    complex_vector = np.array([41, 4, 20]).astype(np.complex128)

    for problem_type in ["real", "complex"]:
        if problem_type == "real":
            input_matrix = real_input_matrix
            vector = real_vector
        elif problem_type == "complex":
            input_matrix = complex_input_matrix
            vector = complex_vector

        # Our implementation.
        eigen_value, eigen_vector = power_iteration(input_matrix, vector)

        # Numpy implementation.
        eigen_values, eigen_vectors = np.linalg.eigh(input_matrix)
        eigen_value_max = eigen_values[-1]
        eigen_vector_max = eigen_vectors[:, -1]

        # Check that our implementation and numpy's give close answers.
        assert np.abs(eigen_value - eigen_value_max) <= 1e-6
        assert np.linalg.norm(np.abs(eigen_vector) - np.abs(eigen_vector_max)) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_power_iteration()
