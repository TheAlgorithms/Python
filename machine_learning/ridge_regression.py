import numpy as np
import pandas as pd


class RidgeRegression:
    def __init__(
        self, alpha: float = 0.001, lambda_: float = 0.1, iterations: int = 1000
    ) -> None:
        """
        Ridge Regression Constructor
        :param alpha: Learning rate for gradient descent
        :param lambda_: Regularization parameter (L2 regularization)
        :param iterations: Number of iterations for gradient descent
        """
        self.alpha = alpha
        self.lambda_ = lambda_
        self.iterations = iterations
        self.theta: np.ndarray | None = (
            None  # Initialize as None, later will be ndarray
        )

    def feature_scaling(
        self, features: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Normalize features to have mean 0 and standard deviation 1.

        :param features: Input features, shape (m, n)
        :return: Tuple containing:
            - Scaled features
            - Mean of each feature
            - Standard deviation of each feature

        Example:
        >>> rr = RidgeRegression()
        >>> features = np.array([[1, 2], [2, 3], [4, 6]])
        >>> scaled_features, mean, std = rr.feature_scaling(features)
        >>> np.allclose(scaled_features.mean(axis=0), 0)
        True
        >>> np.allclose(scaled_features.std(axis=0), 1)
        True
        """
        mean = np.mean(features, axis=0)
        std = np.std(features, axis=0)

        # Avoid division by zero for constant features (std = 0)
        std[std == 0] = 1  # Set std=1 for constant features to avoid NaN

        scaled_features = (features - mean) / std
        return scaled_features, mean, std

    def fit(self, features: np.ndarray, target: np.ndarray) -> None:
        """
        Fit the Ridge Regression model to the training data.

        :param features: Input features, shape (m, n)
        :param target: Target values, shape (m,)

        Example:
        >>> rr = RidgeRegression(alpha=0.01, lambda_=0.1, iterations=10)
        >>> features = np.array([[1, 2], [2, 3], [4, 6]])
        >>> target = np.array([1, 2, 3])
        >>> rr.fit(features, target)
        >>> rr.theta is not None
        True
        """
        features_scaled, mean, std = self.feature_scaling(
            features
        )  # Normalize features
        m, n = features_scaled.shape
        self.theta = np.zeros(n)  # Initialize weights to zeros

        for _ in range(self.iterations):
            predictions = features_scaled.dot(self.theta)
            error = predictions - target

            # Compute gradient with L2 regularization
            gradient = (features_scaled.T.dot(error) + self.lambda_ * self.theta) / m
            self.theta -= self.alpha * gradient  # Update weights

    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Predict values using the trained model.

        :param features: Input features, shape (m, n)
        :return: Predicted values, shape (m,)

        Example:
        >>> rr = RidgeRegression(alpha=0.01, lambda_=0.1, iterations=10)
        >>> features = np.array([[1, 2], [2, 3], [4, 6]])
        >>> target = np.array([1, 2, 3])
        >>> rr.fit(features, target)
        >>> predictions = rr.predict(features)
        >>> predictions.shape == target.shape
        True
        """
        if self.theta is None:
            raise ValueError("Model is not trained yet. Call the `fit` method first.")

        features_scaled, _, _ = self.feature_scaling(
            features
        )  # Scale features using training data
        return features_scaled.dot(self.theta)

    def compute_cost(self, features: np.ndarray, target: np.ndarray) -> float:
        """
        Compute the cost function with regularization.

        :param features: Input features, shape (m, n)
        :param target: Target values, shape (m,)
        :return: Computed cost

        Example:
        >>> rr = RidgeRegression(alpha=0.01, lambda_=0.1, iterations=10)
        >>> features = np.array([[1, 2], [2, 3], [4, 6]])
        >>> target = np.array([1, 2, 3])
        >>> rr.fit(features, target)
        >>> cost = rr.compute_cost(features, target)
        >>> isinstance(cost, float)
        True
        """
        if self.theta is None:
            raise ValueError("Model is not trained yet. Call the `fit` method first.")

        features_scaled, _, _ = self.feature_scaling(
            features
        )  # Scale features using training data
        m = len(target)
        predictions = features_scaled.dot(self.theta)
        cost = (1 / (2 * m)) * np.sum((predictions - target) ** 2) + (
            self.lambda_ / (2 * m)
        ) * np.sum(self.theta**2)
        return cost

    def mean_absolute_error(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Compute Mean Absolute Error (MAE) between true and predicted values.

        :param y_true: Actual target values, shape (m,)
        :param y_pred: Predicted target values, shape (m,)
        :return: MAE

        Example:
        >>> rr = RidgeRegression(alpha=0.01, lambda_=0.1, iterations=10)
        >>> y_true = np.array([1, 2, 3])
        >>> y_pred = np.array([1.1, 2.1, 2.9])
        >>> mae = rr.mean_absolute_error(y_true, y_pred)
        >>> isinstance(mae, float)
        True
        """
        return np.mean(np.abs(y_true - y_pred))


# Example usage
if __name__ == "__main__":
    # Load dataset
    data = pd.read_csv(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv"
    )
    data_x = data[["Rating"]].to_numpy()  # Feature: Rating
    data_y = data["ADR"].to_numpy()  # Target: ADR
    data_y = (data_y - np.mean(data_y)) / np.std(data_y)

    # Add bias term (intercept) to the feature matrix
    data_x = np.c_[np.ones(data_x.shape[0]), data_x]  # Add intercept term

    # Initialize and train the Ridge Regression model
    model = RidgeRegression(alpha=0.01, lambda_=0.1, iterations=1000)
    model.fit(data_x, data_y)

    # Predictions
    predictions = model.predict(data_x)

    # Results
    print("Optimized Weights:", model.theta)
    print("Cost:", model.compute_cost(data_x, data_y))
    print("Mean Absolute Error:", model.mean_absolute_error(data_y, predictions))
