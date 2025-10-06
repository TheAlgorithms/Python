import numpy as np

# Single-layer Perceptron for binary classification
class Perceptron:
    def __init__(self, n_features, lr=0.01, n_iter=1000):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = np.zeros(n_features)
        self.bias = 0

    def fit(self, X, y):
        # X: (n_samples, n_features), y: (n_samples,)
        for _ in range(self.n_iter):
            for xi, target in zip(X, y):
                update = self.lr * (target - self.predict(xi))
                self.weights += update * xi
                self.bias += update

    def predict(self, X):
        # X: (n_features,) or (n_samples, n_features)
        linear = np.dot(X, self.weights) + self.bias
        return np.where(linear >= 0, 1, 0)
