"""
Implements the Mish activation functions.

The function takes a vector of K real numbers input and then
applies the mish function, x*tanh(softplus(x) to each element of the vector.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)

The proposed paper link is provided below.
https://arxiv.org/abs/1908.08681
"""

import numpy as np
from maths.tanh import tangent_hyperbolic as tanh


def mish_activation(vector: np.ndarray) -> np.ndarray:
    """
        Implements the Mish function

        Parameters:
            vector: np.array

        Returns:
            Mish (np.array): The input numpy array after applying tanh.

        mathematically, mish = x * tanh(softplus(x)  where
        softplus = ln(1+e^(x)) and tanh = (e^x - e^(-x))/(e^x + e^(-x))
        so, mish can be written as x * (2/(1+e^(-2 * softplus))-1

    """
    soft_plus = np.log(np.exp(vector) + 1)
    return vector * tanh(soft_plus)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
