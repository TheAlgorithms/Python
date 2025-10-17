import numpy as np
import pytest

from machine_learning.k_nearest_neighbours import KNN


def test_distance_functions():
    a = np.array([0, 0])
    b = np.array([3, 4])
    assert KNN._euclidean_distance(a, b) == 5.0
    assert KNN._manhattan_distance(a, b) == 7.0
    assert KNN._minkowski_distance(a, b, 2) == 5.0
    assert KNN._minkowski_distance(a, b, 1) == 7.0


@pytest.mark.parametrize(
    ("distance_metric", "p"),
    [
        ("euclidean", None),
        ("manhattan", None),
        ("minkowski", 2),  # p=2 -> Euclidean
        ("minkowski", 3),  # another valid p
    ],
)
def test_classify_with_different_metrics(distance_metric: str, p: float | None):
    train_X = np.array(
        [[0, 0], [1, 0], [0, 1], [0.5, 0.5], [3, 3], [2, 3], [3, 2]]
    )
    train_y = np.array([0, 0, 0, 0, 1, 1, 1])
    classes = ["A", "B"]

    kwargs: dict[str, object] = {"distance_metric": distance_metric}
    if p is not None:
        kwargs["p"] = float(p)

    knn = KNN(train_X, train_y, classes, **kwargs)
    point = np.array([1.2, 1.2])
    # For this dataset/point, the class should be 'A' regardless of metric
    assert knn.classify(point) == "A"


def test_invalid_distance_metric_raises():
    X = np.array([[0.0, 0.0]])
    y = np.array([0])
    labels = ["A"]
    with pytest.raises(ValueError):
        KNN(X, y, labels, distance_metric="chebyshev")


def test_invalid_minkowski_p_raises():
    X = np.array([[0.0, 0.0]])
    y = np.array([0])
    labels = ["A"]
    with pytest.raises(ValueError):
        KNN(X, y, labels, distance_metric="minkowski", p=0.5)


def test_multiple_classify_calls_with_same_instance():
    train_X = np.array([[0, 0], [1, 1], [2, 2]])
    train_y = np.array([0, 0, 1])
    classes = ["A", "B"]
    knn = KNN(train_X, train_y, classes)

    p1 = np.array([0.1, 0.2])
    p2 = np.array([1.9, 2.0])

    # Ensure we can call classify multiple times (zip exhaustion bug regression)
    assert knn.classify(p1) == "A"
    assert knn.classify(p2) in {"A", "B"}


if __name__ == "__main__":
    import pytest as _pytest

    _pytest.main([__file__])
