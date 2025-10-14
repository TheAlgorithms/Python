"""
t-distributed stochastic neighbor embedding (t-SNE)

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


def compute_pairwise_affinities(data_matrix: ndarray, sigma: float = 1.0) -> ndarray:
    """
    Compute high-dimensional affinities (P matrix) using a Gaussian kernel.

    Args:
        data_matrix: Input data of shape (n_samples, n_features).
        sigma: Gaussian kernel bandwidth.

    Returns:
        ndarray: Symmetrized probability matrix.

    >>> x = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> probabilities = compute_pairwise_affinities(x)
    >>> float(round(probabilities[0, 1], 3))
    0.25
    """
    n_samples = data_matrix.shape[0]
    squared_sum = np.sum(np.square(data_matrix), axis=1)
    squared_distance = np.add(
        np.add(-2 * np.dot(data_matrix, data_matrix.T), squared_sum).T, squared_sum
    )

    affinity_matrix = np.exp(-squared_distance / (2 * sigma**2))
    np.fill_diagonal(affinity_matrix, 0)

    affinity_matrix /= np.sum(affinity_matrix)
    return (affinity_matrix + affinity_matrix.T) / (2 * n_samples)


def compute_low_dim_affinities(embedding_matrix: ndarray) -> tuple[ndarray, ndarray]:
    """
    Compute low-dimensional affinities (Q matrix) using a Student-t distribution.

    Args:
        embedding_matrix: Low-dimensional embedding of shape (n_samples, n_components).

    Returns:
        tuple[ndarray, ndarray]: (Q probability matrix, numerator matrix).

    >>> y = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> q_matrix, numerators = compute_low_dim_affinities(y)
    >>> q_matrix.shape
    (2, 2)
    """
    squared_sum = np.sum(np.square(embedding_matrix), axis=1)
    numerator_matrix = 1 / (
        1
        + np.add(
            np.add(-2 * np.dot(embedding_matrix, embedding_matrix.T), squared_sum).T,
            squared_sum,
        )
    )
    np.fill_diagonal(numerator_matrix, 0)

    q_matrix = numerator_matrix / np.sum(numerator_matrix)
    return q_matrix, numerator_matrix


def apply_tsne(
    data_matrix: ndarray,
    n_components: int = 2,
    learning_rate: float = 200.0,
    n_iter: int = 500,
) -> ndarray:
    """
    Apply t-SNE for dimensionality reduction.

    Args:
        data_matrix: Original dataset (features).
        n_components: Target dimension (2D or 3D).
        learning_rate: Step size for gradient descent.
        n_iter: Number of iterations.

    Returns:
        ndarray: Low-dimensional embedding of the data.

    >>> features, _ = collect_dataset()
    >>> embedding = apply_tsne(features, n_components=2, n_iter=50)
    >>> embedding.shape
    (150, 2)
    """
    if n_components < 1 or n_iter < 1:
        raise ValueError("n_components and n_iter must be >= 1")

    n_samples = data_matrix.shape[0]
    rng = np.random.default_rng()
    embedding = rng.standard_normal((n_samples, n_components)) * 1e-4

    high_dim_affinities = compute_pairwise_affinities(data_matrix)
    high_dim_affinities = np.maximum(high_dim_affinities, 1e-12)

    embedding_increment = np.zeros_like(embedding)
    momentum = 0.5

    for iteration in range(n_iter):
        low_dim_affinities, numerator_matrix = compute_low_dim_affinities(embedding)
        low_dim_affinities = np.maximum(low_dim_affinities, 1e-12)

        affinity_diff = high_dim_affinities - low_dim_affinities

        gradient = 4 * (
            np.dot((affinity_diff * numerator_matrix), embedding)
            - np.multiply(
                np.sum(affinity_diff * numerator_matrix, axis=1)[:, np.newaxis],
                embedding,
            )
        )

        embedding_increment = momentum * embedding_increment - learning_rate * gradient
        embedding += embedding_increment

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
    embedding = apply_tsne(features, n_components=2, n_iter=300)

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
