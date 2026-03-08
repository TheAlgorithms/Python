"""Gaussian Naive Bayes classifier implemented from scratch.

This module provides a compact educational implementation of Gaussian
Naive Bayes for multi-class classification without external dependencies.
"""

from __future__ import annotations

import math
from collections import defaultdict


class GaussianNaiveBayes:
    """A simple Gaussian Naive Bayes classifier.

    The model estimates per-class means and variances for each feature and
    uses Bayes' theorem under the naive conditional-independence assumption.

    Examples:
        >>> x_train = [[1.0, 20.0], [2.0, 21.0], [8.0, 3.0], [9.0, 2.0]]
        >>> y_train = [0, 0, 1, 1]
        >>> model = GaussianNaiveBayes().fit(x_train, y_train)
        >>> model.predict([[1.5, 19.0], [8.5, 2.5]])
        [0, 1]
    """

    def __init__(self) -> None:
        self.class_priors: dict[int, float] = {}
        self.class_feature_means: dict[int, list[float]] = {}
        self.class_feature_variances: dict[int, list[float]] = {}

    def fit(self, features: list[list[float]], labels: list[int]) -> GaussianNaiveBayes:
        """Fit the classifier to training data.

        Args:
            features: Training matrix of shape ``(n_samples, n_features)``.
            labels: Class labels of shape ``(n_samples,)``.

        Returns:
            The fitted classifier instance.

        Raises:
            ValueError: If input lengths are invalid or features are inconsistent.
        """
        if not features or not labels:
            raise ValueError("features and labels must be non-empty")
        if len(features) != len(labels):
            raise ValueError("features and labels must have the same length")

        feature_count = len(features[0])
        if feature_count == 0:
            raise ValueError("each sample must contain at least one feature")
        if any(len(row) != feature_count for row in features):
            raise ValueError("all feature rows must have the same length")

        grouped: dict[int, list[list[float]]] = defaultdict(list)
        for row, label in zip(features, labels):
            grouped[label].append(row)

        total_samples = len(features)
        epsilon = 1e-9  # Avoid divide-by-zero for constant features.

        for label, rows in grouped.items():
            self.class_priors[label] = len(rows) / total_samples
            means = []
            variances = []
            for index in range(feature_count):
                column = [row[index] for row in rows]
                mean = sum(column) / len(column)
                variance = sum((value - mean) ** 2 for value in column) / len(column)
                means.append(mean)
                variances.append(max(variance, epsilon))

            self.class_feature_means[label] = means
            self.class_feature_variances[label] = variances

        return self

    def _class_log_probability(self, sample: list[float], label: int) -> float:
        log_prob = math.log(self.class_priors[label])
        means = self.class_feature_means[label]
        variances = self.class_feature_variances[label]

        for value, mean, variance in zip(sample, means, variances):
            log_prob += -0.5 * math.log(2.0 * math.pi * variance)
            log_prob += -((value - mean) ** 2) / (2.0 * variance)
        return log_prob

    def predict(self, features: list[list[float]]) -> list[int]:
        """Predict labels for given feature rows.

        Raises:
            ValueError: If model is not fitted or row widths are invalid.
        """
        if not self.class_priors:
            raise ValueError("the model must be fitted before prediction")
        if not features:
            return []

        expected_width = len(next(iter(self.class_feature_means.values())))
        if any(len(row) != expected_width for row in features):
            raise ValueError("feature width does not match fitted model")

        classes = list(self.class_priors)
        predictions: list[int] = []
        for row in features:
            best_label = max(
                classes,
                key=lambda label: self._class_log_probability(row, label),
            )
            predictions.append(best_label)

        return predictions


if __name__ == "__main__":
    import doctest

    doctest.testmod()
