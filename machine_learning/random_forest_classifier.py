import numpy as np

class DecisionTree:
    """
    Decision Tree classifier.

    Parameters:
        max_depth (int): Maximum depth of the tree. If None, the tree grows until pure nodes or min_samples_split is reached.

    Attributes:
        tree (tuple): The decision tree structure.

    Examples:
        >>> np.random.seed(42)
        >>> X = np.random.rand(100, 2)
        >>> y = (X[:, 0] + X[:, 1] > 1).astype(int)
        >>> tree = DecisionTree(max_depth=3)
        >>> tree.fit(X, y)
        >>> predictions = tree.predict(np.array([[0.7, 0.3], [0.2, 0.8]]))
    """

    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        """
        Fit the decision tree to the training data.

        Parameters:
            X (numpy.ndarray): The input features.
            y (numpy.ndarray): The target labels.

        Returns:
            None
        """
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        """
        Recursively build the decision tree.

        Parameters:
            X (numpy.ndarray): The input features.
            y (numpy.ndarray): The target labels.
            depth (int): The current depth of the tree.

        Returns:
            tuple: The decision tree structure.
        """
        if depth == self.max_depth or len(np.unique(y)) == 1:
            return (np.bincount(y).argmax(),)

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
                weighted_score = (len(y[left_mask]) * left_score + len(y[right_mask]) * right_score) / len(y)

                if weighted_score < best_split_score:
                    best_split_score = weighted_score
                    best_split_feature = feature
                    best_split_value = value

        if best_split_feature is None:
            return (np.bincount(y).argmax(),)

        left_split = self._build_tree(X[X[:, best_split_feature] <= best_split_value], y[X[:, best_split_feature] <= best_split_value], depth + 1)
        right_split = self._build_tree(X[X[:, best_split_feature] > best_split_value], y[X[:, best_split_feature] > best_split_value], depth + 1)

        return (best_split_feature, best_split_value, left_split, right_split)

    def _calculate_gini(self, y):
        """
        Calculate the Gini impurity for a given set of labels.

        Parameters:
            y (numpy.ndarray): An array of labels.

        Returns:
            float: The Gini impurity.
        """
        if len(y) == 0:
            return 0
        p_i = np.bincount(y) / len(y)
        return 1 - np.sum(p_i**2)

    def predict(self, X):
        """
        Make predictions for input features.

        Parameters:
            X (numpy.ndarray): The input features.

        Returns:
            numpy.ndarray: Predicted labels.
        """
        return np.array([self._predict_tree(x, self.tree) for x in X])

    def _predict_tree(self, x, tree):
        """
        Recursively traverse the decision tree to make predictions.

        Parameters:
            x (numpy.ndarray): Input features for a single data point.
            tree (tuple): The decision tree structure.

        Returns:
            int: Predicted label.
        """
        if len(tree) == 1:
            return tree[0]
        feature, value, left, right = tree
        if x[feature] <= value:
            return self._predict_tree(x, left)
        else:
            return self._predict_tree(x, right)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


# Example usage:
#if __name__ == "__main__":
    # Generate some random data for demonstration
    #np.random.seed(42)
    #X = np.random.rand(100, 2)
    #y = (X[:, 0] + X[:, 1] > 1).astype(int)

    # Create and train a Random Forest classifier
    #rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=None)
    #rf_classifier.fit(X, y)

    # Make predictions
    #new_data = np.array([[0.7, 0.3], [0.2, 0.8]])
    #predictions = rf_classifier.predict(new_data)
    #print(predictions)
