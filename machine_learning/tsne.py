"""
t-Distributed Stochastic Neighbor Embedding (t-SNE)
---------------------------------------------------

t-SNE is a nonlinear dimensionality reduction algorithm for visualizing
high-dimensional data in a low-dimensional space (2D or 3D).

It computes pairwise similarities in both spaces and minimizes the 
Kullback-Leibler divergence using gradient descent.

References:
- van der Maaten, L. & Hinton, G. (2008), JMLR.
- https://lvdmaaten.github.io/tsne/
"""

import doctest
import numpy as np
from numpy import ndarray
from sklearn.datasets import load_iris


def collect_dataset() -> tuple[ndarray, ndarray]:
    """
    Load Iris dataset and return features and labels.

    Returns:
        tuple[ndarray, ndarray]: feature matrix and target labels

    Example:
    >>> x, y = collect_dataset()
    >>> x.shape
    (150, 4)
    >>> y.shape
    (150,)
    """
    data = load_iris()
    return np.array(data.data), np.array(data.target)


def compute_pairwise_affinities(data_x: ndarray, sigma: float = 1.0) -> ndarray:
    """
    Compute high-dimensional affinities (P matrix) using Gaussian kernel.

    Args:
        data_x: Input data of shape (n_samples, n_features)
        sigma: Gaussian kernel bandwidth

    Returns:
        ndarray: Symmetrized probability matrix

    Example:
    >>> x = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> p = compute_pairwise_affinities(x)
    >>> float(round(p[0, 1], 3))
    0.25
    """
    n_samples = data_x.shape[0]
    sum_x = np.sum(np.square(data_x), axis=1)
    dist_sq = np.add(np.add(-2 * np.dot(data_x, data_x.T), sum_x).T, sum_x)
    p = np.exp(-dist_sq / (2 * sigma**2))
    np.fill_diagonal(p, 0)
    p /= np.sum(p)
    return (p + p.T) / (2 * n_samples)


def compute_low_dim_affinities(low_dim_embedding: ndarray) -> tuple[ndarray, ndarray]:
    """
    Compute low-dimensional affinities (Q matrix) using Student-t distribution.

    Args:
        low_dim_embedding: shape (n_samples, n_components)

    Returns:
        tuple[ndarray, ndarray]: Q probability matrix and numerator

    Example:
    >>> y = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> q, num = compute_low_dim_affinities(y)
    >>> q.shape
    (2, 2)
    """
    sum_y = np.sum(np.square(low_dim_embedding), axis=1)
    numerator = 1 / (
        1
        + np.add(
            np.add(-2 * np.dot(low_dim_embedding, low_dim_embedding.T), sum_y).T,
            sum_y,
        )
    )
    np.fill_diagonal(numerator, 0)
    q = numerator / np.sum(numerator)
    return q, numerator


def apply_tsne(
    data_x: ndarray,
    n_components: int = 2,
    learning_rate: float = 200.0,
    n_iter: int = 500,
) -> ndarray:
    """
    Apply t-SNE for dimensionality reduction.

    Args:
        data_x: Original dataset (features)
        n_components: Target dimension (2D or 3D)
        learning_rate: Step size for gradient descent
        n_iter: Number of iterations

    Returns:
        ndarray: Low-dimensional embedding of the data

    Example:
    >>> x, _ = collect_dataset()
    >>> y_emb = apply_tsne(x, n_components=2, n_iter=50)
    >>> y_emb.shape
    (150, 2)
    """
    if n_components < 1 or n_iter < 1:
        raise ValueError("n_components and n_iter must be >= 1")

    n_samples = data_x.shape[0]
    rng = np.random.default_rng()
    y = rng.standard_normal((n_samples, n_components)) * 1e-4

    p = compute_pairwise_affinities(data_x)
    p = np.maximum(p, 1e-12)

    y_inc = np.zeros_like(y)
    momentum = 0.5

    for i in range(n_iter):
        q, num = compute_low_dim_affinities(y)
        q = np.maximum(q, 1e-12)

        pq = p - q
        d_y = 4 * (
            np.dot((pq * num), y)
            - np.multiply(np.sum(pq * num, axis=1)[:, np.newaxis], y)
        )

        y_inc = momentum * y_inc - learning_rate * d_y
        y += y_inc

        if i == int(n_iter / 4):
            momentum = 0.8

    return y


def main() -> None:
    """
    Run t-SNE on Iris dataset and display the first 5 embeddings.

    Example:
    >>> main()  # runs without errors
    """
    data_x, _ = collect_dataset()
    y_emb = apply_tsne(data_x, n_components=2, n_iter=300)

    if not isinstance(y_emb, np.ndarray):
        raise TypeError("t-SNE embedding must be an ndarray")

    print("t-SNE embedding (first 5 points):")
    print(y_emb[:5])

    # Optional visualization (commented, Ruff/mypy compliant)
    # import matplotlib.pyplot as plt
    # plt.scatter(
    #     y_emb[:, 0],
    #     y_emb[:, 1],
    #     c=_labels,
    #     cmap="viridis"
    # )
    # plt.show()


if __name__ == "__main__":
    doctest.testmod()
    main()
