import numpy as np

# K-Medoids Clustering (Partitioning Around Medoids)
class KMedoids:
    def __init__(self, n_clusters=3, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        X = np.asarray(X)
        n_samples = X.shape[0]
        # Randomly initialize medoids
        medoid_indices = np.random.choice(n_samples, self.n_clusters, replace=False)
        medoids = X[medoid_indices]
        for _ in range(self.max_iter):
            # Assign each point to the nearest medoid
            labels = np.argmin(np.linalg.norm(X[:, None] - medoids, axis=2), axis=1)
            new_medoids = np.copy(medoids)
            for i in range(self.n_clusters):
                cluster_points = X[labels == i]
                if len(cluster_points) == 0:
                    continue
                # Find the point minimizing total distance to others
                distances = np.sum(np.linalg.norm(cluster_points[:, None] - cluster_points, axis=2), axis=1)
                new_medoids[i] = cluster_points[np.argmin(distances)]
            if np.allclose(medoids, new_medoids):
                break
            medoids = new_medoids
        self.medoids_ = medoids
        self.labels_ = np.argmin(np.linalg.norm(X[:, None] - medoids, axis=2), axis=1)
        return self
