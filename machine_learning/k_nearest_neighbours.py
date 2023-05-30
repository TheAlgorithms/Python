from collections import Counter

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


def euclidean_distance(a: np.ndarray[float], b: np.ndarray[float]) -> float:
    """
    Calculate the Euclidean distance between two points
    >>> euclidean_distance(np.array([0, 0]), np.array([3, 4]))
    5.0
    >>> euclidean_distance(np.array([1, 2, 3]), np.array([1, 8, 11]))
    10.0
    """
    return np.linalg.norm(a - b)


def classifier(
    train_data: np.ndarray[float],
    train_target: np.ndarray[int],
    class_labels: list[str],
    pred_point: np.ndarray[float],
    k: int = 5,
) -> str:
    """
    Classifies a given point using the KNN algorithm
    k closest points are found (ranked in ascending order of Euclidean distance)
    Params:
    :train_data: Set of points that are classified into two or more classes
    :train_target: List of classes in the order of train_data points
    :classes: Labels of the classes
    :point: The data point that needs to be classified

    >>> train_X = np.array([[0, 0], [1, 0], [0, 1], [0.5, 0.5], [3, 3], [2, 3], [3, 2]])
    >>> train_y = np.array([0, 0, 0, 0, 1, 1, 1])
    >>> classes = ['A', 'B']
    >>> point = np.array([1.2, 1.2])
    >>> classifier(train_X, train_y, classes, point)
    'A'
    """
    data = zip(train_data, train_target)
    # List of distances of all points from the point to be classified
    distances = []
    for data_point in data:
        distance = euclidean_distance(data_point[0], pred_point)
        distances.append((distance, data_point[1]))
    # Choosing 'k' points with the least distances.
    votes = [i[1] for i in sorted(distances)[:k]]
    # Most commonly occurring class among them
    # is the class into which the point is classified
    result = Counter(votes).most_common(1)[0][0]
    return class_labels[result]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    iris = datasets.load_iris()

    X = np.array(iris["data"])
    y = np.array(iris["target"])
    iris_classes = iris["target_names"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    iris_point = np.array([4.4, 3.1, 1.3, 1.4])
    print(classifier(X_train, y_train, iris_classes, iris_point))
