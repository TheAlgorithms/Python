"""Random Forest Classifier implementation from scratch.

This module implements a Random Forest Classifier using:
- Decision Tree base learners built from scratch
- Bootstrap sampling (bagging)
- Random feature selection at splits
- Majority voting for aggregation

References:
- https://en.wikipedia.org/wiki/Random_forest
- https://en.wikipedia.org/wiki/Decision_tree_learning
"""
from __future__ import annotations

from collections import Counter
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

TreeNode = Dict[str, Any]


class DecisionTreeClassifier:
    """A Decision Tree Classifier built from scratch.

    This tree uses information gain (entropy-based) for splitting decisions.

    Attributes:
        max_depth: Maximum depth of the tree
        min_samples_split: Minimum samples required to split a node
        n_features: Number of features to consider for best split
        tree: The built tree structure
    """

    def __init__(
        self,
        max_depth: int = 10,
        min_samples_split: int = 2,
        n_features: Optional[int] = None,
    ) -> None:
        self.max_depth: int = max_depth
        self.min_samples_split: int = min_samples_split
        self.n_features: Optional[int] = n_features
        self.tree: Optional[TreeNode] = None

    def fit(self, x: np.ndarray, y: np.ndarray) -> None:
        """Build the decision tree.

        Args:
            x: Training features, shape (n_samples, n_features)
            y: Training labels, shape (n_samples,)

        >>> clf = DecisionTreeClassifier(max_depth=1, min_samples_split=2, n_features=1)
        >>> x = np.array([[0.0], [0.0], [1.0], [1.0]])
        >>> y = np.array([0, 0, 1, 1])
        >>> clf.fit(x, y)
        >>> isinstance(clf.tree, dict)
        True
        """
        n_total_features = x.shape[1]
        self.n_features = (
            n_total_features if self.n_features in (None, 0) else min(self.n_features, n_total_features)
        )
        self.tree = self._grow_tree(x, y, depth=0)

    def _grow_tree(self, x: np.ndarray, y: np.ndarray, depth: int = 0) -> TreeNode:
        """Recursively grow the decision tree.

        >>> clf = DecisionTreeClassifier(max_depth=0)
        >>> x = np.array([[0.0], [1.0]])
        >>> y = np.array([0, 1])
        >>> node = clf._grow_tree(x, y, depth=0)
        >>> node['leaf']
        True
        """
        n_samples, n_features = x.shape
        n_labels = len(np.unique(y))

        # Stopping criteria
        if depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split:
            leaf_value = self._most_common_label(y)
            return {"leaf": True, "value": int(leaf_value)}

        # Find best split
        rng = np.random.default_rng()
        feat_indices = rng.choice(n_features, int(self.n_features), replace=False)
        best_feat, best_thresh = self._best_split(x, y, feat_indices)
        if best_feat is None:
            leaf_value = self._most_common_label(y)
            return {"leaf": True, "value": int(leaf_value)}

        # Split the data
        left_mask = x[:, best_feat] <= best_thresh
        right_mask = ~left_mask

        # Grow subtrees
        left = self._grow_tree(x[left_mask], y[left_mask], depth + 1)
        right = self._grow_tree(x[right_mask], y[right_mask], depth + 1)
        return {
            "leaf": False,
            "feature": int(best_feat),
            "threshold": float(best_thresh),
            "left": left,
            "right": right,
        }

    def _best_split(
        self, x: np.ndarray, y: np.ndarray, feat_indices: Sequence[int]
    ) -> Tuple[Optional[int], Optional[float]]:
        """Find the best feature and threshold to split on.

        >>> clf = DecisionTreeClassifier()
        >>> x = np.array([[0.0], [0.5], [1.0]])
        >>> y = np.array([0, 0, 1])
        >>> feat, thresh = clf._best_split(x, y, [0])
        >>> feat in (None, 0)
        True
        """
        best_gain = -np.inf
        split_idx: Optional[int] = None
        split_thresh: Optional[float] = None

        for feat_idx in feat_indices:
            x_column = x[:, int(feat_idx)]
            thresholds = np.unique(x_column)
            for threshold in thresholds:
                gain = self._information_gain(y, x_column, float(threshold))
                if gain > best_gain:
                    best_gain = gain
                    split_idx = int(feat_idx)
                    split_thresh = float(threshold)
        return split_idx, split_thresh

    def _information_gain(self, y: np.ndarray, x_column: np.ndarray, threshold: float) -> float:
        """Calculate information gain from a split.

        >>> y = np.array([0, 0, 1, 1])
        >>> x_col = np.array([0.0, 0.2, 0.8, 1.0])
        >>> DecisionTreeClassifier()._information_gain(y, x_col, 0.5) >= 0.0
        True
        """
        # Parent entropy
        parent_entropy = self._entropy(y)

        # Create children
        left_mask = x_column <= threshold
        right_mask = ~left_mask
        if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
            return 0.0

        # Calculate weighted average entropy of children
        n = len(y)
        n_left, n_right = int(np.sum(left_mask)), int(np.sum(right_mask))
        e_left, e_right = self._entropy(y[left_mask]), self._entropy(y[right_mask])
        child_entropy = (n_left / n) * e_left + (n_right / n) * e_right

        # Information gain
        ig = parent_entropy - child_entropy
        return float(ig)

    def _entropy(self, y: np.ndarray) -> float:
        """Calculate entropy of a label distribution.

        >>> DecisionTreeClassifier()._entropy(np.array([0, 0, 1, 1])) >= 0
        True
        """
        hist = np.bincount(y)
        ps = hist / len(y)
        return float(-np.sum([p * np.log2(p) for p in ps if p > 0]))

    def _most_common_label(self, y: np.ndarray) -> int:
        """Return the most common label.

        >>> DecisionTreeClassifier()._most_common_label(np.array([0, 1, 1]))
        1
        """
        counter = Counter(y.tolist())
        return int(counter.most_common(1)[0][0])

    def predict(self, x: np.ndarray) -> np.ndarray:
        """Predict class labels for samples in x.

        Args:
            x: Features, shape (n_samples, n_features)
        Returns:
            Predicted labels, shape (n_samples,)

        >>> clf = DecisionTreeClassifier(max_depth=1, n_features=1)
        >>> x = np.array([[0.0], [1.0]])
        >>> y = np.array([0, 1])
        >>> clf.fit(x, y)
        >>> clf.predict(x).tolist()
        [0, 1]
        """
        assert self.tree is not None, "Model is not fitted. Call fit first."
        return np.array([self._traverse_tree(row, self.tree) for row in x])

    def _traverse_tree(self, x_row: np.ndarray, node: TreeNode) -> int:
        """Traverse the tree to make a prediction for a single sample.

        >>> node = {"leaf": True, "value": 1}
        >>> DecisionTreeClassifier()._traverse_tree(np.array([0.0]), node)
        1
        """
        if node["leaf"]:
            return int(node["value"])
        if x_row[int(node["feature"])] <= float(node["threshold"]):
            return self._traverse_tree(x_row, node["left"])  # type: ignore[arg-type]
        return self._traverse_tree(x_row, node["right"])  # type: ignore[arg-type]


