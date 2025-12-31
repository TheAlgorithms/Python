"""
Naive Bayes Classifier implementation.

This module implements Gaussian Naive Bayes from scratch without using
external machine learning libraries.

References:
https://en.wikipedia.org/wiki/Naive_Bayes_classifier
"""

from typing import List, Dict
import math


def gaussian_probability(x: float, mean: float, variance: float) -> float:
    """
    Calculate Gaussian probability density.

    >>> round(gaussian_probability(1.0, 1.0, 1.0), 3)
    0.399
    >>> gaussian_probability(1.0, 1.0, 0.0)
    0.0
    """
    if variance == 0:
        return 0.0

    exponent = math.exp(-((x - mean) ** 2) / (2 * variance))
    return (1 / math.sqrt(2 * math.pi * variance)) * exponent


class GaussianNaiveBayes:
    """
    Gaussian Naive Bayes classifier.
    """

    def __init__(self) -> None:
        self.class_priors: Dict[int, float] = {}
        self.means: Dict[int, List[float]] = {}
        self.variances: Dict[int, List[float]] = {}

    def fit(self, features: List[List[float]], labels: List[int]) -> None:
        """
        Train the Gaussian Naive Bayes classifier.

        :param features: Feature matrix
        :param labels: Class labels
        :raises ValueError: If input sizes mismatch

        >>> model = GaussianNaiveBayes()
        >>> model.fit([[1.0], [2.0], [3.0]], [0, 0, 1])
        """
        if len(features) != len(labels):
            raise ValueError("Features and labels must have the same length")

        separated: Dict[int, List[List[float]]] = {}
        for feature_vector, label in zip(features, labels):
            separated.setdefault(label, []).append(feature_vector)

        total_samples = len(labels)

        for label, rows in separated.items():
            self.class_priors[label] = len(rows) / total_samples

            transposed = list(zip(*rows))
            self.means[label] = [sum(col) / len(col) for col in transposed]

            self.variances[label] = [
                sum((x - mean) ** 2 for x in col) / len(col)
                for col, mean in zip(transposed, self.means[label])
            ]

    def predict(self, features: List[List[float]]) -> List[int]:
        """
        Predict class labels for input features.

        :param features: Feature matrix
        :return: Predicted labels

        >>> model = GaussianNaiveBayes()
        >>> X = [[1.0], [2.0], [3.0], [4.0]]
        >>> y = [0, 0, 1, 1]
        >>> model.fit(X, y)
        >>> model.predict([[1.5], [3.5]])
        [0, 1]
        """
        predictions: List[int] = []

        for row in features:
            class_scores: Dict[int, float] = {}

            for label in self.class_priors:
                score = math.log(self.class_priors[label])

                for index, value in enumerate(row):
                    mean = self.means[label][index]
                    variance = self.variances[label][index]
                    probability = gaussian_probability(value, mean, variance)

                    if probability > 0:
                        score += math.log(probability)

                class_scores[label] = score

            predicted_label = max(
                class_scores.items(),
                key=lambda item: item[1],
            )[0]
            predictions.append(predicted_label)

        return predictions
