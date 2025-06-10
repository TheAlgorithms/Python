import numpy as np
from sklearn.cluster import KMeans
from numpy.linalg import pinv


class RBFNN:
    def __init__(self, num_centers=10, gamma=1.0):
        self.num_centers = num_centers
        self.gamma = gamma
        self.centers = None
        self.weights = None

    def _rbf(self, x, center):
        return np.exp(-self.gamma * np.linalg.norm(x - center) ** 2)

    def _compute_activations(self, X):
        G = np.zeros((X.shape[0], self.num_centers))
        for i, x in enumerate(X):
            for j, c in enumerate(self.centers):
                G[i, j] = self._rbf(x, c)
        return G

    def train(self, X, y):
        kmeans = KMeans(n_clusters=self.num_centers, random_state=0).fit(X)
        self.centers = kmeans.cluster_centers_
        G = self._compute_activations(X)
        self.weights = pinv(G).dot(y)

    def predict(self, X):
        G = self._compute_activations(X)
        return G.dot(self.weights)
