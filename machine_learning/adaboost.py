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

from typing import Any

import numpy as np


class AdaBoost:
    def __init__(self, n_estimators: int = 50) -> None:
        """
        Initialize AdaBoost classifier.

        Args:
            n_estimators: Number of boosting rounds (weak learners).
        """
        self.n_estimators: int = n_estimators
        self.alphas: list[float] = []  # Weights assigned to each weak learner
        self.models: list[dict[str, Any]] = []  # Stores each decision stump

    def fit(self, feature_matrix: np.ndarray, target: np.ndarray) -> None:
        """
        Train AdaBoost model using decision stumps.

        Args:
            feature_matrix: 2D array of shape (n_samples, n_features)
            target: 1D array of binary labels (0 or 1)
        """
        n_samples, _ = feature_matrix.shape

        # Initialize uniform sample weights
        sample_weights = np.ones(n_samples) / n_samples

        # Reset model state
        self.models = []
        self.alphas = []

        # Convert labels to {-1, 1} for boosting
        y_signed = np.where(target == 0, -1, 1)

        for _ in range(self.n_estimators):
            # Train a weighted decision stump
            stump = self._build_stump(feature_matrix, y_signed, sample_weights)
            pred = stump["pred"]
            err = stump["error"]

            # Compute alpha (learner weight) with numerical stability
            alpha = 0.5 * np.log((1 - err) / (err + 1e-10))

            # Update sample weights to focus on misclassified points
            sample_weights *= np.exp(-alpha * y_signed * pred)
            sample_weights /= np.sum(sample_weights)

            # Store the stump and its weight
            self.models.append(stump)
            self.alphas.append(alpha)

    def predict(self, feature_matrix: np.ndarray) -> np.ndarray:
        """
        Predict binary class labels for input samples.

        Args:
            feature_matrix: 2D array of shape (n_samples, n_features)

        Returns:
            1D array of predicted labels (0 or 1)
        """
        clf_preds = np.zeros(feature_matrix.shape[0])

        # Aggregate predictions from all stumps
        for alpha, stump in zip(self.alphas, self.models):
            pred = self._stump_predict(
                feature_matrix,
                stump["feature"],
                stump["threshold"],
                stump["polarity"],
            )
            clf_preds += alpha * pred

        # Final prediction: sign of weighted sum
        return np.where(clf_preds >= 0, 1, 0)

    def _build_stump(
        self,
        feature_matrix: np.ndarray,
        target_signed: np.ndarray,
        sample_weights: np.ndarray,
    ) -> dict[str, Any]:
        """
        Build the best decision stump for current sample weights.

        Returns:
            Dictionary containing stump parameters and predictions.
        """
        _, n_features = feature_matrix.shape
        min_error = float("inf")
        best_stump: dict[str, Any] = {}

        # Iterate over all features and thresholds
        for feature in range(n_features):
            thresholds = np.unique(feature_matrix[:, feature])
            for threshold in thresholds:
                for polarity in [1, -1]:
                    pred = self._stump_predict(
                        feature_matrix,
                        feature,
                        threshold,
                        polarity,
                    )
                    error = np.sum(sample_weights * (pred != target_signed))

                    # Keep stump with lowest weighted error
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
        self,
        feature_matrix: np.ndarray,
        feature: int,
        threshold: float,
        polarity: int,
    ) -> np.ndarray:
        """
        Predict using a single decision stump.

        Returns:
            1D array of predictions in {-1, 1}
        """
        pred = np.ones(feature_matrix.shape[0])

        # Apply polarity to threshold comparison
        if polarity == 1:
            pred[feature_matrix[:, feature] < threshold] = -1
        else:
            pred[feature_matrix[:, feature] > threshold] = -1

        return pred
