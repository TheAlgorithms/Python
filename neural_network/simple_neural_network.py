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

# Output
expected = int(input("What is the expected value? (1-100): "))

expected = expected / 100

# Number of propagations
n = int(input("How many propagations?: "))

# Random weight
syn0 = 2 * (ran.randint(1, 34)) - 1

for _ in range(n):

    # Forward propagation
    layer_1 = sigmoid_function((INITIAL_VALUE * syn0))

    # How much did we miss?
    layer_1_error = expected - layer_1

    # Error delta
    layer_1_delta = layer_1_error * sigmoid_function(layer_1, True)

    # Update weight
    syn0 += INITIAL_VALUE * layer_1_delta

print("Output after training:")
print(layer_1 * 100)
