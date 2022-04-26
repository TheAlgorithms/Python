import numpy as np


def power_iteration(
    input_matrix: np.ndarray,
    vector: np.ndarray,
    error_tol: float = 1e-12,
    max_iterations: int = 100,
    ord: int = 2,
) -> tuple[float, np.ndarray]:
    """
    Power Iteration.
    Find the largest eignevalue and corresponding eigenvector
    of matrix input_matrix given a random vector in the same space.
    Will work so long as vector has component of largest eigenvector.
    input_matrix must be symmetric.
    Input
    input_matrix: input matrix whose largest eigenvalue we will find.
    Numpy array. np.shape(input_matrix) == (N,N).
    vector: random initial vector in same space as matrix.
    Numpy array. np.shape(vector) == (N,) or (N,1)
    ord: The order of the norm used in normalization. Optional.
    {non-zero int, np.inf, -1*np.inf, ‘fro’, ‘nuc’}
    See https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html
    for more details on the valid inputs of ord.
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
    (79.6608637878838, array([0.44472726, 0.46209842, 0.76725662]))
    """

    # Ensure matrix is square.
    assert np.shape(input_matrix)[0] == np.shape(input_matrix)[1]
    # Ensure proper dimensionality.
    assert np.shape(input_matrix)[0] == np.shape(vector)[0]

    # Set convergence to False. Will define convergence when we exceed max_iterations
    # or when we have small changes from one iteration to next.

    convergence = False
    lamda_previous = 0
    iterations = 0
    error = 1e12

    while not convergence:
        # Multiple matrix by the vector.
        w = np.dot(input_matrix, vector)
        # Normalize the resulting output vector.
        vector = w / np.linalg.norm(w, ord)
        # Find rayleigh quotient
        lamda = np.dot(vector.T, np.dot(input_matrix, vector)) / np.dot(
            vector.T, vector
        )

        # Check convergence.
        error = np.abs(lamda - lamda_previous) / lamda
        iterations += 1

        if error <= error_tol or iterations >= max_iterations:
            convergence = True
            # Nornmalize vector with 2 norm
            vector = vector / np.linalg.norm(vector)

        lamda_previous = lamda

    return lamda, vector


def test_power_iteration() -> None:
    """
    >>> test_power_iteration()  # self running tests
    """
    # Our implementation with norm 2 on a symmetric matrix
    input_matrix_symmetric = np.array([[41, 4, 20], [4, 26, 30], [20, 30, 50]])
    vector = np.array([41, 4, 20])
    eigen_value, eigen_vector = power_iteration(input_matrix_symmetric, vector)

    # Numpy implementation on a symmetric matrix.
    # Get eigen values and eigen vectors using built in numpy eigh
    eigen_values, eigen_vectors = np.linalg.eigh(input_matrix_symmetric)
    # Last eigen value is the maximum one.
    eigen_value_max = eigen_values[-1]
    # Last column in this matrix is eigen vector corresponding to largest eigen value.
    eigen_vector_max = eigen_vectors[:, -1]

    # Compare our implementation to numpy for eigen value.
    assert np.abs(eigen_value - eigen_value_max) <= 1e-6

    # Compare our implementation to numpy for eigen vector.
    # Take absolute values element wise of each eigenvector since they are only
    # unique to a minus sign.
    assert np.linalg.norm(np.abs(eigen_vector) - np.abs(eigen_vector_max)) <= 1e-6

    # Our implementation with norm inf on a nonsymmetric matrix.
    # It is standard to use the inf norm for nonsymmetric matrices and
    # the 2 norm for symmetric matrices.
    input_matrix_nonsymmetric = np.array([[41, 10, 17], [4, 26, 4], [39, 30, 50]])
    eigen_value, eigen_vector = power_iteration(
        input_matrix_nonsymmetric, vector, ord=np.inf
    )

    # Numpy implementation on a nonsymmetric matrix.
    # Get eigen values and eigen vectors using built in numpy eig
    eigen_values, eigen_vectors = np.linalg.eig(input_matrix_nonsymmetric)
    # Get the largest eigen value
    i = np.argmax(eigen_values)
    eigen_value_max = eigen_values[i]
    # Last column in this matrix is eigen vector corresponding to largest eigen value.
    eigen_vector_max = eigen_vectors[:, i]

    # Check our implementation and numpy for eigen value.
    assert np.abs(eigen_value - eigen_value_max) <= 1e-6

    # Check our implementation and numpy for eigen vector.
    assert np.linalg.norm(np.abs(eigen_vector) - np.abs(eigen_vector_max)) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_power_iteration()