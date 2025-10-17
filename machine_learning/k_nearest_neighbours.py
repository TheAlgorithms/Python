"""
k-Nearest Neighbours (kNN) is a simple non-parametric supervised learning
algorithm used for classification. Given some labelled training data, a given
point is classified using its k nearest neighbours according to some distance
metric. The most commonly occurring label among the neighbours becomes the label
of the given point. In effect, the label of the given point is decided by a
majority vote.

This implementation uses the Euclidean distance metric by default, and also
supports Manhattan (L1) and Minkowski (Lp) distances.

Reference: https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
"""

from collections import Counter
from heapq import nsmallest

import numpy as np


class KNN:
    def __init__(
        self,
        train_data: np.ndarray[float],
        train_target: np.ndarray[int],
        class_labels: list[str],
        *,
        distance_metric: str = "euclidean",
        p: float = 2.0,
    ) -> None:
        """
        Create a kNN classifier using the given training data and class labels

        Parameters
        ----------
        train_data : np.ndarray[float]
            Training features.
        train_target : np.ndarray[int]
            Training labels as integer indices.
        class_labels : list[str]
            Mapping from label index to label name.
        distance_metric : {"euclidean", "manhattan", "minkowski"}
            Distance to use for neighbour search. Defaults to "euclidean".
        p : float
            Power parameter for Minkowski distance (Lp norm). Must be >= 1 when
            distance_metric is "minkowski". Defaults to 2.0.
        """
        # Store a reusable copy; zip() returns an iterator that would be
        # exhausted after one classification otherwise.
        self.data = list(zip(train_data, train_target))
        self.labels = class_labels
        self.distance_metric = distance_metric.lower()
        self.p = float(p)

        if self.distance_metric not in {"euclidean", "manhattan", "minkowski"}:
            msg = (
                "distance_metric must be one of {'euclidean', 'manhattan', 'minkowski'}"
            )
            raise ValueError(msg)
        if self.distance_metric == "minkowski" and self.p < 1:
            msg = "For Minkowski distance, p must be >= 1"
            raise ValueError(msg)

    @staticmethod
    def _euclidean_distance(a: np.ndarray[float], b: np.ndarray[float]) -> float:
        """
        Calculate the Euclidean distance between two points
        >>> KNN._euclidean_distance(np.array([0, 0]), np.array([3, 4]))
        5.0
        >>> KNN._euclidean_distance(np.array([1, 2, 3]), np.array([1, 8, 11]))
        10.0
        """
        return float(np.linalg.norm(a - b))

    @staticmethod
    def _manhattan_distance(a: np.ndarray[float], b: np.ndarray[float]) -> float:
        """
        Calculate the Manhattan (L1) distance between two points
        >>> KNN._manhattan_distance(np.array([0, 0]), np.array([3, 4]))
        7.0
        >>> KNN._manhattan_distance(np.array([1, 2, 3]), np.array([1, 8, 11]))
        14.0
        """
        return float(np.linalg.norm(a - b, ord=1))

    @staticmethod
    def _minkowski_distance(
        a: np.ndarray[float], b: np.ndarray[float], p: float
    ) -> float:
        """
        Calculate the Minkowski (Lp) distance between two points
        >>> KNN._minkowski_distance(np.array([0, 0]), np.array([3, 4]), 2)
        5.0
        >>> KNN._minkowski_distance(np.array([0, 0]), np.array([3, 4]), 1)
        7.0
        """
        return float(np.linalg.norm(a - b, ord=p))

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
        >>> # Manhattan distance yields the same class here
        >>> knn_l1 = KNN(train_X, train_y, classes, distance_metric='manhattan')
        >>> knn_l1.classify(point)
        'A'
        >>> # Minkowski with p=2 equals Euclidean
        >>> knn_lp = KNN(train_X, train_y, classes, distance_metric='minkowski', p=2)
        >>> knn_lp.classify(point)
        'A'
        >>> # Invalid distance metric
        >>> try:
        ...     _ = KNN(train_X, train_y, classes, distance_metric='chebyshev')
        ... except ValueError as e:
        ...     'distance_metric' in str(e)
        True
        >>> # Invalid Minkowski power
        >>> try:
        ...     _ = KNN(train_X, train_y, classes, distance_metric='minkowski', p=0.5)
        ... except ValueError as e:
        ...     'p must be >=' in str(e)
        True
        """
        # Choose the distance function once
        if self.distance_metric == "euclidean":
            def dist_fn(a: np.ndarray[float]) -> float:
                return self._euclidean_distance(a, pred_point)
        elif self.distance_metric == "manhattan":
            def dist_fn(a: np.ndarray[float]) -> float:
                return self._manhattan_distance(a, pred_point)
        else:  # minkowski
            p = self.p

            def dist_fn(a: np.ndarray[float]) -> float:
                return self._minkowski_distance(a, pred_point, p)

        # Distances of all points from the point to be classified
        distances = ((dist_fn(dp), lbl) for dp, lbl in self.data)

        # Choosing k points with the shortest distances
        votes = (i[1] for i in nsmallest(k, distances))

        # Most commonly occurring class is the one into which the point is classified
        result = Counter(votes).most_common(1)[0][0]
        return self.labels[result]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Optional demo using scikit-learn's iris dataset. Kept under __main__ to
    # avoid making scikit-learn a hard dependency for importing this module.
    from sklearn import datasets
    from sklearn.model_selection import train_test_split

    iris = datasets.load_iris()

    X = np.array(iris["data"])
    y = np.array(iris["target"])
    iris_classes = iris["target_names"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    iris_point = np.array([4.4, 3.1, 1.3, 1.4])
    classifier = KNN(X_train, y_train, iris_classes)
    print(classifier.classify(iris_point, k=3))
