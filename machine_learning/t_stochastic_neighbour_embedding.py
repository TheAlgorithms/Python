"""
t-distributed Stochastic Neighbor Embedding (t-SNE)

t-SNE is a nonlinear dimensionality reduction technique particularly well-suited
for visualizing high-dimensional datasets in 2D or 3D space. It works by:
1. Computing pairwise similarities in high-dimensional space using Gaussian kernels
2. Computing pairwise similarities in low-dimensional space using Student-t distribution
3. Minimizing the Kullback-Leibler divergence between these two distributions

Reference:
    van der Maaten, L., & Hinton, G. (2008). Visualizing data using t-SNE.
    Journal of Machine Learning Research, 9(86), 2579-2605.

For more details, see:
https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding
"""

import doctest

import numpy as np
from numpy import ndarray
from sklearn.datasets import load_iris


def collect_dataset() -> tuple[ndarray, ndarray]:
    """
    Load the Iris dataset and return features and labels.

    Returns:
        tuple[ndarray, ndarray]: Feature matrix and target labels.

    >>> features, targets = collect_dataset()
    >>> features.shape
    (150, 4)
    >>> targets.shape
    (150,)
    """
    iris_dataset = load_iris()
    return np.array(iris_dataset.data), np.array(iris_dataset.target)


def compute_perplexity_based_sigma(
    distances: ndarray,
    target_perplexity: float,
    tolerance: float = 1e-5,
    max_iter: int = 50,
) -> float:
    """
    Compute the optimal sigma (bandwidth) for a given perplexity using binary search.

    Perplexity is a measure of the effective number of neighbors. This function
    finds the Gaussian kernel bandwidth that produces the target perplexity.

    Args:
        distances: Squared distances from a point to all other points.
        target_perplexity: Desired perplexity value (typically 5-50).
        tolerance: Convergence tolerance for binary search.
        max_iter: Maximum number of binary search iterations.

    Returns:
        float: Optimal sigma value for the target perplexity.

    >>> distances = np.array([0.0, 1.0, 4.0, 9.0])
    >>> sigma = compute_perplexity_based_sigma(distances, target_perplexity=2.0)
    >>> 0.5 < sigma < 2.0
    True
    """
    # Binary search bounds for sigma
    sigma_min, sigma_max = 1e-20, 1e20
    sigma = 1.0

    for _ in range(max_iter):
        # Compute probabilities with current sigma
        probabilities = np.exp(-distances / (2 * sigma**2))
        probabilities[probabilities == np.inf] = 0
        sum_probs = np.sum(probabilities)

        if sum_probs == 0:
            probabilities = np.ones_like(probabilities) / len(probabilities)
            sum_probs = 1.0

        probabilities /= sum_probs

        # Compute Shannon entropy and perplexity
        # H = -sum(p * log2(p)), Perplexity = 2^H
        entropy = -np.sum(probabilities * np.log2(probabilities + 1e-12))
        perplexity = 2**entropy

        # Adjust sigma based on perplexity difference
        perplexity_diff = perplexity - target_perplexity
        if abs(perplexity_diff) < tolerance:
            break

        if perplexity_diff > 0:
            sigma_max = sigma
            sigma = (sigma + sigma_min) / 2
        else:
            sigma_min = sigma
            sigma = (sigma + sigma_max) / 2

    return sigma


def compute_pairwise_affinities(
    data_matrix: ndarray, perplexity: float = 30.0
) -> ndarray:
    """
    Compute high-dimensional affinities (P matrix) using a Gaussian kernel.

    This function computes pairwise conditional probabilities p_j|i that represent
    the similarity between points in the high-dimensional space. The bandwidth (sigma)
    for each point is chosen to achieve the target perplexity.

    Args:
        data_matrix: Input data of shape (n_samples, n_features).
        perplexity: Target perplexity, controls effective number of neighbors
                   (typically 5-50).

    Returns:
        ndarray: Symmetrized probability matrix P where P_ij = (p_j|i + p_i|j) / (2n).

    >>> x = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    >>> probabilities = compute_pairwise_affinities(x, perplexity=2.0)
    >>> probabilities.shape
    (3, 3)
    >>> np.allclose(probabilities, probabilities.T)  # Check symmetry
    True
    """
    n_samples = data_matrix.shape[0]
    # Compute pairwise squared Euclidean distances
    squared_sum = np.sum(np.square(data_matrix), axis=1)
    squared_distances = np.add(
        np.add(-2 * np.dot(data_matrix, data_matrix.T), squared_sum).T, squared_sum
    )

    # Compute conditional probabilities p_j|i for each point i
    affinity_matrix = np.zeros((n_samples, n_samples))
    for i in range(n_samples):
        # Find optimal sigma for this point to achieve target perplexity
        distances_i = squared_distances[i].copy()
        distances_i[i] = 0  # Distance to self is 0
        sigma_i = compute_perplexity_based_sigma(distances_i, perplexity)

        # Compute conditional probabilities for point i
        affinity_matrix[i] = np.exp(-squared_distances[i] / (2 * sigma_i**2))
        affinity_matrix[i, i] = 0  # Set diagonal to 0

        # Normalize to get probabilities
        sum_affinities = np.sum(affinity_matrix[i])
        if sum_affinities > 0:
            affinity_matrix[i] /= sum_affinities

    # Symmetrize: P_ij = (p_j|i + p_i|j) / (2n)
    affinity_matrix = (affinity_matrix + affinity_matrix.T) / (2 * n_samples)
    return affinity_matrix


