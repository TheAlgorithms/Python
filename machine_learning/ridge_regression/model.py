import numpy as np
import pandas as pd


class RidgeRegression:
    def __init__(self,
            alpha: float = 0.001,
            regularization_param: float = 0.1,
            num_iterations: int = 1000,
            ) -> None:
        self.alpha: float = alpha
        self.regularization_param: float = regularization_param
        self.num_iterations: int = num_iterations
        self.theta: np.ndarray = None

    def feature_scaling(
        self, X: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)

        # avoid division by zero for constant features (std = 0)
        std[std == 0] = 1  # set std=1 for constant features to avoid NaN

        x_scaled = (x - mean) / std
        return x_scaled, mean, std

    def fit(self, x: np.ndarray, y: np.ndarray) -> None:
        x_scaled, mean, std = self.feature_scaling(x)
        m, n = x_scaled.shape
        self.theta = np.zeros(n)  # initializing weights to zeros

        for i in range(self.num_iterations):
            predictions = x_scaled.dot(self.theta)
            error = predictions - y

            # computing gradient with L2 regularization
            gradient = (
                x_scaled.T.dot(error) + self.regularization_param * self.theta
            ) / m
            self.theta -= self.alpha * gradient  # updating weights

    def predict(self, X: np.ndarray) -> np.ndarray:
        X_scaled, _, _ = self.feature_scaling(X)
        return X_scaled.dot(self.theta)

    def compute_cost(self, x: np.ndarray, y: np.ndarray) -> float:
        x_scaled, _, _ = self.feature_scaling(x)
        m = len(y)

        predictions = x_scaled.dot(self.theta)
        cost = (
            1 / (2 * m)) * np.sum((predictions - y) ** 2) + (
                self.regularization_param / (2 * m)
                ) * np.sum(self.theta**2)
        return cost

    def mean_absolute_error(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        return np.mean(np.abs(y_true - y_pred))


# Example usage
if __name__ == "__main__":
    df = pd.read_csv("ADRvsRating.csv")
    x = df[["Rating"]].values
    y = df["ADR"].values
    y = (y - np.mean(y)) / np.std(y)

    # added bias term to the feature matrix
    x = np.c_[np.ones(x.shape[0]), x]

    # initialize and train the ridge regression model
    model = RidgeRegression(alpha=0.01, regularization_param=0.1, num_iterations=1000)
    model.fit(x, y)

    # predictions
    predictions = model.predict(x)

    # results
    print("Optimized Weights:", model.theta)
    print("Cost:", model.compute_cost(x, y))
    print("Mean Absolute Error:", model.mean_absolute_error(y, predictions))
