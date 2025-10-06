"""
AdaBoost implementation for binary classification using decision stumps.

Reference: https://en.wikipedia.org/wiki/AdaBoost

>>> import numpy as np
>>> X = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
>>> y = np.array([0, 1, 1, 0])
>>> clf = AdaBoost(n_estimators=5)
>>> clf.fit(X, y)
>>> clf.predict(np.array([[0, 0], [1, 1]]))
array([0, 1])
"""

import numpy as np
from typing import Any, Dict, List


class AdaBoost:
    def __init__(self, n_estimators: int = 50) -> None:
        """Initialize AdaBoost classifier.
        Args:
            n_estimators: Number of boosting rounds.
        """
        self.n_estimators: int = n_estimators
        self.alphas: List[float] = []  # Weights for each weak learner
        self.models: List[Dict[str, Any]] = []  # List of weak learners (stumps)

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """Fit AdaBoost model.
        Args:
            X: (n_samples, n_features) feature matrix
            y: (n_samples,) labels (0 or 1)
        """
        n_samples, n_features = X.shape
        w = np.ones(n_samples) / n_samples  # Initialize sample weights
        self.models = []
        self.alphas = []
        y_ = np.where(y == 0, -1, 1)  # Convert labels to -1, 1
        for _ in range(self.n_estimators):
            # Train a decision stump with weighted samples
            stump = self._build_stump(X, y_, w)
            pred = stump["pred"]
            err = stump["error"]
            # Compute alpha (learner weight)
            alpha = 0.5 * np.log((1 - err) / (err + 1e-10))
            # Update sample weights
            w *= np.exp(-alpha * y_ * pred)
            w /= np.sum(w)
            self.models.append(stump)
            self.alphas.append(alpha)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict class labels for samples in X.
        Args:
            X: (n_samples, n_features) feature matrix
        Returns:
            (n_samples,) predicted labels (0 or 1)
        >>> import numpy as np
        >>> X = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
        >>> y = np.array([0, 1, 1, 0])
        >>> clf = AdaBoost(n_estimators=5)
        >>> clf.fit(X, y)
        >>> clf.predict(np.array([[0, 0], [1, 1]]))
        array([0, 1])
        """
        clf_preds = np.zeros(X.shape[0])
        for alpha, stump in zip(self.alphas, self.models):
            pred = self._stump_predict(
                X, stump["feature"], stump["threshold"], stump["polarity"]
            )
            clf_preds += alpha * pred
        return np.where(clf_preds >= 0, 1, 0)

    def _build_stump(
        self, X: np.ndarray, y: np.ndarray, w: np.ndarray
    ) -> Dict[str, Any]:
        """Find the best decision stump for current weights."""
        n_samples, n_features = X.shape
        min_error = float("inf")
        best_stump: Dict[str, Any] = {}
        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                for polarity in [1, -1]:
                    pred = self._stump_predict(X, feature, threshold, polarity)
                    error = np.sum(w * (pred != y))
                    if error < min_error:
                        min_error = error
                        best_stump = {
                            "feature": feature,
                            "threshold": threshold,
                            "polarity": polarity,
                            "error": error,
                            "pred": pred.copy(),
                        }
        return best_stump

    def _stump_predict(
        self, X: np.ndarray, feature: int, threshold: float, polarity: int
    ) -> np.ndarray:
        """Predict using a single decision stump."""
        pred = np.ones(X.shape[0])
        if polarity == 1:
            pred[X[:, feature] < threshold] = -1
        else:
            pred[X[:, feature] > threshold] = -1
        return pred
