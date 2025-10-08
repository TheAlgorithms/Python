#  Copyright (c) 2023 Diego Gasco (diego.gasco99@gmail.com), Diegomangasco on GitHub

"""
Requirements:
  - numpy version 1.21
  - scipy version 1.3.3
Notes:
  - Each column of the features matrix corresponds to a class item
"""

import logging

import numpy as np
import pytest
from scipy.linalg import eigh

logging.basicConfig(level=logging.INFO, format="%(message)s")


def column_reshape(input_array: np.ndarray) -> np.ndarray:
    """Function to reshape a row Numpy array into a column Numpy array
    >>> input_array = np.array([1, 2, 3])
    >>> column_reshape(input_array)
    array([[1],
           [2],
           [3]])
    """

    return input_array.reshape((input_array.size, 1))


def covariance_within_classes(
    features: np.ndarray, labels: np.ndarray, classes: int
) -> np.ndarray:
    """Function to compute the covariance matrix inside each class.
    >>> features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> labels = np.array([0, 1, 0])
    >>> covariance_within_classes(features, labels, 2)
    array([[0.66666667, 0.66666667, 0.66666667],
           [0.66666667, 0.66666667, 0.66666667],
           [0.66666667, 0.66666667, 0.66666667]])
    """

    covariance_sum = np.nan
    for i in range(classes):
        data = features[:, labels == i]
        data_mean = data.mean(1)
        # Centralize the data of class i
        centered_data = data - column_reshape(data_mean)
        if i > 0:
            # If covariance_sum is not None
            covariance_sum += np.dot(centered_data, centered_data.T)
        else:
            # If covariance_sum is np.nan (i.e. first loop)
            covariance_sum = np.dot(centered_data, centered_data.T)

    return covariance_sum / features.shape[1]


def covariance_between_classes(
    features: np.ndarray, labels: np.ndarray, classes: int
) -> np.ndarray:
    """Function to compute the covariance matrix between multiple classes
    >>> features = np.array([[9, 2, 3], [4, 3, 6], [1, 8, 9]])
    >>> labels = np.array([0, 1, 0])
    >>> covariance_between_classes(features, labels, 2)
    array([[ 3.55555556,  1.77777778, -2.66666667],
           [ 1.77777778,  0.88888889, -1.33333333],
           [-2.66666667, -1.33333333,  2.        ]])
    """

    general_data_mean = features.mean(1)
    covariance_sum = np.nan
    for i in range(classes):
        data = features[:, labels == i]
        device_data = data.shape[1]
        data_mean = data.mean(1)
        if i > 0:
            # If covariance_sum is not None
            covariance_sum += device_data * np.dot(
                column_reshape(data_mean) - column_reshape(general_data_mean),
                (column_reshape(data_mean) - column_reshape(general_data_mean)).T,
            )
        else:
            # If covariance_sum is np.nan (i.e. first loop)
            covariance_sum = device_data * np.dot(
                column_reshape(data_mean) - column_reshape(general_data_mean),
                (column_reshape(data_mean) - column_reshape(general_data_mean)).T,
            )

    return covariance_sum / features.shape[1]


def principal_component_analysis(features: np.ndarray, dimensions: int) -> np.ndarray:
    """
    Principal Component Analysis.

    For more details, see: https://en.wikipedia.org/wiki/Principal_component_analysis.
    Parameters:
        * features: the features extracted from the dataset
        * dimensions: to filter the projected data for the desired dimension

    >>> test_principal_component_analysis()
    """

    # Check if the features have been loaded
    if features.any():
        data_mean = features.mean(1)
        # Center the dataset
        centered_data = features - np.reshape(data_mean, (data_mean.size, 1))
        covariance_matrix = np.dot(centered_data, centered_data.T) / features.shape[1]
        _, eigenvectors = np.linalg.eigh(covariance_matrix)
        # Take all the columns in the reverse order (-1), and then takes only the first
        filtered_eigenvectors = eigenvectors[:, ::-1][:, 0:dimensions]
        # Project the database on the new space
        projected_data = np.dot(filtered_eigenvectors.T, features)
        logging.info("Principal Component Analysis computed")

        return projected_data
    else:
        logging.basicConfig(level=logging.ERROR, format="%(message)s", force=True)
        logging.error("Dataset empty")
        raise AssertionError


