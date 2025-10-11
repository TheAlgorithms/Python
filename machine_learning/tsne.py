"""
t-Distributed Stochastic Neighbor Embedding (t-SNE)
---------------------------------------------------
t-SNE is a nonlinear dimensionality reduction algorithm used for visualizing
high-dimensional data in a lower-dimensional (usually 2D or 3D) space.

It models pairwise similarities between points in both the high-dimensional
and low-dimensional spaces, and minimizes the difference between them
using gradient descent.

This simplified implementation demonstrates the core idea of t-SNE for
educational purposes — it is **not optimized for large datasets**.

This implementation:
- Computes pairwise similarities in the high-dimensional space.
- Computes pairwise similarities in the low-dimensional (embedding) space.
- Minimizes the Kullback–Leibler divergence between these distributions
  using gradient descent.
- Follows the original t-SNE formulation by van der Maaten & Hinton (2008).

References:
- van der Maaten, L. and Hinton, G. (2008).
  "Visualizing Data using t-SNE". Journal of Machine Learning Research.
- https://lvdmaaten.github.io/tsne/

Key Steps:
1. Compute pairwise similarities (P) in high-dimensional space.
2. Initialize low-dimensional map (Y) randomly.
3. Compute pairwise similarities (Q) in low-dimensional space using
   Student-t distribution.
4. Minimize KL-divergence between P and Q using gradient descent.
"""
import doctest
import numpy as np
from sklearn.datasets import load_iris

def collect_dataset() -> tuple[np.ndarray, np.ndarray]:
    """
    Collects the dataset (Iris dataset) and returns feature matrix and target values.

    :return: Tuple containing feature matrix (X) and target labels (y)

    Example:
    >>> X, y = collect_dataset()
    >>> X.shape
    (150, 4)
    >>> y.shape
    (150,)
    """
    data = load_iris()
    return np.array(data.data), np.array(data.target)

def compute_pairwise_affinities(X: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """
    Computes pairwise affinities (P matrix) in high-dimensional space using Gaussian kernel.

    :param X: Input data of shape (n_samples, n_features)
    :param sigma: Variance (Bandwidth) of the Gaussian kernel
    :return: Symmetrized probability matrix P of shape (n_samples, n_samples)/ Pairwise affinity matrix P

    Example:
    >>> import numpy as np
    >>> X = np.array([[0.0, 0.0], [1.0, 0.0]])
    >>> P = compute_pairwise_affinities(X)
    >>> float(round(P[0, 1], 3))
    0.25
    """
    n = X.shape[0]
    sum_X = np.sum(np.square(X), axis=1)
    D = np.add(np.add(-2 * np.dot(X, X.T), sum_X).T, sum_X)
    P = np.exp(-D / (2 * sigma ** 2))
    np.fill_diagonal(P, 0)
    P /= np.sum(P)
    return (P + P.T) / (2 * n)

def compute_low_dim_affinities(Y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Computes low-dimensional similarities (Q matrix) using Student-t distribution.

    :param Y: Low-dimensional embeddings (n_samples, n_components)
    :return: Tuple (Q, num) where Q is the probability matrix and num is numerator array
    """
    sum_Y = np.sum(np.square(Y), axis=1)
    num = 1 / (1 + np.add(np.add(-2 * np.dot(Y, Y.T), sum_Y).T, sum_Y))
    np.fill_diagonal(num, 0)
    Q = num / np.sum(num)
    return Q, num


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
    >>> X, _ = collect_dataset()
    >>> Y = apply_tsne(X, n_components=2, n_iter=250)
    >>> Y.shape
    (150, 2)
    """
    if n_components < 1:
        raise ValueError("n_components must be >= 1")
    if n_iter < 1:
        raise ValueError("n_iter must be >= 1")

    n_samples = data_x.shape[0]

    # Initialize low-dimensional map randomly
    Y = np.random.randn(n_samples, n_components) * 1e-4
    P = compute_pairwise_affinities(data_x)
    P = np.maximum(P, 1e-12)

    # Initialize parameters
    Y_inc = np.zeros_like(Y)
    momentum = 0.5

    for i in range(n_iter):
        Q, num = compute_low_dim_affinities(Y)
        Q = np.maximum(Q, 1e-12)

        PQ = P - Q

        # Compute gradient
        dY = 4 * (
            np.dot((PQ * num), Y)
            - np.multiply(np.sum(PQ * num, axis=1)[:, np.newaxis], Y)
        )

        # Update with momentum and learning rate
        Y_inc = momentum * Y_inc - learning_rate * dY
        Y += Y_inc

        # Adjust momentum halfway through
        if i == int(n_iter / 4):
            momentum = 0.8

    return Y


def main() -> None:
    """
    Driver function for t-SNE demonstration.
    """
    X, y = collect_dataset()

    Y = apply_tsne(X, n_components=2, n_iter=300)
    print("t-SNE embedding (first 5 points):")
    print(Y[:5])

    # Optional visualization (commented to avoid dependency)
    # import matplotlib.pyplot as plt
    # plt.scatter(Y[:, 0], Y[:, 1], c=y, cmap="viridis")
    # plt.title("t-SNE Visualization of Iris Dataset")
    # plt.xlabel("Component 1")
    # plt.ylabel("Component 2")
    # plt.show()


if __name__ == "__main__":
    doctest.testmod()
    main()

"""
Explanation of t-SNE Implementation
-----------------------------------

Input:
- data_x: numpy array of shape (n_samples, n_features)
  Example: Iris dataset (150 samples × 4 features)
- n_components: target dimension (usually 2 or 3 for visualization)
- learning_rate: controls step size in gradient descent
- n_iter: number of iterations for optimization

Output:
- Y: numpy array of shape (n_samples, n_components)
  Each row is the low-dimensional embedding of the corresponding high-dimensional point.

How it works:
1. Compute high-dimensional similarities (P matrix):
   - Measures how likely points are neighbors in the original space.
2. Initialize low-dimensional map (Y) randomly.
3. Compute low-dimensional similarities (Q matrix) using Student-t distribution:
   - Heavy tail prevents distant points from crowding together.
4. Compute gradient of KL divergence between P and Q:
   - If points are too far in low-D (Q < P), pull them closer.
   - If points are too close in low-D (Q > P), push them apart.
5. Update Y using gradient descent with momentum:
   - Repeat for n_iter iterations until low-dimensional layout reflects high-dimensional structure.

Why it works:
- t-SNE tries to preserve **local structure**: neighbors stay close in the embedding.
- Distant points may not be perfectly preserved (global structure is secondary).
- The algorithm minimizes the KL divergence between high-D and low-D similarity distributions.
"""
