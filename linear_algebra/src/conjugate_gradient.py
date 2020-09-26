import numpy as np


def _is_matrix_spd(A: np.array) -> bool:

    """
    Returns True if input matrix A is symmetric positive definite.
    Returns False otherwise.

    For a matrix to be SPD, all eigenvalues must be positive.

    >>> import numpy as np
    >>> A = np.array([
    ... [4.12401784, -5.01453636, -0.63865857],
    ... [-5.01453636, 12.33347422, -3.40493586],
    ... [-0.63865857, -3.40493586,  5.78591885]])
    >>> _is_matrix_spd(A)
    True
    >>> A = np.array([
    ... [0.34634879,  1.96165514,  2.18277744],
    ... [0.74074469, -1.19648894, -1.34223498],
    ... [-0.7687067 ,  0.06018373, -1.16315631]])
    >>> _is_matrix_spd(A)
    False
    """
    # Ensure matrix is square.
    assert np.shape(A)[0] == np.shape(A)[1]

    # Get eigenvalues and eignevectors for a symmetric matrix.
    eigen_values, _ = np.linalg.eigh(A)

    # Check sign of all eigenvalues.
    if np.all(eigen_values > 0):
        return True
    else:
        return False


def _create_spd_matrix(N: np.int64) -> np.array:
    """
    Returns a symmetric positive definite matrix given a dimension.

    Input:
    N is an integer.

    Output:
    A is an NxN symmetric positive definite (SPD) matrix.

    >>> import numpy as np
    >>> N = 3
    >>> A = _create_spd_matrix(N)
    >>> _is_matrix_spd(A)
    True
    """

    A = np.random.randn(N, N)
    A = np.dot(A, A.T)

    assert _is_matrix_spd(A) is True

    return A


def conjugate_gradient(
    A: np.array, b: np.array, max_iterations=1000, tol=1e-8
) -> np.array:
    """
    Returns solution to the linear system Ax = b.

    Input:
    A is an NxN Symmetric Positive Definite (SPD) matrix.
    b is an Nx1 vector.

    Output:
    x is an Nx1 vector.

    >>> import numpy as np
    >>> A = np.array([
    ... [8.73256573, -5.02034289, -2.68709226],
    ... [-5.02034289,  3.78188322,  0.91980451],
    ... [-2.68709226,  0.91980451,  1.94746467]])
    >>> b = np.array([
    ... [-5.80872761],
    ... [ 3.23807431],
    ... [ 1.95381422]])
    >>> conjugate_gradient(A,b)
    array([[-0.63114139],
           [-0.01561498],
           [ 0.13979294]])
    """
    # Ensure proper dimensionality.
    assert np.shape(A)[0] == np.shape(A)[1]
    assert np.shape(b)[0] == np.shape(A)[0]
    assert _is_matrix_spd(A)

    N = np.shape(b)[0]

    # Initialize solution guess, residual, search direction.
    x0 = np.zeros((N, 1))
    r0 = np.copy(b)
    p0 = np.copy(r0)

    # Set initial errors in solution guess and residual.
    error_residual = 1e9
    error_x_solution = 1e9
    error = 1e9

    # Set iteration counter to threshold number of iterations.
    iterations = 0

    while error > tol:

        # Save this value so we only calculate the matrix-vector product once.
        w = np.dot(A, p0)

        # The main algorithm.

        # Update search direction magnitude.
        alpha = np.dot(r0.T, r0) / np.dot(p0.T, w)
        # Update solution guess.
        x = x0 + alpha * p0
        # Calculate new residual.
        r = r0 - alpha * w
        # Calculate new Krylov subspace scale.
        beta = np.dot(r.T, r) / np.dot(r0.T, r0)
        # Calculate new A conjuage search direction.
        p = r + beta * p0

        # Calculate errors.
        error_residual = np.linalg.norm(r - r0)
        error_x_solution = np.linalg.norm(x - x0)
        error = np.maximum(error_residual, error_x_solution)

        # Update variables.
        x0 = np.copy(x)
        r0 = np.copy(r)
        p0 = np.copy(p)

        # Update number of iterations.
        iterations += 1

    return x


def test_conjugate_gradient() -> None:

    """
    >>> test_conjugate_gradient()  # self running tests
    """

    # Create linear system with SPD matrix and known solution x_true.
    N = 3
    A = _create_spd_matrix(N)
    x_true = np.random.randn(N, 1)
    b = np.dot(A, x_true)

    # Numpy solution.
    x_numpy = np.linalg.solve(A, b)

    # Our implementation.
    x_conjugate_gradient = conjugate_gradient(A, b)

    # Ensure both solutions are close to x_true (and therefore one another).
    assert np.linalg.norm(x_numpy - x_true) <= 1e-6
    assert np.linalg.norm(x_conjugate_gradient - x_true) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_conjugate_gradient()
