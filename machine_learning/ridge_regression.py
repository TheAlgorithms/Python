"""Ridge Regression (L2 regularization) implemented with batch gradient descent.

This module provides a small, well-tested `RidgeRegression` class that is
compatible with the existing `linear_regression` demo dataset (ADR vs Rating).

Features:
- Bias (intercept) handled automatically unless the caller provides an
  already-augmented feature matrix.
- L2 regularization that excludes the bias term.
- `mean_absolute_error` utility and a small `main()` demo that fetches the
  CSGO ADR vs Rating CSV used elsewhere in the repository.

Examples
--------
>>> import numpy as np
>>> x = np.array([[1.0], [2.0], [3.0]])
>>> y = np.array([2.0, 4.0, 6.0])
>>> model = RidgeRegression(learning_rate=0.1, lambda_=0.0, epochs=2000)
>>> model.fit(x, y)
>>> np.allclose(model.weights, [0.0, 2.0], atol=1e-2)
True
>>> model.predict(np.array([[4.0], [5.0]]))
array([ 8., 10.])
"""

from __future__ import annotations

from dataclasses import dataclass

import httpx
import numpy as np


@dataclass
class RidgeRegression:
    """Ridge Regression using batch gradient descent.

    Parameters
    ----------
    learning_rate: float
        Step size for gradient descent (must be > 0).
    lambda_: float
        L2 regularization strength (must be >= 0). Regularization is NOT
        applied to the bias (intercept) term.
    epochs: int
        Number of gradient descent iterations (must be > 0).
    """

    learning_rate: float = 0.01
    lambda_: float = 0.1
    epochs: int = 1000
    weights: np.ndarray | None = None

    def __post_init__(self) -> None:
        if self.learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        if self.lambda_ < 0:
            raise ValueError("lambda_ must be non-negative")
        if self.epochs <= 0:
            raise ValueError("epochs must be positive")

    @staticmethod
    def _add_intercept(features: np.ndarray) -> np.ndarray:
        arr = np.asarray(features, dtype=float)
        if arr.ndim != 2:
            raise ValueError("features must be a 2D array")
        n_samples = arr.shape[0]
        return np.c_[np.ones(n_samples), arr]

    def fit(
        self, features: np.ndarray, target: np.ndarray, add_intercept: bool = True
    ) -> None:
        """Train the ridge regression model.

        Parameters
        ----------
        features: np.ndarray
            2D array (n_samples, n_features)
        target: np.ndarray
            1D array (n_samples,)
        add_intercept: bool
            If True the model will add a bias column of ones to `features`.
        """
        features = np.asarray(features, dtype=float)
        target = np.asarray(target, dtype=float)

        if features.ndim != 2:
            raise ValueError("features must be a 2D array")
        if target.ndim != 1:
            raise ValueError("target must be a 1D array")
        if features.shape[0] != target.shape[0]:
            raise ValueError("Number of samples must match")

        x = features if not add_intercept else self._add_intercept(features)
        n_samples, n_features = x.shape

        # initialize weights (including bias as weights[0])
        self.weights = np.zeros(n_features)

        for _ in range(self.epochs):
            preds = x @ self.weights
            errors = preds - target

            # gradient without regularization
            grad = (x.T @ errors) / n_samples

            # add L2 regularization term (do not regularize bias term)
            reg = np.concatenate(([0.0], 2 * self.lambda_ * self.weights[1:]))
            grad += reg

            self.weights -= self.learning_rate * grad

    def predict(self, features: np.ndarray, add_intercept: bool = True) -> np.ndarray:
        """Predict target values for `features`.

        Parameters
        ----------
        features: np.ndarray
            2D array (n_samples, n_features)
        add_intercept: bool
            If True, add bias column to features before prediction.
        """
        if self.weights is None:
            raise ValueError("Model is not trained")

        features = np.asarray(features, dtype=float)
        x = features if not add_intercept else self._add_intercept(features)
        return x @ self.weights


def mean_absolute_error(predicted: np.ndarray, actual: np.ndarray) -> float:
    """Return mean absolute error between two 1D arrays."""
    predicted = np.asarray(predicted)
    actual = np.asarray(actual)
    if predicted.shape != actual.shape:
        raise ValueError("predicted and actual must have the same shape")
    return float(np.mean(np.abs(predicted - actual)))


def collect_dataset() -> np.matrix:
    """Fetch the ADR vs Rating CSV used in the repo's linear regression demo."""
    response = httpx.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    lines = response.text.splitlines()
    data = [line.split(",") for line in lines]
    data.pop(0)
    return np.matrix(data)


def main() -> None:
    data = collect_dataset()

    # features and target (same layout as linear_regression.py)
    x = np.c_[data[:, 0].astype(float)]
    y = np.ravel(data[:, 1].astype(float))

    model = RidgeRegression(learning_rate=0.0002, lambda_=0.01, epochs=50000)
    model.fit(x, y)

    preds = model.predict(x)
    mae = mean_absolute_error(preds, y)

    print("Learned weights:")
    assert model.weights is not None
    for i, w in enumerate(model.weights):
        print(f"w[{i}] = {w:.6f}")
    print(f"MAE on training data: {mae:.6f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
