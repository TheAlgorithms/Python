import numpy as np
from collections import Counter
from sklearn import datasets
from sklearn.model_selection import train_test_split

data = datasets.load_iris()

# print(data)

X = np.array(data['data'])
y = np.array(data['target'])
classes = data['target_names']

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
    """
    data = zip(train_data, train_target)
    distances = []
    for data_point in data:
        distance = euclidean_distance(data_point[0], point)
        distances.append((distance, data_point[1]))
    votes = [i[1] for i in sorted(distances)[:k]]
    result = Counter(votes).most_common(1)[0][0]
    return classes[result]

if __name__ == "__main__":
    print(classifier(X_train, y_train, classes, [4.4, 3.1, 1.3, 1.4]))
