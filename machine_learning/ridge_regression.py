"""
Ridge Regression with L2 Regularization using Gradient Descent.

Ridge Regression is a type of linear regression that includes an L2 regularization
term to prevent overfitting and improve generalization. It is commonly used when
multicollinearity is present in the data.

More on Ridge Regression: https://en.wikipedia.org/wiki/Tikhonov_regularization
"""

from typing import Tuple
import numpy as np
import pandas as pd

def load_data(file_path: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load data from a CSV file and return features and target arrays.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A tuple containing features (X) and target (y) as numpy arrays.

    Example:
    >>> data = pd.DataFrame({'ADR': [200, 220], 'Rating': [1.2, 1.4]})
    >>> data.to_csv('sample.csv', index=False)
    >>> X, y = load_data('sample.csv')
    >>> X.shape == (2, 1) and y.shape == (2,)
    True
    """
    data = pd.read_csv(file_path)
    X = data[['Rating']].to_numpy()  # Use .to_numpy() instead of .values (PD011)
    y = data['ADR'].to_numpy()
    return X, y

def ridge_gradient_descent(
    X: np.ndarray, y: np.ndarray, reg_lambda: float, learning_rate: float,
    num_iters: int = 1000
) -> np.ndarray:
    """
    Perform Ridge Regression using gradient descent.

    Args:
        X: Feature matrix.
        y: Target vector.
        reg_lambda: Regularization parameter (lambda).
        learning_rate: Learning rate for gradient descent.
        num_iters: Number of iterations for gradient descent.

    Returns:
        Optimized weights (coefficients) for predicting ADR from Rating.

    Example:
    >>> X = np.array([[1.2], [1.4]])
    >>> y = np.array([200, 220])
    >>> ridge_gradient_descent(X, y, reg_lambda=0.1, learning_rate=0.01).shape == (1,)
    True
    """
    weights = np.zeros(X.shape[1])
    m = len(y)

    for _ in range(num_iters):
        predictions = X @ weights
        error = predictions - y
        gradient = (X.T @ error + reg_lambda * weights) / m
        weights -= learning_rate * gradient

    return weights

def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the Mean Absolute Error (MAE) between true and predicted values.

    Args:
        y_true: Actual values.
        y_pred: Predicted values.

    Returns:
        Mean absolute error.

    Example:
    >>> mean_absolute_error(np.array([200, 220]), np.array([205, 215]))
    5.0
    """
    return np.mean(np.abs(y_true - y_pred))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Load the data
    X, y = load_data("sample.csv")

    # Fit the Ridge Regression model
    optimized_weights = ridge_gradient_descent(X, y, reg_lambda=0.1, learning_rate=0.01)

    # Make predictions
    y_pred = X @ optimized_weights

    # Calculate Mean Absolute Error
    mae = mean_absolute_error(y, y_pred)
    print("Optimized Weights:", optimized_weights)
    print("Mean Absolute Error:", mae)
