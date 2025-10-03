"""
This script demonstrates the implementation of the Softsign activation function.

Softsign is a smooth activation function defined as:

    f(x) = x / (1 + |x|)

It maps input values into the range (-1, 1), similar to the hyperbolic tangent (tanh)
function but with a polynomial decay instead of exponential.

More about this function can be found in the article:
https://www.gabormelli.com/RKB/Softsign_Activation_Function
"""

import numpy as np


def softsign(vector: np.ndarray) -> np.ndarray:
    """
    Implements the softsign activation function

    Parameters:
        vector (ndarray): A vector that consists of numeric values

    Returns:
        vector (ndarray): Input vector after applying softsign function

    >>> vector = np.array([-5, -1, 0, 1, 5])
    >>> softsign(vector)
    array([-0.83333333, -0.5       ,  0.        ,  0.5       ,  0.83333333])
    """
    return vector / (1 + np.abs(vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
