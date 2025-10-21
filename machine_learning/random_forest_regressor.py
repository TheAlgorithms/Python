"""Random Forest Regressor implementation from scratch.

References:
- https://en.wikipedia.org/wiki/Random_forest
- https://en.wikipedia.org/wiki/Decision_tree_learning
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

TreeNodeReg = Dict[str, Any]


class DecisionTreeRegressor:
    """
    A simple decision tree regressor implementation.

    Parameters
    ----------
    max_depth : int, optional (default=None)
        The maximum depth of the tree.
    min_samples_split : int, optional (default=2)
        The minimum number of samples required to split an internal node.

    Examples
    --------
    >>> x = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])
    >>> y = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    >>> tree = DecisionTreeRegressor(max_depth=2)
    >>> _ = tree.fit(x, y)
    >>> preds = tree.predict(x)
    >>> np.allclose(preds, y, atol=1.0)
    True
    """

    def __init__(self, max_depth: Optional[int] = None, min_samples_split: int = 2) -> None:
        self.max_depth: Optional[int] = max_depth
        self.min_samples_split: int = min_samples_split
        self.tree: Optional[TreeNodeReg] = None

    def fit(self, x: np.ndarray, y: np.ndarray) -> "DecisionTreeRegressor":
        """
        Build a decision tree regressor from the training set (x, y).

        Parameters
        ----------
        x : array-like of shape (n_samples, n_features)
            The training input samples.
        y : array-like of shape (n_samples,)
            The target values.

        Returns
        -------
        self : object
            Fitted estimator.
        """
        self.tree = self._grow_tree(x, y)
        return self

    def _grow_tree(self, x: np.ndarray, y: np.ndarray, depth: int = 0) -> TreeNodeReg:
        """
        Recursively grow the decision tree.

        Parameters
        ----------
        x : array-like of shape (n_samples, n_features)
            Training samples.
        y : array-like of shape (n_samples,)
            Target values.
        depth : int, optional (default=0)
            Current depth of the tree.

        Returns
        -------
        node : dict
            A node in the decision tree.
        """
        n_samples, n_features = x.shape
        # Stopping criteria
        if (
            (self.max_depth is not None and depth >= self.max_depth)
            or n_samples < self.min_samples_split
            or len(np.unique(y)) == 1
        ):
            return {"value": float(np.mean(y))}

        # Find the best split
        best_split = self._best_split(x, y, n_features)
        if best_split is None:
            return {"value": float(np.mean(y))}

        # Recursively build the tree
        left_indices = x[:, best_split["feature"]] <= best_split["threshold"]
        right_indices = ~left_indices
        left_subtree = self._grow_tree(x[left_indices], y[left_indices], depth + 1)
        right_subtree = self._grow_tree(x[right_indices], y[right_indices], depth + 1)
        return {
            "feature": int(best_split["feature"]),
            "threshold": float(best_split["threshold"]),
            "left": left_subtree,
            "right": right_subtree,
        }

    def _best_split(self, x: np.ndarray, y: np.ndarray, n_features: int) -> Optional[Dict[str, Any]]:
        """
        Find the best feature and threshold to split on.

        Parameters
        ----------
        x : array-like of shape (n_samples, n_features)
            Training samples.
        y : array-like of shape (n_samples,)
            Target values.
        n_features : int
            Number of features to consider.

        Returns
        -------
        best_split : dict or None
            The best split configuration.
        """
        best_mse = float("inf")
        best_split: Optional[Dict[str, Any]] = None
        for feature in range(n_features):
            thresholds = np.unique(x[:, feature])
            for threshold in thresholds:
                left_indices = x[:, feature] <= threshold
                right_indices = ~left_indices
                if np.sum(left_indices) == 0 or np.sum(right_indices) == 0:
                    continue
                mse = self._calculate_mse(y[left_indices], y[right_indices], len(y))
                if mse < best_mse:
                    best_mse = mse
                    best_split = {"feature": int(feature), "threshold": float(threshold)}
        return best_split

    def _calculate_mse(self, left_y: np.ndarray, right_y: np.ndarray, n_samples: int) -> float:
        """
        Calculate weighted mean squared error for a split.

        Parameters
        ----------
        left_y : array-like
            Target values in the left split.
        right_y : array-like
            Target values in the right split.
        n_samples : int
            Total number of samples.

        Returns
        -------
        mse : float
            Weighted mean squared error.
        """
        n_left, n_right = len(left_y), len(right_y)
        mse_left = float(np.var(left_y)) if n_left > 0 else 0.0
        mse_right = float(np.var(right_y)) if n_right > 0 else 0.0
        return (n_left / n_samples) * mse_left + (n_right / n_samples) * mse_right

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Predict target values for x.

        Parameters
        ----------
        x : array-like of shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y_pred : array-like of shape (n_samples,)
            The predicted values.
        """
        assert self.tree is not None
        return np.array([self._predict_sample(sample, self.tree) for sample in x])

    def _predict_sample(self, sample: np.ndarray, tree: TreeNodeReg) -> float:
        """
        Predict the target value for a single sample.

        Parameters
        ----------
        sample : array-like
            A single sample.
        tree : dict
            The decision tree node.

        Returns
        -------
        prediction : float
            The predicted value.
        """
        if "value" in tree:
            return float(tree["value"])
        if sample[int(tree["feature"])] <= float(tree["threshold"]):
            return self._predict_sample(sample, tree["left"])  # type: ignore[arg-type]
        return self._predict_sample(sample, tree["right"])  # type: ignore[arg-type]


