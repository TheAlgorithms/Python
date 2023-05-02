"""
Implements the Sigmoid Linear Unit or SiLU function
also known as Swiss functions.

The function takes a vector of K real numbers and then
applies the SiLU function to each element of the vector.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
"""

import numpy as np


def sigmoid_linear_unit(vector: np.ndarray) -> np.ndarray:
    """
         Implements the SiLU activation function.
         Parameters:
             vector: the array containing input of SiLU activation
         return:
            The input numpy array after applying SiLU.

         Mathematically, f(x) = x *  1/1+e^(-x)

    Examples:
    >>> sigmoid_linear_unit(vector=np.array([2.3,0.6,-2,-3.8]))
    array([ 2.09041719,  0.38739378, -0.23840584, -0.08314883])

    >>> sigmoid_linear_unit(vector=np.array([-9.2,-0.3,0.45,-4.56]))
    array([-0.00092947, -0.12766724,  0.27478766, -0.04721304])

    """
    return vector / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
