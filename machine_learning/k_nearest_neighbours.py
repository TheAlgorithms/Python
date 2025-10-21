"""
k-Nearest Neighbours (kNN) is a simple non-parametric supervised learning
algorithm used for classification. Given some labelled training data, a given
point is classified using its k nearest neighbours according to some distance
metric. The most commonly occurring label among the neighbours becomes the label
of the given point. In effect, the label of the given point is decided by a
majority vote.

This implementation uses the commonly used Euclidean distance metric, but other
distance metrics can also be used.

Reference: https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
"""

from collections import Counter
from heapq import nsmallest
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


class KNN:
    def __init__(
        self,
        train_data: np.ndarray[float],
        train_target: np.ndarray[int],
        class_labels: list[str],
        distance_metric: str = "euclidean",
        p: int = 2,
    ) -> None:
        """
        Create a kNN classifier using the given training data and class labels.

        Parameters:
        -----------
        distance_metric : str
            Type of distance metric to use ('euclidean', 'manhattan', 'minkowski')
        p : int
            Power parameter for Minkowski distance (default 2)
        """
        self.data = list(zip(train_data, train_target))
        self.labels = class_labels
        self.distance_metric = distance_metric
        self.p = p

    def _calculate_distance(self, a: np.ndarray[float], b: np.ndarray[float]) -> float:
        """
        Calculate distance between two points based on the selected metric.
        """
        if self.distance_metric == "euclidean":
            return float(np.linalg.norm(a - b))
        elif self.distance_metric == "manhattan":
            return float(np.sum(np.abs(a - b)))
        elif self.distance_metric == "minkowski":
            return float(np.sum(np.abs(a - b) ** self.p) ** (1 / self.p))
        else:
            raise ValueError("Invalid distance metric. Choose 'euclidean', 'manhattan', or 'minkowski'.")

    def classify(self, pred_point: np.ndarray[float], k: int = 5) -> str:
        """
        Classify a given point using the kNN algorithm
        >>> train_X = np.array(
        ...     [[0, 0], [1, 0], [0, 1], [0.5, 0.5], [3, 3], [2, 3], [3, 2]]
        ... )
        >>> train_y = np.array([0, 0, 0, 0, 1, 1, 1])
        >>> classes = ['A', 'B']
        >>> knn = KNN(train_X, train_y, classes)
        >>> point = np.array([1.2, 1.2])
        >>> knn.classify(point)
        'A'
        """
        distances = (
            (self._calculate_distance(data_point[0], pred_point), data_point[1])
            for data_point in self.data
        )

        votes = (i[1] for i in nsmallest(k, distances))
        result = Counter(votes).most_common(1)[0][0]
        return self.labels[result]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    iris = datasets.load_iris()

    X = np.array(iris["data"])
    y = np.array(iris["target"])
    iris_classes = iris["target_names"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    iris_point = np.array([4.4, 3.1, 1.3, 1.4])

    print("\nUsing Euclidean Distance:")
    classifier1 = KNN(X_train, y_train, iris_classes, distance_metric="euclidean")
    print(classifier1.classify(iris_point, k=3))

    print("\nUsing Manhattan Distance:")
    classifier2 = KNN(X_train, y_train, iris_classes, distance_metric="manhattan")
    print(classifier2.classify(iris_point, k=3))

    print("\nUsing Minkowski Distance (p=3):")
    classifier3 = KNN(X_train, y_train, iris_classes, distance_metric="minkowski", p=3)
    print(classifier3.classify(iris_point, k=3))
