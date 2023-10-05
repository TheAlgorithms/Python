import numpy as np


class DecisionTree:
    """
    Decision Tree classifier.

    Parameters:
        max_depth (int, optional): Maximum depth of the tree. If None, the tree grows until pure nodes or min_samples_split is reached.

    Attributes:
        tree (tuple): The decision tree structure.
    """

    def __init__(self, max_depth: int = None) -> None:
        self.max_depth = max_depth

    def fit(self, features: list[np.ndarray], labels: list[int]) -> None:
        """
        Fit the decision tree to the training data.

        Parameters:
            features (list of numpy.ndarray): The input features.
            labels (list of int): The target labels.

        Returns:
            None

        Examples:
            >>> np.random.seed(42)
            >>> X = np.random.rand(100, 2)
            >>> y = (X[:, 0] + X[:, 1] > 1).astype(int)
            >>> tree = DecisionTree(max_depth=3)
            >>> tree.fit(X, y)
        """
        self.tree = self._build_tree(features, labels, depth=0)

    def _build_tree(
        self, features: list[np.ndarray], labels: list[int], depth: int
    ) -> tuple:
        """
        Recursively build the decision tree.

        Parameters:
            features (list of numpy.ndarray): The input features.
            labels (list of int): The target labels.
            depth (int): The current depth of the tree.

        Returns:
            tuple: The decision tree structure.

        Examples:
            >>> np.random.seed(42)
            >>> X = np.random.rand(100, 2)
            >>> y = (X[:, 0] + X[:, 1] > 1).astype(int)
            >>> tree = DecisionTree(max_depth=3)
            >>> tree._build_tree(X, y, depth=0)
        """
        if depth == self.max_depth or len(np.unique(labels)) == 1:
            return (np.bincount(labels).argmax(),)

        num_features = len(features[0])
        best_split_feature = None
        best_split_value = None
        best_split_score = np.inf

        for feature in range(num_features):
            unique_values = np.unique(np.array(features)[:, feature])
            for value in unique_values:
                left_mask = np.array(features)[:, feature] <= value
                right_mask = np.array(features)[:, feature] > value

                if (
                    len(np.array(labels)[left_mask]) == 0
                    or len(np.array(labels)[right_mask]) == 0
                ):
                    continue

                left_score = self._calculate_gini(np.array(labels)[left_mask])
                right_score = self._calculate_gini(np.array(labels)[right_mask])
                weighted_score = (
                    len(np.array(labels)[left_mask]) * left_score
                    + len(np.array(labels)[right_mask]) * right_score
                ) / len(labels)

                if weighted_score < best_split_score:
                    best_split_score = weighted_score
                    best_split_feature = feature
                    best_split_value = value

        if best_split_feature is None:
            return (np.bincount(labels).argmax(),)

        left_split = self._build_tree(
            [
                np.array(features)[
                    np.array(features)[:, best_split_feature] <= best_split_value
                ]
            ],
            [
                np.array(labels)[
                    np.array(features)[:, best_split_feature] <= best_split_value
                ]
            ],
            depth + 1,
        )
        right_split = self._build_tree(
            [
                np.array(features)[
                    np.array(features)[:, best_split_feature] > best_split_value
                ]
            ],
            [
                np.array(labels)[
                    np.array(features)[:, best_split_feature] > best_split_value
                ]
            ],
            depth + 1,
        )

        return (best_split_feature, best_split_value, left_split, right_split)

    def _calculate_gini(self, labels: list[int]) -> float:
        """
        Calculate the Gini impurity for a given set of labels.

        Parameters:
            labels (list of int): A list of labels.

        Returns:
            float: The Gini impurity.

        Examples:
            >>> labels = [0, 0, 1, 1, 1]
            >>> tree = DecisionTree(max_depth=3)
            >>> tree._calculate_gini(labels)
        """
        if len(labels) == 0:
            return 0
        p_i = np.bincount(labels) / len(labels)
        return 1 - np.sum(p_i**2)

    def predict(self, features: list[np.ndarray]) -> list[int]:
        """
        Make predictions for input features.

        Parameters:
            features (list of numpy.ndarray): The input features.

        Returns:
            list of int: Predicted labels.

        Examples:
            >>> np.random.seed(42)
            >>> X = np.random.rand(100, 2)
            >>> y = (X[:, 0] + X[:, 1] > 1).astype(int)
            >>> tree = DecisionTree(max_depth=3)
            >>> tree.fit(X, y)
            >>> predictions = tree.predict([np.array([0.7, 0.3]), np.array([0.2, 0.8])])
        """
        return [self._predict_tree(data_point, self.tree) for data_point in features]

    def _predict_tree(self, data_point: np.ndarray, tree: tuple) -> int:
        """
        Recursively traverse the decision tree to make predictions.

        Parameters:
            data_point (numpy.ndarray): Input features for a single data point.
            tree (tuple): The decision tree structure.

        Returns:
            int: Predicted label.

        Examples:
            >>> np.random.seed(42)
            >>> X = np.random.rand(100, 2)
            >>> y = (X[:, 0] + X[:, 1] > 1).astype(int)
            >>> tree = DecisionTree(max_depth=3)
            >>> tree.fit(X, y)
            >>> data_point = np.array([0.7, 0.3])
            >>> prediction = tree._predict_tree(data_point, tree.tree)
        """
        if len(tree) == 1:
            return tree[0]
        feature, value, left, right = tree
        if data_point[feature] <= value:
            return self._predict_tree(data_point, left)
        else:
            return self._predict_tree(data_point, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