def compute_low_dim_affinities(embedding_matrix: ndarray) -> tuple[ndarray, ndarray]:
    """
    Compute low-dimensional affinities (Q matrix) using a Student-t distribution.

    In the low-dimensional space, t-SNE uses a Student-t distribution (with 1 degree
    of freedom) instead of a Gaussian. This heavy-tailed distribution helps alleviate
    the "crowding problem" by allowing dissimilar points to be farther apart.

    The probability q_ij is proportional to (1 + ||y_i - y_j||^2)^(-1).

    Args:
        embedding_matrix: Low-dimensional embedding of shape (n_samples, n_components).

    Returns:
        tuple[ndarray, ndarray]: (Q probability matrix, numerator matrix for gradient).

    >>> y = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> q_matrix, numerators = compute_low_dim_affinities(y)
    >>> q_matrix.shape
    (2, 2)
    >>> np.allclose(q_matrix.sum(), 1.0)  # Probabilities sum to 1
    True
    """
    # Compute pairwise squared Euclidean distances in low-dimensional space
    squared_sum = np.sum(np.square(embedding_matrix), axis=1)
    squared_distances = np.add(
        np.add(-2 * np.dot(embedding_matrix, embedding_matrix.T), squared_sum).T,
        squared_sum,
    )

    # Student-t distribution with 1 degree of freedom: (1 + d^2)^(-1)
    numerator_matrix = 1 / (1 + squared_distances)
    np.fill_diagonal(numerator_matrix, 0)  # Set diagonal to 0

    # Normalize to get probability distribution Q
    q_matrix = numerator_matrix / np.sum(numerator_matrix)
    return q_matrix, numerator_matrix


def apply_tsne(
    data_matrix: ndarray,
    n_components: int = 2,
    perplexity: float = 30.0,
    learning_rate: float = 200.0,
    n_iter: int = 500,
) -> ndarray:
    """
    Apply t-SNE for dimensionality reduction.

    t-SNE minimizes the Kullback-Leibler divergence between the high-dimensional
    probability distribution P and the low-dimensional distribution Q using
    gradient descent with momentum.

    Args:
        data_matrix: Original dataset of shape (n_samples, n_features).
        n_components: Target dimension (typically 2 or 3 for visualization).
        perplexity: Perplexity parameter, controls effective number of neighbors.
                   Typical values are between 5 and 50. Larger datasets usually
                   require larger perplexity values.
        learning_rate: Step size for gradient descent (typically 10-1000).
        n_iter: Number of gradient descent iterations (typically 250-1000).

    Returns:
        ndarray: Low-dimensional embedding of shape (n_samples, n_components).

    Raises:
        ValueError: If n_components or n_iter is less than 1, or if perplexity
                   is not in valid range.

    >>> features, _ = collect_dataset()
    >>> embedding = apply_tsne(features, n_components=2, perplexity=30.0, n_iter=50)
    >>> embedding.shape
    (150, 2)
    """
    # Validate input parameters
    if n_components < 1 or n_iter < 1:
        raise ValueError("n_components and n_iter must be >= 1")
    if perplexity < 1 or perplexity >= data_matrix.shape[0]:
        raise ValueError("perplexity must be between 1 and n_samples - 1")

    n_samples = data_matrix.shape[0]

    # Initialize embedding with small random values from Gaussian distribution
    rng = np.random.default_rng()
    embedding = rng.standard_normal((n_samples, n_components)) * 1e-4

    # Compute high-dimensional affinities (P matrix) based on perplexity
    high_dim_affinities = compute_pairwise_affinities(data_matrix, perplexity)
    high_dim_affinities = np.maximum(high_dim_affinities, 1e-12)  # Avoid log(0)

    # Initialize momentum-based gradient descent
    embedding_increment = np.zeros_like(embedding)
    momentum = 0.5  # Initial momentum value

    # Gradient descent optimization loop
    for iteration in range(n_iter):
        # Compute low-dimensional affinities (Q matrix) using Student-t distribution
        low_dim_affinities, numerator_matrix = compute_low_dim_affinities(embedding)
        low_dim_affinities = np.maximum(low_dim_affinities, 1e-12)  # Avoid log(0)

        # Compute gradient of KL divergence: dC/dy_i
        # The gradient has an attractive force (P_ij > Q_ij) and
        # a repulsive force (P_ij < Q_ij)
        affinity_diff = high_dim_affinities - low_dim_affinities

        gradient = 4 * (
            np.dot((affinity_diff * numerator_matrix), embedding)
            - np.multiply(
                np.sum(affinity_diff * numerator_matrix, axis=1)[:, np.newaxis],
                embedding,
            )
        )

        # Update embedding using momentum-based gradient descent
        embedding_increment = momentum * embedding_increment - learning_rate * gradient
        embedding += embedding_increment

        # Increase momentum after initial iterations for faster convergence
        if iteration == int(n_iter / 4):
            momentum = 0.8

    return embedding


def main() -> None:
    """
    Run t-SNE on the Iris dataset and display the first 5 embeddings.

    >>> main()  # doctest: +ELLIPSIS
    t-SNE embedding (first 5 points):
    [[...
    """
    features, _labels = collect_dataset()
    embedding = apply_tsne(
        features, n_components=2, perplexity=30.0, learning_rate=200.0, n_iter=300
    )

    if not isinstance(embedding, np.ndarray):
        raise TypeError("t-SNE embedding must be an ndarray")

    print("t-SNE embedding (first 5 points):")
    print(embedding[:5])

    # Optional visualization (Ruff/mypy compliant)

    # import matplotlib.pyplot as plt
    # plt.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap="viridis")
    # plt.title("t-SNE Visualization of the Iris Dataset")
    # plt.xlabel("Dimension 1")
    # plt.ylabel("Dimension 2")
    # plt.show()


if __name__ == "__main__":
    doctest.testmod()
    main()
