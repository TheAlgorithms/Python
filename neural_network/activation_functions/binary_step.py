"""
This script demonstrates the implementation of the Binary Step function.

It's an activation function in which the neuron is activated if the input is positive
or 0, else it is deactivated

It's a simple activation function which is mentioned in this wikipedia article:
https://en.wikipedia.org/wiki/Activation_function
"""

import numpy as np


def binary_step(vector: np.ndarray) -> np.ndarray:
    """
    Implements the binary step function

    Parameters:
        vector (ndarray): A vector that consists of numeric values

    Returns:
        vector (ndarray): Input vector after applying binary step function

    >>> vector = np.array([-1.2, 0, 2, 1.45, -3.7, 0.3])
    >>> binary_step(vector)
    array([0, 1, 1, 1, 0, 1])
    """

    return np.where(vector >= 0, 1, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
