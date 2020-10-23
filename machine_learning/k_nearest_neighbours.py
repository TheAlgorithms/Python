from collections import Counter

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

data = datasets.load_iris()

X = np.array(data["data"])
y = np.array(data["target"])
classes = data["target_names"]

X_train, X_test, y_train, y_test = train_test_split(X, y)


def euclidean_distance(a, b):
    """
    Gives the euclidean distance between two points
    >>> euclidean_distance([0, 0], [3, 4])
    5.0
    >>> euclidean_distance([1, 2, 3], [1, 8, 11])
    10.0
    """
    return np.linalg.norm(np.array(a) - np.array(b))


def classifier(train_data, train_target, classes, point, k=5):
    """
    Classifies the point using the KNN algorithm
    k closest points are found (ranked in ascending order of euclidean distance)
    Params:
    :train_data: Set of points that are classified into two or more classes
    :train_target: List of classes in the order of train_data points
    :classes: Labels of the classes
    :point: The data point that needs to be classifed

    >>> X_train = [[0, 0], [1, 0], [0, 1], [0.5, 0.5], [3, 3], [2, 3], [3, 2]]
    >>> y_train = [0, 0, 0, 0, 1, 1, 1]
    >>> classes = ['A','B']; point = [1.2,1.2]
    >>> classifier(X_train, y_train, classes,point)
    'A'
    """
    data = zip(train_data, train_target)
    # List of distances of all points from the point to be classified
    distances = []
    for data_point in data:
        distance = euclidean_distance(data_point[0], point)
        distances.append((distance, data_point[1]))
    # Choosing 'k' points with the least distances.
    votes = [i[1] for i in sorted(distances)[:k]]
    # Most commonly occurring class among them
    # is the class into which the point is classified
    result = Counter(votes).most_common(1)[0][0]
    return classes[result]


if __name__ == "__main__":
    print(classifier(X_train, y_train, classes, [4.4, 3.1, 1.3, 1.4]))
