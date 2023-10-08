"""
Squareplus Activation Function

Use Case: Squareplus designed to enhance positive values and suppress negative values.
For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Squareplus
"""

import numpy as np


def squareplus(vector: np.ndarray, beta: float) -> np.ndarray:
    """
    Implements the SquarePlus activation function.

    Parameters:
        vector (np.ndarray): The input array for the SquarePlus activation.
        beta (float): size of the curved region

    Returns:
        np.ndarray: The input array after applying the SquarePlus activation.

    Formula: f(x) = ( x + sqrt(x^2 + b) ) / 2

    Examples:
    >>> squareplus(np.array([2.3, 0.6, -2, -3.8]), beta=2)
    array([2.5       , 1.06811457, 0.22474487, 0.12731349])

    >>> squareplus(np.array([-9.2, -0.3, 0.45, -4.56]), beta=3)
    array([0.0808119 , 0.72891979, 1.11977651, 0.15893419])
    """
    return (vector + np.sqrt(vector**2 + beta)) / 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
