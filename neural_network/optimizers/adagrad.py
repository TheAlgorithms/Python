"""
Adagrad Optimizer

Adagrad adapts the learning rate for each parameter individually based on the
historical sum of squared gradients. Parameters with large gradients get smaller
effective learning rates, while parameters with small gradients get larger rates.

The update rules are:
G_t = G_{t-1} + g_t ⊙ g_t  (element-wise squared gradient accumulation)
θ_{t+1} = θ_t - (α / √(G_t + ε)) ⊙ g_t

where G_t accumulates squared gradients, ε prevents division by zero,
and ⊙ denotes element-wise multiplication.
"""

from __future__ import annotations

import math

from .base_optimizer import BaseOptimizer


class Adagrad(BaseOptimizer):
    """
    Adagrad (Adaptive Gradient) optimizer.

    Adagrad automatically adapts the learning rate for each parameter based on
    historical gradient information. Parameters that receive large gradients
    will have their effective learning rate reduced, while parameters with
    small gradients will have their effective learning rate increased.

    Mathematical formulation:
        G_t = G_{t-1} + g_t ⊙ g_t
        θ_{t+1} = θ_t - (α / √(G_t + ε)) ⊙ g_t

    Where:
        - θ_t: parameters at time step t
        - G_t: accumulated squared gradients up to time t
        - α: learning rate
        - ε: small constant for numerical stability (typically 1e-8)
        - g_t: gradients at time step t
        - ⊙: element-wise multiplication

    Parameters:
        learning_rate: The base learning rate (default: 0.01)
        epsilon: Small constant for numerical stability (default: 1e-8)

    Examples:
        >>> adagrad = Adagrad(learning_rate=0.1, epsilon=1e-8)
        >>> params = [1.0, 2.0]
        >>> grads1 = [0.1, 1.0]  # Different gradient magnitudes

        >>> # First update
        >>> updated1 = adagrad.update(params, grads1)
        >>> len(updated1) == 2
        True
        >>> updated1[0] > 0.85  # Small gradient -> larger step
        True
        >>> updated1[1] < 1.95   # Large gradient -> smaller step (but still close to 2.0)
        True

        >>> # Second update (gradients accumulate)
        >>> grads2 = [0.1, 1.0]
        >>> updated2 = adagrad.update(updated1, grads2)
        >>> len(updated2) == 2
        True

        >>> # Test error handling
        >>> try:
        ...     Adagrad(learning_rate=0.1, epsilon=-1e-8)
        ... except ValueError as e:
        ...     print("Caught expected error:", "epsilon" in str(e).lower())
        Caught expected error: True

        >>> # Test reset
        >>> adagrad.reset()
    """

    def __init__(self, learning_rate: float = 0.01, epsilon: float = 1e-8) -> None:
        """
        Initialize Adagrad optimizer.

        Args:
            learning_rate: Base learning rate (must be positive)
            epsilon: Small constant for numerical stability (must be positive)

        Raises:
            ValueError: If learning_rate or epsilon is not positive
        """
        super().__init__(learning_rate)

        if epsilon <= 0:
            msg = f"Epsilon must be positive, got {epsilon}"
            raise ValueError(msg)

        self.epsilon = epsilon
        self._accumulated_gradients = None  # Will be initialized on first update

    def update(
        self,
        parameters: list[float] | list[list[float]],
        gradients: list[float] | list[list[float]],
    ) -> list[float] | list[list[float]]:
        """
        Update parameters using Adagrad rule.

        Performs adaptive gradient update:
        G_t = G_{t-1} + g_t^2
        θ_{t+1} = θ_t - (α / √(G_t + ε)) * g_t

        Args:
            parameters: Current parameter values
            gradients: Gradients of loss function w.r.t. parameters

        Returns:
            Updated parameters

        Raises:
            ValueError: If parameters and gradients have different shapes
        """

        def _adagrad_update_recursive(
            parameters: float | list[float | list[float]],
            gradients: float | list[float | list[float]],
            accumulated_gradients: float | list[float | list[float]]
        ) -> tuple[float | list[float | list[float]], float | list[float | list[float]]]:
            # Handle scalar case
            if isinstance(parameters, (int, float)):
                if not isinstance(gradients, (int, float)):
                    raise ValueError(
                        "Shape mismatch: parameter is scalar but gradient is not"
                    )

                if accumulated_gradients is None:
                    accumulated_gradients = 0.0

                # Accumulate squared gradients: G = G + g^2
                new_acc_grads = accumulated_gradients + gradients * gradients

                # Adaptive learning rate: α / √(G + ε)
                adaptive_lr = self.learning_rate / math.sqrt(
                    new_acc_grads + self.epsilon
                )

                # Parameter update: θ = θ - adaptive_lr * g
                new_param = parameters - adaptive_lr * gradients

                return new_param, new_acc_grads

            # Handle list case
            if len(parameters) != len(gradients):
                msg = (
                    f"Shape mismatch: parameters length {len(parameters)} vs "
                    f"gradients length {len(gradients)}"
                )
                raise ValueError(
                    msg
                )

            if accumulated_gradients is None:
                accumulated_gradients = [None] * len(parameters)
            elif len(accumulated_gradients) != len(parameters):
                raise ValueError("Accumulated gradients shape mismatch")

            new_params = []
            new_acc_grads = []

            for _i, (p, g, ag) in enumerate(zip(parameters, gradients, accumulated_gradients)):
                if isinstance(p, list) and isinstance(g, list):
                    # Recursive case for nested lists
                    new_p, new_ag = _adagrad_update_recursive(p, g, ag)
                    new_params.append(new_p)
                    new_acc_grads.append(new_ag)
                elif isinstance(p, (int, float)) and isinstance(g, (int, float)):
                    # Base case for numbers
                    if ag is None:
                        ag = 0.0

                    # Accumulate squared gradient
                    new_ag = ag + g * g

                    # Adaptive update
                    adaptive_lr = self.learning_rate / math.sqrt(new_ag + self.epsilon)
                    new_p = p - adaptive_lr * g

                    new_params.append(new_p)
                    new_acc_grads.append(new_ag)
                else:
                    msg = f"Shape mismatch: inconsistent types {type(p)} vs {type(g)}"
                    raise ValueError(
                        msg
                    )

            return new_params, new_acc_grads

        # Initialize accumulated gradients if this is the first update
        if self._accumulated_gradients is None:
            self._accumulated_gradients = self._initialize_like(gradients)

        # Perform the Adagrad update
        updated_params, self._accumulated_gradients = _adagrad_update_recursive(
            parameters, gradients, self._accumulated_gradients
        )

        return updated_params

    def _initialize_like(
        self, gradients: list[float] | list[list[float]]
    ) -> list[float] | list[list[float]]:
        """
        Initialize accumulated gradients with same structure as gradients, filled with zeros.

        Args:
            gradients: Reference structure for initialization

        Returns:
            Zero-initialized structure with same shape as gradients
        """
        if isinstance(gradients, (int, float)):
            return 0.0

        acc_grads = []
        for g in gradients:
            if isinstance(g, list):
                acc_grads.append(self._initialize_like(g))
            else:
                acc_grads.append(0.0)

        return acc_grads

    def reset(self) -> None:
        """
        Reset the optimizer's internal state (accumulated gradients).

        This clears all accumulated squared gradients, effectively starting fresh.
        Useful when beginning optimization on a new problem.
        """
        self._accumulated_gradients = None

    def __str__(self) -> str:
        """String representation of Adagrad optimizer."""
        return f"Adagrad(learning_rate={self.learning_rate}, epsilon={self.epsilon})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example demonstrating Adagrad's adaptive behavior
    print("\\nAdagrad Example: Adaptive Learning Rates")
    print("=" * 42)
    print("Function: f(x,y) = x^2 + 100*y^2 (different scales)")
    print("Adagrad should adapt to give y larger effective learning rate")

    from .sgd import SGD

    # Initialize optimizers
    sgd = SGD(learning_rate=0.1)
    adagrad = Adagrad(learning_rate=0.1)

    # Starting point
    x_sgd = [5.0, 1.0]
    x_adagrad = [5.0, 1.0]

    print(f"\\nStarting point: x={x_sgd[0]:.3f}, y={x_sgd[1]:.3f}")
    print(f"Initial f(x,y): {x_sgd[0] ** 2 + 100 * x_sgd[1] ** 2:.3f}")

    for i in range(30):
        # Gradients of f(x,y) = x^2 + 100*y^2 are [2x, 200y]
        grad_sgd = [2 * x_sgd[0], 200 * x_sgd[1]]
        grad_adagrad = [2 * x_adagrad[0], 200 * x_adagrad[1]]

        # Update both optimizers
        x_sgd = sgd.update(x_sgd, grad_sgd)
        x_adagrad = adagrad.update(x_adagrad, grad_adagrad)

        if i % 5 == 4:  # Print every 5 iterations
            f_sgd = x_sgd[0] ** 2 + 100 * x_sgd[1] ** 2
            f_adagrad = x_adagrad[0] ** 2 + 100 * x_adagrad[1] ** 2

            print(f"\\nStep {i + 1:2d}:")
            print(
                f"  SGD:     f = {f_sgd:8.3f}, x = ({x_sgd[0]:6.3f}, {x_sgd[1]:6.3f})"
            )
            print(
                f"  Adagrad: f = {f_adagrad:8.3f}, x = ({x_adagrad[0]:6.3f}, {x_adagrad[1]:6.3f})"
            )

    print("\\nFinal comparison:")
    f_final_sgd = x_sgd[0] ** 2 + 100 * x_sgd[1] ** 2
    f_final_adagrad = x_adagrad[0] ** 2 + 100 * x_adagrad[1] ** 2
    print(f"SGD final loss:     {f_final_sgd:.6f}")
    print(f"Adagrad final loss: {f_final_adagrad:.6f}")

    if f_final_adagrad < f_final_sgd:
        improvement = (f_final_sgd - f_final_adagrad) / f_final_sgd * 100
        print(f"Adagrad achieved {improvement:.1f}% better convergence!")
    else:
        print("SGD performed better on this example.")
