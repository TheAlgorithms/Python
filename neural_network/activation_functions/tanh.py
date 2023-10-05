"""
Hyperbolic Tangent Function (Tanh)
reference : https://paperswithcode.com/method/tanh-activation#:~:text=Tanh%20Activation%20is%20an%20activation,for%20multi%2Dlayer%20neural%20networks.

The hyperbolic tangent function, commonly denoted as "tanh," is a mathematical
function that maps real numbers to the range (-1, 1). It's defined as:

tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))

Where:
- e is the base of the natural logarithm (approximately 2.71828).
- x is the input value to the function.

The tanh function's curve is "S"-shaped and centered at the origin (0,0). It
behaves as follows:
- As x approaches negative infinity, tanh(x) approaches -1.
- As x approaches positive infinity, tanh(x) approaches 1.
- At x = 0, tanh(x) equals 0.

In machine learning, tanh is often used as an activation function in neural
networks, introducing non-linearity and squishing neuron outputs to a range
between -1 and 1.

"""
import numpy as np


def tanh(vector: np.ndarray) -> np.ndarray:
    """_summary_
    Args:
        vector (np.ndarray): numpy array
    Returns:
        np.ndarray: numpy array after applying tanh
    Examples :
    >>> tanh(vector=np.array([-2, -1, 0,  1,  2]))
    array([-0.96402758, -0.76159416,  0.        ,  0.76159416,  0.96402758])
    """
    return (np.exp(vector) - np.exp(-vector)) / (np.exp(vector) + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()