#  Copyright (c) 2023 Diego Gasco (diego.gasco99@gmail.com), Diegomangasco on GitHub
# flake8: noqa: E402
"""
Requirements:
  - numpy version 1.21
  - scipy version 1.3.3
Notes:
  - Each column of the features matrix corresponds to a class item
"""

"""
Implementation of dimensionality reduction algorithms.

Includes:
- Principal Component Analysis (PCA)
- Linear Discriminant Analysis (LDA)
- Locally Linear Embedding (LLE)
- Multidimensional Scaling (MDS)
"""
import doctest
import logging

import numpy as np
from scipy.linalg import eigh
from scipy.spatial.distance import cdist
from sklearn.neighbors import NearestNeighbors

logging.basicConfig(level=logging.INFO, format="%(message)s")


def column_reshape(input_array: np.ndarray) -> np.ndarray:
    """Function to reshape a row Numpy array into a column Numpy array.

    Args:
        input_array: Input row vector.

    Returns:
        Column vector.

    Example:
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
    """Compute the covariance matrix inside each class.

    Args:
        features: Input features matrix (n_features x n_samples).
        labels: Class labels for each sample.
        classes: Number of classes.

    Returns:
        Within-class covariance matrix.

    Example:
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
        centered_data = data - column_reshape(data_mean)
        if i > 0:
            covariance_sum += np.dot(centered_data, centered_data.T)
        else:
            covariance_sum = np.dot(centered_data, centered_data.T)

    return covariance_sum / features.shape[1]


