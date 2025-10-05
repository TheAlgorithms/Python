"""README, Author - Somrita Banerjee(mailto:somritabanerjee126@gmail.com)
Requirements:
- Python >= 3.13
- httpx
- numpy

Inputs:
- Downloads a CSV dataset (ADR vs Rating) from a public GitHub URL.
- The dataset should have features in all columns except the last, which is the label.

Usage:
- Run this script directly:
    python linear_regression_naive.py
- The script will fetch the dataset, run linear regression using gradient descent, and print the learned feature vector (theta) and error at each iteration.

"""

"""
Naive implementation of Linear Regression using Gradient Descent.

This version is intentionally less optimized and more verbose,
designed for educational clarity. It shows the step-by-step
gradient descent update and error calculation.

Dataset used: CSGO dataset (ADR vs Rating)

References:
https://en.wikipedia.org/wiki/Linear_regression
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "numpy",
# ]
# ///

import httpx
import numpy as np


def collect_dataset() -> np.ndarray:
    """Collect dataset of CSGO (ADR vs Rating)

    :return: dataset as numpy matrix

    >>> ds = collect_dataset()
    >>> isinstance(ds, np.matrix)
    True
    >>> ds.shape[1] >= 2
    True
    """
    response = httpx.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    lines = response.text.splitlines()
    data = [line.split(",") for line in lines]
    data.pop(0)  # remove header row
    dataset = np.matrix(data)
    return dataset


def run_steep_gradient_descent(
    data_x: np.ndarray,
    data_y: np.ndarray,
    len_data: int,
    alpha: float,
    theta: np.ndarray,
) -> np.ndarray:
    """Run one step of steep gradient descent.

    :param data_x: dataset features
    :param data_y: dataset labels
    :param len_data: number of samples
    :param alpha: learning rate
    :param theta: feature vector (weights)

    :return: updated theta

    >>> import numpy as np
    >>> data_x = np.array([[1, 2], [3, 4]])
    >>> data_y = np.array([5, 6])
    >>> len_data = len(data_x)
    >>> alpha = 0.01
    >>> theta = np.array([0.1, 0.2])
    >>> run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
    array([0.196, 0.343])
    """
    prod = np.dot(theta, data_x.T)
    prod -= data_y.T
    grad = np.dot(prod, data_x)
    theta = theta - (alpha / len_data) * grad
    return theta


def sum_of_square_error(
    data_x: np.ndarray, data_y: np.ndarray, len_data: int, theta: np.ndarray
) -> float:
    """Return sum of square error for error calculation.

    >>> vc_x = np.array([[1.1], [2.1], [3.1]])
    >>> vc_y = np.array([1.2, 2.2, 3.2])
    >>> round(sum_of_square_error(vc_x, vc_y, 3, np.array([1])), 3)
    0.005
    """
    prod = np.dot(theta, data_x.T)
    prod -= data_y.T
    error = np.sum(np.square(prod)) / (2 * len_data)
    return float(error)


def run_linear_regression(data_x: np.ndarray, data_y: np.ndarray) -> np.ndarray:
    """Run linear regression using gradient descent.

    :param data_x: dataset features
    :param data_y: dataset labels
    :return: learned feature vector theta

    >>> import numpy as np
    >>> x = np.array([[1, 1], [1, 2], [1, 3]])
    >>> y = np.array([1, 2, 3])
    >>> theta = run_linear_regression(x, y)
    Iteration 1: Error = ...
    ... # lots of output omitted
    >>> theta.shape
    (1, 2)
    >>> abs(theta[0, 0] - 0) < 0.1  # intercept close to 0
    True
    >>> abs(theta[0, 1] - 1) < 0.1  # slope close to 1
    True
    """
    iterations = 100000
    alpha = 0.000155

    no_features = data_x.shape[1]
    len_data = data_x.shape[0] - 1

    theta = np.zeros((1, no_features))

    for i in range(iterations):
        theta = run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        print(f"Iteration {i + 1}: Error = {error:.5f}")

    return theta


def mean_absolute_error(predicted_y: np.ndarray, original_y: np.ndarray) -> float:
    """Return mean absolute error.

    >>> predicted_y = np.array([3, -0.5, 2, 7])
    >>> original_y = np.array([2.5, 0.0, 2, 8])
    >>> mean_absolute_error(predicted_y, original_y)
    0.5
    """
    total = sum(abs(predicted_y[i] - y) for i, y in enumerate(original_y))
    return total / len(original_y)


def main() -> None:
    """Driver function."""
    data = collect_dataset()

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y)
    print("Resultant Feature vector:")
    for value in theta.ravel():
        print(f"{value:.5f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
