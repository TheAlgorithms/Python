"""
Momentum SGD Optimizer

Implements SGD with momentum for neural network training using NumPy.
Momentum helps accelerate gradients in the relevant direction and dampens oscillations.

Reference: https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Momentum
Author: Adhithya Laxman Ravi Shankar Geetha
Github: https://github.com/Adhithya-Laxman
Date: 2025.10.22
"""

import numpy as np


class MomentumSGD:
    """
    SGD with momentum optimizer.

    Updates parameters using momentum:
        velocity = momentum * velocity - learning_rate * gradient
        param = param + velocity
    """

    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.9) -> None:
        """
        Initialize Momentum SGD optimizer.

        Args:
            learning_rate (float): Learning rate for weight updates.
            momentum (float): Momentum factor.

        >>> optimizer = MomentumSGD(learning_rate=0.01, momentum=0.9)
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
        Update parameters using momentum.

        Args:
            param_id (int): Unique identifier for parameter group.
            params (np.ndarray): Current parameters.
            gradients (np.ndarray): Gradients of parameters.

        Returns:
            np.ndarray: Updated parameters.

        >>> optimizer = MomentumSGD(learning_rate=0.1, momentum=0.9)
        >>> params = np.array([1.0, 2.0])
        >>> grads = np.array([0.1, 0.2])
        >>> updated = optimizer.update(0, params, grads)
        >>> updated.shape
        (2,)
        """
        if param_id not in self.velocity:
            self.velocity[param_id] = np.zeros_like(params)

        self.velocity[param_id] = (
            self.momentum * self.velocity[param_id] - self.learning_rate * gradients
        )
        return params + self.velocity[param_id]


# Usage example
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Momentum SGD Example: Minimizing f(x) = x^2")

    optimizer = MomentumSGD(learning_rate=0.1, momentum=0.9)
    x = np.array([5.0])

    for step in range(20):
        gradient = 2 * x
        x = optimizer.update(0, x, gradient)
        if step % 5 == 0:
            print(f"Step {step}: x = {x[0]:.4f}, f(x) = {x[0] ** 2:.4f}")

    print(f"Final: x = {x[0]:.4f}, f(x) = {x[0] ** 2:.4f}")
