"""
This is a sigmoid function
x i function sigmoid is function variable
a is the gain
https://en.wikipedia.org/wiki/Sigmoid_function
"""

import math


def sigmoid(x, a):

    """
    Returns value corresponding to sigmoid function.

    >>> sigmoid(0.5, 1)
    0.6224593312018546
    >>> sigmoid(2, 0.5)
    0.7310585786300049
    """
    p = math.exp(-a * x)
    return 1 / (1 + p)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
