"""
t-Distributed Stochastic Neighbor Embedding (t-SNE)
---------------------------------------------------

t-SNE is a nonlinear dimensionality reduction algorithm used for visualizing
high-dimensional data in a lower-dimensional (usually 2D or 3D) space.

It models pairwise similarities between points in both the high-dimensional
and low-dimensional spaces, and minimizes the difference between them using
gradient descent.

This simplified implementation demonstrates the core idea of t-SNE for
educational purposes — it is **not optimized for large datasets**.

This implementation:
- Computes pairwise similarities in the high-dimensional space.
- Computes pairwise similarities in the low-dimensional (embedding) space.
- Minimizes the Kullback-Leibler divergence between these distributions
  using gradient descent.
- Follows the original t-SNE formulation by van der Maaten & Hinton (2008).

References:
- van der Maaten, L. and Hinton, G. (2008).
  "Visualizing Data using t-SNE". Journal of Machine Learning Research.
- https://lvdmaaten.github.io/tsne/
"""

import doctest
import numpy as np
from sklearn.datasets import load_iris


def collect_dataset() -> tuple[np.ndarray, np.ndarray]:
    """
    Collects the Iris dataset and returns features and labels.

    :return: Tuple containing feature matrix and target labels

    Example:
    >>> data_x, data_y = collect_dataset()
    >>> data_x.shape
    (150, 4)
    >>> data_y.shape
    (150,)
    """
    data = load_iris()
    return np.array(data.data), np.array(data.target)


def compute_pairwise_affinities(data_x: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """
    Computes pairwise affinities (P matrix) in high-dimensional space using Gaussian kernel.

    :param data_x: Input data of shape (n_samples, n_features)
    :param sigma: Variance (Bandwidth) of the Gaussian kernel
    :return: Symmetrized probability matrix p

    Example:
    >>> import numpy as np
    >>> data_x = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> p = compute_pairwise_affinities(data_x)
    >>> float(round(p[0, 1], 3))
    0.25
    """
    n_samples = data_x.shape[0]
    sum_x = np.sum(np.square(data_x), axis=1)
    d = np.add(np.add(-2 * np.dot(data_x, data_x.T), sum_x).T, sum_x)
    p = np.exp(-d / (2 * sigma**2))
    np.fill_diagonal(p, 0)
    p /= np.sum(p)
    return (p + p.T) / (2 * n_samples)


def compute_low_dim_affinities(
    embedding_y: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Computes low-dimensional similarities (Q matrix) using Student-t distribution.

    :param embedding_y: Low-dimensional embeddings (n_samples, n_components)
    :return: Tuple (q, num) where q is the probability matrix and num is numerator array

    Example:
    >>> embedding_y = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> q, num = compute_low_dim_affinities(embedding_y)
    >>> q.shape
    (2, 2)
    >>> num.shape
    (2, 2)
    """
    sum_y = np.sum(np.square(embedding_y), axis=1)
    num = 1 / (
        1 + np.add(np.add(-2 * np.dot(embedding_y, embedding_y.T), sum_y).T, sum_y)
    )
    np.fill_diagonal(num, 0)
    q = num / np.sum(num)
    return q, num


def apply_tsne(
    data_x: np.ndarray,
    n_components: int = 2,
    learning_rate: float = 200.0,
    n_iter: int = 500,
) -> np.ndarray:
    """
    Applies t-SNE to reduce data dimensionality for visualization.

    :param data_x: Original dataset (features)
    :param n_components: Target dimension (2D or 3D)
    :param learning_rate: Learning rate for gradient descent
    :param n_iter: Number of iterations
    :return: Transformed dataset (low-dimensional embedding)

    Example:
    >>> data_x, _ = collect_dataset()
    >>> y_emb = apply_tsne(data_x, n_components=2, n_iter=50)
    >>> y_emb.shape
    (150, 2)
    """
    if n_components < 1:
        raise ValueError("n_components must be >= 1")
    if n_iter < 1:
        raise ValueError("n_iter must be >= 1")

    n_samples = data_x.shape[0]

    # Initialize low-dimensional map randomly
    y_emb = np.random.randn(n_samples, n_components) * 1e-4
    p = compute_pairwise_affinities(data_x)
    p = np.maximum(p, 1e-12)

    # Initialize parameters
    y_inc = np.zeros_like(y_emb)
    momentum = 0.5

    for i in range(n_iter):
        q, num = compute_low_dim_affinities(y_emb)
        q = np.maximum(q, 1e-12)

        pq = p - q

        # Compute gradient
        d_y = 4 * (
            np.dot((pq * num), y_emb)
            - np.multiply(np.sum(pq * num, axis=1)[:, np.newaxis], y_emb)
        )

        # Update with momentum and learning rate
        y_inc = momentum * y_inc - learning_rate * d_y
        y_emb += y_inc

        # Adjust momentum halfway through
        if i == int(n_iter / 4):
            momentum = 0.8

    return y_emb


def main() -> None:
    """
    Driver function for t-SNE demonstration.

    Example:
    >>> main()  # doctest: +ELLIPSIS
    t-SNE embedding (first 5 points):
    ...
    """
    data_x, data_y = collect_dataset()
    y_emb = apply_tsne(data_x, n_components=2, n_iter=300)
    print("t-SNE embedding (first 5 points):")
    print(y_emb[:5])

    # Optional visualization (commented to avoid dependency)
    # import matplotlib.pyplot as plt
    # plt.scatter(y_emb[:, 0], y_emb[:, 1], c=data_y, cmap="viridis")
    # plt.title("t-SNE Visualization of Iris Dataset")
    # plt.xlabel("Component 1")
    # plt.ylabel("Component 2")
    # plt.show()


if __name__ == "__main__":
    doctest.testmod()
    main()


"""
Explanation of Input and Output
--------------------------------

Input:
- data_x: numpy array of shape (n_samples, n_features)
  Example: Iris dataset (150 samples × 4 features)
- n_components: target dimension (usually 2 or 3)
- learning_rate: gradient descent step size
- n_iter: number of iterations for optimization

Output:
- y_emb: numpy array of shape (n_samples, n_components)
  Each row is the low-dimensional embedding of the corresponding high-dimensional point.

How it works:
1. Compute high-dimensional similarities (P matrix)
2. Initialize low-dimensional map (y_emb) randomly
3. Compute low-dimensional similarities (Q matrix)
4. Minimize KL divergence between P and Q using gradient descent
5. Update y_emb with momentum and learning rate iteratively
"""
