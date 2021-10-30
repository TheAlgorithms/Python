"""
This script demonstrates the implementation of the GeLU function.

GELUs full form is GAUSSIAN ERROR LINEAR UNIT

GELU is a smooth approximation to the rectifier. It has a non-monotonic “bump” when x < 0.
The function takes a vector of K real numbers as input.
We define Gaussian Error Linear Unit (GELU) as- 
Gelu(x) = xP(X <= x) = xΦ(x) 
We can approximate the GELU with
0.5x(1 + tanh[root(2/π)(x + 0.044715x^3)])


Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
"""


import numpy as np

def gelu(vector: np.array) -> np.array:
    """
    Implements the relu function

    Parameters:
        vector (np.array,list,tuple): A  numpy array of shape (1,n)
        consisting of real values or a similar list,tuple


    Returns:
        gelu_vec : The input numpy array, after applying
        gelu.

    >>> vec = np.array([-1, 0, 5])
    >>> relu(vec)
    array([0, 0, 5])
    """

    return  np.dot(np.dot(0.5,vector),(1 + np.tanh((np.sqrt(2/np.math.pi))*(vector + 0.044715*np.power(vector, 3)))))

if __name__ == "__main__":
    print(np.array(gelu([-1, 0, 5])))  # --> 4.841191761428657
