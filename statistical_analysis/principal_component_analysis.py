import numpy as np


def centering_matrix(n: int):
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


def principal_comoponent_analysis(X, n_components: int):
    """
    Input
    X  -  is (n, p) array-like where n is the number of observations
          and p is the number of differnt variables.
    n_components  -  is the number of principal components to be 
                     included

    Returns
    Data matrix of size (n, n_components), array like 


    https://en.wikipedia.org/wiki/Principal_component_analysis
    """
    n = len(X)
    centering = centering_matrix(n)

    if n_components > min(X.shape):
        raise ValueError(
            "Number of components cannot be more than"
            " the number of observations or variables"
        )

    covariance_matrix = X.transpose() @ centering @ X / (n - 1)

    eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
    # Eigen Values are not necessarily in decreasing order, so need
    # to reorder them

    order = np.argsort(eigen_values)[::-1]
    # eigen_values = eigen_values[order]
    eigen_vectors = eigen_vectors[:, order]

    return centering @ X @ eigen_vectors[:, :n_components]


if __name__ == "__main__":
    X = np.array([[1, 0], [2, 1], [3, 2], [4, 3]])
    print(principal_comoponent_analysis(X, 1))
