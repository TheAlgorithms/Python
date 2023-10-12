"""
Categorical Cross-Entropy Loss

This function calculates the Categorical Cross-Entropy Loss between true class
labels and predicted class probabilities.

Formula:
Categorical Cross-Entropy Loss = -Σ(y_true * ln(y_pred))

Resources:
- [Wikipedia - Cross entropy](https://en.wikipedia.org/wiki/Cross_entropy)
"""

import numpy as np


def categorical_cross_entropy(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    """
    Calculate Categorical Cross-Entropy Loss between true class labels and
    predicted class probabilities.

    Parameters:
    - y_true: True class labels (one-hot encoded) as a NumPy array.
    - y_pred: Predicted class probabilities as a NumPy array.
    - epsilon: Small constant to avoid numerical instability.

    Returns:
    - ce_loss: Categorical Cross-Entropy Loss as a floating-point number.

    Example:
    >>> true_labels = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1], [0.0, 0.1, 0.9]])
    >>> categorical_cross_entropy(true_labels, pred_probs)
    0.567395975254385

    >>> y_true = np.array([[1, 0], [0, 1]])
    >>> y_pred = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(y_true, y_pred)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same shape.

    >>> y_true = np.array([[2, 0, 1], [1, 0, 0]])
    >>> y_pred = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(y_true, y_pred)
    Traceback (most recent call last):
        ...
    ValueError: y_true must be one-hot encoded.

    >>> y_true = np.array([[1, 0, 1], [1, 0, 0]])
    >>> y_pred = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(y_true, y_pred)
    Traceback (most recent call last):
        ...
    ValueError: y_true must be one-hot encoded.

    >>> y_true = np.array([[1, 0, 0], [0, 1, 0]])
    >>> y_pred = np.array([[0.9, 0.1, 0.1], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(y_true, y_pred)
    Traceback (most recent call last):
        ...
    ValueError: Predicted probabilities must sum to approximately 1.
    """
    if y_true.shape != y_pred.shape:
        raise ValueError("Input arrays must have the same shape.")

    if np.any((y_true != 0) & (y_true != 1)) or np.any(y_true.sum(axis=1) != 1):
        raise ValueError("y_true must be one-hot encoded.")

    if not np.all(np.isclose(np.sum(y_pred, axis=1), 1, rtol=epsilon, atol=epsilon)):
        raise ValueError("Predicted probabilities must sum to approximately 1.")

    # Clip predicted probabilities to avoid log(0)
    y_pred = np.clip(y_pred, epsilon, 1)

    # Calculate categorical cross-entropy loss
    return -np.sum(y_true * np.log(y_pred))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
