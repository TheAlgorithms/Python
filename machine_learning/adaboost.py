"""
AdaBoost implementation for binary classification using decision stumps.

Reference: https://en.wikipedia.org/wiki/AdaBoost

>>> import numpy as np
>>> features = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
>>> labels = np.array([0, 1, 1, 0])
>>> clf = AdaBoost(n_estimators=5)
>>> clf.fit(features, labels)
>>> clf.predict(np.array([[0, 0], [1, 1]]))
array([0, 1])
"""

import numpy as np
from typing import Any


class AdaBoost:
    def __init__(self, n_estimators: int = 50) -> None:
        """Initialize AdaBoost classifier.
        Args:
            n_estimators: Number of boosting rounds.
        """
        self.n_estimators: int = n_estimators
        self.alphas: list[float] = []  # Weights for each weak learner
        self.models: list[dict[str, Any]] = []  # List of weak learners (stumps)

    def fit(self, feature_matrix: np.ndarray, target: np.ndarray) -> None:
        """Fit AdaBoost model.
        Args:
            feature_matrix: (n_samples, n_features) feature matrix
            target: (n_samples,) labels (0 or 1)
        """
        n_samples, _ = feature_matrix.shape
        sample_weights = np.ones(n_samples) / n_samples
        self.models = []
        self.alphas = []
        y_signed = np.where(target == 0, -1, 1)
        for _ in range(self.n_estimators):
            stump = self._build_stump(feature_matrix, y_signed, sample_weights)
            pred = stump["pred"]
            err = stump["error"]
            alpha = 0.5 * np.log((1 - err) / (err + 1e-10))
            sample_weights *= np.exp(-alpha * y_signed * pred)
            sample_weights /= np.sum(sample_weights)
            self.models.append(stump)
            self.alphas.append(alpha)

    def predict(self, feature_matrix: np.ndarray) -> np.ndarray:
        """Predict class labels for samples in feature_matrix.
        Args:
            feature_matrix: (n_samples, n_features) feature matrix
        Returns:
            (n_samples,) predicted labels (0 or 1)
        """
        clf_preds = np.zeros(feature_matrix.shape[0])
        for alpha, stump in zip(self.alphas, self.models):
            pred = self._stump_predict(
                feature_matrix, stump["feature"], stump["threshold"], stump["polarity"]
            )
            clf_preds += alpha * pred
        return np.where(clf_preds >= 0, 1, 0)

    def _build_stump(
        self,
        feature_matrix: np.ndarray,
        target_signed: np.ndarray,
        sample_weights: np.ndarray,
    ) -> dict[str, Any]:
        """Find the best decision stump for current weights."""
        _, n_features = feature_matrix.shape
        min_error = float("inf")
        best_stump: dict[str, Any] = {}
        for feature in range(n_features):
            thresholds = np.unique(feature_matrix[:, feature])
            for threshold in thresholds:
                for polarity in [1, -1]:
                    pred = self._stump_predict(feature_matrix, feature, threshold, polarity)
                    error = np.sum(sample_weights * (pred != target_signed))
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
        self, feature_matrix: np.ndarray, feature: int, threshold: float, polarity: int
    ) -> np.ndarray:
        """Predict using a single decision stump."""
        pred = np.ones(feature_matrix.shape[0])
        if polarity == 1:
            pred[feature_matrix[:, feature] < threshold] = -1
        else:
            pred[feature_matrix[:, feature] > threshold] = -1
        return pred