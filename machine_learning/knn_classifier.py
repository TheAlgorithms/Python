from collections import Counter
from math import sqrt


def euclidean_distance(point1: list[float], point2: list[float]) -> float:
    """
    Calculate the Euclidean distance between two points.

    >>> euclidean_distance([1, 2], [4, 6])
    5.0
    """
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensions")

    return sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def knn_classifier(
    training_data: list[list[float]],
    training_labels: list[int],
    test_point: list[float],
    k: int = 3,
) -> int:
    """
    Classify a test point using the K-Nearest Neighbors algorithm.

    >>> training_data = [[1, 2], [2, 3], [3, 3], [6, 7]]
    >>> training_labels = [0, 0, 0, 1]
    >>> knn_classifier(training_data, training_labels, [2, 2])
    0
    """
    if len(training_data) != len(training_labels):
        raise ValueError("Training data and labels must have the same length")

    if k <= 0:
        raise ValueError("k must be greater than 0")

    distances = []

    for data_point, label in zip(training_data, training_labels):
        distance = euclidean_distance(data_point, test_point)
        distances.append((distance, label))

    distances.sort(key=lambda item: item[0])

    nearest_neighbors = distances[:k]

    labels = [label for _, label in nearest_neighbors]

    return Counter(labels).most_common(1)[0][0]
