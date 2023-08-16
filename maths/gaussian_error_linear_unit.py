"""
This script demonstrates an implementation of the Gaussian Error Linear Unit function.
* https://en.wikipedia.org/wiki/Activation_function#Comparison_of_activation_functions

The function takes a vector of K real numbers as input and returns x * sigmoid(1.702*x).
Gaussian Error Linear Unit (GELU) is a high-performing neural network activation
function.

This script is inspired by a corresponding research paper.
* https://arxiv.org/abs/1606.08415
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


def gaussian_error_linear_unit(vector: np.ndarray) -> np.ndarray:
    """
    Implements the Gaussian Error Linear Unit (GELU) function

    Parameters:
        vector (np.array): A  numpy array of shape (1,n)
        consisting of real values

    Returns:
        gelu_vec (np.array): The input numpy array, after applying
        gelu.

    Examples:
    >>> gaussian_error_linear_unit(np.array([-1.0, 1.0, 2.0]))
    array([-0.15420423,  0.84579577,  1.93565862])

    >>> gaussian_error_linear_unit(np.array([-3]))
    array([-0.01807131])
    """
    return vector * sigmoid(1.702 * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
