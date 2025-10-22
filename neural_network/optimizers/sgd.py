"""
Stochastic Gradient Descent (SGD) Optimizer

SGD is the most basic optimization algorithm for neural networks. It updates
parameters by moving in the direction opposite to the gradient of the loss function.

The update rule is: θ = θ - alpha * ∇θ
where θ are the parameters, alpha is the learning rate, and ∇θ is the gradient.
"""

from __future__ import annotations

from .base_optimizer import BaseOptimizer


class SGD(BaseOptimizer):
    """
    Stochastic Gradient Descent optimizer.

    This is the simplest and most fundamental optimizer. It performs parameter
    updates by moving in the direction opposite to the gradient, scaled by
    the learning rate.

    Mathematical formulation:
        θ_{t+1} = θ_t - alpha * g_t

    Where:
        - θ_t: parameters at time step t
        - alpha: learning rate
        - g_t: gradients at time step t

    Parameters:
        learning_rate: The step size for parameter updates (default: 0.01)

    Examples:
        >>> sgd = SGD(learning_rate=0.1)
        >>> params = [1.0, 2.0]
        >>> grads = [0.1, 0.2]
        >>> updated = sgd.update(params, grads)
        >>> updated == [0.99, 1.98]
        True

        >>> # Test with 2D parameters (list of lists)
        >>> params_2d = [[1.0, 2.0], [3.0, 4.0]]
        >>> grads_2d = [[0.1, 0.2], [0.3, 0.4]]
        >>> updated_2d = sgd.update(params_2d, grads_2d)
        >>> expected = [[0.99, 1.98], [2.97, 3.96]]
        >>> updated_2d == expected
        True

        >>> # Test error handling
        >>> try:
        ...     SGD(learning_rate=-0.1)
        ... except ValueError as e:
        ...     print("Caught expected error:", str(e))
        Caught expected error: Learning rate must be positive, got -0.1

        >>> # Test mismatched shapes
        >>> try:
        ...     sgd.update([1.0], [1.0, 2.0])
        ... except ValueError as e:
        ...     print("Caught expected error:", "Shape mismatch" in str(e))
        Caught expected error: True
    """

    def __init__(self, learning_rate: float = 0.01) -> None:
        """
        Initialize SGD optimizer.

        Args:
            learning_rate: Step size for parameter updates (must be positive)

        Raises:
            ValueError: If learning_rate is not positive
        """
        super().__init__(learning_rate)

    def update(
        self,
        parameters: list[float] | list[list[float]],
        gradients: list[float] | list[list[float]],
    ) -> list[float] | list[list[float]]:
        """
        Update parameters using SGD rule.

        Performs the classic SGD update: θ = θ - alpha * ∇θ

        Args:
            parameters: Current parameter values
            gradients: Gradients of loss function w.r.t. parameters

        Returns:
            Updated parameters

        Raises:
            ValueError: If parameters and gradients have different shapes
        """

        def _check_and_update_recursive(
            parameters: float | list[float | list[float]],
            gradients: float | list[float | list[float]],
        ) -> float | list[float | list[float]]:
            # Handle 1D case (list of floats)
            if isinstance(parameters, (int, float)):
                if not isinstance(gradients, (int, float)):
                    raise ValueError(
                        "Shape mismatch: parameter is scalar but gradient is not"
                    )
                return parameters - self.learning_rate * gradients

            # Handle list case
            if len(parameters) != len(gradients):
                msg = (
                    f"Shape mismatch: parameters length {len(parameters)} vs "
                    f"gradients length {len(gradients)}"
                )
                raise ValueError(msg)

            result = []
            for p, g in zip(parameters, gradients):
                if isinstance(p, list) and isinstance(g, list):
                    # Recursive case for nested lists
                    result.append(_check_and_update_recursive(p, g))
                elif isinstance(p, (int, float)) and isinstance(g, (int, float)):
                    # Base case for numbers
                    result.append(p - self.learning_rate * g)
                else:
                    msg = f"Shape mismatch: inconsistent types {type(p)} vs {type(g)}"
                    raise ValueError(msg)

            return result

        return _check_and_update_recursive(parameters, gradients)

    def __str__(self) -> str:
        """String representation of SGD optimizer."""
        return f"SGD(learning_rate={self.learning_rate})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example optimization of a simple quadratic function
    # f(x) = x^2, so gradient f'(x) = 2x
    # Global minimum at x = 0

    print("\\nSGD Example: Minimizing f(x) = x^2")
    print("=" * 40)

    sgd = SGD(learning_rate=0.1)
    x = [5.0]  # Starting point

    print(f"Initial x: {x[0]:.6f}, f(x): {x[0] ** 2:.6f}")

    for i in range(20):
        gradient = [2 * x[0]]  # Gradient of x^2 is 2x
        x = sgd.update(x, gradient)

        if i % 5 == 4:  # Print every 5 iterations
            print(f"Step {i + 1:2d}: x = {x[0]:8.6f}, f(x) = {x[0] ** 2:8.6f}")

    print(f"\\nFinal result: x = {x[0]:.6f} (should be close to 0)")
