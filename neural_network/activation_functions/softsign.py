"""
Softsign activation function

Use Case: Softsign provides a smooth transition without sharp gradients
and is an alternative to sigmoid functions.

For more detailed information, you can refer to the following link:
https://paperswithcode.com/method/softsign-activation
"""

import numpy as np


def softsign(vector: np.ndarray) -> np.ndarray:
    """
    Implements the Softsign Activation Function.

    Parameters:
        vector (np.ndarray): The input array for Softsign activation.

    Returns:
        np.ndarray: The output after applying Softsign activation.

    Formula: f(x) = x / (1 + |x|)

    Examples:
    >>> softsign(np.array([-10, -5, -1, 0 ,1 ,5 ,10]))
    array([-0.90909091, -0.83333333, -0.5       ,  0.        ,  0.5       ,
            0.83333333,  0.90909091])

    >>> softsign(np.array([100]))
    array([0.99009901])

    """
    return vector / (1 + np.abs(vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
