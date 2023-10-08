"""
Binary Cross-Entropy (BCE) Loss Function

Description:
Quantifies dissimilarity between true labels (0 or 1) and predicted probabilities.
It's widely used in binary classification tasks.

Formula:
BCE = -Σ(y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred))

Source:
[Wikipedia - Cross entropy](https://en.wikipedia.org/wiki/Cross_entropy)
"""

import numpy as np


def binary_cross_entropy(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    """
    Calculate the BCE Loss between true labels and predicted probabilities.

    Parameters:
    - y_true: True binary labels (0 or 1).
    - y_pred: Predicted probabilities for class 1.
    - epsilon: Small constant to avoid numerical instability.

    Returns:
    - bce_loss: Binary Cross-Entropy Loss.

    Example Usage:
    >>> true_labels = np.array([0, 1, 1, 0, 1])
    >>> predicted_probs = np.array([0.2, 0.7, 0.9, 0.3, 0.8])
    >>> binary_cross_entropy(true_labels, predicted_probs)
    0.2529995012327421
    >>> true_labels = np.array([0, 1, 1, 0, 1])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 0.2])
    >>> binary_cross_entropy(true_labels, predicted_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")
    # Clip predicted probabilities to avoid log(0) and log(1)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    # Calculate binary cross-entropy loss
    bce_loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    # Take the mean over all samples
    return np.mean(bce_loss)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
