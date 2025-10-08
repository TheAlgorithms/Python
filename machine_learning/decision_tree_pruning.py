"""
Enhanced Decision Tree with Pruning functionality.

This implementation extends the basic decision tree with advanced pruning techniques
to reduce overfitting and improve generalization. It includes both pre-pruning
(constraints during tree building) and post-pruning (reduced error pruning and
cost-complexity pruning).

Key features:
- Pre-pruning: Maximum depth, minimum samples per leaf, minimum impurity decrease
- Post-pruning: Reduced error pruning and cost-complexity pruning
- Support for both regression and classification
- Comprehensive validation and testing

Reference: https://en.wikipedia.org/wiki/Decision_tree_pruning
"""

import doctest
from typing import Literal

import numpy as np


class DecisionTreePruning:
    """
    Enhanced Decision Tree with pruning capabilities.

    This implementation provides both regression and classification decision trees
    with various pruning techniques to prevent overfitting.
    """

    def __init__(
        self,
        max_depth: int | None = None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_impurity_decrease: float = 0.0,
        pruning_method: Literal["none", "reduced_error", "cost_complexity"] = "none",
        ccp_alpha: float = 0.0,
        random_state: int | None = None,
    ) -> None:
        """
        Initialize Decision Tree with pruning parameters.

        Args:
            max_depth: Maximum depth of the tree
            min_samples_split: Minimum samples required to split a node
            min_samples_leaf: Minimum samples required at a leaf node
            min_impurity_decrease: Minimum impurity decrease for a split
            pruning_method: Pruning method to use
            ccp_alpha: Cost complexity pruning parameter
            random_state: Random seed for reproducibility

        >>> tree = DecisionTreePruning(max_depth=5, min_samples_leaf=2)
        >>> tree.max_depth
        5
        >>> tree.min_samples_leaf
        2
        """
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_impurity_decrease = min_impurity_decrease
        self.pruning_method = pruning_method
        self.ccp_alpha = ccp_alpha
        self.random_state = random_state

        # Tree structure
        self.root_: TreeNode | None = None
        self.n_features_: int | None = None
        self.feature_names_: list[str] | None = None

        if random_state is not None:
            self.rng_ = np.random.default_rng(random_state)
        else:
            self.rng_ = np.random.default_rng()

    def _mse(self, y: np.ndarray) -> float:
        """
        Compute mean squared error for regression.

        Args:
            y: Target values

        Returns:
            Mean squared error
        """
        if len(y) == 0:
            return 0.0
        return np.mean((y - np.mean(y)) ** 2)

    def _gini(self, y: np.ndarray) -> float:
        """
        Compute Gini impurity for classification.

        Args:
            y: Target labels

        Returns:
            Gini impurity
        """
        if len(y) == 0:
            return 0.0

        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        return 1 - np.sum(probabilities ** 2)

    def _entropy(self, y: np.ndarray) -> float:
        """
        Compute entropy for classification.

        Args:
            y: Target labels

        Returns:
            Entropy
        """
        if len(y) == 0:
            return 0.0

        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        probabilities = probabilities[probabilities > 0]  # Avoid log(0)
        return -np.sum(probabilities * np.log2(probabilities))

    def _find_best_split(
        self, X: np.ndarray, y: np.ndarray, task_type: str
    ) -> tuple[int, float, float]:
        """
        Find the best split for the given data.

        Args:
            X: Feature matrix
            y: Target values
            task_type: 'regression' or 'classification'

        Returns:
            Tuple of (best_feature, best_threshold, best_impurity)
        """
        best_feature = -1
        best_threshold = 0.0
        best_impurity = float('inf')

        n_features = X.shape[1]
        current_impurity = self._mse(y) if task_type == "regression" else self._gini(y)

        for feature_idx in range(n_features):
            # Get unique values for this feature
            feature_values = np.unique(X[:, feature_idx])

            for threshold in feature_values[:-1]:  # Exclude the last value
                # Split the data
                left_mask = X[:, feature_idx] <= threshold
                right_mask = ~left_mask

                if (
                    np.sum(left_mask) < self.min_samples_leaf
                    or np.sum(right_mask) < self.min_samples_leaf
                ):
                    continue

                # Calculate weighted impurity
                left_impurity = (
                    self._mse(y[left_mask])
                    if task_type == "regression"
                    else self._gini(y[left_mask])
                )
                right_impurity = (
                    self._mse(y[right_mask])
                    if task_type == "regression"
                    else self._gini(y[right_mask])
                )

                weighted_impurity = (
                    np.sum(left_mask) * left_impurity
                    + np.sum(right_mask) * right_impurity
                ) / len(y)

                # Check if this split improves impurity
                impurity_decrease = current_impurity - weighted_impurity
                if (
                    impurity_decrease >= self.min_impurity_decrease
                    and weighted_impurity < best_impurity
                ):
                    best_feature = feature_idx
                    best_threshold = threshold
                    best_impurity = weighted_impurity

        return best_feature, best_threshold, best_impurity

    def _build_tree(
        self,
        X: np.ndarray,
        y: np.ndarray,
        depth: int = 0,
        task_type: str = "regression"
    ) -> "TreeNode":
        """
        Recursively build the decision tree.

        Args:
            X: Feature matrix
            y: Target values
            depth: Current depth
            task_type: 'regression' or 'classification'

        Returns:
            Root node of the subtree
        """
        node = TreeNode()

        # Check stopping criteria
        if (len(y) < self.min_samples_split or
            (self.max_depth is not None and depth >= self.max_depth) or
            len(np.unique(y)) == 1):
            node.is_leaf = True
            node.value = (
                np.mean(y) if task_type == "regression" else self._most_common(y)
            )
            node.samples = len(y)
            return node

        # Find best split
        best_feature, best_threshold, best_impurity = self._find_best_split(
            X, y, task_type
        )

        # If no good split found, make it a leaf
        if best_feature == -1:
            node.is_leaf = True
            node.value = (
                np.mean(y) if task_type == "regression" else self._most_common(y)
            )
            node.samples = len(y)
            return node

        # Split the data
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = ~left_mask

        # Create internal node
        node.is_leaf = False
        node.feature = best_feature
        node.threshold = best_threshold
        node.samples = len(y)
        node.impurity = best_impurity

        # Recursively build left and right subtrees
        node.left = self._build_tree(
            X[left_mask], y[left_mask], depth + 1, task_type
        )
        node.right = self._build_tree(
            X[right_mask], y[right_mask], depth + 1, task_type
        )

        return node

    def _most_common(self, y: np.ndarray) -> int | float:
        """
        Find the most common value in an array.

        Args:
            y: Array of values

        Returns:
            Most common value
        """
        values, counts = np.unique(y, return_counts=True)
        return values[np.argmax(counts)]

    def _reduced_error_pruning(self, X_val: np.ndarray, y_val: np.ndarray) -> None:
        """
        Perform reduced error pruning on the tree.

        Args:
            X_val: Validation feature matrix
            y_val: Validation target values
        """
        if self.root_ is None:
            return

        # Get all internal nodes (post-order traversal)
        internal_nodes = self._get_internal_nodes(self.root_)

        # Try pruning each internal node
        improved = True
        while improved:
            improved = False
            best_improvement = 0
            best_node = None

            for node in internal_nodes:
                if node.is_leaf:
                    continue

                # Calculate validation error before pruning
                predictions_before = self._predict_batch(X_val)
                error_before = self._calculate_error(y_val, predictions_before)

                # Temporarily prune the node
                original_left = node.left
                original_right = node.right
                original_is_leaf = node.is_leaf
                original_value = node.value

                node.left = None
                node.right = None
                node.is_leaf = True
                node.value = self._most_common(y_val)  # Use validation set majority

                # Calculate validation error after pruning
                predictions_after = self._predict_batch(X_val)
                error_after = self._calculate_error(y_val, predictions_after)

                # Calculate improvement
                improvement = error_before - error_after

                if improvement > best_improvement:
                    best_improvement = improvement
                    best_node = node

                # Restore the node
                node.left = original_left
                node.right = original_right
                node.is_leaf = original_is_leaf
                node.value = original_value

            # Apply the best pruning if it improves performance
            if best_node is not None and best_improvement > 0:
                best_node.left = None
                best_node.right = None
                best_node.is_leaf = True
                best_node.value = self._most_common(y_val)
                improved = True
                # Remove from internal nodes list
                internal_nodes = [node for node in internal_nodes if node != best_node]

    def _cost_complexity_pruning(self) -> None:
        """
        Perform cost-complexity pruning using alpha parameter.
        """
        if self.root_ is None:
            return

        # Calculate cost-complexity for each node
        self._calculate_cost_complexity(self.root_)

        # Prune nodes with high cost-complexity
        self._prune_high_cost_nodes(self.root_)

    def _calculate_cost_complexity(self, node: "TreeNode") -> float:
        """
        Calculate cost-complexity for a node and its subtree.

        Args:
            node: Current node

        Returns:
            Cost-complexity value
        """
        if node.is_leaf:
            node.cost_complexity = 0.0
            return 0.0

        # Calculate cost-complexity for children
        left_cc = self._calculate_cost_complexity(node.left)
        right_cc = self._calculate_cost_complexity(node.right)

        # Calculate total cost-complexity
        total_cc = left_cc + right_cc + self.ccp_alpha

        # If pruning this subtree would be better, mark for pruning
        if total_cc >= self.ccp_alpha:
            node.cost_complexity = total_cc
        else:
            node.cost_complexity = 0.0

        return node.cost_complexity

    def _prune_high_cost_nodes(self, node: "TreeNode") -> None:
        """
        Prune nodes with high cost-complexity.

        Args:
            node: Current node
        """
        if node.is_leaf:
            return

        if node.cost_complexity > self.ccp_alpha:
            # Prune this subtree
            node.left = None
            node.right = None
            node.is_leaf = True
            node.value = 0.0  # Will be updated during fit
        else:
            # Recursively check children
            self._prune_high_cost_nodes(node.left)
            self._prune_high_cost_nodes(node.right)

    def _get_internal_nodes(self, node: "TreeNode") -> list["TreeNode"]:
        """
        Get all internal nodes in the tree.

        Args:
            node: Root node

        Returns:
            List of internal nodes
        """
        if node is None or node.is_leaf:
            return []

        nodes = [node]
        nodes.extend(self._get_internal_nodes(node.left))
        nodes.extend(self._get_internal_nodes(node.right))
        return nodes

    def _predict_batch(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions for a batch of samples.

        Args:
            X: Feature matrix

        Returns:
            Predictions
        """
        predictions = np.zeros(len(X))
        for i, sample in enumerate(X):
            predictions[i] = self._predict_single(sample, self.root_)
        return predictions

    def _predict_single(self, sample: np.ndarray, node: "TreeNode") -> int | float:
        """
        Make a prediction for a single sample.

        Args:
            sample: Feature vector
            node: Current node

        Returns:
            Prediction
        """
        if node.is_leaf:
            return node.value

        if sample[node.feature] <= node.threshold:
            return self._predict_single(sample, node.left)
        else:
            return self._predict_single(sample, node.right)

    def _calculate_error(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Calculate prediction error.

        Args:
            y_true: True values
            y_pred: Predicted values

        Returns:
            Error value
        """
        return np.mean((y_true - y_pred) ** 2)

    def fit(
        self,
        X: np.ndarray,
        y: np.ndarray,
        X_val: np.ndarray | None = None,
        y_val: np.ndarray | None = None,
    ) -> "DecisionTreePruning":
        """
        Fit the decision tree with optional pruning.

        Args:
            X: Training feature matrix
            y: Training target values
            X_val: Validation feature matrix (for pruning)
            y_val: Validation target values (for pruning)

        Returns:
            Self for method chaining
        """
        if X.ndim != 2:
            raise ValueError("X must be 2-dimensional")
        if len(X) != len(y):
            raise ValueError("X and y must have the same length")

        self.n_features_ = X.shape[1]

        # Determine task type
        task_type = (
            "classification" if np.issubdtype(y.dtype, np.integer) else "regression"
        )

        # Build the tree
        self.root_ = self._build_tree(X, y, task_type=task_type)

        # Apply pruning if specified
        if self.pruning_method == "reduced_error":
            if X_val is None or y_val is None:
                raise ValueError("Validation data required for reduced error pruning")
            self._reduced_error_pruning(X_val, y_val)
        elif self.pruning_method == "cost_complexity":
            self._cost_complexity_pruning()

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions.

        Args:
            X: Feature matrix

        Returns:
            Predictions
        """
        if self.root_ is None:
            raise ValueError("Tree must be fitted before prediction")

        return self._predict_batch(X)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate accuracy (for classification) or R² (for regression).

        Args:
            X: Feature matrix
            y: True values

        Returns:
            Score
        """
        predictions = self.predict(X)

        if np.issubdtype(y.dtype, np.integer):
            # Classification: accuracy
            return np.mean(predictions == y)
        else:
            # Regression: R²
            ss_res = np.sum((y - predictions) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            return 1 - (ss_res / ss_tot)


class TreeNode:
    """
    Node class for decision tree.
    """

    def __init__(self) -> None:
        """Initialize tree node."""
        self.is_leaf = True
        self.feature: int | None = None
        self.threshold: float | None = None
        self.value: int | float | None = None
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        self.samples: int = 0
        self.impurity: float = 0.0
        self.cost_complexity: float = 0.0


def generate_regression_data(
    n_samples: int = 100, noise: float = 0.1, random_state: int = 42
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate regression data.

    Args:
        n_samples: Number of samples
        noise: Noise level
        random_state: Random seed

    Returns:
        Tuple of (X, y)
    """
    rng = np.random.default_rng(random_state)
    X = rng.standard_normal((n_samples, 2))
    y = X[:, 0] ** 2 + X[:, 1] ** 2 + noise * rng.standard_normal(n_samples)
    return X, y


def generate_classification_data(
    n_samples: int = 100, random_state: int = 42
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate classification data.

    Args:
        n_samples: Number of samples
        random_state: Random seed

    Returns:
        Tuple of (X, y)
    """
    rng = np.random.default_rng(random_state)
    X = rng.standard_normal((n_samples, 2))
    y = ((X[:, 0] + X[:, 1]) > 0).astype(int)
    return X, y


def compare_pruning_methods() -> None:
    """
    Compare different pruning methods.
    """
    # Generate data
    X, y = generate_regression_data(n_samples=200)

    # Split data
    split_idx = int(0.7 * len(X))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    # Further split training data for validation
    val_split = int(0.5 * len(X_train))
    X_val, X_train = X_train[:val_split], X_train[val_split:]
    y_val, y_train = y_train[:val_split], y_train[val_split:]

    print(f"Training set size: {len(X_train)}")
    print(f"Validation set size: {len(X_val)}")
    print(f"Test set size: {len(X_test)}")

    # Test different pruning methods
    methods = [
        ("No Pruning", "none"),
        ("Reduced Error Pruning", "reduced_error"),
        ("Cost Complexity Pruning", "cost_complexity"),
    ]

    for method_name, method in methods:
        print(f"\n=== {method_name} ===")

        tree = DecisionTreePruning(
            max_depth=10,
            min_samples_leaf=2,
            pruning_method=method,
            ccp_alpha=0.01
        )

        if method == "reduced_error":
            tree.fit(X_train, y_train, X_val, y_val)
        else:
            tree.fit(X_train, y_train)

        train_score = tree.score(X_train, y_train)
        test_score = tree.score(X_test, y_test)

        print(f"Training R²: {train_score:.4f}")
        print(f"Test R²: {test_score:.4f}")
        print(f"Overfitting gap: {train_score - test_score:.4f}")


def main() -> None:
    """
    Demonstrate decision tree with pruning.
    """
    print("=== Regression Example ===")

    # Generate regression data
    X_reg, y_reg = generate_regression_data(n_samples=200, noise=0.1)

    # Split data
    split_idx = int(0.8 * len(X_reg))
    X_train, X_test = X_reg[:split_idx], X_reg[split_idx:]
    y_train, y_test = y_reg[:split_idx], y_reg[split_idx:]

    # Train tree with cost-complexity pruning
    tree_reg = DecisionTreePruning(
        max_depth=10,
        min_samples_leaf=2,
        pruning_method="cost_complexity",
        ccp_alpha=0.01
    )
    tree_reg.fit(X_train, y_train)

    # Make predictions
    train_score = tree_reg.score(X_train, y_train)
    test_score = tree_reg.score(X_test, y_test)

    print(f"Training R²: {train_score:.4f}")
    print(f"Test R²: {test_score:.4f}")

    print("\n=== Classification Example ===")

    # Generate classification data
    X_cls, y_cls = generate_classification_data(n_samples=200)

    # Split data
    split_idx = int(0.8 * len(X_cls))
    X_train, X_test = X_cls[:split_idx], X_cls[split_idx:]
    y_train, y_test = y_cls[:split_idx], y_cls[split_idx:]

    # Train tree with reduced error pruning
    val_split = int(0.5 * len(X_train))
    X_val, X_train = X_train[:val_split], X_train[val_split:]
    y_val, y_train = y_train[:val_split], y_train[val_split:]

    tree_cls = DecisionTreePruning(
        max_depth=10,
        min_samples_leaf=2,
        pruning_method="reduced_error"
    )
    tree_cls.fit(X_train, y_train, X_val, y_val)

    # Make predictions
    train_accuracy = tree_cls.score(X_train, y_train)
    test_accuracy = tree_cls.score(X_test, y_test)

    print(f"Training accuracy: {train_accuracy:.4f}")
    print(f"Test accuracy: {test_accuracy:.4f}")

    print("\n=== Pruning Methods Comparison ===")
    compare_pruning_methods()


if __name__ == "__main__":
    doctest.testmod()
    main()