def covariance_between_classes(
    features: np.ndarray, labels: np.ndarray, classes: int
) -> np.ndarray:
    """Compute the covariance matrix between multiple classes.

    Args:
        features: Input features matrix (n_features x n_samples).
        labels: Class labels for each sample.
        classes: Number of classes.

    Returns:
        Between-class covariance matrix.

    Example:
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
            covariance_sum += device_data * np.dot(
                column_reshape(data_mean) - column_reshape(general_data_mean),
                (column_reshape(data_mean) - column_reshape(general_data_mean)).T,
            )
        else:
            covariance_sum = device_data * np.dot(
                column_reshape(data_mean) - column_reshape(general_data_mean),
                (column_reshape(data_mean) - column_reshape(general_data_mean)).T,
            )

    return covariance_sum / features.shape[1]


def principal_component_analysis(features: np.ndarray, dimensions: int) -> np.ndarray:
    """Principal Component Analysis (PCA).

    For more details: https://en.wikipedia.org/wiki/Principal_component_analysis

    Args:
        features: Input features matrix (n_features x n_samples).
        dimensions: Target dimensionality.

    Returns:
        Projected data in lower dimensions.

    Example:
    >>> features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> pca_result = principal_component_analysis(features, 2)
    >>> pca_result.shape
    (2, 3)
    """
    if features.any():
        data_mean = features.mean(1)
        centered_data = features - np.reshape(data_mean, (data_mean.size, 1))
        covariance_matrix = np.dot(centered_data, centered_data.T) / features.shape[1]
        _, eigenvectors = np.linalg.eigh(covariance_matrix)
        filtered_eigenvectors = eigenvectors[:, ::-1][:, 0:dimensions]
        projected_data = np.dot(filtered_eigenvectors.T, features)
        logging.info("Principal Component Analysis computed")
        return projected_data
    else:
        logging.error("Dataset empty")
        raise AssertionError


def linear_discriminant_analysis(
    features: np.ndarray, labels: np.ndarray, classes: int, dimensions: int
) -> np.ndarray:
    """Linear Discriminant Analysis (LDA).

    For more details: https://en.wikipedia.org/wiki/Linear_discriminant_analysis

    Args:
        features: Input features matrix (n_features x n_samples).
        labels: Class labels for each sample.
        classes: Number of classes.
        dimensions: Target dimensionality.

    Returns:
        Projected data in lower dimensions.

    Example:
    >>> features = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]])
    >>> labels = np.array([0, 0, 0, 1, 1])
    >>> lda_result = linear_discriminant_analysis(features, labels, 2, 1)
    >>> lda_result.shape
    (1, 5)
    """
    assert classes > dimensions

    if features.any():
        # Add regularization to avoid singular matrix
        sw = covariance_within_classes(features, labels, classes)
        sb = covariance_between_classes(features, labels, classes)

        # Regularize the within-class covariance matrix
        reg_param = 1e-6
        sw_reg = sw + reg_param * np.eye(sw.shape[0])

        try:
            _, eigenvectors = eigh(sb, sw_reg)
            filtered_eigenvectors = eigenvectors[:, ::-1][:, :dimensions]
            svd_matrix, _, _ = np.linalg.svd(filtered_eigenvectors)
            filtered_svd_matrix = svd_matrix[:, 0:dimensions]
            projected_data = np.dot(filtered_svd_matrix.T, features)
            logging.info("Linear Discriminant Analysis computed")
            return projected_data
        except np.linalg.LinAlgError:
            # Fallback: use pseudoinverse if still singular
            try:
                sw_pinv = np.linalg.pinv(sw_reg)
                _, eigenvectors = eigh(sb, sw_pinv)
                filtered_eigenvectors = eigenvectors[:, ::-1][:, :dimensions]
                projected_data = np.dot(filtered_eigenvectors.T, features)
                logging.info("Linear Discriminant Analysis computed with pseudoinverse")
                return projected_data
            except np.linalg.LinAlgError:
                logging.error("LDA failed: matrix is too ill-conditioned")
                raise AssertionError("LDA computation failed")
    else:
        logging.error("Dataset empty")
        raise AssertionError


def locally_linear_embedding(
    features: np.ndarray, dimensions: int, n_neighbors: int = 12, reg: float = 1e-3
) -> np.ndarray:
    """Locally Linear Embedding (LLE).

    For more details: https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction

    Args:
        features: Input features matrix (shape: [n_features, n_samples]).
        dimensions: Target dimension for embedding.
        n_neighbors: Number of neighbors to consider for each point.
        reg: Regularization constant.

    Returns:
        Embedded data in lower dimensions.

    Example:
    >>> features = np.array([[1.0, 2.0, 3.0, 4.0],
    ...                      [2.0, 3.0, 4.0, 5.0],
    ...                      [3.0, 4.0, 5.0, 6.0]])
    >>> lle_result = locally_linear_embedding(features, 2, n_neighbors=2)
    >>> lle_result.shape
    (2, 4)
    """
    if not features.any():
        logging.error("Dataset empty")
        raise AssertionError

    # Transpose to have shape [n_samples, n_features] for easier processing
    x_data = features.T.astype(np.float64)  # Ensure float64 to avoid dtype issues
    n_samples, _ = x_data.shape

    # Find k-nearest neighbors
    knn = NearestNeighbors(n_neighbors=n_neighbors + 1)
    knn.fit(x_data)
    _, indices = knn.kneighbors(x_data)

    # Remove the first index (point itself)
    indices = indices[:, 1:]

    # Create weight matrix w
    w_matrix = np.zeros((n_samples, n_samples))

    for i in range(n_samples):
        # Get neighbors (excluding the point itself)
        neighbors = indices[i]
        # Center the neighbors
        z_matrix = x_data[neighbors] - x_data[i]
        # Local covariance matrix - ensure float64
        cov_matrix = np.dot(z_matrix, z_matrix.T).astype(np.float64)

        # Regularization
        trace_val = np.trace(cov_matrix)
        reg_value = reg * trace_val if trace_val > 0 else reg

        # Ensure we're working with floats for the diagonal update
        cov_matrix = cov_matrix.astype(np.float64)
        np.fill_diagonal(cov_matrix, cov_matrix.diagonal() + reg_value)

        # Solve for weights
        try:
            weights = np.linalg.solve(cov_matrix, np.ones(n_neighbors))
        except np.linalg.LinAlgError:
            # If singular, use pseudoinverse
            weights = np.linalg.pinv(cov_matrix).dot(np.ones(n_neighbors))

        # Normalize weights
        weights /= np.sum(weights)
        w_matrix[i, neighbors] = weights

    # Create cost matrix m = (i_mat - w)^T (i_mat - w)
    i_mat = np.eye(n_samples)
    m_matrix = (i_mat - w_matrix).T.dot(i_mat - w_matrix)

    # Compute eigenvectors - use all and then select
    eigenvalues, eigenvectors = eigh(m_matrix)

    # Sort eigenvalues and take the ones after the first (skip the zero eigenvalue)
    idx = np.argsort(eigenvalues)[1 : dimensions + 1]  # Skip first (zero) eigenvalue
    embedding = eigenvectors[:, idx].T

    logging.info("Locally Linear Embedding computed")
    return embedding


def multidimensional_scaling(
    features: np.ndarray, dimensions: int, metric: bool = True
) -> np.ndarray:
    """Multidimensional Scaling (MDS).

    For more details: https://en.wikipedia.org/wiki/Multidimensional_scaling

    Args:
        features: Input features matrix (shape: [n_features, n_samples]).
        dimensions: Target dimension for embedding.
        metric: If True, use metric MDS (classical), if False use non-metric MDS.

    Returns:
        Embedded data in lower dimensions.

    Example:
    >>> features = np.array([[1.0, 2.0, 3.0, 4.0],
    ...                      [2.0, 3.0, 4.0, 5.0],
    ...                      [3.0, 4.0, 5.0, 6.0]])
    >>> mds_result = multidimensional_scaling(features, 2, metric=True)
    >>> mds_result.shape
    (2, 4)
    """
    if not features.any():
        logging.error("Dataset empty")
        raise AssertionError

    # Transpose to have shape [n_samples, n_features]
    x_data = features.T
    n_samples = x_data.shape[0]

    if metric:
        # Classical MDS
        # Compute distance matrix
        dist_matrix = cdist(x_data, x_data, metric="euclidean")
        dist_squared = dist_matrix**2

        # Double centering
        h_matrix = np.eye(n_samples) - np.ones((n_samples, n_samples)) / n_samples
        b_matrix = -0.5 * h_matrix.dot(dist_squared).dot(h_matrix)

        # Eigen decomposition - get all eigenvectors and select top ones
        eigenvalues, eigenvectors = eigh(b_matrix)

        # Sort in descending order and take top dimensions
        idx = np.argsort(eigenvalues)[::-1][:dimensions]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        # Embedding
        embedding = eigenvectors * np.sqrt(eigenvalues)

    else:
        logging.warning("Using simplified non-metric MDS implementation")

        # Initialize random configuration
        rng = np.random.RandomState(42)
        embedding = rng.randn(n_samples, dimensions)

        # Simple gradient descent (very basic implementation)
        dist_original = cdist(x_data, x_data, metric="euclidean")

        for _ in range(100):
            dist_embedded = cdist(embedding, embedding, metric="euclidean")

            # Simple gradient update
            grad = np.zeros_like(embedding)
            for i in range(n_samples):
                for j in range(n_samples):
                    if i != j:
                        diff = embedding[i] - embedding[j]
                        dist = np.linalg.norm(diff)
                        if dist > 1e-10:
                            grad[i] += (
                                2
                                * (dist_embedded[i, j] - dist_original[i, j])
                                * (diff / dist)
                            )

            embedding -= 0.01 * grad / n_samples

    logging.info("Multidimensional Scaling computed")
    return embedding.T  # Transpose back to match original format


def test_locally_linear_embedding() -> None:
    """Test function for Locally Linear Embedding."""
    # Use float data to avoid dtype issues
    features = np.array(
        [[1.0, 2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0], [3.0, 4.0, 5.0, 6.0]]
    )
    dimensions = 2

    try:
        embedding = locally_linear_embedding(features, dimensions, n_neighbors=2)
        assert embedding.shape[0] == dimensions
        assert embedding.shape[1] == features.shape[1]
        logging.info("LLE test passed")
    except Exception as e:
        logging.error(f"LLE test failed: {e}")
        raise


def test_multidimensional_scaling() -> None:
    """Test function for Multidimensional Scaling."""
    features = np.array(
        [[1.0, 2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0], [3.0, 4.0, 5.0, 6.0]]
    )
    dimensions = 2

    try:
        # Test metric MDS
        embedding_metric = multidimensional_scaling(features, dimensions, metric=True)
        assert embedding_metric.shape[0] == dimensions
        assert embedding_metric.shape[1] == features.shape[1]

        # Test non-metric MDS
        embedding_nonmetric = multidimensional_scaling(
            features, dimensions, metric=False
        )
        assert embedding_nonmetric.shape[0] == dimensions
        assert embedding_nonmetric.shape[1] == features.shape[1]

        logging.info("MDS test passed")
    except Exception as e:
        logging.error(f"MDS test failed: {e}")
        raise


def test_linear_discriminant_analysis() -> None:
    """Test function for Linear Discriminant Analysis."""
    # Create dummy dataset with 2 classes and 3 features
    features = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]])
    labels = np.array([0, 0, 0, 1, 1])
    classes = 2
    dimensions = 1  # Changed to 1 since classes=2 and dimensions must be < classes

    try:
        # This should work since dimensions < classes
        lda_result = linear_discriminant_analysis(features, labels, classes, dimensions)
        assert lda_result.shape == (dimensions, features.shape[1])
        logging.info("LDA test passed")
    except Exception as e:
        logging.error(f"LDA test failed: {e}")
        raise


def test_principal_component_analysis() -> None:
    """Test function for Principal Component Analysis."""
    features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    dimensions = 2
    expected_output = np.array([[6.92820323, 8.66025404, 10.39230485], [3.0, 3.0, 3.0]])

    output = principal_component_analysis(features, dimensions)
    if not np.allclose(expected_output, output):
        raise AssertionError("PCA output does not match expected result")


def test_dimensionality_reduction() -> None:
    """Test all dimensionality reduction algorithms."""
    print("Testing all dimensionality reduction algorithms...")

    # Create sample data using numpy Generator
    rng = np.random.default_rng(42)
    features = rng.random((5, 50))
    labels = rng.integers(0, 3, 50)
    dimensions = 2

    try:
        # Test PCA
        pca_result = principal_component_analysis(features, dimensions)
        assert pca_result.shape == (dimensions, features.shape[1])
        print("✓ PCA test passed")

        # Test LDA
        lda_result = linear_discriminant_analysis(features, labels, 3, dimensions)
        assert lda_result.shape == (dimensions, features.shape[1])
        print("✓ LDA test passed")

        # Test LLE
        lle_result = locally_linear_embedding(features, dimensions, n_neighbors=5)
        assert lle_result.shape == (dimensions, features.shape[1])
        print("✓ LLE test passed")

        # Test MDS
        mds_result = multidimensional_scaling(features, dimensions, metric=True)
        assert mds_result.shape == (dimensions, features.shape[1])
        print("✓ MDS test passed")

        print("All tests passed!")

    except Exception as e:
        print(f"Error during testing: {e}")
        raise


if __name__ == "__main__":
    doctest.testmod()
    test_dimensionality_reduction()