def linear_discriminant_analysis(
    features: np.ndarray, labels: np.ndarray, classes: int, dimensions: int
) -> np.ndarray:
    """
    Linear Discriminant Analysis.

    For more details, see: https://en.wikipedia.org/wiki/Linear_discriminant_analysis.
    Parameters:
        * features: the features extracted from the dataset
        * labels: the class labels of the features
        * classes: the number of classes present in the dataset
        * dimensions: to filter the projected data for the desired dimension

    >>> test_linear_discriminant_analysis()
    """

    # Check if the dimension desired is less than the number of classes
    assert classes > dimensions

    # Check if features have been already loaded
    if features.any:
        _, eigenvectors = eigh(
            covariance_between_classes(features, labels, classes),
            covariance_within_classes(features, labels, classes),
        )
        filtered_eigenvectors = eigenvectors[:, ::-1][:, :dimensions]
        svd_matrix, _, _ = np.linalg.svd(filtered_eigenvectors)
        filtered_svd_matrix = svd_matrix[:, 0:dimensions]
        projected_data = np.dot(filtered_svd_matrix.T, features)
        logging.info("Linear Discriminant Analysis computed")

        return projected_data
    else:
        logging.basicConfig(level=logging.ERROR, format="%(message)s", force=True)
        logging.error("Dataset empty")
        raise AssertionError


def t_distributed_stochastic_neighbor_embedding(
    features: np.ndarray,
    dimensions: int = 2,
    perplexity: float = 30.0,
    learning_rate: float = 200.0,
    max_iterations: int = 1000,
    random_state: int = 42,
) -> np.ndarray:
    """
    t-Distributed Stochastic Neighbor Embedding (t-SNE) algorithm for
    dimensionality reduction.

    t-SNE is a machine learning algorithm for visualization developed by
    Laurens van der Maaten and Geoffrey Hinton. It is a nonlinear
    dimensionality reduction technique particularly well suited for the
    visualization of high-dimensional datasets.

    For more details, see:
    https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding
    Original paper:
    https://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf

    Parameters:
        * features: Input data matrix where each column represents a data point
        * dimensions: Number of dimensions for the output (typically 2 or 3)
        * perplexity: Controls the effective number of neighbors (typically 5-50)
        * learning_rate: Learning rate for gradient descent
        * max_iterations: Maximum number of optimization iterations
        * random_state: Random seed for reproducible results

    Returns:
        * projected_data: Low-dimensional representation of the input data

    >>> # Test with simple 3D to 2D reduction
    >>> features = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=float).T
    >>> result = t_distributed_stochastic_neighbor_embedding(
    ...     features, dimensions=2, max_iterations=10
    ... )
    >>> result.shape
    (2, 4)

    >>> # Test with invalid dimensions
    >>> try:
    ...     t_distributed_stochastic_neighbor_embedding(features, dimensions=0)
    ... except ValueError as e:
    ...     print("ValueError raised for invalid dimensions")
    ValueError raised for invalid dimensions
    """

    if not isinstance(features, np.ndarray) or features.size == 0:
        raise ValueError("Features must be a non-empty numpy array")

    if dimensions <= 0:
        raise ValueError("Dimensions must be a positive integer")

    if perplexity <= 0:
        raise ValueError("Perplexity must be positive")

    if learning_rate <= 0:
        raise ValueError("Learning rate must be positive")

    if max_iterations <= 0:
        raise ValueError("Max iterations must be positive")

    rng = np.random.default_rng(random_state)
    _, num_samples = features.shape

    if num_samples < dimensions + 1:
        min_samples = dimensions + 1
        msg = (
            f"Need at least {min_samples} samples for t-SNE with {dimensions} "
            f"dimensions, but got {num_samples} samples"
        )
        raise ValueError(msg)

    # Compute pairwise squared Euclidean distances
    def compute_pairwise_distances(data: np.ndarray) -> np.ndarray:
        """Compute pairwise squared Euclidean distances."""
        sum_data = np.sum(np.square(data), axis=0)
        distances = sum_data + sum_data[:, np.newaxis] - 2 * np.dot(data.T, data)
        return np.maximum(distances, 0)  # Ensure non-negative

    # Compute perplexity-based probabilities using binary search
    def compute_conditional_probabilities(
        distances: np.ndarray, target_perplexity: float
    ) -> np.ndarray:
        """Compute conditional probabilities with target perplexity."""
        num_points = distances.shape[0]
        probabilities = np.zeros((num_points, num_points))

        for i in range(num_points):
            # Binary search for optimal sigma
            beta_min, beta_max = -np.inf, np.inf
            beta = 1.0

            for _ in range(50):  # Max iterations for binary search
                # Compute probabilities
                exp_distances = np.exp(-distances[i] * beta)
                exp_distances[i] = 0  # Set self-similarity to 0
                sum_exp = np.sum(exp_distances)

                if sum_exp == 0:
                    probabilities[i] = 0
                    break

                current_probabilities = exp_distances / sum_exp

                # Compute perplexity
                entropy = -np.sum(
                    current_probabilities * np.log2(current_probabilities + 1e-12)
                )
                current_perplexity = 2**entropy

                # Check if we're close enough
                if abs(current_perplexity - target_perplexity) < 1e-5:
                    probabilities[i] = current_probabilities
                    break

                # Adjust beta
                if current_perplexity > target_perplexity:
                    beta_min = beta
                    beta = beta * 2 if beta_max == np.inf else (beta + beta_max) / 2
                else:
                    beta_max = beta
                    beta = beta / 2 if beta_min == -np.inf else (beta + beta_min) / 2
            else:
                probabilities[i] = current_probabilities

        return probabilities

    # Compute high-dimensional probabilities
    distances = compute_pairwise_distances(features)
    conditional_probs = compute_conditional_probabilities(distances, perplexity)

    # Symmetrize probabilities
    high_dim_probs = (conditional_probs + conditional_probs.T) / (2 * num_samples)
    high_dim_probs = np.maximum(high_dim_probs, 1e-12)

    # Initialize low-dimensional embedding
    projected_data = rng.normal(0, 1e-4, (dimensions, num_samples))

    # Gradient descent optimization
    momentum = np.zeros_like(projected_data)

    for _ in range(max_iterations):
        # Compute low-dimensional probabilities (Student-t distribution)
        low_dim_distances = compute_pairwise_distances(projected_data)
        low_dim_probs_denom = 1 + low_dim_distances
        low_dim_probs_denom[np.diag_indices_from(low_dim_probs_denom)] = np.inf

        low_dim_probs = 1 / low_dim_probs_denom
        np.fill_diagonal(low_dim_probs, 0)
        sum_low_dim = np.sum(low_dim_probs)

        if sum_low_dim == 0:
            low_dim_probs = np.ones_like(low_dim_probs) / (
                num_samples * (num_samples - 1)
            )
        else:
            low_dim_probs = low_dim_probs / sum_low_dim

        low_dim_probs = np.maximum(low_dim_probs, 1e-12)

        # Compute gradient
        prob_diff = high_dim_probs - low_dim_probs
        gradient = np.zeros_like(projected_data)

        for i in range(num_samples):
            diff = projected_data[:, i : i + 1] - projected_data
            gradient[:, i] = np.sum(
                (prob_diff[i] * (1 / low_dim_probs_denom[i])).reshape(1, -1) * diff,
                axis=1,
            )

        gradient *= 4  # Factor from t-SNE gradient derivation

        # Update with momentum
        momentum = 0.5 * momentum - learning_rate * gradient
        projected_data += momentum

    logging.info("t-SNE computation completed")
    return projected_data


