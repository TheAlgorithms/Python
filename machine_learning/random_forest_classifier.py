import numpy as np
from typing import Optional, List

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

    def fit(self, X: List[np.ndarray], y: List[int]) -> None:
        """
        Fit the decision tree to the training data.

        Parameters:
            X (List[numpy.ndarray]): The input features.
            y (List[int]): The target labels.

        Returns:
            None
        """
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X: List[np.ndarray], y: List[int], depth: int) -> tuple:
        """
        Recursively build the decision tree.

        Parameters:
            X (List[numpy.ndarray]): The input features.
            y (List[int]): The target labels.
            depth (int): The current depth of the tree.

        Returns:
            tuple: The decision tree structure.
        """
        if depth == self.max_depth or len(np.unique(y)) == 1:
            return (np.bincount(y).argmax(),)

        num_features = len(X[0])
        best_split_feature = None
        best_split_value = None
        best_split_score = np.inf

        for feature in range(num_features):
            unique_values = np.unique(np.array(X)[:, feature])
            for value in unique_values:
                left_mask = np.array(X)[:, feature] <= value
                right_mask = np.array(X)[:, feature] > value

                if len(np.array(y)[left_mask]) == 0 or len(np.array(y)[right_mask]) == 0:
                    continue

                left_score = self._calculate_gini(np.array(y)[left_mask])
                right_score = self._calculate_gini(np.array(y)[right_mask])
                weighted_score = (len(np.array(y)[left_mask]) * left_score +
                                  len(np.array(y)[right_mask]) * right_score) / len(y)

                if weighted_score < best_split_score:
                    best_split_score = weighted_score
                    best_split_feature = feature
                    best_split_value = value

        if best_split_feature is None:
            return (np.bincount(y).argmax(),)

        left_split = self._build_tree([np.array(X)[np.array(X)[:, best_split_feature] <= best_split_value]],
                                      [np.array(y)[np.array(X)[:, best_split_feature] <= best_split_value]], depth + 1)
        right_split = self._build_tree([np.array(X)[np.array(X)[:, best_split_feature] > best_split_value]],
                                       [np.array(y)[np.array(X)[:, best_split_feature] > best_split_value]], depth + 1)

        return (best_split_feature, best_split_value, left_split, right_split)

    def _calculate_gini(self, y: List[int]) -> float:
        """
        Calculate the Gini impurity for a given set of labels.

        Parameters:
            y (List[int]): A list of labels.

        Returns:
            float: The Gini impurity.
        """
        if len(y) == 0:
            return 0
        p_i = np.bincount(y) / len(y)
        return 1 - np.sum(p_i**2)

    def predict(self, X: List[np.ndarray]) -> List[int]:
        """
        Make predictions for input features.

        Parameters:
            X (List[numpy.ndarray]): The input features.

        Returns:
            List[int]: Predicted labels.
        """
        return [self._predict_tree(x, self.tree) for x in X]

    def _predict_tree(self, x: np.ndarray, tree: tuple) -> int:
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
