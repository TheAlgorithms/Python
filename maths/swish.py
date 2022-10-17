"""
This script demonstrates the implementation of the Swish function.

The function takes a vector x of K real numbers as input and then
returns x * sigmoid(x).
Swish is a smooth, non-monotonic function defined as
f(x) = x ·sigmoid(x).
Extensive experiments shows that Swish consistently
matches or outperforms ReLU on deep networks applied to a variety
of challenging domains such as image classification and
machine translation.

Script inspired from its corresponding research paper
https://arxiv.org/abs/1710.05941
"""

import numpy as np


def sigmoid(vector: np.array) -> np.array:
    """
    Swish function can be implemented easily with the help of
    sigmoid function
    """
    return 1 / (1 + np.exp(-vector))


def swish(vector: np.array) -> np.array:
    """
    Implements the swish function

    Parameters:
        vector (np.array): A  numpy array consisting of real
        values.

    Returns:
        vector (np.array): The input numpy array, after applying
        swish.

    Examples:
    >>> swish(np.array([-1.0, 1.0, 2.0]))
    array([-0.26894142,  0.73105858,  1.76159416])

    >>> swish(np.array([-2]))
    array([-0.23840584])
    """
    return vector * sigmoid(vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
