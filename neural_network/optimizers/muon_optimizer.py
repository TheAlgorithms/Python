"""
Muon Optimizer

Implements Muon optimizer for neural network hidden layers using NumPy.
Muon uses Newton-Schulz orthogonalization iterations for improved convergence.

Reference: https://kellerjordan.github.io/posts/muon/
Author: Adhithya Laxman Ravi Shankar Geetha
Date: 2025.10.21
"""

import numpy as np


class Muon:
    """
    Muon optimizer for hidden layer weight matrices.

    Applies Newton-Schulz orthogonalization to gradients before updates.
    """

    def __init__(
        self, learning_rate: float = 0.02, momentum: float = 0.95, ns_steps: int = 5
    ) -> None:
        """
        Initialize Muon optimizer.

        Args:
            learning_rate (float): Learning rate for updates.
            momentum (float): Momentum factor.
            ns_steps (int): Number of Newton-Schulz iteration steps.

        >>> optimizer = Muon(learning_rate=0.02, momentum=0.95, ns_steps=5)
        >>> optimizer.momentum
        0.95
        """
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.ns_steps = ns_steps
        self.velocity: dict[int, np.ndarray] = {}

    def newton_schulz_orthogonalize(self, matrix: np.ndarray) -> np.ndarray:
        """
        Orthogonalize matrix using Newton-Schulz iterations.

        Args:
            matrix (np.ndarray): Input matrix.

        Returns:
            np.ndarray: Orthogonalized matrix.

        >>> optimizer = Muon()
        >>> mat = np.array([[1.0, 0.5], [0.5, 1.0]])
        >>> orth = optimizer.newton_schulz_orthogonalize(mat)
        >>> orth.shape
        (2, 2)
        """
        if matrix.shape[0] < matrix.shape[1]:
            matrix = matrix.T
            transposed = True
        else:
            transposed = False

        a = matrix.copy()
        for _ in range(self.ns_steps):
            a = 1.5 * a - 0.5 * a @ (a.T @ a)

        return a.T if transposed else a

    def update(
        self, param_id: int, params: np.ndarray, gradients: np.ndarray
    ) -> np.ndarray:
        """
        Update parameters using Muon.

        Args:
            param_id (int): Unique identifier for parameter group.
            params (np.ndarray): Current parameters.
            gradients (np.ndarray): Gradients of parameters.

        Returns:
            np.ndarray: Updated parameters.

        >>> optimizer = Muon(learning_rate=0.1, momentum=0.9)
        >>> params = np.array([[1.0, 2.0], [3.0, 4.0]])
        >>> grads = np.array([[0.1, 0.2], [0.3, 0.4]])
        >>> updated = optimizer.update(0, params, grads)
        >>> updated.shape
        (2, 2)
        """
        if param_id not in self.velocity:
            self.velocity[param_id] = np.zeros_like(params)

        ortho_grad = self.newton_schulz_orthogonalize(gradients)
        self.velocity[param_id] = self.momentum * self.velocity[param_id] + ortho_grad

        return params - self.learning_rate * self.velocity[param_id]


# Usage example
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Muon Example: Optimizing a 2x2 matrix")

    optimizer = Muon(learning_rate=0.05, momentum=0.9)
    weights = np.array([[1.0, 2.0], [3.0, 4.0]])

    for step in range(10):
        gradients = 0.1 * weights  # Simplified gradient
        weights = optimizer.update(0, weights, gradients)
        if step % 3 == 0:
            print(f"Step {step}: weights =\n{weights}")

    print(f"Final weights:\n{weights}")
