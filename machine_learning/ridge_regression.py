"""
Ridge Regression using Gradient Descent.

This script implements Ridge Regression (L2 regularization) using gradient descent.
It predicts Average Damage per Round (ADR) using player ratings.

Author: Nitin Pratap Singh
"""

import numpy as np
import httpx


def collect_dataset():
    """
    Collects CSGO dataset from a remote CSV file.

    The CSV contains ADR vs Rating of players.

    :return: Numpy array of shape (n_samples, 2)

    >>> data = collect_dataset()
    >>> data.shape[1]
    2
    """
    response = httpx.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    lines = response.text.splitlines()
    data = [line.split(",") for line in lines]
    data.pop(0)  # Remove header
    dataset = np.array(data, dtype=float)
    return dataset


def ridge_cost_function(X, y, theta, lam):
    """
    Computes the cost for Ridge Regression (L2 regularization).

    :param X: Feature matrix (n_samples, n_features)
    :param y: Target vector (n_samples,)
    :param theta: Coefficients (n_features,)
    :param lam: Regularization strength (lambda)
    :return: Cost value (float)

    >>> X = np.array([[1, 1], [1, 2]])
    >>> y = np.array([1, 2])
    >>> theta = np.zeros(2)
    >>> round(ridge_cost_function(X, y, theta, 0.1), 2)
    1.25
    """
    m = len(y)
    predictions = X @ theta
    error = predictions - y
    cost = (1 / (2 * m)) * np.dot(error, error)
    reg_cost = (lam / (2 * m)) * np.dot(theta[1:], theta[1:])
    return cost + reg_cost


def ridge_gradient_descent(X, y, theta, alpha, iterations, lam, verbose=True):
    """
    Performs gradient descent with L2 regularization.

    :param X: Feature matrix (n_samples, n_features)
    :param y: Target values (n_samples,)
    :param theta: Initial weights (n_features,)
    :param alpha: Learning rate (float)
    :param iterations: Number of iterations (int)
    :param lam: Regularization strength (lambda)
    :param verbose: Print cost every 10,000 steps if True
    :return: Optimized weights (n_features,)

    >>> X = np.array([[1, 1], [1, 2]])
    >>> y = np.array([1, 2])
    >>> theta = np.zeros(2)
    >>> final_theta = ridge_gradient_descent(X, y, theta, 0.1, 10, 0.01, verbose=False)
    >>> len(final_theta)
    2
    """
    m = len(y)
    for i in range(iterations):
        predictions = X @ theta
        error = predictions - y
        gradient = (1 / m) * (X.T @ error)
        reg_term = (lam / m) * theta
        reg_term[0] = 0  # Do not regularize the bias term
        theta = theta - alpha * (gradient + reg_term)

        if i % 10000 == 0 and verbose:
            cost = ridge_cost_function(X, y, theta, lam)
            print(f"Iteration {i}: Cost = {cost:.5f}")

    return theta


def main():
    """
    Driver function for running Ridge Regression
    """
    data = collect_dataset()

    # Normalize feature column to avoid overflow
    feature = data[:, 0]
    feature = (feature - feature.mean()) / feature.std()

    X = np.c_[np.ones(data.shape[0]), feature]  # Add bias term
    y = data[:, 1]

    theta = np.zeros(X.shape[1])
    alpha = 0.001  # Lowered learning rate
    iterations = 100000
    lam = 0.1  # Regularization strength

    final_theta = ridge_gradient_descent(X, y, theta, alpha, iterations, lam)

    print("\nOptimized weights (theta):")
    for i, value in enumerate(final_theta):
        print(f"θ{i}: {value:.5f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
