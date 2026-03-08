from sklearn.neural_network import MLPClassifier

X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
y = [0, 1, 0, 0]


clf = MLPClassifier(
    solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1
)

clf.fit(X, y)


test = [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
Y = clf.predict(test)


def wrapper(y):
    """
    >>> [int(x) for x in wrapper(Y)]
    [0, 0, 1]
    """
    return list(y)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
