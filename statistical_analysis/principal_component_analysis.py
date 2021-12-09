import numpy as np


def centering_matrix(n: int) -> np.ndarray:
    """
    Returns the centering matrix H = I - (1/n)J
    where I is the identity matrix and J is the matrix
    that has 1 in every entry.
    """
    identity = np.diag(
        np.ones(
            n,
        )
    )
    ones = np.ones((n, n))
    centering = identity - ones / n
    return centering


def principal_comoponent_analysis(
    data_matrix: np.ndarray, n_components: int
) -> np.ndarray:
    """
    Input
    data_matrix   - is (n, p) array-like where n is the number of observations
                    and p is the number of different variables.
    n_components  - is the number of principal components to be
                    included

    Returns
    Data matrix of size (n, n_components), array like


    https://en.wikipedia.org/wiki/Principal_component_analysis
    """
    n = len(data_matrix)
    centering = centering_matrix(n)

    if n_components > min(data_matrix.shape):
        raise ValueError(
            "Number of components cannot be more than"
            " the number of observations or variables"
        )

    covariance_matrix = data_matrix.transpose() @ centering @ data_matrix / (n - 1)

    eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
    # Eigen Values are not necessarily in decreasing order, so need
    # to reorder them

    order = np.argsort(eigen_values)[::-1]
    # eigen_values = eigen_values[order]
    eigen_vectors = eigen_vectors[:, order]

    return np.array(centering @ data_matrix @ eigen_vectors[:, :n_components])


if __name__ == "__main__":
    data_matrix = np.array([[1, 0], [2, 1], [3, 2], [4, 3]])
    print(principal_comoponent_analysis(data_matrix, 1))
