"""
t-Distributed Stochastic Neighbor Embedding (t-SNE)
---------------------------------------------------

Nonlinear dimensionality reduction for visualizing high-dimensional data
in 2D or 3D. Computes pairwise similarities in high and low-dimensional
spaces and minimizes Kullback-Leibler divergence using gradient descent.

References:
- van der Maaten, L. & Hinton, G. (2008), JMLR.
- https://lvdmaaten.github.io/tsne/
"""

import numpy as np
from numpy import ndarray
from sklearn.datasets import load_iris


def _compute_pairwise_affinities(data_x: ndarray, sigma: float = 1.0) -> ndarray:
    """
    Compute high-dimensional affinities using Gaussian kernel.

    Args:
        data_x (ndarray): shape (n_samples, n_features)
        sigma (float): Gaussian kernel bandwidth

    Returns:
        ndarray: Symmetrized probability matrix

    Example:
    >>> x = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> p = _compute_pairwise_affinities(x)
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


def _compute_low_dim_affinities(low_dim_embedding: ndarray) -> tuple[ndarray, ndarray]:
    """
    Compute low-dimensional affinities using Student-t distribution.

    Args:
        low_dim_embedding (ndarray): shape (n_samples, n_components)

    Returns:
        tuple[ndarray, ndarray]: Q matrix and numerator

    Example:
    >>> y = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> q, num = _compute_low_dim_affinities(y)
    >>> q.shape
    (2, 2)
    """
    sum_y = np.sum(np.square(low_dim_embedding), axis=1)
    num = 1 / (
        1
        + np.add(
            np.add(-2 * np.dot(low_dim_embedding, low_dim_embedding.T), sum_y).T, sum_y
        )
    )
    np.fill_diagonal(num, 0)
    q = num / np.sum(num)
    return q, num


class TSNE:
    """
    t-SNE class for dimensionality reduction.

    Args:
        n_components (int): target dimension (default: 2)
        learning_rate (float): gradient descent step size (default: 200)
        n_iter (int): number of iterations (default: 500)

    Example:
    >>> x, _ = load_iris(return_X_y=True)
    >>> tsne = TSNE(n_components=2, n_iter=50)
    >>> tsne.fit(x)
    >>> emb = tsne.embedding_
    >>> emb.shape
    (150, 2)
    """

    def __init__(
        self, *, n_components: int = 2, learning_rate: float = 200.0, n_iter: int = 500
    ) -> None:
        if n_components < 1:
            raise ValueError("n_components must be >= 1")
        if n_iter < 1:
            raise ValueError("n_iter must be >= 1")
        self.n_components = n_components
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.embedding_: ndarray | None = None

    def fit(self, data_x: ndarray) -> None:
        """
        Fit t-SNE on data and compute low-dimensional embedding.

        Args:
            data_x (ndarray): shape (n_samples, n_features)

        Example:
        >>> x, _ = load_iris(return_X_y=True)
        >>> tsne = TSNE(n_iter=10)
        >>> tsne.fit(x)
        >>> tsne.embedding_.shape
        (150, 2)
        """
        n_samples = data_x.shape[0]
        rng = np.random.default_rng()
        y = rng.standard_normal((n_samples, self.n_components)) * 1e-4

        p = _compute_pairwise_affinities(data_x)
        p = np.maximum(p, 1e-12)

        y_inc = np.zeros_like(y)
        momentum = 0.5

        for i in range(self.n_iter):
            q, num = _compute_low_dim_affinities(y)
            q = np.maximum(q, 1e-12)
            pq = p - q

            d_y = 4 * (
                np.dot((pq * num), y)
                - np.multiply(np.sum(pq * num, axis=1)[:, np.newaxis], y)
            )

            y_inc = momentum * y_inc - self.learning_rate * d_y
            y += y_inc

            if i == int(self.n_iter / 4):
                momentum = 0.8

        self.embedding_ = y

    def transform(self, data_x: ndarray) -> ndarray:
        """
        Return the computed embedding after fitting.

        Args:
            data_x (ndarray): unused, exists for API consistency

        Returns:
            ndarray: low-dimensional embedding

        Example:
        >>> x, _ = load_iris(return_X_y=True)
        >>> tsne = TSNE(n_iter=10)
        >>> tsne.fit(x)
        >>> tsne.transform(x).shape
        (150, 2)
        """
        if self.embedding_ is None:
            raise ValueError("Fit the model first using fit()")
        return self.embedding_


def collect_dataset() -> tuple[ndarray, ndarray]:
    """
    Load Iris dataset.

    Returns:
        tuple[ndarray, ndarray]: features and labels

    Example:
    >>> x, y = collect_dataset()
    >>> x.shape
    (150, 4)
    >>> y.shape
    (150,)
    """
    data = load_iris()
    return np.array(data.data), np.array(data.target)


def main() -> None:
    """
    Run t-SNE on Iris dataset and print first 5 points.

    Example:
    >>> main()  # runs without errors
    """
    data_x, _ = collect_dataset()
    tsne = TSNE(n_components=2, n_iter=300)
    tsne.fit(data_x)
    print("t-SNE embedding (first 5 points):")
    print(tsne.embedding_[:5])

    # Optional visualization
    # import matplotlib.pyplot as plt
    # plt.scatter(tsne.embedding_[:, 0], tsne.embedding_[:, 1], c=_labels, cmap="viridis")
    # plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
