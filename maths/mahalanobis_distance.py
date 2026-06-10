from __future__ import annotations

import numpy as np


def mahalanobis_distance(
    point: np.ndarray,
    mean: np.ndarray,
    covariance: np.ndarray,
) -> float:
    """
    Compute the Mahalanobis distance between a point and a distribution.

    The Mahalanobis distance measures how many standard deviations away
    a point is from the mean of a distribution, taking into account the
    correlations between variables. It is defined as:

    D_M(x) = sqrt((x - μ)^T * Σ^(-1) * (x - μ))

    where x is the point, μ is the mean vector, and Σ is the covariance matrix.

    https://en.wikipedia.org/wiki/Mahalanobis_distance

    Parameters
    ----------
    point : np.ndarray
        The observation point (1D array).
    mean : np.ndarray
        The mean vector of the distribution (1D array).
    covariance : np.ndarray
        The covariance matrix of the distribution (2D array).

    Returns
    -------
    float
        The Mahalanobis distance.

    Raises
    ------
    ValueError
        If the point and mean have different dimensions.
        If the covariance matrix is not square.
        If the covariance matrix dimension does not match the point dimension.
        If the covariance matrix is singular (not invertible).

    Examples
    --------
    >>> import numpy as np
    >>> point = np.array([1, 1])
    >>> mean = np.array([0, 0])
    >>> cov = np.array([[1, 0], [0, 1]])
    >>> round(mahalanobis_distance(point, mean, cov), 6)
    1.414214

    >>> round(mahalanobis_distance(np.array([0, 0]), np.array([0, 0]), cov), 6)
    0.0

    >>> cov_correlated = np.array([[2, 0.5], [0.5, 1]])
    >>> d = mahalanobis_distance(np.array([2, 2]), np.array([0, 0]), cov_correlated)
    >>> round(d, 6)
    2.13809

    >>> mahalanobis_distance(np.array([1, 2]), np.array([0, 0]), np.eye(2))
    2.23606797749979

    # 1D case — same as z-score normalized by standard deviation
    >>> round(mahalanobis_distance(np.array([3]), np.array([0]), np.eye(1)), 6)
    3.0

    # Error: dimension mismatch between point and mean
    >>> mahalanobis_distance(np.array([1, 2]), np.array([0]), np.eye(2))
    Traceback (most recent call last):
        ...
    ValueError: Point and mean must have the same dimension.

    # Error: non-square covariance matrix
    >>> mahalanobis_distance(np.array([1, 2]), np.array([0, 0]), np.array([[1, 0]]))
    Traceback (most recent call last):
        ...
    ValueError: Covariance matrix must be square.

    # Error: dimension mismatch between covariance and point
    >>> mahalanobis_distance(np.array([1, 2]), np.array([0, 0]), np.eye(3))
    Traceback (most recent call last):
        ...
    ValueError: Covariance matrix dimension must match the point dimension.

    # Error: singular covariance matrix
    >>> mahalanobis_distance(
    ...     np.array([1, 1]), np.array([0, 0]), np.array([[1, 1], [1, 1]])
    ... )
    Traceback (most recent call last):
        ...
    ValueError: Covariance matrix is singular; cannot compute its inverse.
    """
    if point.shape != mean.shape:
        raise ValueError("Point and mean must have the same dimension.")

    if covariance.ndim != 2 or covariance.shape[0] != covariance.shape[1]:
        raise ValueError("Covariance matrix must be square.")

    n = covariance.shape[0]
    if point.shape[0] != n:
        raise ValueError("Covariance matrix dimension must match the point dimension.")

    try:
        inv_covariance = np.linalg.inv(covariance)
    except np.linalg.LinAlgError as e:
        raise ValueError(
            "Covariance matrix is singular; cannot compute its inverse."
        ) from e

    diff = point - mean
    return float(np.sqrt(diff @ inv_covariance @ diff))


def mahalanobis_distance_from_sample(
    point: np.ndarray,
    sample: np.ndarray,
) -> float:
    """
    Compute the Mahalanobis distance from a point to a sample distribution.

    The sample covariance matrix is used to estimate the population
    covariance. Uses np.cov which computes the unbiased covariance
    (divides by n-1).

    https://en.wikipedia.org/wiki/Mahalanobis_distance

    Parameters
    ----------
    point : np.ndarray
        The observation point (1D array).
    sample : np.ndarray
        The sample data as a 2D array where each row is an observation
        and each column is a variable.

    Returns
    -------
    float
        The Mahalanobis distance.

    Raises
    ------
    ValueError
        If the point dimension does not match the number of sample columns.
        If the sample has fewer than 2 rows (need at least 2 for covariance).
        If the sample covariance matrix is singular.

    Examples
    --------
    >>> import numpy as np
    >>> sample = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
    >>> d = mahalanobis_distance_from_sample(np.array([2, 2]), sample)
    >>> round(d, 6)
    3.674235

    >>> d = mahalanobis_distance_from_sample(np.array([0, 0]), sample)
    >>> round(d, 6)
    1.224745

    >>> mahalanobis_distance_from_sample(np.array([1, 2, 3]), sample)
    Traceback (most recent call last):
        ...
    ValueError: Point dimension (3) must match the number of sample columns (2).

    >>> mahalanobis_distance_from_sample(np.array([1, 2]), np.array([[1, 2]]))
    Traceback (most recent call last):
        ...
    ValueError: Sample must have at least 2 observations to compute covariance.
    """
    if sample.ndim != 2:
        sample = sample.reshape(-1, 1)

    n_rows, n_cols = sample.shape
    if point.shape[0] != n_cols:
        msg = (
            f"Point dimension ({point.shape[0]}) must match the number of "
            f"sample columns ({n_cols})."
        )
        raise ValueError(msg)

    if n_rows < 2:
        raise ValueError(
            "Sample must have at least 2 observations to compute covariance."
        )

    mean = np.mean(sample, axis=0)
    covariance = np.cov(sample, rowvar=False)

    return mahalanobis_distance(point, mean, covariance)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
