"""Linear Regression Implementation.

Linear regression is a fundamental supervised machine learning algorithm used for
predictive analysis. It models the relationship between a dependent variable (y)
and one or more independent variables (x) by fitting a linear equation.

Mathematical Foundation:
    The model assumes: y = θ₀ + θ₁x₁ + θ₂x₂ + ... + θₙxₙ + ε
    where θ are the parameters (weights) and ε is the error term.

    The cost function (Mean Squared Error) is minimized using gradient descent:
    J(θ) = (1/2m) * Σ(h(x⁽ⁱ⁾) - y⁽ⁱ⁾)²

    Gradient descent update rule:
    θⱼ := θⱼ - α * (∂J/∂θⱼ)

Time Complexity:
    - Training: O(n * m * iterations) where n = features, m = samples
    - Prediction: O(n) per sample

Space Complexity: O(n * m) for storing the dataset

References:
    - https://en.wikipedia.org/wiki/Linear_regression
    - https://en.wikipedia.org/wiki/Gradient_descent
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
from numpy.typing import NDArray


def collect_dataset() -> NDArray:
    """Collect dataset of CSGO player statistics.

    Fetches a CSV dataset containing ADR (Average Damage per Round) vs Rating
    of CSGO players from an external source.

    Returns:
        NDArray: A numpy matrix containing the dataset with ADR and Rating values.

    Raises:
        httpx.TimeoutException: If the request times out after 10 seconds.
        httpx.HTTPError: If there's an error fetching the dataset.

    Example:
        >>> dataset = collect_dataset()  # doctest: +SKIP
        >>> dataset.shape[1] == 2  # doctest: +SKIP
        True
    """
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
    data.pop(0)  # Remove the header labels
    dataset = np.matrix(data)
    return dataset


def run_steep_gradient_descent(
    data_x: NDArray,
    data_y: NDArray,
    len_data: int,
    alpha: float,
    theta: NDArray,
) -> NDArray:
    """Perform one iteration of gradient descent to update feature weights.

    Gradient descent is an optimization algorithm that iteratively adjusts
    parameters to minimize the cost function.

    Args:
        data_x: Input feature matrix of shape (m, n) where m = samples, n = features.
        data_y: Target values array of shape (m,).
        len_data: Number of training samples.
        alpha: Learning rate controlling the step size (typically 0.001 to 0.1).
        theta: Current weight vector of shape (1, n).

    Returns:
        NDArray: Updated weight vector after one gradient descent step.

    Time Complexity: O(m * n) for matrix operations.
    Space Complexity: O(m * n) for intermediate calculations.

    Example:
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
    data_x: NDArray,
    data_y: NDArray,
    len_data: int,
    theta: NDArray,
) -> float:
    """Calculate the Sum of Squared Errors (SSE) for the current model.

    SSE measures how well the model fits the data by computing the sum of
    squared differences between predicted and actual values.

    Args:
        data_x: Input feature matrix of shape (m, n).
        data_y: Actual target values of shape (m,).
        len_data: Number of data samples.
        theta: Current weight vector of shape (1, n).

    Returns:
        float: The mean squared error value (SSE divided by 2m).

    Time Complexity: O(m * n) for prediction and error calculation.
    Space Complexity: O(m) for storing predictions.

    Example:
        >>> import numpy as np
        >>> vc_x = np.array([[1.1], [2.1], [3.1]])
        >>> vc_y = np.array([1.2, 2.2, 3.2])
        >>> round(sum_of_square_error(vc_x, vc_y, 3, np.array([1])), 3)
        np.float64(0.005)

        >>> # Test with perfect fit
        >>> x = np.array([[1], [2], [3]])
        >>> y = np.array([1, 2, 3])
        >>> sum_of_square_error(x, y, 3, np.array([1]))
        np.float64(0.0)
    """
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))
    error = sum_elem / (2 * len_data)
    return error


def run_linear_regression(data_x: NDArray, data_y: NDArray) -> NDArray:
    """Train a linear regression model using gradient descent.

    Iteratively optimizes the weight parameters to minimize the cost function
    (mean squared error) over the training data.

    Args:
        data_x: Input feature matrix of shape (m, n).
        data_y: Target values of shape (m,).

    Returns:
        NDArray: Optimized weight vector (theta) of shape (1, n).

    Time Complexity: O(iterations * m * n) where default iterations = 100000.
    Space Complexity: O(m * n) for storing the dataset.

    Note:
        The learning rate (alpha) is set to 0.0001550 and may need tuning
        for different datasets.
    """
    iterations = 100000
    alpha = 0.0001550
    no_features = data_x.shape[1]
    len_data = data_x.shape[0] - 1
    theta = np.zeros((1, no_features))

    for i in range(iterations):
        theta = run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        print(f"At Iteration {i + 1} - Error is {error:.5f}")

    return theta


def mean_absolute_error(predicted_y: list, original_y: list) -> float:
    """Calculate Mean Absolute Error (MAE) between predicted and actual values.

    MAE is a common metric for regression models that measures the average
    magnitude of errors without considering direction.

    Args:
        predicted_y: List of predicted values.
        original_y: List of actual/expected values.

    Returns:
        float: The mean absolute error.

    Time Complexity: O(n) where n is the number of samples.
    Space Complexity: O(1) for accumulator.

    Example:
        >>> predicted_y = [3, -0.5, 2, 7]
        >>> original_y = [2.5, 0.0, 2, 8]
        >>> mean_absolute_error(predicted_y, original_y)
        0.5

        >>> # Test with identical values (perfect prediction)
        >>> mean_absolute_error([1, 2, 3], [1, 2, 3])
        0.0

        >>> # Test with negative values
        >>> mean_absolute_error([-1, -2], [1, 2])
        3.0
    """
    total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    return total / len(original_y)


def main() -> None:
    """Driver function to demonstrate linear regression.

    Loads the CSGO dataset, trains a linear regression model,
    and prints the resulting feature vector.
    """
    data = collect_dataset()
    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y)
    len_result = theta.shape[1]
    print("Resultant Feature vector : ")
    for i in range(len_result):
        print(f"{theta[0, i]:.5f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
