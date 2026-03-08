"""Random Forest classifier from scratch.

This educational implementation uses an ensemble of simple decision stumps
trained on bootstrap samples with random feature sub-selection.
"""

from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class DecisionStumpClassifier:
    """A one-level decision tree for classification."""

    feature_index: int
    threshold: float
    left_label: int
    right_label: int

    def predict(self, row: list[float]) -> int:
        return (
            self.left_label
            if row[self.feature_index] <= self.threshold
            else self.right_label
        )


class RandomForestClassifier:
    """A compact random forest classifier implementation.

    Examples:
        >>> x = [[0.0], [0.2], [0.9], [1.0], [1.1]]
        >>> y = [0, 0, 1, 1, 1]
        >>> model = RandomForestClassifier(num_trees=7, random_seed=0)
        >>> model.fit(x, y)
        >>> preds = model.predict([[0.1], [1.05]])
        >>> len(preds) == 2 and set(preds) <= {0, 1}
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
        self._trees: list[DecisionStumpClassifier] = []

    def fit(self, features: list[list[float]], labels: list[int]) -> None:
        if not features or not labels:
            raise ValueError("features and labels must be non-empty")
        if len(features) != len(labels):
            raise ValueError("features and labels must have same length")

        width = len(features[0])
        if width == 0 or any(len(row) != width for row in features):
            raise ValueError("all rows must have same non-zero width")

        rng = random.Random(self.random_seed)
        self._trees = []
        feature_budget = self.max_features or max(1, int(width**0.5))
        feature_budget = min(feature_budget, width)

        for _ in range(self.num_trees):
            sample_indexes = [
                rng.randrange(len(features)) for _ in range(len(features))
            ]
            sampled_x = [features[index] for index in sample_indexes]
            sampled_y = [labels[index] for index in sample_indexes]

            candidate_features = rng.sample(range(width), k=feature_budget)
            stump = _best_stump_classifier(sampled_x, sampled_y, candidate_features)
            self._trees.append(stump)

    def predict(self, features: list[list[float]]) -> list[int]:
        if not self._trees:
            raise ValueError("model must be fitted before predict")
        return [
            _majority_vote([tree.predict(row) for tree in self._trees])
            for row in features
        ]


def _majority_vote(values: list[int]) -> int:
    counts = Counter(values)
    return max(sorted(counts), key=lambda value: counts[value])


def _best_stump_classifier(
    features: list[list[float]],
    labels: list[int],
    candidate_features: list[int],
) -> DecisionStumpClassifier:
    best_stump: DecisionStumpClassifier | None = None
    best_score = -1

    for feature_index in candidate_features:
        thresholds = sorted({row[feature_index] for row in features})
        for threshold in thresholds:
            left_labels = [
                label
                for row, label in zip(features, labels)
                if row[feature_index] <= threshold
            ]
            right_labels = [
                label
                for row, label in zip(features, labels)
                if row[feature_index] > threshold
            ]
            if not left_labels or not right_labels:
                continue

            left_major = _majority_vote(left_labels)
            right_major = _majority_vote(right_labels)
            correct = sum(
                1
                for row, label in zip(features, labels)
                if (left_major if row[feature_index] <= threshold else right_major)
                == label
            )
            if correct > best_score:
                best_score = correct
                best_stump = DecisionStumpClassifier(
                    feature_index=feature_index,
                    threshold=threshold,
                    left_label=left_major,
                    right_label=right_major,
                )

    if best_stump is None:
        default = _majority_vote(labels)
        return DecisionStumpClassifier(0, features[0][0], default, default)
    return best_stump


if __name__ == "__main__":
    import doctest

    doctest.testmod()
