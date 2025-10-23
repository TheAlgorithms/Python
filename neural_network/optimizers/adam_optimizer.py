"""
Adam Optimizer

Implements Adam (Adaptive Moment Estimation) for neural network training using NumPy.
Adam combines momentum and adaptive learning rates using first and
second moment estimates.

Reference: https://arxiv.org/abs/1412.6980
Author: Adhithya Laxman Ravi Shankar Geetha
Date: 2025.10.21
"""

import numpy as np


class Adam:
    """
    Adam optimizer.

    Combines momentum and RMSProp:
        m = beta1 * m + (1 - beta1) * gradient
        v = beta2 * v + (1 - beta2) * gradient^2
        m_hat = m / (1 - beta1^t)
        v_hat = v / (1 - beta2^t)
        param = param - learning_rate * m_hat / (sqrt(v_hat) + epsilon)
    """

    def __init__(
        self,
        learning_rate: float = 0.001,
        beta1: float = 0.9,
        beta2: float = 0.999,
        epsilon: float = 1e-8,
    ) -> None:
        """
        Initialize Adam optimizer.

        Args:
            learning_rate (float): Learning rate.
            beta1 (float): Exponential decay rate for first moment.
            beta2 (float): Exponential decay rate for second moment.
            epsilon (float): Small constant for numerical stability.

        >>> optimizer = Adam(learning_rate=0.001, beta1=0.9, beta2=0.999)
        >>> optimizer.beta1
        0.9
        """
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m: dict[int, np.ndarray] = {}
        self.v: dict[int, np.ndarray] = {}
        self.t: dict[int, int] = {}

    def update(
        self, param_id: int, params: np.ndarray, gradients: np.ndarray
    ) -> np.ndarray:
        """
        Update parameters using Adam.

        Args:
            param_id (int): Unique identifier for parameter group.
            params (np.ndarray): Current parameters.
            gradients (np.ndarray): Gradients of parameters.

        Returns:
            np.ndarray: Updated parameters.

        >>> optimizer = Adam(learning_rate=0.1)
        >>> params = np.array([1.0, 2.0])
        >>> grads = np.array([0.1, 0.2])
        >>> updated = optimizer.update(0, params, grads)
        >>> updated.shape
        (2,)
        """
        if param_id not in self.m:
            self.m[param_id] = np.zeros_like(params)
            self.v[param_id] = np.zeros_like(params)
            self.t[param_id] = 0

        self.t[param_id] += 1

        self.m[param_id] = self.beta1 * self.m[param_id] + (1 - self.beta1) * gradients
        self.v[param_id] = self.beta2 * self.v[param_id] + (1 - self.beta2) * (
            gradients**2
        )

        m_hat = self.m[param_id] / (1 - self.beta1 ** self.t[param_id])
        v_hat = self.v[param_id] / (1 - self.beta2 ** self.t[param_id])

        return params - self.learning_rate * m_hat / (np.sqrt(v_hat) + self.epsilon)


# Usage example
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Adam Example: Minimizing f(x) = x^2")

    optimizer = Adam(learning_rate=0.1)
    x = np.array([5.0])

    for step in range(20):
        gradient = 2 * x
        x = optimizer.update(0, x, gradient)
        if step % 5 == 0:
            print(f"Step {step}: x = {x[0]:.4f}, f(x) = {x[0] ** 2:.4f}")

    print(f"Final: x = {x[0]:.4f}, f(x) = {x[0] ** 2:.4f}")
