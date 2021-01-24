import numpy as np  # type: ignore
from sklearn.datasets import make_blobs # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.colors import ListedColormap # type: ignore

from typing import Any, Tuple, Generator


def generate_batches(X: Any, y: Any, batch_size: int) -> Generator[Tuple[Any, Any], None, None]:
    assert len(X) == len(y)
    np.random.seed(42)
    X = np.array(X)
    y = np.array(y)
    perm = np.random.permutation(len(X))
    k = int(len(X) / batch_size)
    for i in range(k):
        batch_indx = perm[i * batch_size : (i + 1) * batch_size]
        yield X[batch_indx], y[batch_indx]


def logit(x: Any, w: Any):
    return np.dot(x, w)


def sigmoid(h: Any) -> Any:
    return 1.0 / (1 + np.exp(-h))


class MyElasticLogisticRegression(object):
    """
    Elastic net is a regularized regression method that
    linearly combines the L1 and L2 penalties
    of the lasso and ridge methods.

    More at Wikipedia:
    https://en.wikipedia.org/wiki/Elastic_net_regularization
    
    Original paper:
    https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.124.4696
    """

    def __init__(self, l1_coef, l2_coef):
        self.l1_coef = l1_coef
        self.l2_coef = l2_coef
        self.w = None

    def fit(self, X, y, epochs=10, lr=0.1, batch_size=100):
        n, k = X.shape
        if self.w is None:
            np.random.seed(42)
            self.w = np.random.randn(k + 1)

        X_train = np.concatenate((np.ones((n, 1)), X), axis=1)

        losses = []

        # Train loop
        for _ in range(epochs):
            gen = generate_batches
            for X_batch, y_batch in gen(X_train, y, batch_size):
                y_pred = sigmoid(logit(X_batch, self.w))

                grad = self.get_grad(X_batch, y_batch, y_pred)
                self.w -= grad * lr

                losses.append(self.__loss(y_batch, y_pred))

        return losses

    def get_grad(self, X_batch, y_batch, predictions):
        """
        Accepts X_batch with ones column. 
        """

        n, k = X_batch.shape
        w0 = self.w.copy()
        w0[0] = 0
        grad = X_batch.T @ (predictions - y_batch) / n
        grad += self.l1_coef * np.sign(w0)
        grad += 2 * self.l2_coef * w0

        return grad

    def predict_proba(self, X):
        n, k = X.shape
        X_ = np.concatenate((np.ones((n, 1)), X), axis=1)
        return sigmoid(logit(X_, self.w))

    def predict(self, X, threshold=0.5):
        return self.predict_proba(X) >= threshold

    def get_weights(self):
        return self.w

    def __loss(self, y, p):
        p = np.clip(p, 1e-10, 1 - 1e-10)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))


if __name__ == "__main__":
    X, y = make_blobs(
        n_samples=1000, centers=[[-2, 0.5], [3, -0.5]], cluster_std=1, random_state=42
    )

    colors = ("red", "green")
    colored_y = np.zeros(y.size, dtype=str)

    for i, cl in enumerate([0, 1]):
        colored_y[y == cl] = str(colors[i])

    plt.figure(figsize=(15, 10))
    plt.scatter(X[:, 0], X[:, 1], c=colored_y)
    plt.show()

    clf = MyElasticLogisticRegression(0.1, 0.1)
    clf.fit(X, y, epochs=1000, batch_size=100)
    w = clf.get_weights()

    eps = 0.1
    xx, yy = np.meshgrid(
        np.linspace(np.min(X[:, 0]) - eps, np.max(X[:, 0]) + eps, 200),
        np.linspace(np.min(X[:, 1]) - eps, np.max(X[:, 1]) + eps, 200),
    )
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA"])
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light, shading="auto")

    plt.scatter(X[:, 0], X[:, 1], c=colored_y)

