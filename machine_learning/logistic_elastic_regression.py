from typing import Any, Generator, Tuple

import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
from matplotlib.colors import ListedColormap  # type: ignore
from sklearn.datasets import make_blobs  # type: ignore

Batch = Generator[Tuple[Any, Any], None, None]


def generate_batches(inputs: Any, labels: Any, batch_size: int) -> Batch:
    """
    >>> temp = [2, 3]
    >>> temparr = np.array([1, 2, 3, 4, 5])
    >>> temparr_out = temparr[temp]
    >>> temparr_out
    array([3, 4])
    """
    assert len(inputs) == len(labels)
    np.random.seed(42)
    inputs = np.array(inputs)
    labels = np.array(labels)
    perm = np.random.permutation(len(inputs))
    k = int(len(inputs) / batch_size)
    for i in range(k):
        batch_indx = perm[i * batch_size : (i + 1) * batch_size]
        yield inputs[batch_indx], labels[batch_indx]


def logit(inputs: Any, weights: Any) -> Any:
    """
    >>> logit(1, 3)
    3
    """
    return np.dot(inputs, weights)


def sigmoid(outputs: Any) -> Any:
    """
    >>> sigmoid(0.2)
    0.54...
    """
    return 1.0 / (1 + np.exp(-outputs))


class MyElasticLogisticRegression(object):
    """
    Elastic net is a regularized regression method that
    linearly combines the L1 and L2 penalties
    of the lasso and ridge methods.

    More at Wikipedia:
    https://en.wikipedia.org/wiki/Elastic_net_regularization
    """

    def __init__(self, l1_coef: float, l2_coef: float) -> None:
        self.l1_coef = l1_coef
        self.l2_coef = l2_coef
        self.w = None

    def fit(
        self,
        inputs: Any,
        labels: Any,
        epochs: int = 10,
        lr: float = 0.1,
        batch_size: int = 100,
    ) -> list[float]:
        """
        >>> from sklearn.datasets import make_blobs
        >>> X, y = make_blobs(n_samples=10,
        >>>                   centers=[[-2,0.5],[3,-0.5]],
        >>>                   cluster_std=1,
        >>>                   random_state=42)
        >>> clf = MyElasticLogisticRegression(0.1, 0.1)
        >>> losses = clf.fit(X, y, epochs=1, batch_size=5)
        >>> losses
        [1.48..., 0.96...]
        """
        n, k = inputs.shape
        if self.w is None:
            np.random.seed(42)
            self.w = np.random.randn(k + 1)

        x_train = np.concatenate((np.ones((n, 1)), inputs), axis=1)

        losses = []

        # Train loop
        for _ in range(epochs):
            gen = generate_batches
            for x_batch, y_batch in gen(x_train, labels, batch_size):
                y_pred = sigmoid(logit(x_batch, self.w))

                n, k = x_batch.shape
                w0 = self.w.copy()
                w0[0] = 0
                grad = x_batch.T @ (y_pred - y_batch) / n
                grad += self.l1_coef * np.sign(w0)
                grad += 2 * self.l2_coef * w0
                self.w -= grad * lr

                losses.append(self.loss(y_batch, y_pred))

        return losses

    def predict_proba(self, inputs: Any) -> Any:
        """
        >>> from sklearn.datasets import load_iris
        >>> from sklearn.linear_model import LogisticRegression
        >>> X, y = load_iris(return_X_y=True)
        >>> clf = LogisticRegression(random_state=0).fit(X, y)
        >>> clf.predict(X[:2, :])
        array([0, 0])
        >>> clf.predict_proba(X[:2, :])
        array([[9.8...e-01, 1.8...e-02, 1.4...e-08],
            [9.7...e-01, 2.8...e-02, ...e-08]])
        """
        n, k = inputs.shape
        inputs_modified = np.concatenate((np.ones((n, 1)), inputs), axis=1)
        return sigmoid(logit(inputs_modified, self.w))

    def predict(self, inputs: Any, threshold: float = 0.5) -> Any:
        """
        >>> from sklearn.datasets import load_iris
        >>> from sklearn.linear_model import LogisticRegression
        >>> X, y = load_iris(return_X_y=True)
        >>> clf = LogisticRegression(random_state=0).fit(X, y)
        >>> clf.predict(X[:2, :])
        array([0, 0])
        """
        return self.predict_proba(inputs) >= threshold

    def get_weights(self) -> Any:
        """
        >>> from sklearn.model_selection import train_test_split
        >>> def linear_expression(x):
        >>>     return 5 * x + 6
        >>> objects_num = 50
        >>> X = np.linspace(-5, 5, objects_num)
        >>> y = linear_expression(X) + np.random.randn(objects_num) * 5
        >>> X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)
        >>> regressor = MyElasticLogisticRegression()
        >>> regressor.fit(X_train[:, np.newaxis], y_train)
        >>> predictions = regressor.predict(X_test[:, np.newaxis])
        >>> w = regressor.get_weights()
        >>> w
        array([4.7..., 5.7...])
        """
        return self.w

    def loss(self, labels: Any, predictions: Any) -> float:
        """
        >>> from sklearn.datasets import make_blobs
        >>> X, y = make_blobs(n_samples=10,
        >>>                   centers=[[-2,0.5],[3,-0.5]],
        >>>                   cluster_std=1,
        >>>                   random_state=42)
        >>> clf = MyElasticLogisticRegression(0.1, 0.1)
        >>> losses = clf.fit(X, y, epochs=1, batch_size=5)
        >>> y_pred = clf.predict_proba(X)
        >>> loss = clf.loss(y, y_pred)
        >>> loss
        0.87...
        """
        predictions = np.clip(predictions, 1e-10, 1 - 1e-10)
        return -np.mean(
            labels * np.log(predictions) + (1 - labels) * np.log(1 - predictions)
        )


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
