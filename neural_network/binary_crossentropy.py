"""
Implementation of Binary Cross Entropy or Log loss function

The function takes two vector of K real numbers called y_true and y_pred, then
applies binary cross entropy function to each element of the vectors.


Script inspired from its corresponding Wikipedia article
https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a
"""

import numpy as np


def binary_cross_entropy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
             Implements the Binary Cross Entropy function.
             Parameters:
                 y_true: the array containing input of actual label output i.e 0 or 1
                 y_pred: the array containing predicted output
             return:
             float: the output value of binary crossentropy

             Mathematically, BCE= −(1/N) * Sum(y_i * log(p_i) + (1-y_i)log(1-p_i))

        Examples:
        >>> binary_cross_entropy(np.array([1, 0, 1]), np.array([0.9, 0.2, 0.8]))
        0.18388253942874858

        
    """
    log_loss = - np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return log_loss


if __name__ == "__main__":
    import doctest

    doctest.testmod()
