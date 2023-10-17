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


def hinge_loss(y_true: np.ndarray, pred: np.ndarray) -> float:
    """
    Calculate the hinge loss for y_true and pred for binary classification.

    Args:
        y_true: Array of actual values (ground truth) encoded as -1 and 1.
        pred: Array of predicted values.

    Returns:
        Hinge loss

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
    """

    if len(y_true) != len(pred):
        raise ValueError("Length of predicted and actual array must be same.")

    intermidiate_result = 1.0 - (y_true * pred)
    intermidiate_result[intermidiate_result < 0] = 0
    loss = np.mean(intermidiate_result)
    return loss


if __name__ == "__main__":
    import doctest

    doctest.testmod()
