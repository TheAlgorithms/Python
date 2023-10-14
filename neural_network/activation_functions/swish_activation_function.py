"""
This script demonstrates the implementation of the General Swish Functions
* https://en.wikipedia.org/wiki/Swish_function

The function takes a vector x of K real numbers as input and returns x * sigmoid(bx).
Swish is a smooth, non-monotonic function defined as f(x) = x * sigmoid(bx).
Extensive experiments shows that Swish consistently matches or outperforms ReLU
on deep networks applied to a variety of challenging domains such as
image classification and machine translation.

This script is inspired by a corresponding research paper.
* https://blog.paperspace.com/swish-activation-function/
"""

import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    """
    Mathematical function sigmoid takes a vector x of K real numbers as input and
    returns 1/ (1 + e^-x).
    https://en.wikipedia.org/wiki/Sigmoid_function

    >>> sigmoid(np.array([-1.0, 1.0, 2.0]))
    array([0.26894142, 0.73105858, 0.88079708])
    """
    return 1 / (1 + np.exp(-vector))


def general_swish(vector: np.ndarray, trainable_parameter: int) -> np.ndarray:
    """
    Parameters:
        vector (np.ndarray): A  numpy array consisting of real values
        trainable_parameter: Use to implement various Swish Activation Functions

    Returns:
        swish_vec (np.ndarray): The input numpy array, after applying swish

    Examples:
    >>> general_swish(np.array([-1.0, 1.0, 2.0]), 2)
    array([-0.11920292,  0.88079708,  1.96402758])

    >>> general_swish(np.array([-2]), 1)
    array([-0.23840584])
    """
    return vector * sigmoid(trainable_parameter * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
