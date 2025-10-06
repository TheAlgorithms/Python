import numpy as np

# Mean Shift Clustering
class MeanShift:
    def __init__(self, bandwidth=1.0, max_iter=300):
        self.bandwidth = bandwidth
        self.max_iter = max_iter

    def fit(self, X):
        X = np.asarray(X)
        n_samples, n_features = X.shape
        # Initialize centroids to all points
        centroids = X.copy()
        for _ in range(self.max_iter):
            for i in range(n_samples):
                # Find points within bandwidth
                distances = np.linalg.norm(X - centroids[i], axis=1)
                in_bandwidth = X[distances < self.bandwidth]
                # Update centroid to mean of points in bandwidth
                if len(in_bandwidth) > 0:
                    centroids[i] = np.mean(in_bandwidth, axis=0)
        # Remove duplicates (merge close centroids)
        unique = []
        for c in centroids:
            if not any(np.linalg.norm(c - u) < 1e-2 for u in unique):
                unique.append(c)
        self.cluster_centers_ = np.array(unique)
        # Assign labels
        labels = np.zeros(n_samples, dtype=int)
        for i, x in enumerate(X):
            labels[i] = np.argmin([np.linalg.norm(x - center) for center in self.cluster_centers_])
        self.labels_ = labels
        return self
