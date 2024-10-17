"""
Ridge Regression is a type of linear regression that includes an L2 regularization term 
to prevent overfitting and improve generalization. It is commonly used when multicollinearity 
occurs, as it helps to reduce the model's complexity by penalizing large coefficients, 
resulting in better prediction performance on unseen data.

This implementation uses gradient descent to optimize the weights, with an L2 penalty to 
regularize the feature vector. The code reads a dataset with Average Damage per Round (ADR) 
and player ratings, processes the data, and applies ridge regression to predict ADR 
based on player ratings.

WIKI: https://en.wikipedia.org/wiki/Ridge_regression
"""

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error

class RidgeRegression:
    """
    A Ridge Regression model with L2 regularization.

    Attributes:
        learning_rate (float): Step size for gradient descent optimization.
        regularization_param (float): Regularization strength (lambda), penalizing large weights.
        num_iterations (int): Number of iterations for gradient descent.
        weights (np.ndarray): Feature weights.
        bias (float): Bias term for the regression model.
    """
    def __init__(self, learning_rate=0.01, regularization_param=0.1, num_iterations=1000):
        self.learning_rate = learning_rate
        self.regularization_param = regularization_param
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        """
        Fits the ridge regression model to the data using gradient descent.

        Args:
            X (np.ndarray): Input features.
            y (np.ndarray): Target variable.

        >>> model = RidgeRegression(learning_rate=0.01, regularization_param=0.1, num_iterations=1000)
        >>> X = np.array([[1], [2], [3], [4]])
        >>> y = np.array([2, 3, 4, 5])
        >>> model.fit(X, y)
        >>> round(model.weights[0], 2)
        0.86
        """
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)

        for i in range(self.num_iterations):
            y_pred = self.predict(X)
            error = y_pred - y

            # Calculate gradients with L2 regularization
            dw = (1 / num_samples) * (X.T.dot(error) + self.regularization_param * self.weights)
            db = (1 / num_samples) * np.sum(error)

            # Update weights and bias
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        """
        Predicts target values for the input data X using the trained model.

        Args:
            X (np.ndarray): Input features for which to predict target values.

        Returns:
            np.ndarray: Predicted target values.

        >>> model = RidgeRegression()
        >>> model.weights, model.bias = np.array([0.5]), 1
        >>> X = np.array([[1], [2], [3]])
        >>> model.predict(X)
        array([1.5, 2. , 2.5])
        """
        return X.dot(self.weights) + self.bias

    def calculate_error(self, X, y):
        """
        Calculates the Mean Squared Error (MSE) between the predicted and actual target values.

        Args:
            X (np.ndarray): Input features.
            y (np.ndarray): Actual target values.

        Returns:
            float: Mean Squared Error (MSE).

        >>> model = RidgeRegression()
        >>> model.weights, model.bias = np.array([0.5]), 1
        >>> X = np.array([[1], [2], [3]])
        >>> y = np.array([1.5, 2.5, 3.5])
        >>> round(model.calculate_error(X, y), 2)
        0.0
        """
        y_pred = self.predict(X)
        return np.mean((y - y_pred) ** 2)  # Mean squared error

    def calculate_mae(self, X, y):
        """
        Calculates the Mean Absolute Error (MAE) between the predicted and actual target values.

        Args:
            X (np.ndarray): Input features.
            y (np.ndarray): Actual target values.

        Returns:
            float: Mean Absolute Error (MAE).

        >>> model = RidgeRegression()
        >>> model.weights, model.bias = np.array([0.5]), 1
        >>> X = np.array([[1], [2], [3]])
        >>> y = np.array([1.5, 2.5, 3.5])
        >>> round(model.calculate_mae(X, y), 2)
        0.0
        """
        y_pred = self.predict(X)
        return mean_absolute_error(y, y_pred)

# Load data
def load_data(filepath):
    """
    Loads data from a CSV file, extracting 'PlayerRating' as the feature 
    and 'ADR' as the target variable.

    Args:
        filepath (str): Path to the CSV file containing data.

    Returns:
        tuple: (X, y) where X is the feature array and y is the target array.

    >>> data = load_data('player_data.csv')
    >>> isinstance(data[0], np.ndarray) and isinstance(data[1], np.ndarray)
    True
    """
    data = pd.read_csv(filepath)
    X = data[['PlayerRating']].values  # Feature
    y = data['ADR'].values  # Target
    return X, y

# Example usage
if __name__ == "__main__":
    """
    Ridge Regression model for predicting Average Damage per Round (ADR) based on player ratings.

    The model is initialized with a learning rate, regularization parameter, and a specified 
    number of gradient descent iterations. After training, it outputs the optimized weights 
    and bias, and displays the Mean Squared Error (MSE) and Mean Absolute Error (MAE).

    >>> model = RidgeRegression(learning_rate=0.01, regularization_param=0.5, num_iterations=1000)
    >>> X, y = load_data('player_data.csv')
    >>> model.fit(X, y)
    >>> isinstance(model.weights, np.ndarray) and isinstance(model.bias, float)
    True
    """
    import doctest

    doctest.testmod()

    # Load and preprocess the data
    filepath = 'player_data.csv'  # Replace with actual file path
    X, y = load_data(filepath)

    # Initialize and train the model
    model = RidgeRegression(learning_rate=0.01, regularization_param=0.5, num_iterations=1000)
    model.fit(X, y)

    # Calculate and display errors
    mse = model.calculate_error(X, y)
    mae = model.calculate_mae(X, y)
    
    print(f"Optimized weights: {model.weights}")
    print(f"Bias: {model.bias}")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
