"""
k-Medoids Clustering Algorithm

For more details, see:
https://en.wikipedia.org/wiki/K-medoids
"""

import doctest

import numpy as np
from numpy import ndarray
from sklearn.datasets import load_iris


def _get_data() -> tuple[ndarray, ndarray]:
    """
    Load the Iris dataset and return features and labels.

    Returns:
        tuple[ndarray, ndarray]: Feature matrix and target labels.

    >>> features, labels = _get_data()
    >>> features.shape
    (150, 4)
    >>> labels.shape
    (150,)
    """
    iris = load_iris()
    return np.array(iris.data), np.array(iris.target)


def _compute_distances(data_matrix: ndarray, medoids: ndarray) -> ndarray:
    """
    Compute pairwise distances between points and medoids.

    Args:
        data_matrix: Input dataset.
        medoids: Indices of current medoids.

    Returns:
        ndarray: Distance matrix of shape (n_samples, n_clusters).

    >>> x = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    >>> d = _compute_distances(x, np.array([0, 2]))
    >>> d.shape
    (3, 2)
    """
    return np.linalg.norm(data_matrix[:, np.newaxis] - data_matrix[medoids], axis=2)


def _assign_clusters(distances: ndarray) -> ndarray:
    """
    Assign each data point to the nearest medoid.

    Args:
        distances: Pairwise distance matrix.

    Returns:
        ndarray: Cluster assignments.

    >>> d = np.array([[0.1, 0.4], [0.2, 0.3], [0.9, 0.1]])
    >>> _assign_clusters(d)
    array([0, 0, 1])
    """
    return np.argmin(distances, axis=1).astype(int)


def _initialize_medoids(
    n_samples: int, n_clusters: int, random_state: int | None = None
) -> ndarray:
    """
    Randomly select initial medoids.

    Args:
        n_samples: Total number of samples.
        n_clusters: Number of clusters.
        random_state: Optional random seed.

    Returns:
        ndarray: Indices of initial medoids.

    >>> np.random.seed(42)
    >>> _initialize_medoids(10, 3).shape
    (3,)
    """
    rng = np.random.default_rng(random_state)
    return rng.choice(n_samples, n_clusters, replace=False)


def _update_medoids(
    data_matrix: ndarray, clusters: ndarray, n_clusters: int
) -> ndarray:
    """
    Update medoids by minimizing intra-cluster distances.

    Args:
        data_matrix: Dataset.
        clusters: Cluster assignments.
        n_clusters: Number of clusters.

    Returns:
        ndarray: Updated medoid indices.

    >>> x = np.array([[0.0, 0.0], [1.0, 0.0], [5.0, 0.0]])
    >>> clusters = np.array([0, 0, 1])
    >>> _update_medoids(x, clusters, 2).shape
    (2,)
    """
    new_medoids = np.zeros(n_clusters, dtype=int)
    for k in range(n_clusters):
        cluster_points = np.where(clusters == k)[0]
        if len(cluster_points) == 0:
            continue

        intra_distances = np.sum(
            np.linalg.norm(
                data_matrix[cluster_points][:, np.newaxis]
                - data_matrix[cluster_points],
                axis=2,
            ),
            axis=1,
        )
        new_medoids[k] = cluster_points[np.argmin(intra_distances)]

    return new_medoids


def apply_k_medoids(
    data_matrix: ndarray,
    n_clusters: int = 3,
    max_iter: int = 100,
    random_state: int | None = None,
) -> tuple[ndarray, ndarray]:
    """
    Apply k-Medoids clustering to a dataset.

    Args:
        data_matrix: Input dataset.
        n_clusters: Number of clusters.
        max_iter: Maximum iterations.
        random_state: Optional random seed.

    Returns:
        tuple[ndarray, ndarray]: Final medoids and cluster assignments.

    >>> features, _ = _get_data()
    >>> medoids, clusters = apply_k_medoids(features, n_clusters=3, max_iter=10)
    >>> len(medoids)
    3
    """
    if n_clusters < 1 or max_iter < 1:
        raise ValueError("n_clusters and max_iter must be >= 1")

    n_samples = data_matrix.shape[0]
    medoids = _initialize_medoids(n_samples, n_clusters, random_state)

    for _ in range(max_iter):
        distances = _compute_distances(data_matrix, medoids)
        clusters = _assign_clusters(distances)
        new_medoids = _update_medoids(data_matrix, clusters, n_clusters)

        if np.array_equal(medoids, new_medoids):
            break
        medoids = new_medoids

    return medoids, clusters


def main() -> None:
    """
    Run k-Medoids on the Iris dataset and display results.

    >>> main()  # doctest: +ELLIPSIS
    k-Medoids clustering (first 10 assignments):
    [...]
    """
    features, _ = _get_data()
    _, clusters = apply_k_medoids(features, n_clusters=3, max_iter=50, random_state=42)

    if not isinstance(clusters, np.ndarray):
        raise TypeError("Cluster assignments must be an ndarray")

    print("k-Medoids clustering (first 10 assignments):")
    print(clusters[:10])

    # Optional visualization
    # import matplotlib.pyplot as plt
    # plt.scatter(features[:, 0], features[:, 1], c=clusters, cmap="viridis", s=30)
    # plt.scatter(
    #     features[medoids, 0],
    #     features[medoids, 1],
    #     c="red",
    #     marker="x",
    #     s=100,
    # )
    # plt.title("k-Medoids Clustering (Iris Dataset)")
    # plt.xlabel("Feature 1")
    # plt.ylabel("Feature 2")
    # plt.show()


if __name__ == "__main__":
    doctest.testmod()
    main()
