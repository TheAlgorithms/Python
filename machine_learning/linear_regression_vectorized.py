"""README, Author - Somrita Banerjee(mailto:somritabanerjee126@gmail.com)
Requirements:
- Python >= 3.13
- httpx
- numpy

Inputs:
- The script automatically downloads a CSV dataset (ADR vs Rating) from a public GitHub URL.
- The dataset must have features in all columns except the last, which is the label (rating).

Usage:
- Run this script directly:
    python linear_regression_vectorized.py
- The script will fetch the dataset, run linear regression using gradient descent, and print the learned feature vector (theta) and error at intervals.

"""
"""
Vectorized implementation of Linear Regression using Gradient Descent.

This version uses NumPy vectorization for efficiency.
It is faster and cleaner than the naive version but assumes
readers are familiar with matrix operations.

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
    """Collect dataset of CSGO (ADR vs Rating).

    :return: dataset as numpy array

    >>> ds = collect_dataset()
    >>> isinstance(ds, np.ndarray)
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
    return np.array(data, dtype=float)


def gradient_descent(
    features: np.ndarray, labels: np.ndarray, alpha: float = 0.000155, iterations: int = 100000
) -> np.ndarray:
    """Run gradient descent in a fully vectorized form.

    :param features: dataset features
    :param labels: dataset labels
    :param alpha: learning rate
    :param iterations: number of iterations
    :return: learned feature vector theta

    >>> import numpy as np
    >>> features = np.array([[1, 1], [1, 2], [1, 3]])
    >>> labels = np.array([[1], [2], [3]])
    >>> theta = gradient_descent(features, labels, alpha=0.01, iterations=1000)
    Iteration 1: Error = ...
    ... # output omitted
    >>> theta.shape
    (2, 1)
    >>> abs(theta[0, 0] - 0) < 0.1  # intercept close to 0
    True
    >>> abs(theta[1, 0] - 1) < 0.1  # slope close to 1
    True
    """
    m, n = features.shape
    theta = np.zeros((n, 1))

    for i in range(iterations):
        predictions = features @ theta
        errors = predictions - labels
        gradients = (features.T @ errors) / m
        theta -= alpha * gradients

        if i % (iterations // 10) == 0:  # log occasionally
            cost = np.sum(errors**2) / (2 * m)
            print(f"Iteration {i + 1}: Error = {cost:.5f}")

    return theta


def mean_absolute_error(predicted_y: np.ndarray, original_y: np.ndarray) -> float:
    """Return mean absolute error.

    >>> pred = np.array([3, -0.5, 2, 7])
    >>> orig = np.array([2.5, 0.0, 2, 8])
    >>> mean_absolute_error(pred, orig)
    0.5
    """
    return float(np.mean(np.abs(original_y - predicted_y)))


def main() -> None:
    """Driver function.

    >>> main()  # doctest: +SKIP
    """
    dataset = collect_dataset()

    m = dataset.shape[0]
    features = np.c_[np.ones(m), dataset[:, :-1]]  # add intercept term
    labels = dataset[:, -1].reshape(-1, 1)

    theta = gradient_descent(features, labels)
    print("Resultant Feature vector:")
    for value in theta.ravel():
        print(f"{value:.5f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
