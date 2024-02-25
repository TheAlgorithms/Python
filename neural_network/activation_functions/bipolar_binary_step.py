"""
This script demonstrates the implementation of the Bipolar Binary Step function.

It's an activation function in which the neuron outputs 1 if the input is positive
or 0, else outputs -1 if the input is negative.

It's a simple activation function which is mentioned in this wikipedia article:
https://en.wikipedia.org/wiki/Activation_function
"""

import numpy as np


def bipolar_binary_step(vector: np.ndarray) -> np.ndarray:
    """
    Implements the binary step function

    Parameters:
        vector (ndarray): A vector that consists of numeric values

    Returns:
        vector (ndarray): Input vector after applying binary step function

    >>> vector = np.array([-1.2, 0, 2, 1.45, -3.7, 0.3])
    >>> bipolar_binary_step(vector) # doctest: +NORMALIZE_WHITESPACE
    array([-1, 1, 1, 1, -1, 1])
    """

    return np.where(vector >= 0, 1, -1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
