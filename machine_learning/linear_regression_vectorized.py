"""
Vectorized implementation of Linear Regression using Gradient Descent.

This version uses NumPy vectorization for efficiency.
It is faster and cleaner than the naive version but assumes
readers are familiar with matrix operations.

Dataset used: CSGO dataset (ADR vs Rating)
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
    x: np.ndarray, y: np.ndarray, alpha: float = 0.000155, iterations: int = 100000
) -> np.ndarray:
    """Run gradient descent in a fully vectorized form.

    :param x: dataset features
    :param y: dataset labels
    :param alpha: learning rate
    :param iterations: number of iterations
    :return: learned feature vector theta
    """
    m, n = x.shape
    theta = np.zeros((n, 1))

    for i in range(iterations):
        predictions = x @ theta
        errors = predictions - y
        gradients = (x.T @ errors) / m
        theta -= alpha * gradients

        if i % (iterations // 10) == 0:  # log occasionally
            cost = np.sum(errors**2) / (2 * m)
            print(f"Iteration {i+1}: Error = {cost:.5f}")

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
    """Driver function."""
    dataset = collect_dataset()

    m = dataset.shape[0]
    x = np.c_[np.ones(m), dataset[:, :-1]]  # add intercept term
    y = dataset[:, -1].reshape(-1, 1)

    theta = gradient_descent(x, y)
    print("Resultant Feature vector:")
    for value in theta.ravel():
        print(f"{value:.5f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

