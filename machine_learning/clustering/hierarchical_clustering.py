"""
Hierarchical Clustering using Euclidean distance and single linkage.
Reference: https://en.wikipedia.org/wiki/Hierarchical_clustering

>>> import numpy as np
>>> data = np.array([[0, 0], [1, 1], [5, 5], [6, 6]])
>>> hc = HierarchicalClustering()
>>> hc.fit(data)
>>> hc.clusters
[[0, 1], [2, 3]]
"""

import numpy as np


class HierarchicalClustering:
    def __init__(self) -> None:
        """Initialize the clustering model."""
        self.clusters: list[list[int]] = []

    def euclidean_distance(self, point_a: np.ndarray, point_b: np.ndarray) -> float:
        """Compute Euclidean distance between two points."""
        return np.linalg.norm(point_a - point_b)

    def fit(self, data: np.ndarray) -> None:
        """
        Perform hierarchical clustering using single linkage.

        Args:
            data: 2D numpy array of shape (n_samples, n_features)
        """
        n_samples = len(data)
        clusters = [[i] for i in range(n_samples)]

        while len(clusters) > 2:
            min_dist = float("inf")
            to_merge = (0, 1)

            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    dist = min(
                        self.euclidean_distance(data[p1], data[p2])
                        for p1 in clusters[i]
                        for p2 in clusters[j]
                    )
                    if dist < min_dist:
                        min_dist = dist
                        to_merge = (i, j)

            merged = clusters[to_merge[0]] + clusters[to_merge[1]]
            clusters = [
                c for idx, c in enumerate(clusters) if idx not in to_merge
            ]
            clusters.append(merged)

        self.clusters = clusters
