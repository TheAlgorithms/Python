"""
Nesterov Accelerated Gradient (NAG) Optimizer

Implements Nesterov momentum for neural network training using NumPy.
NAG looks ahead and computes gradients at the anticipated position.

Reference: https://cs231n.github.io/neural-networks-3/#sgd
Author: Adhithya Laxman Ravi Shankar Geetha
Date: 2025.10.21
"""

import numpy as np


class NesterovAcceleratedGradient:
    """
    Nesterov Accelerated Gradient (NAG) optimizer.

    Updates parameters using Nesterov momentum:
        velocity = momentum * velocity - learning_rate * gradient_at_lookahead
        param = param + velocity
    """

    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.9) -> None:
        """
        Initialize NAG optimizer.

        Args:
            learning_rate (float): Learning rate for weight updates.
            momentum (float): Momentum factor.

        >>> optimizer = NesterovAcceleratedGradient(learning_rate=0.01, momentum=0.9)
        >>> optimizer.momentum
        0.9
        """
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.velocity: dict[int, np.ndarray] = {}

    def update(
        self, param_id: int, params: np.ndarray, gradients: np.ndarray
    ) -> np.ndarray:
        """
        Update parameters using NAG.

        Args:
            param_id (int): Unique identifier for parameter group.
            params (np.ndarray): Current parameters.
            gradients (np.ndarray): Gradients at lookahead position.

        Returns:
            np.ndarray: Updated parameters.

        >>> optimizer = NesterovAcceleratedGradient(learning_rate=0.1, momentum=0.9)
        >>> params = np.array([1.0, 2.0])
        >>> grads = np.array([0.1, 0.2])
        >>> updated = optimizer.update(0, params, grads)
        >>> updated.shape
        (2,)
        """
        if param_id not in self.velocity:
            self.velocity[param_id] = np.zeros_like(params)

        velocity_prev = self.velocity[param_id].copy()
        self.velocity[param_id] = (
            self.momentum * self.velocity[param_id] - self.learning_rate * gradients
        )
        return (
            params
            - self.momentum * velocity_prev
            + (1 + self.momentum) * self.velocity[param_id]
        )


# Usage example
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("NAG Example: Minimizing f(x) = x^2")

    optimizer = NesterovAcceleratedGradient(learning_rate=0.1, momentum=0.9)
    x = np.array([5.0])

    for step in range(20):
        gradient = 2 * x
        x = optimizer.update(0, x, gradient)
        if step % 5 == 0:
            print(f"Step {step}: x = {x[0]:.4f}, f(x) = {x[0] ** 2:.4f}")

    print(f"Final: x = {x[0]:.4f}, f(x) = {x[0] ** 2:.4f}")
