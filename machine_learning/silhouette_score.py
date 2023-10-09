"""
Silhouette Score Calculation : https://en.wikipedia.org/wiki/Silhouette_(clustering)

The Silhouette Score is a metric used to evaluate the quality of clusters in a clustering algorithm.
It measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation).
A higher silhouette score indicates better clustering quality.

In this algorithm:
- Pairwise distances between data points are computed using Euclidean distance.
- For each data point:
  1. 'a' is calculated as the average distance to other data points in the same cluster.
  2. 'b' is calculated as the minimum average distance to data points in different clusters.
  3. The silhouette score is determined as (b - a) / max(a, b) and ranges from -1 to +1.
     (0 indicates overlapping clusters, negative values suggest incorrect clustering, and positive values indicate good clustering)
"""

import numpy as np
from typing import Union


def pairwise_distances(data_points: np.ndarray) -> np.ndarray:
    """
    Compute pairwise distances between data points in the input array X.

    Parameters:
    data_points (numpy.ndarray): The input data array of shape (n_samples, n_features).

    Returns:
    numpy.ndarray: A square matrix of pairwise distances where distances[i, j] represents
    the Euclidean distance between X[i] and X[j].

    Example:
    >>> import numpy as np
    >>> from machine_learning.silhouette_score import pairwise_distances
    >>> data_points = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    >>> distances = pairwise_distances(data_points)
    >>> distances
    array([[0.        , 1.41421356, 2.82842712, 4.24264069],
           [1.41421356, 0.        , 1.41421356, 2.82842712],
           [2.82842712, 1.41421356, 0.        , 1.41421356],
           [4.24264069, 2.82842712, 1.41421356, 0.        ]])
    """
    n = data_points.shape[0]
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            distances[i, j] = np.linalg.norm(data_points[i] - data_points[j])
            distances[j, i] = distances[i, j]
    return distances


def silhouette_score(
    data_points: np.ndarray, cluster_labels: Union[list, np.ndarray]
) -> float:
    """
    Calculate the silhouette score for a set of data points and their corresponding cluster labels.

    The silhouette score measures the quality of clustering. It quantifies how similar an object
    is to its own cluster compared to other clusters.

    Parameters:
    data_points (numpy.ndarray): The input data array of shape (n_samples, n_features).
    cluster_labels (list or numpy.ndarray): List of cluster labels assigned to each data point in X.

    Returns:
    float: The average silhouette score for the clustering. The score ranges from -1 (a poor clustering)
    to +1 (a perfect clustering), with 0 indicating overlapping clusters.

    Example:
    >>> import numpy as np
    >>> from machine_learning.silhouette_score import silhouette_score
    >>> data_points = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    >>> cluster_labels = [0, 0, 1, 1]
    >>> score = silhouette_score(data_points, cluster_labels)
    >>> round(score, 2)
    0.36
    """
    distances = pairwise_distances(data_points)
    n = len(data_points)
    silhouette_values = []

    for i in range(n):
        a = np.mean(
            [
                distances[i, j]
                for j in range(n)
                if cluster_labels[j] == cluster_labels[i] and j != i
            ]
        )
        b_values = [
            np.mean([distances[i, j] for j in range(n) if cluster_labels[j] == k])
            for k in set(cluster_labels)
            if k != cluster_labels[i]
        ]
        b = min(b_values) if b_values else 0.0
        silhouette = (b - a) / max(a, b) if max(a, b) != 0 else 0.0
        silhouette_values.append(silhouette)

    average_silhouette_score = np.mean(silhouette_values)
    return average_silhouette_score
