# XGBoost Regressor Example
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


class SimpleXGBoostRegressor:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def _negative_gradient(self, y_true, y_pred):
        """Compute the negative gradient (residuals) for regression."""
        return y_true - y_pred

    def _update_predictions(self, predictions, residuals):
        """Update the predictions using the residuals and learning rate."""
        return predictions + self.learning_rate * residuals

    def fit(self, X, y):
        """Fit the model using gradient boosting."""
        # Initialize predictions as the average of the target
        predictions = np.full(y.shape, np.mean(y))

        for _ in range(self.n_estimators):
            # Compute residuals (negative gradient)
            residuals = self._negative_gradient(y, predictions)

            # Fit a weak learner (decision tree) to the residuals
            tree = DecisionTreeRegressor(max_depth=self.max_depth)
            tree.fit(X, residuals)

            # Update the predictions
            predictions = self._update_predictions(predictions, tree.predict(X))

            # Store the tree
            self.trees.append(tree)

    def predict(self, X):
        """Make predictions by summing the weak learners' outputs."""
        predictions = np.zeros(X.shape[0])

        for tree in self.trees:
            predictions += self.learning_rate * tree.predict(X)

        return predictions


def data_handling(data: dict) -> tuple:
    # Split dataset into features and target.  Data is features.
    """
    >>> data_handling((
    ...  {'data':'[ 8.3252 41. 6.9841269 1.02380952  322. 2.55555556   37.88 -122.23 ]'
    ...  ,'target':([4.526])}))
    ('[ 8.3252 41. 6.9841269 1.02380952  322. 2.55555556   37.88 -122.23 ]', [4.526])
    """
    return (data["data"], data["target"])


def main() -> None:
    """
    The URL for this algorithm
    https://xgboost.readthedocs.io/en/stable/
    California house price dataset is used to demonstrate the algorithm.

    Expected error values:
    Mean Absolute Error: 0.30957163379906033
    Mean Square Error: 0.22611560196662744
    """
    # Load California house price dataset
    california = fetch_california_housing()
    data, target = data_handling(california)
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=1
    )
    xgboost_regressor = SimpleXGBoostRegressor(n_estimators=50, learning_rate=0.1, max_depth=3)
    xgboost_regressor.fit(x_train, y_train)
    predictions = xgboost_regressor.predict(x_test)
    # Error printing
    print(f"Mean Absolute Error: {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error: {mean_squared_error(y_test, predictions)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()