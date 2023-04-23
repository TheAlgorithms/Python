"""
This script demonstrates the implementation of the tangent hyperbolic or tanh function.

The function takes a vector of K real numbers as input and then (e^x - e^(-x))/(e^x + e^(-x)).
After through tanh, the element of the vector mostly -1 between 1.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Activation_function
"""
import numpy
import numpy as np


def tanh(vector):
    '''
        Implements the tanh function

        Parameters:
            vector: np.array, list, tuple consisting real values

        Returns:
            tanh (np.array): The input numpy array  after applying
        tanh.

        mathematically (e^x - e^(-x))/(e^x + e^(-x)) can be written as (2/(1+e^(-2x))-1
    '''
    exp_vector = np.exp(-2 * vector)
    return (2 / (1 + exp_vector)) - 1


if __name__ == '__main__':
    print(tanh(np.array([1, 5, 6, 113, 13, 16, -5.23])))
