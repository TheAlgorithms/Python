"""
Forward propagation explanation:
https://towardsdatascience.com/forward-propagation-in-neural-networks-simplified-math-and-code-version-bbcfef6f9250
"""

import random as ran
import math


# Sigmoid
def sigmoid_function(value: float, deriv: bool = False) -> float:
    """Return the sigmoid function of a float.

    >>> sigmoid_function(3.5)
    0.9706877692486436
    >>> sigmoid_function(3.5, True)
    -8.75
    """
    if deriv:
        return value * (1 - value)
    return 1 / (1 + math.exp(-value))


# Initial Value
INITIAL_VALUE = 0.02


def forward_propagation(expected: int, number_propagations: int) -> float:
    """Return the value found after the forward propagation training.

    >>> res = forward_propagation(32, 10000000)
    >>> res > 31 and res < 33
    True

    >>> res = forward_propagation(32, 1000)
    >>> res > 31 and res < 33
    False
    """
    expected = expected / 100

    # Random weight
    weight = 2 * (ran.randint(1, 100)) - 1

    for _ in range(number_propagations):
        # Forward propagation
        layer_1 = sigmoid_function((INITIAL_VALUE * weight))
        # How much did we miss?
        layer_1_error = expected - layer_1
        # Error delta
        layer_1_delta = layer_1_error * sigmoid_function(layer_1, True)
        # Update weight
        weight += INITIAL_VALUE * layer_1_delta

    return layer_1 * 100
