"""
Mean Squared Logarithmic Error (MSLE) Loss Function

Description:
MSLE measures the mean squared logarithmic difference between
true values and predicted values, particularly useful when
dealing with regression problems involving skewed or large-value
targets. It is often used when the relative differences between
predicted and true values are more important than absolute
differences.

Formula:
MSLE = (1/n) * Σ(log(1 + y_true) - log(1 + y_pred))^2

Source:
(https://insideaiml.com/blog/MeanSquared-Logarithmic-Error-Loss-1035)
"""

import numpy as np


def mean_squared_logarithmic_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the Mean Squared Logarithmic Error (MSLE) between two arrays.

    Parameters:
    - y_true: The true values (ground truth).
    - y_pred: The predicted values.

    Returns:
    - msle: The Mean Squared Logarithmic Error between y_true and y_pred.

    Example usage:
    >>> true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> mean_squared_logarithmic_error(true_values, predicted_values)
    0.0030860877925181344
    >>> true_labels = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 0.2])
    >>> mean_squared_logarithmic_error(true_labels, predicted_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    squared_logarithmic_errors = (np.log1p(y_true) - np.log1p(y_pred)) ** 2
    return np.mean(squared_logarithmic_errors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
