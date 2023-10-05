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
        # Your existing _build_tree implementation

    def _calculate_gini(self, labels) -> float:
        """
        Calculate the Gini impurity for a given set of labels.

        Parameters:
            labels: A list of labels.

        Returns:
            float: The Gini impurity.
        """
        # Your existing _calculate_gini implementation

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
        # Your existing _predict_tree implementation

if __name__ == "__main__":
    import doctest

    doctest.testmod()
