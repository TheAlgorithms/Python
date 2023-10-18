"""
Binary Focal Cross-Entropy (BFCE) Loss Function

Description:
Quantifies dissimilarity between true labels (0 or 1) and predicted probabilities.
It's a variation of binary cross-entropy that addresses class imbalance by 
focusing on hard examples.

Formula:
Focal Loss = -Σ(alpha * (1 - y_pred)**gamma * y_true * log(y_pred) + (1 - alpha) * y_pred**gamma * (1 - y_true) * log(1 - y_pred))

Source:
[Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)
"""


import numpy as np

def binary_focal_cross_entropy(
        y_true: np.ndarray, y_pred: np.ndarray, 
        gamma: float = 2.0, alpha: float = 0.25, epsilon: float = 1e-15
) -> float:
    """
    Calculate the BFCE Loss between true labels and predicted probabilities.

    Parameters:
    - y_true: True binary labels (0 or 1).
    - y_pred: Predicted probabilities for class 1.
    - gamma: Focusing parameter for modulating the loss (default: 2.0).
    - alpha: Weighting factor for class 1 (default: 0.25).
    - epsilon: Small constant to avoid numerical instability.

    Returns:
    - bcfe_loss: Binary Focal Cross-Entropy Loss.

    Example Usage:
    >>> true_labels = np.array([0, 1, 1, 0, 1])
    >>> predicted_probs = np.array([0.2, 0.7, 0.9, 0.3, 0.8])
    >>> binary_focal_cross_entropy(true_labels, predicted_probs)
    0.008257977659239775
    >>> true_labels = np.array([0, 1, 1, 0, 1])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 0.2])
    >>> binary_focal_cross_entropy(true_labels, predicted_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")
    # Clip predicted probabilities to avoid log(0) and log(1)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    # Focal loss calculation
    bcfe_loss = -(alpha * (1 - y_pred) ** gamma * y_true * np.log(y_pred) 
                   + (1 - alpha) * y_pred ** gamma * (1 - y_true) * np.log(1 - y_pred))

    # Take the mean over all samples
    return np.mean(bcfe_loss)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
