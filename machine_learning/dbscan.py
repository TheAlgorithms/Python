
import numpy as np
from collections import deque

# DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
# Groups points that are closely packed together, marks outliers as noise
class DBSCAN:
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps  # Neighborhood radius
        self.min_samples = min_samples  # Minimum points to form a dense region

    def fit(self, X):
        n = X.shape[0]
        labels = np.full(n, -1)  # Initialize all points as noise (-1)
        cluster_id = 0
        visited = np.zeros(n, dtype=bool)
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            neighbors = self._region_query(X, i)
            if len(neighbors) < self.min_samples:
                labels[i] = -1  # Not enough neighbors, mark as noise
            else:
                # Expand cluster from this core point
                self._expand_cluster(X, labels, i, neighbors, cluster_id, visited)
                cluster_id += 1
        self.labels_ = labels
        return self

    def _region_query(self, X, idx):
        # Find all points within eps of point idx
        dists = np.linalg.norm(X - X[idx], axis=1)
        return np.where(dists <= self.eps)[0].tolist()

    def _expand_cluster(self, X, labels, idx, neighbors, cluster_id, visited):
        # Add point idx and all density-reachable points to cluster
        labels[idx] = cluster_id
        queue = deque(neighbors)
        while queue:
            n_idx = queue.popleft()
            if not visited[n_idx]:
                visited[n_idx] = True
                n_neighbors = self._region_query(X, n_idx)
                if len(n_neighbors) >= self.min_samples:
                    # Add new neighbors to queue if they are core points
                    queue.extend(n for n in n_neighbors if labels[n] == -1)
            if labels[n_idx] == -1:
                labels[n_idx] = cluster_id
