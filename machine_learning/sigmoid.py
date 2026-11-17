"""Sigmoid activation function for binary classification models.

The sigmoid function maps a real-valued input to the interval (0, 1).

>>> sigmoid(0)
0.5
>>> round(sigmoid(2), 4)
0.8808
>>> round(sigmoid(-2), 4)
0.1192
>>> sigmoid(1000)
1.0
>>> sigmoid(-1000)
0.0
"""

import math


def sigmoid(value: float) -> float:
    """Return the numerically stable sigmoid of *value*."""
    if value >= 0:
        return 1 / (1 + math.exp(-value))
    exp_value = math.exp(value)
    return exp_value / (1 + exp_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
