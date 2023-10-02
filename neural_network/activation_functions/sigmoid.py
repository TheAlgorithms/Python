"""
Sigmoid Activation Function

Use Case: Sigmoid is used in the output layer of a binary classification problems.
For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Sigmoid_function
"""

import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    """
        Implements the Sigmoid activation function.

        Parameters:
            vector (np.ndarray): The input array for Sigmoid activation.

        Returns:
            np.ndarray: The input array after applying the Sigmoid activation.

        Formula: f(x) = 1 / (1 + e^(-x))

    Examples:
    >>> sigmoid(vector=np.array([-0.7, 1.5, -2.8, 0.9]))
    array([0.33181223, 0.81757448, 0.05732418, 0.7109495 ])

    >>> sigmoid(np.array([0.2, -0.3, 1.8, -1.2]))
    array([0.549834  , 0.42555748, 0.85814894, 0.23147522])

    """
    return 1 / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
