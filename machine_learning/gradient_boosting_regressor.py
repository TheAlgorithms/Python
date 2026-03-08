"""Gradient Boosting regressor from scratch using decision stumps."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean

from machine_learning.random_forest_regressor import DecisionStumpRegressor


@dataclass(frozen=True)
class BoostedStump:
    """A weak learner weighted by a learning rate."""

    stump: DecisionStumpRegressor
    weight: float

    def predict(self, row: list[float]) -> float:
        return self.weight * self.stump.predict(row)


class GradientBoostingRegressor:
    """A minimal gradient boosting regressor.

    Examples:
        >>> x = [[0.0], [1.0], [2.0], [3.0], [4.0]]
        >>> y = [0.0, 1.0, 2.0, 3.0, 4.0]
        >>> model = GradientBoostingRegressor(num_estimators=20, learning_rate=0.1)
        >>> model.fit(x, y)
        >>> preds = model.predict([[0.2], [3.8]])
        >>> len(preds) == 2 and preds[0] < preds[1]
        True
    """

    def __init__(self, num_estimators: int = 50, learning_rate: float = 0.1) -> None:
        if num_estimators <= 0:
            raise ValueError("num_estimators must be positive")
        if learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        self.num_estimators = num_estimators
        self.learning_rate = learning_rate
        self.base_prediction: float = 0.0
        self.models: list[BoostedStump] = []

    def fit(self, features: list[list[float]], targets: list[float]) -> None:
        if not features or not targets:
            raise ValueError("features and targets must be non-empty")
        if len(features) != len(targets):
            raise ValueError("features and targets must have same length")

        self.base_prediction = mean(targets)
        predictions = [self.base_prediction] * len(targets)
        self.models = []

        for _ in range(self.num_estimators):
            residuals = [target - pred for target, pred in zip(targets, predictions)]
            stump = _fit_residual_stump(features, residuals)
            boosted = BoostedStump(stump=stump, weight=self.learning_rate)
            self.models.append(boosted)
            predictions = [
                pred + boosted.predict(row) for pred, row in zip(predictions, features)
            ]

    def predict(self, features: list[list[float]]) -> list[float]:
        if not self.models and self.base_prediction == 0.0:
            raise ValueError("model must be fitted before predict")

        outputs = [self.base_prediction for _ in features]
        for model in self.models:
            outputs = [
                current + model.predict(row) for current, row in zip(outputs, features)
            ]
        return outputs


def _fit_residual_stump(
    features: list[list[float]], residuals: list[float]
) -> DecisionStumpRegressor:
    # Single-feature support is enough for an educational weak learner.
    feature_index = 0
    thresholds = sorted({row[feature_index] for row in features})

    best: DecisionStumpRegressor | None = None
    best_error = float("inf")

    for threshold in thresholds:
        left = [
            res
            for row, res in zip(features, residuals)
            if row[feature_index] <= threshold
        ]
        right = [
            res
            for row, res in zip(features, residuals)
            if row[feature_index] > threshold
        ]
        if not left or not right:
            continue

        left_mean = mean(left)
        right_mean = mean(right)
        error = sum(
            ((left_mean if row[feature_index] <= threshold else right_mean) - residual)
            ** 2
            for row, residual in zip(features, residuals)
        )
        if error < best_error:
            best_error = error
            best = DecisionStumpRegressor(
                feature_index, threshold, left_mean, right_mean
            )

    if best is None:
        baseline = mean(residuals)
        return DecisionStumpRegressor(0, features[0][0], baseline, baseline)
    return best


if __name__ == "__main__":
    import doctest

    doctest.testmod()
