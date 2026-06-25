"""
Gaussian Naive Bayes Classifier

A probabilistic classifier based on Bayes' theorem with the assumption that
features follow a Gaussian (normal) distribution within each class.

Despite its simplicity, Gaussian Naive Bayes performs well on many real-world
problems, especially when the number of features is large relative to the
number of training samples.

How it works:
    1. Training:   Compute the mean and variance of each feature per class,
                   and the prior probability of each class.
    2. Prediction: For each class, compute the log-likelihood of the input
                   using the Gaussian probability density function, add the
                   log prior, and pick the class with the highest score.

Bayes' theorem:
    P(class | X) ∝ P(X | class) * P(class)

Gaussian PDF:
    P(x | mean, var) = exp(-0.5 * ((x - mean)^2 / var)) / sqrt(2 * pi * var)

Time Complexity:  O(n * d) for training, O(k * d) per sample for prediction
                  where n = samples, k = classes, d = features

References:
    - https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Gaussian_naive_Bayes
    - https://en.wikipedia.org/wiki/Bayes%27_theorem
"""

import math
from collections import defaultdict


def separate_by_class(
    data: list[list[float]], labels: list[int]
) -> dict[int, list[list[float]]]:
    """
    Separate training data by class label.

    Args:
        data:   List of feature vectors.
        labels: List of class labels corresponding to each feature vector.

    Returns:
        A dictionary mapping each class label to its list of feature vectors.

    Raises:
        ValueError: If data and labels have different lengths.
        ValueError: If data is empty.

    >>> data = [[1.0, 2.0], [3.0, 4.0], [1.5, 2.5]]
    >>> labels = [0, 1, 0]
    >>> separated = separate_by_class(data, labels)
    >>> separated[0]
    [[1.0, 2.0], [1.5, 2.5]]
    >>> separated[1]
    [[3.0, 4.0]]
    >>> separate_by_class([], [])
    Traceback (most recent call last):
        ...
    ValueError: Data must not be empty.
    >>> separate_by_class([[1.0, 2.0]], [0, 1])
    Traceback (most recent call last):
        ...
    ValueError: Data and labels must have the same length.
    """
    if not data:
        raise ValueError("Data must not be empty.")
    if len(data) != len(labels):
        raise ValueError("Data and labels must have the same length.")

    separated: dict[int, list[list[float]]] = defaultdict(list)
    for feature_vector, label in zip(data, labels):
        separated[label].append(feature_vector)
    return dict(separated)


def compute_mean_variance(values: list[float]) -> tuple[float, float]:
    """
    Compute the mean and variance of a list of values.

    Uses population variance (divides by n) consistent with the Gaussian PDF
    assumption in Naive Bayes.

    Args:
        values: A non-empty list of numerical values.

    Returns:
        A tuple of (mean, variance). Variance is clamped to a minimum of 1e-9
        to avoid division by zero in the Gaussian PDF.

    Raises:
        ValueError: If values is empty.

    >>> mean, var = compute_mean_variance([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])
    >>> round(mean, 4)
    5.0
    >>> round(var, 4)
    4.0
    >>> compute_mean_variance([5.0])
    (5.0, 1e-09)
    >>> compute_mean_variance([])
    Traceback (most recent call last):
        ...
    ValueError: Values must not be empty.
    """
    if not values:
        raise ValueError("Values must not be empty.")

    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    return mean, max(variance, 1e-9)


def train(
    data: list[list[float]], labels: list[int]
) -> tuple[dict[int, float], dict[int, list[tuple[float, float]]]]:
    """
    Train a Gaussian Naive Bayes classifier.

    Args:
        data:   List of feature vectors (training samples).
        labels: List of class labels corresponding to each sample.

    Returns:
        A tuple of:
        - priors: dict mapping class label to its log prior probability.
        - summaries: dict mapping class label to a list of (mean, variance)
          tuples, one per feature.

    Raises:
        ValueError: If data is empty or lengths mismatch (via helpers).

    >>> data = [[1.0, 2.0], [2.0, 3.0], [10.0, 11.0], [11.0, 12.0]]
    >>> labels = [0, 0, 1, 1]
    >>> priors, summaries = train(data, labels)
    >>> round(priors[0], 4)
    -0.6931
    >>> len(summaries[0])  # two features
    2
    >>> round(summaries[1][0][0], 1)  # mean of feature 0 in class 1
    10.5
    """
    n_samples = len(data)
    separated = separate_by_class(data, labels)

    priors: dict[int, float] = {}
    summaries: dict[int, list[tuple[float, float]]] = {}

    for class_label, class_samples in separated.items():
        priors[class_label] = math.log(len(class_samples) / n_samples)
        # transpose to get per-feature lists
        features_by_column = [list(col) for col in zip(*class_samples)]
        summaries[class_label] = [
            compute_mean_variance(column) for column in features_by_column
        ]

    return priors, summaries