def test_linear_discriminant_analysis() -> None:
    # Create dummy dataset with 2 classes and 3 features
    features = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]])
    labels = np.array([0, 0, 0, 1, 1])
    classes = 2
    dimensions = 2

    # Assert that the function raises an AssertionError if dimensions > classes
    with pytest.raises(AssertionError) as error_info:  # noqa: PT012
        projected_data = linear_discriminant_analysis(
            features, labels, classes, dimensions
        )
        if isinstance(projected_data, np.ndarray):
            raise AssertionError(
                "Did not raise AssertionError for dimensions > classes"
            )
        assert error_info.type is AssertionError


def test_principal_component_analysis() -> None:
    features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    dimensions = 2
    expected_output = np.array([[6.92820323, 8.66025404, 10.39230485], [3.0, 3.0, 3.0]])

    with pytest.raises(AssertionError) as error_info:  # noqa: PT012
        output = principal_component_analysis(features, dimensions)
        if not np.allclose(expected_output, output):
            raise AssertionError
        assert error_info.type is AssertionError


def test_t_distributed_stochastic_neighbor_embedding() -> None:
    """Test t-SNE algorithm with various input conditions."""
    # Test with valid input
    features = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=float)
    dimensions = 2
    max_iterations = 10
    result = t_distributed_stochastic_neighbor_embedding(
        features, dimensions=dimensions, max_iterations=max_iterations
    )

    # Check the shape of the result
    assert result.shape == (2, 4), f"Expected shape (2, 4), got {result.shape}"

    # Test with empty array
    try:
        empty_features = np.array([])
        t_distributed_stochastic_neighbor_embedding(empty_features)
        raise AssertionError("Should raise ValueError for empty array")
    except ValueError:
        pass

    # Test with invalid dimensions
    try:
        t_distributed_stochastic_neighbor_embedding(features, dimensions=0)
        raise AssertionError("Should raise ValueError for invalid dimensions")
    except ValueError:
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
