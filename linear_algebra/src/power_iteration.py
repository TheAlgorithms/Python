import numpy as np


def power_iteration(
    input_matrix: np.ndarray,
    vector: np.ndarray,
    error_tol: float = 1e-12,
    max_iterations: int = 100,
) -> tuple[float, np.ndarray]:
    """
    Power Iteration.
    Find the largest eigenvalue and corresponding eigenvector
    of matrix input_matrix given a random vector in the same space.
    Will work so long as vector has component of largest eigenvector.
    input_matrix must be either real or Hermitian.

    Input
    input_matrix: input matrix whose largest eigenvalue we will find.
    Numpy array. np.shape(input_matrix) == (N,N).
    vector: random initial vector in same space as matrix.
    Numpy array. np.shape(vector) == (N,) or (N,1)

    Output
    largest_eigenvalue: largest eigenvalue of the matrix input_matrix.
    Float. Scalar.
    largest_eigenvector: eigenvector corresponding to largest_eigenvalue.
    Numpy array. np.shape(largest_eigenvector) == (N,) or (N,1).

    >>> import numpy as np
    >>> input_matrix = np.array([
    ... [41,  4, 20],
    ... [ 4, 26, 30],
    ... [20, 30, 50]
    ... ])
    >>> vector = np.array([41,4,20])
    >>> power_iteration(input_matrix,vector)
    (79.66086378788381, array([0.44472726, 0.46209842, 0.76725662]))
    """

    # Ensure matrix is square.
    assert np.shape(input_matrix)[0] == np.shape(input_matrix)[1]
    # Ensure proper dimensionality.
    assert np.shape(input_matrix)[0] == np.shape(vector)[0]
    # Ensure inputs are either both complex or both real
    assert np.iscomplexobj(input_matrix) == np.iscomplexobj(vector)
    is_complex = np.iscomplexobj(input_matrix)
    if is_complex:
        # Ensure complex input_matrix is Hermitian
        assert np.array_equal(input_matrix, input_matrix.conj().T)

    # Set convergence to False. Will define convergence when we exceed max_iterations
    # or when we have small changes from one iteration to next.

    convergence = False
    lambda_previous = 0
    iterations = 0
    error = 1e12

    while not convergence:
        # Multiple matrix by the vector.
        w = np.dot(input_matrix, vector)
        # Normalize the resulting output vector.
        vector = w / np.linalg.norm(w)
        # Find rayleigh quotient
        # (faster than usual b/c we know vector is normalized already)
        vector_h = vector.conj().T if is_complex else vector.T
        lambda_ = np.dot(vector_h, np.dot(input_matrix, vector))

        # Check convergence.
        error = np.abs(lambda_ - lambda_previous) / lambda_
        iterations += 1

        if error <= error_tol or iterations >= max_iterations:
            convergence = True

        lambda_previous = lambda_

    if is_complex:
        lambda_ = np.real(lambda_)

    return float(lambda_), vector


def test_power_iteration() -> None:
    """
    >>> test_power_iteration()  # self running tests
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

        # Get eigenvalues and eigenvectors using built-in numpy
        # eigh (eigh used for symmetric or hermetian matrices).
        eigen_values, eigen_vectors = np.linalg.eigh(input_matrix)
        # Last eigenvalue is the maximum one.
        eigen_value_max = eigen_values[-1]
        # Last column in this matrix is eigenvector corresponding to largest eigenvalue.
        eigen_vector_max = eigen_vectors[:, -1]

        # Check our implementation and numpy gives close answers.
        assert np.abs(eigen_value - eigen_value_max) <= 1e-6
        # Take absolute values element wise of each eigenvector.
        # as they are only unique to a minus sign.
        assert np.linalg.norm(np.abs(eigen_vector) - np.abs(eigen_vector_max)) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_power_iteration()
