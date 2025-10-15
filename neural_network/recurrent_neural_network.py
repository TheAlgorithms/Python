"""
Minimal Recurrent Neural Network (RNN) demonstration.

Forward propagation explanation:
https://towardsdatascience.com/forward-propagation-in-neural-networks-simplified-math-and-code-version-bbcfef6f9250
RNN fundamentals:
https://towardsdatascience.com/recurrent-neural-networks-d4642c9bc7ce/
"""

import math
import random


# Sigmoid activation
def sigmoid_function(value: float, deriv: bool = False) -> float:
    """Return the sigmoid function of a float.

    >>> round(sigmoid_function(3.5), 4)
    0.9707
    >>> round(sigmoid_function(0.5, True), 4)
    0.25
    """
    if deriv:
        return value * (1 - value)
    return 1 / (1 + math.exp(-value))


# Initial constants
INITIAL_VALUE = 0.02  # learning rate
SEQUENCE_LENGTH = 5  # time steps in the sequence


def forward_propagation_rnn(expected: int, number_propagations: int) -> float:
    """Return the value found after RNN forward propagation training.

    >>> res = forward_propagation_rnn(50, 500_000)
    >>> res > 45 and res < 55
    True

    >>> res = forward_propagation_rnn(50, 500)
    >>> res > 48 and res < 50
    True
    """
    random.seed(0)

    # Random weight initialization
    w_xh = random.random() * 2 - 1  # Input to hidden
    w_hh = random.random() * 2 - 1  # Hidden to hidden (recurrent)
    w_hy = random.random() * 2 - 1  # Hidden to output

    # Training loop
    for _ in range(number_propagations):
        h_prev = 0.0  # hidden state starts at zero
        total_error = 0.0

        # Forward pass through time
        for _t in range(SEQUENCE_LENGTH):
            # Fake input sequence: small constant or could be pattern-based
            x_t = INITIAL_VALUE

            # Hidden state update
            h_t = sigmoid_function(w_xh * x_t + w_hh * h_prev)

            # Output
            y_t = sigmoid_function(w_hy * h_t)

            # Error (target distributed over time steps)
            error_t = (expected / 100) - y_t
            total_error += abs(error_t)

            # Backpropagation Through Time (simplified)
            d_y = error_t * sigmoid_function(y_t, True)
            d_h = d_y * w_hy * sigmoid_function(h_t, True)

            # Weight updates
            w_hy += INITIAL_VALUE * d_y * h_t
            w_xh += INITIAL_VALUE * d_h * x_t
            w_hh += INITIAL_VALUE * d_h * h_prev

            # Move to next time step
            h_prev = h_t

    # Final output after training
    final_output = y_t * 100
    return final_output


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    expected = int(input("Expected value: "))
    number_propagations = int(input("Number of propagations: "))
    print(forward_propagation_rnn(expected, number_propagations))
