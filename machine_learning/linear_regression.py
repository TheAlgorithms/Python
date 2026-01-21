"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The algorithm iteratively updates a weight vector to fit a
line through the data using gradient descent.

Time complexity: O(iterations * n_samples * n_features)
Space complexity: O(n_features)
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "numpy",
# ]
# ///
from collections.abc import Sequence

import httpx
import numpy as np


def collect_dataset() -> np.ndarray:
    """Collect a small CSGO dataset (ADR vs Rating) as a NumPy array."""
    response = httpx.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    lines = response.text.splitlines()
    data = []
    for item in lines:
        item = item.split(",")
        data.append(item)
    data.pop(0)  # This is for removing the labels from the list
    dataset = np.array(data, dtype=float)
    return dataset


def run_steep_gradient_descent(
    data_x: np.ndarray,
    data_y: np.ndarray,
    len_data: int,
    alpha: float,
    theta: np.ndarray,
) -> np.ndarray:
    """Run steep gradient descent and update the weight vector accordingly.

    >>> import numpy as np
    >>> data_x = np.array([[1, 2], [3, 4]])
    >>> data_y = np.array([5, 6])
    >>> len_data = len(data_x)
    >>> alpha = 0.01
    >>> theta = np.array([0.1, 0.2])
    >>> run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
    array([0.196, 0.343])
    """
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    theta = theta - (alpha / n) * sum_grad
    return theta


def sum_of_square_error(
    data_x: np.ndarray, data_y: np.ndarray, len_data: int, theta: np.ndarray
) -> float:
    """Return sum of square error for error calculation.

    Example:
    >>> vc_x = np.array([[1.1], [2.1], [3.1]])
    >>> vc_y = np.array([1.2, 2.2, 3.2])
    >>> float(round(sum_of_square_error(vc_x, vc_y, 3, np.array([1])), 3))
    0.005
    """
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))
    error: float = sum_elem / (2 * len_data)
    return error


def run_linear_regression(
    data_x: np.ndarray,
    data_y: np.ndarray,
    iterations: int = 100000,
    alpha: float = 0.0001550,
    verbose: bool = False,
) -> np.ndarray:
    """Implement Linear Regression over the dataset using gradient descent.

    >>> data_x = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
    >>> data_y = np.array([1.0, 4.0, 7.0])
    >>> run_linear_regression(
    ...     data_x, data_y, iterations=2000, alpha=0.05, verbose=False
    ... )
    array([[1., 3.]])
    """
    no_features = data_x.shape[1]
    len_data = data_x.shape[0]

    theta = np.zeros((1, no_features))

    for i in range(iterations):
        theta = run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
        if verbose:
            error = sum_of_square_error(data_x, data_y, len_data, theta)
            print(f"At Iteration {i + 1} - Error is {error:.5f}")

    return theta


def mean_absolute_error(
    predicted_y: Sequence[float], original_y: Sequence[float]
) -> float:
    """Return the mean absolute error between two sequences.

    >>> predicted_y = [3, -0.5, 2, 7]
    >>> original_y = [2.5, 0.0, 2, 8]
    >>> mean_absolute_error(predicted_y, original_y)
    0.5
    """
    total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    return total / len(original_y)


def main() -> None:
    """Driver function for manual runs."""
    data = collect_dataset()

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y, verbose=False)
    len_result = theta.shape[1]
    print("Resultant Feature vector : ")
    for i in range(len_result):
        print(f"{theta[0, i]:.5f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
