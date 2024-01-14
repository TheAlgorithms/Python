import numpy as np

class CustomXGBoostClassifier:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        y = np.where(y == 0, -1, 1)  # Convert 0/1 labels to -1/1

        predictions = np.zeros(n_samples)

        for _ in range(self.n_estimators):
            residual = y - predictions
            tree = DecisionTree(max_depth=self.max_depth)
            tree.fit(X, residual)
            tree_predictions = tree.predict(X)
            predictions += self.learning_rate * tree_predictions
            self.trees.append(tree)

    def predict(self, X):
        result = np.zeros(X.shape[0])

        for tree in self.trees:
            result += self.learning_rate * tree.predict(X)

        return np.where(result >= 0, 1, 0)

# Example Usage:
# clf = CustomXGBoostClassifier()
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)
