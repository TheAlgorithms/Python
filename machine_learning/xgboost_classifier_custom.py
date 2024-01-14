import numpy as np
from sklearn.tree import DecisionTreeClassifier


class CustomXGBoostClassifier:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def fit(self, x, y):
        n_samples, n_features = x.shape
        y = np.where(y == 0, -1, 1)  # Convert 0/1 labels to -1/1

        predictions = np.zeros(n_samples)

        for _ in range(self.n_estimators):
            residual = y - predictions
            tree = DecisionTreeClassifier(max_depth=self.max_depth)
            tree.fit(x, residual)
            tree_predictions = tree.predict(x)
            predictions += self.learning_rate * tree_predictions
            self.trees.append(tree)

    def predict(self, x):
        result = np.zeros(x.shape[0])

        for tree in self.trees:
            result += self.learning_rate * tree.predict(x)

        return np.where(result >= 0, 1, 0)


# Example Usage:
# clf = CustomXGBoostClassifier()
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)
