"""
Squareplus Activation Function

Use Case: Squareplus designed to enhance positive values and suppress negative values.
For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Squareplus
"""

import numpy as np


def squareplus(vector: np.ndarray) -> np.ndarray:
    """
    Implements the SquarePlus activation function.

    Parameters:
        vector (np.ndarray): The input array for the SquarePlus activation.

    Returns:
        np.ndarray: The input array after applying the SquarePlus activation.

    Formula: f(x) = x^2 if x > 0 else f(x) = 0

    Examples:
    >>> squareplus(np.array([2.3, 0.6, -2, -3.8]))
    array([5.29, 0.36, 0.  , 0.  ])

    >>> squareplus(np.array([-9.2, -0.3, 0.45, -4.56]))
    array([0.    , 0.    , 0.2025, 0.    ])
    """
    return np.where(vector > 0, vector**2, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
