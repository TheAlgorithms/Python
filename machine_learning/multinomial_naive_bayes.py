"""
Multinomial Naive Bayes Classifier implementation.

This module implements Multinomial Naive Bayes from scratch without using
external machine learning libraries. It is commonly used for text
classification tasks such as spam detection.

References:
https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Multinomial_naive_bayes
"""

import math


class MultinomialNaiveBayes:
    """
    Multinomial Naive Bayes classifier.
    """

    def __init__(self, alpha: float = 1.0) -> None:
        """
        Initialize the classifier.

        :param alpha: Laplace smoothing parameter
        """
        if alpha <= 0:
            raise ValueError("Alpha must be greater than 0")

        self.alpha = alpha
        self.class_priors: dict[int, float] = {}
        self.feature_log_prob: dict[int, list[float]] = {}
        self.num_features: int = 0

    def fit(self, features: list[list[int]], labels: list[int]) -> None:
        """
        Train the Multinomial Naive Bayes classifier.

        :param features: Feature matrix (counts of features)
        :param labels: Class labels
        :raises ValueError: If input sizes mismatch

        >>> model = MultinomialNaiveBayes()
        >>> X = [[2, 1], [1, 1], [0, 2]]
        >>> y = [0, 0, 1]
        >>> model.fit(X, y)
        """
        if len(features) != len(labels):
            raise ValueError("Features and labels must have the same length")

        if not features:
            raise ValueError("Feature matrix must not be empty")

        self.num_features = len(features[0])

        separated: dict[int, list[list[int]]] = {}
        for row, label in zip(features, labels):
            separated.setdefault(label, []).append(row)

        total_samples = len(labels)

        for label, rows in separated.items():
            self.class_priors[label] = math.log(len(rows) / total_samples)

            feature_counts = [0] * self.num_features
            total_count = 0

            for row in rows:
                for index, value in enumerate(row):
                    feature_counts[index] += value
                    total_count += value

            self.feature_log_prob[label] = [
                math.log(
                    (count + self.alpha)
                    / (total_count + self.alpha * self.num_features)
                )
                for count in feature_counts
            ]

    def predict(self, features: list[list[int]]) -> list[int]:
        """
        Predict class labels for input features.

        :param features: Feature matrix
        :return: Predicted labels

        >>> model = MultinomialNaiveBayes()
        >>> X = [[2, 1], [1, 1], [0, 2]]
        >>> y = [0, 0, 1]
        >>> model.fit(X, y)
        >>> model.predict([[1, 0], [0, 2]])
        [0, 1]
        """
        predictions: list[int] = []

        for row in features:
            class_scores: dict[int, float] = {}

            for label in self.class_priors:
                score = self.class_priors[label]

                for index, value in enumerate(row):
                    score += value * self.feature_log_prob[label][index]

                class_scores[label] = score

            predicted_label = max(
                class_scores.items(),
                key=lambda item: item[1],
            )[0]
            predictions.append(predicted_label)

        return predictions
