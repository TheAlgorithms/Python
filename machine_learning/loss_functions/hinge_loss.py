"""
Hinge Loss

Description:
Compute the Hinge loss used for training SVM (Support Vector Machine).

Formula:
loss = max(0, 1 - true * pred)

Reference: https://en.wikipedia.org/wiki/Hinge_loss

Author: Poojan Smart
Email: smrtpoojan@gmail.com
"""

import numpy as np


def hinge_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the mean hinge loss for y_true and y_pred for binary classification.

    Args:
        y_true: Array of actual values (ground truth) encoded as -1 and 1.
        y_pred: Array of predicted values.

    Returns:
        The hinge loss between y_true and y_pred.

    Examples:
    >>> y_true = np.array([-1, 1, 1, -1, 1])
    >>> pred = np.array([-4, -0.3, 0.7, 5, 10])
    >>> hinge_loss(y_true, pred)
    1.52
    >>> y_true = np.array([-1, 1, 1, -1, 1, 1])
    >>> pred = np.array([-4, -0.3, 0.7, 5, 10])
    >>> hinge_loss(y_true, pred)
    Traceback (most recent call last):
    ...
    ValueError: Length of predicted and actual array must be same.
    >>> y_true = np.array([-1, 1, 10, -1, 1])
    >>> pred = np.array([-4, -0.3, 0.7, 5, 10])
    >>> hinge_loss(y_true, pred)
    Traceback (most recent call last):
    ...
    ValueError: y_true can have values -1 or 1 only.
    """

    if len(y_true) != len(y_pred):
        raise ValueError("Length of predicted and actual array must be same.")

    # Raise value error when y_true (encoded labels) have any other values
    # than -1 and 1
    if np.any((y_true != -1) & (y_true != 1)):
        raise ValueError("y_true can have values -1 or 1 only.")

    hinge_losses = np.maximum(0, 1.0 - (y_true * y_pred))
    return np.mean(hinge_losses)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
