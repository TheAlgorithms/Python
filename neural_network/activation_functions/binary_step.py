"""
This script demonstrates the implementation of the Binary Step function.

It's a kind of activation functionif in which if the input to the activation function is greater than a threshold,
the neuron is activated, else it is deactivated
"""


import numpy as np


def binary_step(vector: np.ndarray) -> np.ndarray:
    """
    Implements the binary step function

    Parameters:
        vector (ndarray): A vector that consitis of numeric values

    Returns:
        vector (ndarray): A vector that consitis of values 0 or 1

    >>> vector = np.array([-1.2, 0, 2, 1.45, -3.7, 0.3])
    >>> binary_step(vector)
    array([0, 0, 1, 1, 0, 1])
    """

    return np.where(vector > 0, 1, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
