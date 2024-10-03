"""
Hard Sigmoid Activation Function

Use Case: The Hard Sigmoid function serves as a computationally efficient alternative
to the standard sigmoid function, particularly useful in scenarios where speed is
critical, such as in deep learning models.

For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Hard_sigmoid
"""

import numpy as np


def hard_sigmoid(vector: np.ndarray) -> np.ndarray:
    """
    Implements the Hard Sigmoid Activation Function.

    Parameters:
        vector (np.ndarray): The input array for the hard sigmoid activation function.

    Returns:
        np.ndarray: The output array after applying the hard sigmoid function.

    Formula:
    f(x) = 0 if x < -2.5
            = 1 if x > 2.5
            = (x + 2.5) / 5 if -2.5 <= x <= 2.5

    Examples:
    >>> hard_sigmoid(np.array([-3, -2, -1, 0, 1, 2, 3]))
    array([0. , 0.1, 0.3, 0.5, 0.7, 0.9, 1. ])

    >>> hard_sigmoid(np.array([-10, -5, -2.5, 2.5, 10]))
    array([0., 0., 0., 1., 1.])

    >>> hard_sigmoid(np.array([0]))
    array([0.5])

    """
    return np.clip((vector + 2.5) / 5, 0, 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()