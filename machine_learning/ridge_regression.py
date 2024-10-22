import numpy as np
import pandas as pd


class RidgeRegression:
    def __init__(self, alpha: float = 0.001, lambda_: float = 0.1, iterations: int = 1000) -> None:
        """
        Ridge Regression Constructor
        :param alpha: Learning rate for gradient descent
        :param lambda_: Regularization parameter (L2 regularization)
        :param iterations: Number of iterations for gradient descent
        """
        self.alpha = alpha
        self.lambda_ = lambda_
        self.iterations = iterations
        self.theta = None

    def feature_scaling(self, features: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
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

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the Ridge Regression model to the training data.

        :param X: Input features, shape (m, n)
        :param y: Target values, shape (m,)
        """
        X_scaled, mean, std = self.feature_scaling(X)  # Normalize features
        m, n = X_scaled.shape
        self.theta = np.zeros(n)  # Initialize weights to zeros

        for i in range(self.iterations):
            predictions = X_scaled.dot(self.theta)
            error = predictions - y

            # Compute gradient with L2 regularization
            gradient = (X_scaled.T.dot(error) + self.lambda_ * self.theta) / m
            self.theta -= self.alpha * gradient  # Update weights

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict values using the trained model.

        :param X: Input features, shape (m, n)
        :return: Predicted values, shape (m,)
        """
        X_scaled, _, _ = self.feature_scaling(X)  # Scale features using training data
        return X_scaled.dot(self.theta)

    def compute_cost(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Compute the cost function with regularization.

        :param X: Input features, shape (m, n)
        :param y: Target values, shape (m,)
        :return: Computed cost
        """
        X_scaled, _, _ = self.feature_scaling(X)  # Scale features using training data
        m = len(y)
        predictions = X_scaled.dot(self.theta)
        cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2) + (
            self.lambda_ / (2 * m)
        ) * np.sum(self.theta**2)
        return cost

    def mean_absolute_error(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Compute Mean Absolute Error (MAE) between true and predicted values.

        :param y_true: Actual target values, shape (m,)
        :param y_pred: Predicted target values, shape (m,)
        :return: MAE
        """
        return np.mean(np.abs(y_true - y_pred))


# Example usage
if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv"
    )
    X = df[["Rating"]].values  # Feature: Rating
    y = df["ADR"].values  # Target: ADR
    y = (y - np.mean(y)) / np.std(y)

    # Add bias term (intercept) to the feature matrix
    X = np.c_[np.ones(X.shape[0]), X]  # Add intercept term

    # Initialize and train the Ridge Regression model
    model = RidgeRegression(alpha=0.01, lambda_=0.1, iterations=1000)
    model.fit(X, y)

    # Predictions
    predictions = model.predict(X)

    # Results
    print("Optimized Weights:", model.theta)
    print("Cost:", model.compute_cost(X, y))
    print("Mean Absolute Error:", model.mean_absolute_error(y, predictions))
