"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The idea is pretty simple: we have a dataset and we have
features associated with it. Features should be chosen very cautiously
as they determine how much our model will be able to make future predictions.
We try to set the weight of these features, over many iterations, so that they best
fit our dataset. In this particular code, I had used a CSGO dataset (ADR vs
Rating). We try to best fit a line through dataset and estimate the parameters.
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


def collect_dataset():
    """Collect dataset of CSGO (ADR vs Rating)."""
    response = httpx.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    lines = response.text.strip().splitlines()
    data = [line.split(",") for line in lines[1:]]  # skip header
    return np.array(data, dtype=float)


def run_steep_gradient_descent(data_x, data_y, alpha, theta):
    """Perform one step of gradient descent."""
    n = data_x.shape[0]
    predictions = data_x @ theta.T
    errors = predictions.flatten() - data_y
    gradient = (1 / n) * (errors @ data_x)
    theta = theta - alpha * gradient
    return theta


def sum_of_square_error(data_x, data_y, theta):
    """Compute mean squared error."""
    n = data_x.shape[0]
    predictions = data_x @ theta.T
    errors = predictions.flatten() - data_y
    return np.sum(errors**2) / (2 * n)


def run_linear_regression(data_x, data_y, iterations=100000, alpha=0.000155):
    """Run gradient descent to learn parameters."""
    theta = np.zeros((1, data_x.shape[1]))
    for i in range(iterations):
        theta = run_steep_gradient_descent(data_x, data_y, alpha, theta)
        error = sum_of_square_error(data_x, data_y, theta)
        print(f"Iteration {i + 1}: Error = {error:.5f}")
    return theta


def mean_absolute_error(predicted_y, original_y):
    """Compute MAE (fully vectorized)."""
    predicted_y = np.array(predicted_y)
    original_y = np.array(original_y)
    return np.mean(np.abs(predicted_y - original_y))


def main():
    data = collect_dataset()
    data_x = np.c_[np.ones(data.shape[0]), data[:, 0]]  # Add bias term
    data_y = data[:, 1]  # Rating

    theta = run_linear_regression(data_x, data_y)

    print("Learned Parameters (theta):")
    for val in theta[0]:
        print(f"{val:.5f}")

    predictions = data_x @ theta.T
    mae = mean_absolute_error(predictions.flatten(), data_y)
    print(f"Mean Absolute Error: {mae:.5f}")


if __name__ == "__main__":
    main()
