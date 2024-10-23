import numpy as np
import pandas as pd


class RidgeRegression:
    def __init__(self, alpha=0.001, regularization_param=0.1, num_iterations=1000):
        self.alpha = alpha
        self.regularization_param = regularization_param
        self.num_iterations = num_iterations
        self.theta = None

    def feature_scaling(self, X):
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)

        # avoid division by zero for constant features (std = 0)
        std[std == 0] = 1  # set std=1 for constant features to avoid NaN

        X_scaled = (X - mean) / std
        return X_scaled, mean, std

    def fit(self, X, y):
        X_scaled, mean, std = self.feature_scaling(X)
        m, n = X_scaled.shape
        self.theta = np.zeros(n)  # initializing weights to zeros

        for i in range(self.num_iterations):
            predictions = X_scaled.dot(self.theta)
            error = predictions - y

            # computing gradient with L2 regularization
            gradient = (
                X_scaled.T.dot(error) + self.regularization_param * self.theta
            ) / m
            self.theta -= self.alpha * gradient  # updating weights

    def predict(self, X):
        X_scaled, _, _ = self.feature_scaling(X)
        return X_scaled.dot(self.theta)

    def compute_cost(self, X, y):
        X_scaled, _, _ = self.feature_scaling(X)
        m = len(y)

        predictions = X_scaled.dot(self.theta)
        cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2) + (
            self.regularization_param / (2 * m)
        ) * np.sum(self.theta**2)
        return cost

    def mean_absolute_error(self, y_true, y_pred):
        return np.mean(np.abs(y_true - y_pred))


# Example usage
if __name__ == "__main__":
    df = pd.read_csv("ADRvsRating.csv")
    X = df[["Rating"]].values
    y = df["ADR"].values
    y = (y - np.mean(y)) / np.std(y)

    # Add bias term (intercept) to the feature matrix
    X = np.c_[np.ones(X.shape[0]), X]

    # initialize and train the Ridge Regression model
    model = RidgeRegression(alpha=0.01, regularization_param=0.1, num_iterations=1000)
    model.fit(X, y)

    # predictions
    predictions = model.predict(X)

    # results
    print("Optimized Weights:", model.theta)
    print("Cost:", model.compute_cost(X, y))
    print("Mean Absolute Error:", model.mean_absolute_error(y, predictions))
