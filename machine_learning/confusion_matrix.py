"""
Confusion Matrix implementation for evaluating classification models.

A confusion matrix is a table used to evaluate the performance of a
classification algorithm by comparing predicted labels against actual labels.

Reference: https://en.wikipedia.org/wiki/Confusion_matrix
"""

import numpy as np


def confusion_matrix(actual: list, predicted: list) -> np.ndarray:
    """
    Calculate the confusion matrix for binary or multiclass classification.

    Args:
        actual: List of actual class labels.
        predicted: List of predicted class labels.

    Returns:
        A 2D numpy array representing the confusion matrix.

    Examples:
    >>> actual = [1, 0, 1, 1, 0, 1]
    >>> predicted = [1, 0, 0, 1, 0, 0]
    >>> confusion_matrix(actual, predicted)
    array([[2, 0],
           [2, 2]])

    >>> actual = [0, 0, 1, 1, 2, 2]
    >>> predicted = [0, 1, 1, 2, 2, 0]
    >>> confusion_matrix(actual, predicted)
    array([[1, 1, 0],
           [0, 1, 1],
           [1, 0, 1]])
    """
    classes = sorted(set(actual) | set(predicted))
    n = len(classes)
    class_to_index = {c: i for i, c in enumerate(classes)}

    matrix = np.zeros((n, n), dtype=int)
    for a, p in zip(actual, predicted):
        matrix[class_to_index[a]][class_to_index[p]] += 1

    return matrix


def precision(actual: list, predicted: list, positive_label: int = 1) -> float:
    """
    Calculate precision: TP / (TP + FP).

    Args:
        actual: List of actual class labels.
        predicted: List of predicted class labels.
        positive_label: The label considered as positive class.

    Returns:
        Precision score as a float.

    Examples:
    >>> actual = [1, 0, 1, 1, 0, 1]
    >>> predicted = [1, 0, 0, 1, 0, 0]
    >>> precision(actual, predicted)
    1.0

    >>> actual = [1, 0, 1, 1, 0, 1]
    >>> predicted = [1, 1, 0, 1, 0, 0]
    >>> precision(actual, predicted)
    0.6666666666666666
    """
    tp = sum(1 for a, p in zip(actual, predicted) if a == positive_label and p == positive_label)
    fp = sum(1 for a, p in zip(actual, predicted) if a != positive_label and p == positive_label)
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0


def recall(actual: list, predicted: list, positive_label: int = 1) -> float:
    """
    Calculate recall (sensitivity): TP / (TP + FN).

    Args:
        actual: List of actual class labels.
        predicted: List of predicted class labels.
        positive_label: The label considered as positive class.

    Returns:
        Recall score as a float.

    Examples:
    >>> actual = [1, 0, 1, 1, 0, 1]
    >>> predicted = [1, 0, 0, 1, 0, 0]
    >>> recall(actual, predicted)
    0.5

    >>> actual = [1, 0, 1, 1, 0, 1]
    >>> predicted = [1, 1, 1, 1, 0, 1]
    >>> recall(actual, predicted)
    1.0
    """
    tp = sum(1 for a, p in zip(actual, predicted) if a == positive_label and p == positive_label)
    fn = sum(1 for a, p in zip(actual, predicted) if a == positive_label and p != positive_label)
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0


def f1_score(actual: list, predicted: list, positive_label: int = 1) -> float:
    """
    Calculate F1 score: harmonic mean of precision and recall.

    Args:
        actual: List of actual class labels.
        predicted: List of predicted class labels.
        positive_label: The label considered as positive class.

    Returns:
        F1 score as a float.

    Examples:
    >>> actual = [1, 0, 1, 1, 0, 1]
    >>> predicted = [1, 0, 0, 1, 0, 0]
    >>> round(f1_score(actual, predicted), 4)
    0.6667

    >>> actual = [1, 0, 1, 1, 0, 1]
    >>> predicted = [1, 0, 1, 1, 0, 1]
    >>> f1_score(actual, predicted)
    1.0
    """
    p = precision(actual, predicted, positive_label)
    r = recall(actual, predicted, positive_label)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
