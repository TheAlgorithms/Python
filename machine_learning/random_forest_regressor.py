"""Random Forest regressor from scratch.

This simplified random forest regressor is based on bagged decision stumps.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class DecisionStumpRegressor:
    """A one-level regression tree."""

    feature_index: int
    threshold: float
    left_value: float
    right_value: float

    def predict(self, row: list[float]) -> float:
        return (
            self.left_value
            if row[self.feature_index] <= self.threshold
            else self.right_value
        )


class RandomForestRegressor:
    """Small educational random forest regressor.

    Examples:
        >>> x = [[0.0], [1.0], [2.0], [3.0], [4.0]]
        >>> y = [0.0, 1.0, 2.0, 3.0, 4.0]
        >>> model = RandomForestRegressor(num_trees=9, random_seed=0)
        >>> model.fit(x, y)
        >>> preds = model.predict([[0.2], [3.8]])
        >>> len(preds) == 2 and preds[0] < preds[1]
        True
    """

    def __init__(
        self,
        num_trees: int = 25,
        max_features: int | None = None,
        random_seed: int = 0,
    ) -> None:
        if num_trees <= 0:
            raise ValueError("num_trees must be positive")
        self.num_trees = num_trees
        self.max_features = max_features
        self.random_seed = random_seed
        self._trees: list[DecisionStumpRegressor] = []

    def fit(self, features: list[list[float]], targets: list[float]) -> None:
        if not features or not targets:
            raise ValueError("features and targets must be non-empty")
        if len(features) != len(targets):
            raise ValueError("features and targets must have same length")

        width = len(features[0])
        if width == 0 or any(len(row) != width for row in features):
            raise ValueError("all rows must have same non-zero width")

        rng = random.Random(self.random_seed)
        feature_budget = self.max_features or max(1, int(width**0.5))
        feature_budget = min(feature_budget, width)

        self._trees = []
        for _ in range(self.num_trees):
            sample_indexes = [
                rng.randrange(len(features)) for _ in range(len(features))
            ]
            sampled_x = [features[index] for index in sample_indexes]
            sampled_y = [targets[index] for index in sample_indexes]

            candidate_features = rng.sample(range(width), k=feature_budget)
            stump = _best_stump_regressor(sampled_x, sampled_y, candidate_features)
            self._trees.append(stump)

    def predict(self, features: list[list[float]]) -> list[float]:
        if not self._trees:
            raise ValueError("model must be fitted before predict")
        return [mean(tree.predict(row) for tree in self._trees) for row in features]


def _best_stump_regressor(
    features: list[list[float]],
    targets: list[float],
    candidate_features: list[int],
) -> DecisionStumpRegressor:
    best_stump: DecisionStumpRegressor | None = None
    best_error = float("inf")

    for feature_index in candidate_features:
        thresholds = sorted({row[feature_index] for row in features})
        for threshold in thresholds:
            left_targets = [
                target
                for row, target in zip(features, targets)
                if row[feature_index] <= threshold
            ]
            right_targets = [
                target
                for row, target in zip(features, targets)
                if row[feature_index] > threshold
            ]
            if not left_targets or not right_targets:
                continue

            left_mean = mean(left_targets)
            right_mean = mean(right_targets)
            squared_error = sum(
                (
                    (left_mean if row[feature_index] <= threshold else right_mean)
                    - target
                )
                ** 2
                for row, target in zip(features, targets)
            )
            if squared_error < best_error:
                best_error = squared_error
                best_stump = DecisionStumpRegressor(
                    feature_index=feature_index,
                    threshold=threshold,
                    left_value=left_mean,
                    right_value=right_mean,
                )

    if best_stump is None:
        base = mean(targets)
        return DecisionStumpRegressor(0, features[0][0], base, base)
    return best_stump


if __name__ == "__main__":
    import doctest

    doctest.testmod()