class RandomForestRegressor:
    """
    Random Forest Regressor implementation from scratch.

    A random forest is an ensemble of decision trees, generally trained via
    the bagging method. The predictions are made by averaging the predictions
    of individual trees.

    Parameters
    ----------
    n_estimators : int, optional (default=100)
        The number of trees in the forest.
    max_depth : int, optional (default=None)
        The maximum depth of the trees.
    min_samples_split : int, optional (default=2)
        The minimum number of samples required to split an internal node.
    max_features : int, str or None, optional (default='sqrt')
        The number of features to consider when looking for the best split.
        - If int, then consider max_features features at each split.
        - If 'sqrt', then max_features=sqrt(n_features).
        - If None, then max_features=n_features.
    random_state : int or None, optional (default=None)
        Controls the randomness of the estimator.

    Examples
    --------
    >>> x = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
    >>> y = np.array([1.5, 2.5, 3.5])
    >>> rf = RandomForestRegressor(n_estimators=3, max_depth=2, random_state=42)
    >>> _ = rf.fit(x, y)
    >>> preds = rf.predict(x)
    >>> preds.shape
    (3,)
    """

    def __init__(
        self,
        n_estimators: int = 100,
        max_depth: Optional[int] = None,
        min_samples_split: int = 2,
        max_features: Optional["str|int"] = "sqrt",
        random_state: Optional[int] = None,
    ) -> None:
        self.n_estimators: int = n_estimators
        self.max_depth: Optional[int] = max_depth
        self.min_samples_split: int = min_samples_split
        self.max_features: Optional["str|int"] = max_features
        self.random_state: Optional[int] = random_state
        self.trees: List[Tuple[DecisionTreeRegressor, np.ndarray]] = []

    def fit(self, x: np.ndarray, y: np.ndarray) -> "RandomForestRegressor":
        """
        Build a random forest regressor from the training set (x, y).

        Parameters
        ----------
        x : array-like of shape (n_samples, n_features)
            The training input samples.
        y : array-like of shape (n_samples,)
            The target values.

        Returns
        -------
        self : object
            Fitted estimator.
        """
        rng = np.random.default_rng(self.random_state)
        x = np.array(x)
        y = np.array(y)
        n_samples, n_features = x.shape
        # Determine max_features
        if self.max_features == "sqrt":
            max_features = int(np.sqrt(n_features))
        elif self.max_features is None:
            max_features = n_features
        elif isinstance(self.max_features, int):
            max_features = int(self.max_features)
        else:
            raise ValueError("max_features must be int, 'sqrt', or None")

        self.trees = []
        for _ in range(self.n_estimators):
            # Bootstrap sampling
            indices = rng.choice(n_samples, n_samples, replace=True)
            x_bootstrap = x[indices]
            y_bootstrap = y[indices]
            # Feature sampling
            feature_indices = rng.choice(n_features, max_features, replace=False)
            x_bootstrap = x_bootstrap[:, feature_indices]
            # Train decision tree
            tree = DecisionTreeRegressor(max_depth=self.max_depth, min_samples_split=self.min_samples_split)
            tree.fit(x_bootstrap, y_bootstrap)
            self.trees.append((tree, feature_indices))
        return self

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Predict target values for x.

        Parameters
        ----------
        x : array-like of shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y_pred : array-like of shape (n_samples,)
            The predicted values (average of all tree predictions).
        """
        x = np.array(x)
        preds: List[np.ndarray] = []
        for tree, feature_indices in self.trees:
            x_subset = x[:, feature_indices]
            preds.append(tree.predict(x_subset))
        # Average predictions from all trees
        return np.mean(preds, axis=0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    from sklearn.datasets import make_regression
    from sklearn.metrics import mean_squared_error, r2_score
    from sklearn.model_selection import train_test_split

    # Generate synthetic regression data
    x, y = make_regression(n_samples=200, n_features=5, n_informative=3, noise=10, random_state=42)

    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    # Train the Random Forest Regressor
    rf_regressor = RandomForestRegressor(n_estimators=10, max_depth=5, random_state=42)
    rf_regressor.fit(x_train, y_train)

    # Make predictions
    y_pred = rf_regressor.predict(x_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.2f}")
    print(f"Number of trees: {len(rf_regressor.trees)}")
