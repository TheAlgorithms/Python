import numpy as np
import pandas as pd


class RidgeRegression:
    def __init__(
        self,
        alpha: float = 0.001,
        regularization_param: float = 0.1,
        num_iterations: int = 1000,
    ) -> None:
        self.alpha: float = alpha
        self.regularization_param: float = regularization_param
        self.num_iterations: int = num_iterations
        self.theta: np.ndarray = None

    def feature_scaling(
        self, features: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        mean = np.mean(features, axis=0)
        std = np.std(features, axis=0)

        # avoid division by zero for constant features (std = 0)
        std[std == 0] = 1  # set std=1 for constant features to avoid NaN

        features_scaled = (features - mean) / std
        return features_scaled, mean, std

    def fit(self, features: np.ndarray, target: np.ndarray) -> None:
        features_scaled, mean, std = self.feature_scaling(features)
        m, n = features_scaled.shape
        self.theta = np.zeros(n)  # initializing weights to zeros

        for _ in range(self.num_iterations):
            predictions = features_scaled.dot(self.theta)
            error = predictions - target

            # computing gradient with L2 regularization
            gradient = (
                features_scaled.T.dot(error) + self.regularization_param * self.theta
            ) / m
            self.theta -= self.alpha * gradient  # updating weights

    def predict(self, features: np.ndarray) -> np.ndarray:
        features_scaled, _, _ = self.feature_scaling(features)
        return features_scaled.dot(self.theta)

    def compute_cost(self, features: np.ndarray, target: np.ndarray) -> float:
        features_scaled, _, _ = self.feature_scaling(features)
        m = len(target)

        predictions = features_scaled.dot(self.theta)
        cost = (1 / (2 * m)) * np.sum((predictions - target) ** 2) + (
            self.regularization_param / (2 * m)
        ) * np.sum(self.theta**2)
        return cost

    def mean_absolute_error(self, target: np.ndarray, predictions: np.ndarray) -> float:
        return np.mean(np.abs(target - predictions))


# Example usage
if __name__ == "__main__":
    data = pd.read_csv("ADRvsRating.csv")
    features_matrix = data[["Rating"]].to_numpy()
    target = data["ADR"].to_numpy()
    target = (target - np.mean(target)) / np.std(target)

    # added bias term to the feature matrix
    x = np.c_[np.ones(features_matrix.shape[0]), features_matrix]

    # initialize and train the ridge regression model
    model = RidgeRegression(alpha=0.01, regularization_param=0.1, num_iterations=1000)
    model.fit(features_matrix, target)

    # predictions
    predictions = model.predict(features_matrix)

    # results
    print("Optimized Weights:", model.theta)
    print("Cost:", model.compute_cost(features_matrix, target))
    print("Mean Absolute Error:", model.mean_absolute_error(target, predictions))
