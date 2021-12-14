import numpy as np


def centering_matrix(n_dim: int) -> np.ndarray:
    """
    Returns the centering matrix H = I - (1/n)J
    where I is the identity matrix and J is the matrix
    that has 1 in every entry.

    >>> centering_matrix(2)
    array([[ 0.5, -0.5],
           [-0.5,  0.5]])
    >>> centering_matrix(1)
    array([[0.]])
    """

    identity = np.diag(np.ones(n_dim))
    ones = np.ones((n_dim, n_dim))
    centering = identity - ones / n_dim
    return centering


def principal_comoponent_analysis(
    data_matrix: np.ndarray, n_components: int = 2, n_digits: int = -1
) -> np.ndarray:
    """
    Input
    data_matrix   - is (n, p) array-like where n is the number of observations
                    and p is the number of different variables.
    n_components  - is the number of principal components to be
                    included
    n_digits      - Number of digits wanted after decimal
                    (negative values corresponds to no rounding)

    Returns
    Data matrix of size (n, n_components), array like

    >>> x = np.array([[1, 0], [2, 1], [3, 2], [4, 3]])
    >>> principal_comoponent_analysis(x, n_digits = 2)
    array([[-2.12,  0.  ],
           [-0.71,  0.  ],
           [ 0.71, -0.  ],
           [ 2.12, -0.  ]])

    https://en.wikipedia.org/wiki/Principal_component_analysis
    """
    n_obs = len(data_matrix)
    centering = centering_matrix(n_obs)

    if n_components > min(data_matrix.shape):
        raise ValueError(
            "Number of components cannot be more than"
            " the number of observations or variables"
        )

    covariance_matrix = data_matrix.transpose() @ centering @ data_matrix / (n_obs - 1)

    eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
    # Eigen Values are not necessarily in decreasing order, so need
    # to reorder them

    order = np.argsort(eigen_values)[::-1]
    eigen_vectors = eigen_vectors[:, order]

    result = np.array(centering @ data_matrix @ eigen_vectors[:, :n_components])

    if n_digits <= 0:
        return result
    return np.round(result, n_digits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    data_matrix = np.array([[1, 0], [2, 1], [3, 2], [4, 3]])
    result = principal_comoponent_analysis(data_matrix, 1, 2)

    print("The first Principal component of ")
    print(data_matrix)
    print("is")
    print(result)
