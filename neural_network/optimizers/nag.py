"""
Nesterov Accelerated Gradient (NAG) Optimizer

NAG is an improved version of momentum that evaluates the gradient not at the current
position, but at the approximate future position. This "look-ahead" helps reduce
overshooting and often leads to better convergence.

The update rules are:
θ_lookahead = θ_t - alpha * β * v_{t-1}
g_t = ∇f(θ_lookahead)  # Gradient at lookahead position
v_t = β * v_{t-1} + (1-β) * g_t
θ_{t+1} = θ_t - alpha * v_t

However, a more efficient formulation equivalent to the above is:
v_t = β * v_{t-1} + (1-β) * g_t
θ_{t+1} = θ_t - alpha * (β * v_t + (1-β) * g_t)
"""

from __future__ import annotations

from .base_optimizer import BaseOptimizer


class NAG(BaseOptimizer):
    """
    Nesterov Accelerated Gradient optimizer.

    NAG improves upon momentum by evaluating the gradient at an approximate
    future position rather than the current position. This lookahead mechanism
    helps prevent overshooting and often leads to better convergence properties.

    Mathematical formulation (efficient version):
        v_t = β * v_{t-1} + (1-β) * g_t
        θ_{t+1} = θ_t - alpha * (β * v_t + (1-β) * g_t)

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
        >>> nag = NAG(learning_rate=0.1, momentum=0.9)
        >>> params = [1.0, 2.0]
        >>> grads1 = [0.1, 0.2]

        >>> # First update (no previous momentum)
        >>> updated1 = nag.update(params, grads1)
        >>> updated1 == [0.9981, 1.9962]
        True

        >>> # Second update (with lookahead)
        >>> grads2 = [0.1, 0.2]
        >>> updated2 = nag.update(updated1, grads2)
        >>> len(updated2) == 2
        True
        >>> updated2[0] < updated1[0]  # Should move further
        True

        >>> # Test error handling
        >>> try:
        ...     NAG(learning_rate=0.1, momentum=-0.1)
        ... except ValueError as e:
        ...     print("Caught expected error:", "momentum" in str(e).lower())
        Caught expected error: True

        >>> # Test reset functionality
        >>> nag.reset()
    """

    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.9) -> None:
        """
        Initialize NAG optimizer.

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
        Update parameters using NAG rule.

        Performs Nesterov update using efficient formulation:
        v_t = β * v_{t-1} + (1-β) * g_t
        θ_{t+1} = θ_t - alpha * (β * v_t + (1-β) * g_t)

        Args:
            parameters: Current parameter values
            gradients: Gradients of loss function w.r.t. parameters

        Returns:
            Updated parameters

        Raises:
            ValueError: If parameters and gradients have different shapes
        """

        def _nag_update_recursive(
            parameters: float | list,
            gradients: float | list,
            velocity: float | list | None
        ) -> tuple[float | list, float | list]:
            # Handle scalar case
            if isinstance(parameters, (int, float)):
                if not isinstance(gradients, (int, float)):
                    raise ValueError(
                        "Shape mismatch: parameter is scalar but gradient is not"
                    )

                if velocity is None:
                    velocity = 0.0

                # Update velocity: v = β * v + (1-β) * g
                new_velocity = (
                    self.momentum * velocity + (1 - self.momentum) * gradients
                )

                # NAG update: θ = θ - alpha * (β * v + (1-β) * g)
                nesterov_update = (
                    self.momentum * new_velocity + (1 - self.momentum) * gradients
                )
                new_param = parameters - self.learning_rate * nesterov_update

                return new_param, new_velocity

            # Handle list case
            if len(parameters) != len(gradients):
                msg = (
                    f"Shape mismatch: parameters length {len(parameters)} vs "
                    f"gradients length {len(gradients)}"
                )
                raise ValueError(
                    msg
                )

            if velocity is None:
                velocity = [None] * len(parameters)
            elif len(velocity) != len(parameters):
                raise ValueError("Velocity shape mismatch")

            new_params = []
            new_velocity = []

            for _i, (p, g, v) in enumerate(zip(parameters, gradients, velocity)):
                if isinstance(p, list) and isinstance(g, list):
                    # Recursive case for nested lists
                    new_p, new_v = _nag_update_recursive(p, g, v)
                    new_params.append(new_p)
                    new_velocity.append(new_v)
                elif isinstance(p, (int, float)) and isinstance(g, (int, float)):
                    # Base case for numbers
                    if v is None:
                        v = 0.0

                    # Update velocity
                    new_v = self.momentum * v + (1 - self.momentum) * g

                    # NAG update with lookahead
                    nesterov_update = self.momentum * new_v + (1 - self.momentum) * g
                    new_p = p - self.learning_rate * nesterov_update

                    new_params.append(new_p)
                    new_velocity.append(new_v)
                else:
                    msg = f"Shape mismatch: inconsistent types {type(p)} vs {type(g)}"
                    raise ValueError(
                        msg
                    )

            return new_params, new_velocity

        # Initialize velocity if this is the first update
        if self._velocity is None:
            self._velocity = self._initialize_velocity_like(gradients)

        # Perform the NAG update
        updated_params, self._velocity = _nag_update_recursive(
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
        """String representation of NAG optimizer."""
        return f"NAG(learning_rate={self.learning_rate}, momentum={self.momentum})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example demonstrating NAG vs regular Momentum on a function with local minima
    print("\\nNAG Example: Comparing NAG vs Momentum SGD")
    print("=" * 45)
    print("Function: f(x) = 0.1*x^4 - 2*x^2 + x (has local minima)")

    from .momentum_sgd import MomentumSGD

    # Initialize optimizers with same parameters
    momentum_sgd = MomentumSGD(learning_rate=0.01, momentum=0.9)
    nag = NAG(learning_rate=0.01, momentum=0.9)

    # Starting point (near local minimum)
    x_momentum = [2.5]
    x_nag = [2.5]

    def gradient_f(x: float) -> float:
        """Gradient of f(x) = 0.1*x^4 - 2*x^2 + x is f'(x) = 0.4*x^3 - 4*x + 1"""
        return 0.4 * x**3 - 4 * x + 1

    def f(x: float) -> float:
        """The function f(x) = 0.1*x^4 - 2*x^2 + x"""
        return 0.1 * x**4 - 2 * x**2 + x

    print(f"\\nStarting point: x = {x_momentum[0]:.3f}")
    print(f"Initial f(x): {f(x_momentum[0]):.6f}")

    for i in range(100):
        # Calculate gradients
        grad_momentum = [gradient_f(x_momentum[0])]
        grad_nag = [gradient_f(x_nag[0])]

        # Update both optimizers
        x_momentum = momentum_sgd.update(x_momentum, grad_momentum)
        x_nag = nag.update(x_nag, grad_nag)

        if i % 20 == 19:  # Print every 20 iterations
            f_momentum = f(x_momentum[0])
            f_nag = f(x_nag[0])

            print(f"\\nStep {i + 1:3d}:")
            print(f"  Momentum: x = {x_momentum[0]:8.4f}, f(x) = {f_momentum:8.6f}")
            print(f"  NAG:      x = {x_nag[0]:8.4f}, f(x) = {f_nag:8.6f}")

    print("\\nFinal comparison:")
    f_final_momentum = f(x_momentum[0])
    f_final_nag = f(x_nag[0])
    print(f"Momentum final: x = {x_momentum[0]:.4f}, f = {f_final_momentum:.6f}")
    print(f"NAG final:      x = {x_nag[0]:.4f}, f = {f_final_nag:.6f}")

    if f_final_nag < f_final_momentum:
        improvement = (f_final_momentum - f_final_nag) / abs(f_final_momentum) * 100
        print(f"NAG achieved {improvement:.1f}% better function value!")
    else:
        print("Both optimizers achieved similar performance.")
