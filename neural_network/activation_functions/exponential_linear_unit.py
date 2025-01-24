"""
Implements the Exponential Linear Unit or ELU function.

The function takes a vector of K real numbers and a real number alpha as
input and then applies the ELU function to each element of the vector.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
"""

import numpy as np


def exponential_linear_unit(vector: np.ndarray, alpha: float) -> np.ndarray:
    """
         Implements the ELU activation function.
         Parameters:
             vector: the array containing input of elu activation
             alpha: hyper-parameter
         return:
         elu (np.array): The input numpy array after applying elu.

         Mathematically, f(x) = x, x>0 else (alpha * (e^x -1)), x<=0, alpha >=0

    Examples:
    >>> exponential_linear_unit(vector=np.array([2.3,0.6,-2,-3.8]), alpha=0.3)
    array([ 2.3       ,  0.6       , -0.25939942, -0.29328877])

    >>> exponential_linear_unit(vector=np.array([-9.2,-0.3,0.45,-4.56]), alpha=0.067)
    array([-0.06699323, -0.01736518,  0.45      , -0.06629904])


    """
    return np.where(vector > 0, vector, (alpha * (np.exp(vector) - 1)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
