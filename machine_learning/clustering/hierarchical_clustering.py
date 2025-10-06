import numpy as np
from scipy.spatial.distance import pdist, squareform

# Agglomerative Hierarchical Clustering (Single Linkage)
class AgglomerativeClustering:
    def __init__(self, n_clusters=2):
        self.n_clusters = n_clusters

    def fit(self, X):
        # Number of samples
        n = X.shape[0]
        # Start with each point as its own cluster
        clusters = [[i] for i in range(n)]
        # Compute initial distance matrix
        dists = squareform(pdist(X))
        np.fill_diagonal(dists, np.inf)
        while len(clusters) > self.n_clusters:
            # Find the two closest clusters
            min_dist = np.inf
            to_merge = (None, None)
            for i in range(len(clusters)):
                for j in range(i+1, len(clusters)):
                    # Single linkage: min distance between points in clusters
                    dist = np.min(dists[np.ix_(clusters[i], clusters[j])])
                    if dist < min_dist:
                        min_dist = dist
                        to_merge = (i, j)
            # Merge clusters
            i, j = to_merge
            clusters[i] += clusters[j]
            del clusters[j]
        # Assign cluster labels
        labels = np.zeros(n, dtype=int)
        for idx, cluster in enumerate(clusters):
            for sample in cluster:
                labels[sample] = idx
        self.labels_ = labels
        return self