class RandomForestClassifier:
    """Random Forest Classifier built from scratch.

    Random Forest is an ensemble learning method that constructs multiple
    decision trees during training and outputs the mode of the classes
    (classification) of the individual trees.

    Features:
    - Bootstrap sampling (bagging) to create diverse trees
    - Random feature selection at each split
    - Majority voting for final predictions

    Attributes:
        n_estimators: Number of trees in the forest
        max_depth: Maximum depth of each tree
        min_samples_split: Minimum samples required to split a node
        n_features: Number of features to consider for best split
        trees: List of trained decision trees

    Example:
        >>> from sklearn.datasets import make_classification
        >>> from sklearn.model_selection import train_test_split
        >>> x, y = make_classification(n_samples=200, n_features=10, random_state=0)
        >>> x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
        >>> rf = RandomForestClassifier(n_estimators=5, max_depth=5, n_features=3)
        >>> _ = rf.fit(x_train, y_train)
        >>> y_pred = rf.predict(x_test)
        >>> isinstance(y_pred, np.ndarray)
        True
    """

    def __init__(
        self,
        n_estimators: int = 100,
        max_depth: int = 10,
        min_samples_split: int = 2,
        n_features: Optional[int] = None,
    ) -> None:
        """Initialize Random Forest Classifier.

        Args:
            n_estimators: Number of trees in the forest (default: 100)
            max_depth: Maximum depth of each tree (default: 10)
            min_samples_split: Minimum samples required to split (default: 2)
            n_features: Number of features to consider for best split.
                       If None, uses sqrt(n_features) (default: None)
        """
        self.n_estimators: int = n_estimators
        self.max_depth: int = max_depth
        self.min_samples_split: int = min_samples_split
        self.n_features: Optional[int] = n_features
        self.trees: List[DecisionTreeClassifier] = []

    def fit(self, x: np.ndarray, y: np.ndarray) -> "RandomForestClassifier":
        """Build a forest of trees from the training set (x, y).

        Args:
            x: Training features, shape (n_samples, n_features)
            y: Training labels, shape (n_samples,)
        Returns:
            self: Fitted classifier

        >>> rf = RandomForestClassifier(n_estimators=2, max_depth=2, n_features=1)
        >>> x = np.array([[0.0], [0.1], [0.9], [1.0]])
        >>> y = np.array([0, 0, 1, 1])
        >>> isinstance(rf.fit(x, y), RandomForestClassifier)
        True
        """
        self.trees = []
        n_features = x.shape[1]
        # Default to sqrt of total features if not specified
        if self.n_features is None:
            self.n_features = int(np.sqrt(n_features))
        for _ in range(self.n_estimators):
            tree = DecisionTreeClassifier(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split,
                n_features=self.n_features,
            )
            x_sample, y_sample = self._bootstrap_sample(x, y)
            tree.fit(x_sample, y_sample)
            self.trees.append(tree)
        return self

    def _bootstrap_sample(self, x: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Create a bootstrap sample from the dataset.

        Bootstrap sampling randomly samples with replacement from the dataset.
        This creates diverse training sets for each tree.

        Args:
            x: Features, shape (n_samples, n_features)
            y: Labels, shape (n_samples,)
        Returns:
            x_sample: Bootstrap sample of features
            y_sample: Bootstrap sample of labels

        >>> rf = RandomForestClassifier()
        >>> x = np.arange(10).reshape(5, 2).astype(float)
        >>> y = np.array([0, 1, 0, 1, 0])
        >>> xs, ys = rf._bootstrap_sample(x, y)
        >>> xs.shape[0] == x.shape[0] == ys.shape[0]
        True
        """
        n_samples = x.shape[0]
        rng = np.random.default_rng()
        idxs = rng.choice(n_samples, n_samples, replace=True)
        return x[idxs], y[idxs]

    def predict(self, x: np.ndarray) -> np.ndarray:
        """Predict class labels for samples in x.

        Uses majority voting: each tree votes for a class, and the
        class with the most votes becomes the final prediction.

        Args:
            x: Features, shape (n_samples, n_features)
        Returns:
            Predicted labels, shape (n_samples,)

        >>> rf = RandomForestClassifier(n_estimators=3, max_depth=2, n_features=1)
        >>> x = np.array([[0.0], [1.0]])
        >>> y = np.array([0, 1])
        >>> _ = rf.fit(x, y)
        >>> rf.predict(x).shape
        (2,)
        """
        if not self.trees:
            raise RuntimeError("Model is not fitted. Call fit first.")
        # Get predictions from all trees
        tree_preds = np.array([tree.predict(x) for tree in self.trees])
        # Majority voting: transpose to get predictions per sample then most common
        tree_preds = np.swapaxes(tree_preds, 0, 1)
        y_pred = [self._most_common_label(sample_preds) for sample_preds in tree_preds]
        return np.array(y_pred)

    def _most_common_label(self, y: Sequence[int]) -> int:
        """Return the most common label (majority vote).

        >>> RandomForestClassifier()._most_common_label([0, 1, 1])
        1
        """
        counter = Counter(list(map(int, y)))
        return int(counter.most_common(1)[0][0])


if __name__ == "__main__":
    # Example usage with synthetic data
    from sklearn.datasets import make_classification
    from sklearn.metrics import accuracy_score, classification_report
    from sklearn.model_selection import train_test_split

    print("Random Forest Classifier - Example Usage")
    print("=" * 50)

    # Generate sample classification dataset
    x, y = make_classification(
        n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=42
    )

    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    print(f"Training samples: {x_train.shape[0]}")
    print(f"Test samples: {x_test.shape[0]}")
    print(f"Number of features: {x_train.shape[1]}")
    print()

    # Train Random Forest Classifier
    print("Training Random Forest Classifier...")
    rf_classifier = RandomForestClassifier(n_estimators=10, max_depth=10, min_samples_split=2)
    rf_classifier.fit(x_train, y_train)
    print("Training complete!")
    print()

    # Make predictions
    y_pred = rf_classifier.predict(x_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print()
    print("Classification Report:")
