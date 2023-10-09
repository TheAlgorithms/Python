"""
Huber Loss Function

Description:
Huber loss function describes the penalty incurred by an estimation procedure.
It serves as a measure of the model's accuracy in regression tasks.

Formula:
Huber Loss = if |y_true - y_pred| <= delta then 0.5 * (y_true - y_pred)^2
             else delta * |y_true - y_pred| - 0.5 * delta^2

Source:
[Wikipedia - Huber Loss](https://en.wikipedia.org/wiki/Huber_loss)
"""

import numpy as np


def huber_loss(y_true: np.ndarray, y_pred: np.ndarray, delta: float) -> float:
    """
    Calculate the mean of Huber Loss.

    Parameters:
    - y_true: The true values (ground truth).
    - y_pred: The predicted values.

    Returns:
    - huber_loss: The mean of Huber Loss between y_true and y_pred.

    Example usage:
    >>> true_values = np.array([0.9, 10.0, 2.0, 1.0, 5.2])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> np.isclose(huber_loss(true_values, predicted_values, 1.0), 2.102)
    True
    >>> true_labels = np.array([11.0, 21.0, 3.32, 4.0, 5.0])
    >>> predicted_probs = np.array([8.3, 20.8, 2.9, 11.2, 5.0])
    >>> np.isclose(huber_loss(true_labels, predicted_probs, 1.0), 1.80164)
    True
    """

    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    huber_mse = 0.5 * (y_true - y_pred) ** 2
    huber_mae = delta * (np.abs(y_true - y_pred) - 0.5 * delta)
    return np.where(np.abs(y_true - y_pred) <= delta, huber_mse, huber_mae).mean()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
