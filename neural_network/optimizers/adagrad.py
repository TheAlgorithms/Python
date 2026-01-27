"""
Adagrad Optimizer

Implements Adagrad (Adaptive Gradient) for neural network training using NumPy.
Adagrad adapts the learning rate for each parameter based on historical gradients.

Reference: https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad
Author: Adhithya Laxman Ravi Shankar Geetha
Date: 2025.10.22
"""

import numpy as np


class Adagrad:
    """
    Adagrad optimizer.

    Adapts learning rate individually for each parameter:
        accumulated_grad += gradient^2
        param = param - (learning_rate / sqrt(accumulated_grad + epsilon)) * gradient
    """

    def __init__(self, learning_rate: float = 0.01, epsilon: float = 1e-8) -> None:
        """
        Initialize Adagrad optimizer.

        Args:
            learning_rate (float): Initial learning rate.
            epsilon (float): Small constant for numerical stability.

        >>> optimizer = Adagrad(learning_rate=0.01, epsilon=1e-8)
        >>> optimizer.learning_rate
        0.01
        """
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.accumulated_grad: dict[int, np.ndarray] = {}

    def update(
        self, param_id: int, params: np.ndarray, gradients: np.ndarray
    ) -> np.ndarray:
        """
        Update parameters using Adagrad.

        Args:
            param_id (int): Unique identifier for parameter group.
            params (np.ndarray): Current parameters.
            gradients (np.ndarray): Gradients of parameters.

        Returns:
            np.ndarray: Updated parameters.

        >>> optimizer = Adagrad(learning_rate=0.1)
        >>> params = np.array([1.0, 2.0])
        >>> grads = np.array([0.1, 0.2])
        >>> updated = optimizer.update(0, params, grads)
        >>> updated.shape
        (2,)
        """
        if param_id not in self.accumulated_grad:
            self.accumulated_grad[param_id] = np.zeros_like(params)

        self.accumulated_grad[param_id] += gradients**2
        adjusted_lr = self.learning_rate / (
            np.sqrt(self.accumulated_grad[param_id]) + self.epsilon
        )
        return params - adjusted_lr * gradients


# Usage example
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Adagrad Example: Minimizing f(x) = x^2")

    optimizer = Adagrad(learning_rate=1.0)
    x = np.array([5.0])

    for step in range(20):
        gradient = 2 * x
        x = optimizer.update(0, x, gradient)
        if step % 5 == 0:
            print(f"Step {step}: x = {x[0]:.4f}, f(x) = {x[0] ** 2:.4f}")

    print(f"Final: x = {x[0]:.4f}, f(x) = {x[0] ** 2:.4f}")
