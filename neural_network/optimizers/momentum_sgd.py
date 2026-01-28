"""
Momentum SGD Optimizer

SGD with momentum adds a "velocity" term that accumulates gradients over time,
helping to accelerate convergence and reduce oscillations. This is especially
useful when the loss surface has steep, narrow valleys.

The update rules are:
v_t = β * v_{t-1} + (1-β) * g_t
θ_t = θ_{t-1} - alpha * v_t

where v_t is the velocity (momentum), β is the momentum coefficient,
alpha is the learning rate, and g_t is the gradient.
"""

from __future__ import annotations

from typing import Any

from .base_optimizer import BaseOptimizer


class MomentumSGD(BaseOptimizer):
    """
    SGD optimizer with momentum.

    This optimizer adds a momentum term to SGD, which helps accelerate
    convergence in relevant directions and reduce oscillations. The momentum
    term accumulates a moving average of past gradients.

    Mathematical formulation:
        v_t = β * v_{t-1} + (1-β) * g_t
        θ_{t+1} = θ_t - alpha * v_t

    Where:
        - θ_t: parameters at time step t
        - v_t: velocity (momentum) at time step t
        - alpha: learning rate
        - β: momentum coefficient (typically 0.9)
        - g_t: gradients at time step t

    Parameters:
        learning_rate: The step size for parameter updates (default: 0.01)
        momentum: The momentum coefficient β (default: 0.9)

    Examples:
        >>> momentum_sgd = MomentumSGD(learning_rate=0.1, momentum=0.9)
        >>> params = [1.0, 2.0]
        >>> grads1 = [0.1, 0.2]

        >>> # First update (no previous momentum)
        >>> updated1 = momentum_sgd.update(params, grads1)
        >>> updated1 == [0.999, 1.998]
        True

        >>> # Second update (with accumulated momentum)
        >>> grads2 = [0.1, 0.2]
        >>> updated2 = momentum_sgd.update(updated1, grads2)
        >>> len(updated2) == 2
        True
        >>> updated2[0] < updated1[0]  # Should move further due to momentum
        True

        >>> # Test error handling
        >>> try:
        ...     MomentumSGD(learning_rate=0.1, momentum=1.5)
        ... except ValueError as e:
        ...     print("Caught expected error:", "momentum" in str(e).lower())
        Caught expected error: True

        >>> # Test reset functionality
        >>> momentum_sgd.reset()
        >>> # After reset, velocity should be cleared
    """

    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.9) -> None:
        """
        Initialize Momentum SGD optimizer.

        Args:
            learning_rate: Step size for parameter updates (must be positive)
            momentum: Momentum coefficient β (must be in [0, 1))

        Raises:
            ValueError: If learning_rate is not positive or momentum not in [0, 1)
        """
        super().__init__(learning_rate)

        if not 0 <= momentum < 1:
            msg = f"Momentum must be in [0, 1), got {momentum}"
            raise ValueError(msg)

        self.momentum = momentum
        self._velocity = None  # Will be initialized on first update

    def update(
        self,
        parameters: list[float] | list[list[float]],
        gradients: list[float] | list[list[float]],
    ) -> list[float] | list[list[float]]:
        """
        Update parameters using Momentum SGD rule.

        Performs momentum update:
        v_t = β * v_{t-1} + (1-β) * g_t
        θ_t = θ_{t-1} - alpha * v_t

        Args:
            parameters: Current parameter values
            gradients: Gradients of loss function w.r.t. parameters

        Returns:
            Updated parameters

        Raises:
            ValueError: If parameters and gradients have different shapes
        """

        def _check_shapes_and_get_velocity(
            parameters: Any,
            gradients: Any,
            velocity_values: Any,
        ) -> tuple[Any, Any]:
            # Handle scalar case
            if isinstance(parameters, (int, float)):
                if not isinstance(gradients, (int, float)):
                    raise ValueError(
                        "Shape mismatch: parameter is scalar but gradient is not"
                    )

                if velocity_values is None:
                    velocity_values = 0.0

                # Update velocity: v = β * v + (1-β) * g
                new_velocity = (
                    self.momentum * velocity_values + (1 - self.momentum) * gradients
                )
                # Update parameter: θ = θ - alpha * v
                new_param = parameters - self.learning_rate * new_velocity

                return new_param, new_velocity

            # Handle list case
            if len(parameters) != len(gradients):
                msg = (
                    f"Shape mismatch: parameters length {len(parameters)} vs "
                    f"gradients length {len(gradients)}"
                )
                raise ValueError(msg)

            if velocity_values is None:
                velocity_values = [None] * len(parameters)
            elif len(velocity_values) != len(parameters):
                raise ValueError("Velocity shape mismatch")

            new_params = []
            new_velocity = []

            for _i, (p, g, v) in enumerate(zip(parameters, gradients, velocity_values)):
                if isinstance(p, list) and isinstance(g, list):
                    # Recursive case for nested lists
                    new_p, new_v = _check_shapes_and_get_velocity(p, g, v)
                    new_params.append(new_p)
                    new_velocity.append(new_v)
                elif isinstance(p, (int, float)) and isinstance(g, (int, float)):
                    # Base case for numbers
                    if v is None:
                        v = 0.0

                    new_v = self.momentum * v + (1 - self.momentum) * g
                    new_p = p - self.learning_rate * new_v

                    new_params.append(new_p)
                    new_velocity.append(new_v)
                else:
                    msg = f"Shape mismatch: inconsistent types {type(p)} vs {type(g)}"
                    raise ValueError(msg)

            return new_params, new_velocity

        # Initialize velocity if this is the first update
        if self._velocity is None:
            self._velocity = self._initialize_velocity_like(gradients)

        # Perform the momentum update
        updated_params, self._velocity = _check_shapes_and_get_velocity(
            parameters, gradients, self._velocity
        )

        return updated_params

    def _initialize_velocity_like(
        self, gradients: list[float] | list[list[float]]
    ) -> list[float] | list[list[float]]:
        """
        Initialize velocity with the same structure as gradients, filled with zeros.

        Args:
            gradients: Reference structure for velocity initialization

        Returns:
            Zero-initialized velocity with same structure as gradients
        """
        if isinstance(gradients, (int, float)):
            return 0.0

        velocity = []
        for g in gradients:
            if isinstance(g, list):
                velocity.append(self._initialize_velocity_like(g))
            else:
                velocity.append(0.0)

        return velocity

    def reset(self) -> None:
        """
        Reset the optimizer's internal state (velocity).

        This clears the accumulated momentum, effectively starting fresh.
        Useful when beginning optimization on a new problem.
        """
        self._velocity = None

    def __str__(self) -> str:
        """String representation of Momentum SGD optimizer."""
        return (
            f"MomentumSGD(learning_rate={self.learning_rate}, momentum={self.momentum})"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example optimization comparing SGD vs Momentum SGD
    print("\\nMomentum SGD Example: Minimizing f(x,y) = x^2 + 10*y^2")
    print("=" * 55)
    print("This function has different curvatures in x and y directions.")
    print("Momentum should help accelerate convergence along the x-axis.")

    # Initialize both optimizers
    from .sgd import SGD  # Import regular SGD for comparison

    sgd = SGD(learning_rate=0.01)
    momentum_sgd = MomentumSGD(learning_rate=0.01, momentum=0.9)

    # Starting point
    x_sgd = [3.0, 1.0]
    x_momentum = [3.0, 1.0]

    print(f"\\nInitial point: x={x_sgd[0]:.3f}, y={x_sgd[1]:.3f}")
    print(f"Initial f(x,y): {x_sgd[0] ** 2 + 10 * x_sgd[1] ** 2:.3f}")

    for i in range(50):
        # Gradients of f(x,y) = x^2 + 10*y^2 are [2x, 20y]
        grad_sgd = [2 * x_sgd[0], 20 * x_sgd[1]]
        grad_momentum = [2 * x_momentum[0], 20 * x_momentum[1]]

        # Update both
        x_sgd = sgd.update(x_sgd, grad_sgd)
        x_momentum = momentum_sgd.update(x_momentum, grad_momentum)

        if i % 10 == 9:  # Print every 10 iterations
            f_sgd = x_sgd[0] ** 2 + 10 * x_sgd[1] ** 2
            f_momentum = x_momentum[0] ** 2 + 10 * x_momentum[1] ** 2

            print(f"Step {i + 1:2d}:")
            print(
                f"  SGD:      f = {f_sgd:.6f}, x = ({x_sgd[0]:6.3f}, {x_sgd[1]:6.3f})"
            )
            print(
                f"  Momentum: f = {f_momentum:.6f}, x = "
                f"({x_momentum[0]:6.3f}, {x_momentum[1]:6.3f})"
            )

    print("\\nFinal comparison:")
    f_final_sgd = x_sgd[0] ** 2 + 10 * x_sgd[1] ** 2
    f_final_momentum = x_momentum[0] ** 2 + 10 * x_momentum[1] ** 2
    print(f"SGD final loss: {f_final_sgd:.6f}")
    print(f"Momentum final loss: {f_final_momentum:.6f}")
    print(
        f"Improvement with momentum: "
        f"{((f_final_sgd - f_final_momentum) / f_final_sgd * 100):.1f}%"
    )
