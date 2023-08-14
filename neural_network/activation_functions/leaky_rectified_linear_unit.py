"""
Leaky Rectified Linear Unit (LeakyReLU)

Input: vector (type: np.ndarray) , alpha (type: float)
Output: vector (type: np.ndarray)

UseCase: LeakyReLU solves the issue of dead neurons or vanishing gradient problem.
Refer the below link for more information:
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Leaky_ReLU

Applications:
Generative Adversarial Networks (GANs)
Object Detection and Image Segmentation
"""

import numpy as np


def leaky_rectified_linear_unit(vector: np.ndarray, alpha: float) -> np.ndarray:
    """
         Implements the LeakyReLU activation function.
         Parameters:
             vector: the array containing input of leakyReLu activation
             alpha: hyperparameter
         return:
         leaky_relu (np.array): The input numpy array after applying leakyReLu.

         Formula : f(x) = x if x > 0 else f(x) = alpha * x

    Examples:
    >>> leaky_rectified_linear_unit(vector=np.array([2.3,0.6,-2,-3.8]), alpha=0.3)
    array([ 2.3 ,  0.6 , -0.6 , -1.14])

    >>> leaky_rectified_linear_unit(vector=np.array([-9.2,-0.3,0.45,-4.56]), \
    alpha=0.067)
    array([-0.6164 , -0.0201 ,  0.45   , -0.30552])

    """
    return np.where(vector > 0, vector, alpha * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
