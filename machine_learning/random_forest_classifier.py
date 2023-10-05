import numpy as np

# Define a decision tree class
class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        # Check termination conditions
        if depth == self.max_depth or len(np.unique(y)) == 1:
            return (np.bincount(y).argmax(),)  # Return a tuple with the class label

        # Find the best split
        num_features = X.shape[1]
        best_split_feature = None
        best_split_value = None
        best_split_score = np.inf

        for feature in range(num_features):
            unique_values = np.unique(X[:, feature])
            for value in unique_values:
                left_mask = X[:, feature] <= value
                right_mask = X[:, feature] > value

                if len(y[left_mask]) == 0 or len(y[right_mask]) == 0:
                    continue

                left_score = self._calculate_gini(y[left_mask])
                right_score = self._calculate_gini(y[right_mask])
                weighted_score = (
                    len(y[left_mask]) * left_score + len(y[right_mask]) * right_score
                ) / len(y)

                if weighted_score < best_split_score:
                    best_split_score = weighted_score
                    best_split_feature = feature
                    best_split_value = value

        if best_split_feature is None:
            return (np.bincount(y).argmax(),)  # Return a tuple with the class label

        left_split = self._build_tree(
            X[X[:, best_split_feature] <= best_split_value],
            y[X[:, best_split_feature] <= best_split_value],
            depth + 1,
        )
        right_split = self._build_tree(
            X[X[:, best_split_feature] > best_split_value],
            y[X[:, best_split_feature] > best_split_value],
            depth + 1,
        )

        return (best_split_feature, best_split_value, left_split, right_split)

    def _calculate_gini(self, y):
        if len(y) == 0:
            return 0
        p_i = np.bincount(y) / len(y)
        return 1 - np.sum(p_i**2)

    def predict(self, X):
        return np.array([self._predict_tree(x, self.tree) for x in X])

    def _predict_tree(self, x, tree):
        if len(tree) == 1:
            return tree[0]  # Leaf node, return class label
        feature, value, left, right = tree
        if x[feature] <= value:
            return self._predict_tree(x, left)
        else:
            return self._predict_tree(x, right)


# Random Forest Classifier
class RandomForestClassifier:
    def __init__(self, n_estimators=100, max_depth=None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        for _ in range(self.n_estimators):
            # Randomly sample data with replacement
            indices = np.random.choice(len(X), len(X), replace=True)
            X_subset = X[indices]
            y_subset = y[indices]

            tree = DecisionTree(max_depth=self.max_depth)
            tree.fit(X_subset, y_subset)
            self.trees.append(tree)

    def predict(self, X):
        predictions = np.array([tree.predict(X) for tree in self.trees])
        # Use majority vote for classification
        return np.apply_along_axis(
            lambda x: np.bincount(x).argmax(), axis=0, arr=predictions
        )


# Example usage:
if __name__ == "__main__":
    # Generate some random data for demonstration
    np.random.seed(42)
    X = np.random.rand(100, 2)
    y = (X[:, 0] + X[:, 1] > 1).astype(int)

    # Create and train a Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=None)
    rf_classifier.fit(X, y)

    # Make predictions
    new_data = np.array([[0.7, 0.3], [0.2, 0.8]])
    predictions = rf_classifier.predict(new_data)
    print(predictions)
