import numpy as np


def binary_cross_entropy(y_true, y_pred, epsilon=1e-15):
    """
    Calculate the BCE Loss between true labels and predicted probabilities.

    Parameters:
    - y_true: True binary labels (0 or 1).
    - y_pred: Predicted probabilities for class 1.
    - epsilon: Small constant to avoid numerical instability.

    Returns:
    - bce_loss: Binary Cross-Entropy Loss.

    Example Usage:
    true_labels = np.array([0, 1, 1, 0, 1])
    predicted_probs = np.array([0.2, 0.7, 0.9, 0.3, 0.8])
    bce_loss = binary_cross_entropy(true_labels, predicted_probs)
    print(f"Binary Cross-Entropy Loss: {bce_loss}")
    """
    # Clip predicted probabilities to avoid log(0) and log(1)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    # Calculate binary cross-entropy loss
    bce_loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    # Take the mean over all samples
    bce_loss = np.mean(bce_loss)

    return bce_loss