def gaussian_log_probability(x: float, mean: float, variance: float) -> float:
    """
    Compute the log of the Gaussian probability density for a single value.

    Uses the formula:
        log P(x | mean, var) = -0.5 * log(2 * pi * var)
                               - 0.5 * ((x - mean)^2 / var)

    Args:
        x:        The observed value.
        mean:     Mean of the Gaussian distribution.
        variance: Variance of the Gaussian distribution (must be > 0).

    Returns:
        Log probability density as a float.

    Raises:
        ValueError: If variance is not positive.

    >>> round(gaussian_log_probability(1.0, 0.0, 1.0), 4)
    -1.4189
    >>> round(gaussian_log_probability(0.0, 0.0, 1.0), 4)
    -0.9189
    >>> gaussian_log_probability(1.0, 0.0, 0.0)
    Traceback (most recent call last):
        ...
    ValueError: Variance must be positive.
    """
    if variance <= 0:
        raise ValueError("Variance must be positive.")
    return -0.5 * math.log(2 * math.pi * variance) - 0.5 * ((x - mean) ** 2 / variance)


def predict_single(
    feature_vector: list[float],
    priors: dict[int, float],
    summaries: dict[int, list[tuple[float, float]]],
) -> int:
    """
    Predict the class label for a single feature vector.

    Args:
        feature_vector: A list of feature values to classify.
        priors:         Log prior probabilities per class (from train()).
        summaries:      Per-class (mean, variance) per feature (from train()).

    Returns:
        The predicted class label (integer).

    >>> data = [[1.0, 2.0], [2.0, 3.0], [10.0, 11.0], [11.0, 12.0]]
    >>> labels = [0, 0, 1, 1]
    >>> priors, summaries = train(data, labels)
    >>> predict_single([1.5, 2.5], priors, summaries)
    0
    >>> predict_single([10.5, 11.5], priors, summaries)
    1
    """
    best_label = -1
    best_score = float("-inf")

    for class_label, feature_summaries in summaries.items():
        score = priors[class_label]
        for feature_value, (mean, variance) in zip(feature_vector, feature_summaries):
            score += gaussian_log_probability(feature_value, mean, variance)
        if score > best_score:
            best_score = score
            best_label = class_label

    return best_label


def predict(
    data: list[list[float]],
    priors: dict[int, float],
    summaries: dict[int, list[tuple[float, float]]],
) -> list[int]:
    """
    Predict class labels for a list of feature vectors.

    Args:
        data:      List of feature vectors to classify.
        priors:    Log prior probabilities per class (from train()).
        summaries: Per-class (mean, variance) per feature (from train()).

    Returns:
        List of predicted class labels.

    Raises:
        ValueError: If data is empty.

    >>> data = [[1.0, 2.0], [2.0, 3.0], [10.0, 11.0], [11.0, 12.0]]
    >>> labels = [0, 0, 1, 1]
    >>> priors, summaries = train(data, labels)
    >>> predict([[1.5, 2.5], [10.5, 11.5]], priors, summaries)
    [0, 1]
    >>> predict([[0.5, 1.5], [12.0, 13.0]], priors, summaries)
    [0, 1]
    >>> predict([], priors, summaries)
    Traceback (most recent call last):
        ...
    ValueError: Data must not be empty.
    """
    if not data:
        raise ValueError("Data must not be empty.")
    return [predict_single(vector, priors, summaries) for vector in data]


def accuracy(predictions: list[int], actual: list[int]) -> float:
    """
    Compute classification accuracy as a fraction of correct predictions.

    Args:
        predictions: List of predicted class labels.
        actual:      List of true class labels.

    Returns:
        Accuracy as a float between 0.0 and 1.0.

    Raises:
        ValueError: If inputs are empty or have different lengths.

    >>> accuracy([0, 1, 1, 0], [0, 1, 1, 0])
    1.0
    >>> accuracy([0, 1, 1, 0], [0, 1, 0, 0])
    0.75
    >>> accuracy([0], [1])
    0.0
    >>> accuracy([], [])
    Traceback (most recent call last):
        ...
    ValueError: Inputs must not be empty.
    >>> accuracy([0, 1], [0])
    Traceback (most recent call last):
        ...
    ValueError: Predictions and actual labels must have the same length.
    """
    if not predictions:
        raise ValueError("Inputs must not be empty.")
    if len(predictions) != len(actual):
        raise ValueError("Predictions and actual labels must have the same length.")
    correct = sum(p == a for p, a in zip(predictions, actual))
    return correct / len(actual)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
