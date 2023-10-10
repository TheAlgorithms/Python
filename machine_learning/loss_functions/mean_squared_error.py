"""
Mean Squared Error (MSE) Loss Function

Description:
MSE measures the mean squared difference between true values and predicted values.
It serves as a measure of the model's accuracy in regression tasks.

Formula:
MSE = (1/n) * Σ(y_true - y_pred)^2

Source:
[Wikipedia - Mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error)
"""

import numpy as np


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the Mean Squared Error (MSE) between two arrays.

    Parameters:
    - y_true: The true values (ground truth).
    - y_pred: The predicted values.

    Returns:
    - mse: The Mean Squared Error between y_true and y_pred.

    Example usage:
    >>> true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> mean_squared_error(true_values, predicted_values)
    0.028000000000000032
    >>> true_labels = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 0.2])
    >>> mean_squared_error(true_labels, predicted_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    squared_errors = (y_true - y_pred) ** 2
    return np.mean(squared_errors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
