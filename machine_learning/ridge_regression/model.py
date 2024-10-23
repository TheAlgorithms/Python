import numpy as np
import pandas as pd


class RidgeRegression:
    def __init__(self, alpha:float=0.001, regularization_param:float=0.1, num_iterations:int=1000) -> None:
        self.alpha:float = alpha
        self.regularization_param:float = regularization_param
        self.num_iterations:int = num_iterations
        self.theta:np.ndarray = None

<<<<<<< HEAD

    def feature_scaling(self, X:np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
=======
    def feature_scaling(self, X):
>>>>>>> d4fc2bf852ec4a023380f4ef367edefa88fd6881
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)

        # avoid division by zero for constant features (std = 0)
        std[std == 0] = 1  # set std=1 for constant features to avoid NaN

        X_scaled = (X - mean) / std
        return X_scaled, mean, std

    def fit(self, X:np.ndarray, y:np.ndarray) -> None:
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

    def predict(self, X:np.ndarray) -> np.ndarray:
        X_scaled, _, _ = self.feature_scaling(X)
        return X_scaled.dot(self.theta)

<<<<<<< HEAD
    def compute_cost(self, X:np.ndarray, y:np.ndarray) -> float:
        X_scaled, _, _ = self.feature_scaling(X)  
=======
    def compute_cost(self, X, y):
        X_scaled, _, _ = self.feature_scaling(X)
>>>>>>> d4fc2bf852ec4a023380f4ef367edefa88fd6881
        m = len(y)

        predictions = X_scaled.dot(self.theta)
        cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2) + (
            self.regularization_param / (2 * m)
        ) * np.sum(self.theta**2)
        return cost

    def mean_absolute_error(self, y_true:np.ndarray, y_pred:np.ndarray) -> float:
        return np.mean(np.abs(y_true - y_pred))


# Example usage
if __name__ == "__main__":
    df = pd.read_csv("ADRvsRating.csv")
    X = df[["Rating"]].values
    y = df["ADR"].values
    y = (y - np.mean(y)) / np.std(y)

<<<<<<< HEAD
    # added bias term to the feature matrix
    X = np.c_[np.ones(X.shape[0]), X] 
=======
    # Add bias term (intercept) to the feature matrix
    X = np.c_[np.ones(X.shape[0]), X]
>>>>>>> d4fc2bf852ec4a023380f4ef367edefa88fd6881

    # initialize and train the ridge regression model
    model = RidgeRegression(alpha=0.01, regularization_param=0.1, num_iterations=1000)
    model.fit(X, y)

    # predictions
    predictions = model.predict(X)

    # results
    print("Optimized Weights:", model.theta)
    print("Cost:", model.compute_cost(X, y))
    print("Mean Absolute Error:", model.mean_absolute_error(y, predictions))
