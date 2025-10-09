"""
This script demonstrates the implementation of the Sigmoid function.

The sigmoid function is a logistic function, which describes growth as being initially
exponential, but then slowing down and barely growing at all when a limit is reached.
It's commonly used as an activation function in neural networks.

For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Sigmoid_function
"""

import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    """
    Implements the sigmoid activation function.

    Parameters:
        vector (np.ndarray): A vector that consists of numeric values

    Returns:
        np.ndarray: Input vector after applying sigmoid activation function

    Formula: f(x) = 1 / (1 + e^(-x))

    Examples:
    >>> sigmoid(np.array([-1.0, 0.0, 1.0, 2.0]))
    array([0.26894142, 0.5       , 0.73105858, 0.88079708])

    >>> sigmoid(np.array([-5.0, -2.5, 2.5, 5.0]))
    array([0.00669285, 0.07585818, 0.92414182, 0.99330715])
    """
    return 1 / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
