import numpy as np
from typing import Optional


class DecisionTree:
    """
    Decision Tree classifier.

    Parameters:
        max_depth (Optional[int]): Maximum depth of the tree. If None, the tree grows until pure nodes or min_samples_split is reached.

    Attributes:
        tree (tuple): The decision tree structure.
    """

    def __init__(self, max_depth: Optional[int] = None) -> None:
        self.max_depth = max_depth

    def fit(self, features, labels) -> None:
        """
        Fit the decision tree to the training data.

        Parameters:
            features: The input features.
            labels: The target labels.

        Returns:
            None
        """
        self.tree = self._build_tree(features, labels, depth=0)

    def _build_tree(self, features, labels, depth) -> tuple:
        """
        Recursively build the decision tree.

        Parameters:
            features: The input features.
            labels: The target labels.
            depth: The current depth of the tree.

        Returns:
            tuple: The decision tree structure.
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

    def _calculate_gini(self, labels) -> float:
        """
        Calculate the Gini impurity for a given set of labels.

        Parameters:
            labels: A list of labels.

        Returns:
            float: The Gini impurity.
        """
        if len(labels) == 0:
            return 0
        p_i = np.bincount(labels) / len(labels)
        return 1 - np.sum(p_i**2)

    def predict(self, features) -> list:
        """
        Make predictions for input features.

        Parameters:
            features: The input features.

        Returns:
            list: Predicted labels.
        """
        return [self._predict_tree(data_point, self.tree) for data_point in features]

    def _predict_tree(self, data_point, tree) -> int:
        """
        Recursively traverse the decision tree to make predictions.

        Parameters:
            data_point: Input features for a single data point.
            tree: The decision tree structure.

        Returns:
            int: Predicted label.
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
