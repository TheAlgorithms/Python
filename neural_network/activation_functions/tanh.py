"""
This script demonstrates the implementation of the Hyperbolic Tangent (Tanh) function.

The tanh function is a hyperbolic function that maps any real-valued input to a value
between -1 and 1. It's commonly used as an activation function in neural networks
and is a scaled version of the sigmoid function.

For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Hyperbolic_functions#Hyperbolic_tangent
"""

import numpy as np


def tanh(vector: np.ndarray) -> np.ndarray:
    """
    Implements the hyperbolic tangent (tanh) activation function.

    Parameters:
        vector (np.ndarray): A vector that consists of numeric values

    Returns:
        np.ndarray: Input vector after applying tanh activation function

    Formula: f(x) = (e^x - e^(-x)) / (e^x + e^(-x)) = (e^(2x) - 1) / (e^(2x) + 1)

    Examples:
    >>> tanh(np.array([-1.0, 0.0, 1.0, 2.0]))
    array([-0.76159416,  0.        ,  0.76159416,  0.96402758])

    >>> tanh(np.array([-5.0, -2.5, 2.5, 5.0]))
    array([-0.9999092, -0.9866143,  0.9866143,  0.9999092])
    """
    return np.tanh(vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
