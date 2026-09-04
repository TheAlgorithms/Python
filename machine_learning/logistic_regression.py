#!/usr/bin/python3
"""
Implementing Logistic Regression (Binary, One-vs-Rest, and Softmax Multi-class)
from scratch using NumPy.

References:
- Wikipedia: https://en.wikipedia.org/wiki/Logistic_regression
- Coursera Machine Learning Course by Andrew Ng
"""

import numpy as np


def sigmoid_function(z: float | np.ndarray) -> float | np.ndarray:
    """
    Also known as the Logistic Function.

                1
    f(z) =  -------
              1 + e⁻ᶻ

    The sigmoid function approaches a value of 1 as its input 'z' becomes
    increasingly positive, and approaches 0 as it becomes negative.

    @param z: Input scalar or array to the function.
    @returns: Value(s) restricted in the range 0 to 1.

    Examples:
    >>> float(sigmoid_function(4))
    0.9820137900379085
    >>> sigmoid_function(np.array([-3, 3]))
    array([0.04742587, 0.95257413])
    """
    z_clipped = np.clip(z, -500, 500)  # Safe protection against exponent overflow
    return 1 / (1 + np.exp(-z_clipped))


class LogisticRegression:
    """
    A robust Logistic Regression classifier supporting Binary, One-vs-Rest (OVR),
    and Softmax Multi-class classification using Mini-batch Gradient Descent.

    Examples:
    >>> clf = LogisticRegression(learning_rate=0.1, n_epochs=5, multi_class='binary')
    >>> mock_features = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])
    >>> mock_targets = np.array([0, 0, 1, 1])
    >>> _ = clf.fit(mock_features, mock_targets)
    >>> len(clf.predict(mock_features))
    4
    """

    def __init__(
        self,
        learning_rate: float = 0.02,
        n_epochs: int = 200,
        multi_class: str = "binary",
    ) -> None:
        self.learning_rate = learning_rate
        self.epochs = n_epochs
        self.weights: np.ndarray | None = None
        self.bias: float | np.ndarray | None = None
        self.multiclass = multi_class
        self.loss_history: list[float] = []
        self.classifiers: list["LogisticRegression"] | None = None

        if self.multiclass not in ["binary", "ovr", "softmax"]:
            raise ValueError(
                "Incorrect class selection. Choose 'binary', 'ovr', or 'softmax'."
            )

    def _softmax(self, z: np.ndarray) -> np.ndarray:
        """Compute the softmax scaling values for each row of the matrix array."""
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def _one_hot_encode(self, targets: np.ndarray, num_classes: int) -> np.ndarray:
        """Transform numerical class vectors to a structural binary matrix."""
        y_hot_encode = np.zeros((len(targets), num_classes))
        y_hot_encode[np.arange(len(targets)), targets] = 1
        return y_hot_encode

    def _softmax_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute categorical cross-entropy loss metrics."""
        return float(-np.sum(y_true * np.log(y_pred)) / len(y_true))

    def _compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute binary cross-entropy log loss metrics."""
        return float(
            -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        )

    def fit(self, features: np.ndarray, targets: np.ndarray) -> "LogisticRegression":
        """Fit the model weights according to the specified multi_class parameters."""
        samples, total_features = features.shape
        batch_size = 32
        rng = np.random.default_rng()

        if self.multiclass == "binary":
            targets_reshaped = targets.reshape(-1, 1)
            self.weights = rng.standard_normal((total_features, 1)) * 0.01
            self.bias = 0.0

            for _ in range(self.epochs):
                indices = rng.permutation(samples)
                x_shuffled = features[indices]
                y_shuffled = targets_reshaped[indices]

                num_batches = (samples + batch_size - 1) // batch_size
                converged = False

                for i in range(num_batches):
                    start_idx = i * batch_size
                    end_idx = min((i + 1) * batch_size, samples)

                    x_batch = x_shuffled[start_idx:end_idx, :]
                    y_batch = y_shuffled[start_idx:end_idx, :]

                    z = x_batch @ self.weights + self.bias
                    y_pred = np.clip(sigmoid_function(z), 1e-15, 1 - 1e-15)

                    loss = self._compute_loss(y_batch, y_pred)
                    self.loss_history.append(loss)

                    if (
                        len(self.loss_history) > 2
                        and abs(self.loss_history[-1] - self.loss_history[-2]) < 1e-6
                    ):
                        converged = True
                        break

                    up_bias = self.learning_rate * np.mean(y_pred - y_batch)
                    up_weights = (
                        self.learning_rate
                        * (x_batch.T @ (y_pred - y_batch))
                        / len(y_batch)
                    )

                    self.bias -= up_bias
                    self.weights -= up_weights

                if converged:
                    break
            return self

        elif self.multiclass == "ovr":
            self.classifiers = []
            for class_label in np.unique(targets):
                y_bin = np.where(targets == class_label, 1, 0)
                clf = LogisticRegression(
                    learning_rate=self.learning_rate,
                    n_epochs=self.epochs,
                    multi_class="binary",
                )
                clf.fit(features, y_bin)
                self.classifiers.append(clf)
            return self

        elif self.multiclass == "softmax":
            num_classes = len(np.unique(targets))
            self.weights = rng.standard_normal((total_features, num_classes)) * 0.01
            self.bias = np.zeros((1, num_classes))
            y_hot_encode = self._one_hot_encode(targets, num_classes)

            for _ in range(self.epochs):
                indices = rng.permutation(samples)
                x_shuffled = features[indices]
                y_shuffled = y_hot_encode[indices]

                num_batches = (samples + batch_size - 1) // batch_size
                converged = False

                for i in range(num_batches):
                    start_idx = i * batch_size
                    end_idx = min((i + 1) * batch_size, samples)

                    x_batch = x_shuffled[start_idx:end_idx, :]
                    y_batch = y_shuffled[start_idx:end_idx, :]

                    z = x_batch @ self.weights + self.bias
                    y_pred = np.clip(self._softmax(z), 1e-15, 1 - 1e-15)

                    loss = self._softmax_loss(y_batch, y_pred)
                    self.loss_history.append(loss)

                    if (
                        len(self.loss_history) > 2
                        and abs(self.loss_history[-1] - self.loss_history[-2]) < 1e-6
                    ):
                        converged = True
                        break

                    up_bias = self.learning_rate * np.mean(
                        y_pred - y_batch, axis=0, keepdims=True
                    )
                    up_weights = (
                        self.learning_rate
                        * (x_batch.T @ (y_pred - y_batch))
                        / len(y_batch)
                    )

                    self.bias -= up_bias
                    self.weights -= up_weights

                if converged:
                    break
            return self

        return self

    def predict_proba(self, features: np.ndarray) -> np.ndarray:
        """
        Return the calculated matrix vector distributions representing
        class probabilities.
        """
        if self.multiclass == "binary":
            if self.weights is None or self.bias is None:
                raise ValueError("Model must be fitted before calling predict_proba.")
            z = features @ self.weights + self.bias
            return np.asarray(sigmoid_function(z))
        elif self.multiclass == "ovr":
            if self.classifiers is None:
                raise ValueError("Model must be fitted before calling predict_proba.")
            probs = np.column_stack(
                [clf.predict_proba(features) for clf in self.classifiers]
            )
            return probs
        elif self.multiclass == "softmax":
            if self.weights is None or self.bias is None:
                raise ValueError("Model must be fitted before calling predict_proba.")
            z = features @ self.weights + self.bias
            return self._softmax(z)

        return np.array([])

    def predict(self, features: np.ndarray) -> np.ndarray:
        """Return clear label classifications vector maps across test arrays."""
        if self.multiclass == "binary":
            return (self.predict_proba(features) >= 0.5).astype(int).flatten()
        elif self.multiclass in ["ovr", "softmax"]:
            return np.argmax(self.predict_proba(features), axis=1)

        return np.array([])


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Pure NumPy execution logic to ensure external packages like
    # sklearn aren't dependencies
    rng_test = np.random.default_rng(seed=42)
    sample_features = rng_test.standard_normal((100, 4))
    sample_targets = rng_test.choice([0, 1, 2], size=100)

    model = LogisticRegression(learning_rate=0.05, n_epochs=50, multi_class="softmax")
    model.fit(sample_features, sample_targets)
    predictions = model.predict(sample_features)

    print(f"Successfully tracked execution array shape output: {predictions.shape}")
