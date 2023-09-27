"""
This script demonstrates the implementation of the Sigmoid Linear Unit (SiLU)
or swish function.
* https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
* https://en.wikipedia.org/wiki/Swish_function

The function takes a vector x of K real numbers as input and returns x * sigmoid(x).
Swish is a smooth, non-monotonic function defined as f(x) = x * sigmoid(x).
Extensive experiments shows that Swish consistently matches or outperforms ReLU
on deep networks applied to a variety of challenging domains such as
image classification and machine translation.

This script is inspired by a corresponding research paper.
* https://arxiv.org/abs/1710.05941
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


def sigmoid_linear_unit(vector: np.ndarray) -> np.ndarray:
    """
    Implements the Sigmoid Linear Unit (SiLU) or swish function

    Parameters:
        vector (np.ndarray): A  numpy array consisting of real values

    Returns:
        swish_vec (np.ndarray): The input numpy array, after applying swish

    Examples:
    >>> sigmoid_linear_unit(np.array([-1.0, 1.0, 2.0]))
    array([-0.26894142,  0.73105858,  1.76159416])

    >>> sigmoid_linear_unit(np.array([-2]))
    array([-0.23840584])
    """
    return vector * sigmoid(vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
