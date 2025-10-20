"""Random Forest Regressor implementation from scratch."""

import numpy as np
from collections import Counter


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
    >>> X = np.array([[1], [2], [3], [4], [5]])
    >>> y = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    >>> tree = DecisionTreeRegressor(max_depth=2)
    >>> tree.fit(X, y)
    >>> predictions = tree.predict(X)
    >>> np.allclose(predictions, y, atol=0.5)
    True
    """

    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def fit(self, X, y):
        """
        Build a decision tree regressor from the training set (X, y).

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The training input samples.
        y : array-like of shape (n_samples,)
            The target values.

        Returns
        -------
        self : object
            Fitted estimator.
        """
        self.tree = self._grow_tree(X, y)
        return self

    def _grow_tree(self, X, y, depth=0):
        """
        Recursively grow the decision tree.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
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
        n_samples, n_features = X.shape

        # Stopping criteria
        if (
            depth == self.max_depth
            or n_samples < self.min_samples_split
            or len(np.unique(y)) == 1
        ):
            return {"value": np.mean(y)}

        # Find the best split
        best_split = self._best_split(X, y, n_features)
        if best_split is None:
            return {"value": np.mean(y)}

        # Recursively build the tree
        left_indices = X[:, best_split["feature"]] <= best_split["threshold"]
        right_indices = ~left_indices

        left_subtree = self._grow_tree(X[left_indices], y[left_indices], depth + 1)
        right_subtree = self._grow_tree(X[right_indices], y[right_indices], depth + 1)

        return {
            "feature": best_split["feature"],
            "threshold": best_split["threshold"],
            "left": left_subtree,
            "right": right_subtree,
        }

    def _best_split(self, X, y, n_features):
        """
        Find the best feature and threshold to split on.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
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
        best_split = None

        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_indices = X[:, feature] <= threshold
                right_indices = ~left_indices

                if np.sum(left_indices) == 0 or np.sum(right_indices) == 0:
                    continue

                mse = self._calculate_mse(y[left_indices], y[right_indices], len(y))

                if mse < best_mse:
                    best_mse = mse
                    best_split = {"feature": feature, "threshold": threshold}

        return best_split

    def _calculate_mse(self, left_y, right_y, n_samples):
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
        mse_left = np.var(left_y) if n_left > 0 else 0
        mse_right = np.var(right_y) if n_right > 0 else 0
        return (n_left / n_samples) * mse_left + (n_right / n_samples) * mse_right

    def predict(self, X):
        """
        Predict target values for X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y_pred : array-like of shape (n_samples,)
            The predicted values.
        """
        return np.array([self._predict_sample(sample, self.tree) for sample in X])

    def _predict_sample(self, sample, tree):
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
            return tree["value"]

        if sample[tree["feature"]] <= tree["threshold"]:
            return self._predict_sample(sample, tree["left"])
        return self._predict_sample(sample, tree["right"])


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
    >>> X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    >>> y = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    >>> rf = RandomForestRegressor(n_estimators=5, max_depth=2, random_state=42)
    >>> rf.fit(X, y)
    >>> predictions = rf.predict(X)
    >>> len(predictions) == len(y)
    True
    >>> np.all((predictions >= y.min()) & (predictions <= y.max()))
    True
    """

    def __init__(
        self,
        n_estimators=100,
        max_depth=None,
        min_samples_split=2,
        max_features="sqrt",
        random_state=None,
    ):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.random_state = random_state
        self.trees = []

    def fit(self, X, y):
        """
        Build a random forest regressor from the training set (X, y).

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The training input samples.
        y : array-like of shape (n_samples,)
            The target values.

        Returns
        -------
        self : object
            Fitted estimator.
        """
        np.random.seed(self.random_state)
        X = np.array(X)
        y = np.array(y)

        n_samples, n_features = X.shape

        # Determine max_features
        if self.max_features == "sqrt":
            max_features = int(np.sqrt(n_features))
        elif self.max_features is None:
            max_features = n_features
        else:
            max_features = self.max_features

        self.trees = []
        for _ in range(self.n_estimators):
            # Bootstrap sampling
            indices = np.random.choice(n_samples, n_samples, replace=True)
            X_bootstrap = X[indices]
            y_bootstrap = y[indices]

            # Feature sampling
            feature_indices = np.random.choice(n_features, max_features, replace=False)
            X_bootstrap = X_bootstrap[:, feature_indices]

            # Train decision tree
            tree = DecisionTreeRegressor(
                max_depth=self.max_depth, min_samples_split=self.min_samples_split
            )
            tree.fit(X_bootstrap, y_bootstrap)

            self.trees.append((tree, feature_indices))

        return self

    def predict(self, X):
        """
        Predict target values for X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y_pred : array-like of shape (n_samples,)
            The predicted values (average of all tree predictions).
        """
        X = np.array(X)
        predictions = []

        for tree, feature_indices in self.trees:
            X_subset = X[:, feature_indices]
            predictions.append(tree.predict(X_subset))

        # Average predictions from all trees
        return np.mean(predictions, axis=0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    from sklearn.datasets import make_regression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score

    # Generate synthetic regression data
    X, y = make_regression(
        n_samples=200, n_features=5, n_informative=3, noise=10, random_state=42
    )

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Train the Random Forest Regressor
    rf_regressor = RandomForestRegressor(n_estimators=10, max_depth=5, random_state=42)
    rf_regressor.fit(X_train, y_train)

    # Make predictions
    y_pred = rf_regressor.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.2f}")
    print(f"Number of trees: {len(rf_regressor.trees)}")
