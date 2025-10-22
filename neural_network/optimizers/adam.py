"""
Adam Optimizer

Adam (Adaptive Moment Estimation) combines the benefits of momentum and adaptive
learning rates. It maintains running averages of both gradients (first moment)
and squared gradients (second moment), with bias correction for initialization.

The update rules are:
m_t = β₁ * m_{t-1} + (1-β₁) * g_t        # First moment estimate
v_t = β₂ * v_{t-1} + (1-β₂) * g_t²       # Second moment estimate
m̂_t = m_t / (1 - β₁^t)                   # Bias-corrected first moment
v̂_t = v_t / (1 - β₂^t)                   # Bias-corrected second moment
θ_{t+1} = θ_t - α * m̂_t / (√v̂_t + ε)    # Parameter update
"""

from __future__ import annotations

import math
from typing import List, Union

from .base_optimizer import BaseOptimizer


class Adam(BaseOptimizer):
    """
    Adam (Adaptive Moment Estimation) optimizer.

    Adam combines the advantages of AdaGrad (which works well with sparse gradients)
    and RMSProp (which works well in non-stationary settings). It computes adaptive
    learning rates for each parameter from estimates of first and second moments
    of the gradients, with bias correction.

    Mathematical formulation:
        m_t = β₁ * m_{t-1} + (1-β₁) * g_t
        v_t = β₂ * v_{t-1} + (1-β₂) * g_t²
        m̂_t = m_t / (1 - β₁^t)
        v̂_t = v_t / (1 - β₂^t)
        θ_{t+1} = θ_t - α * m̂_t / (√v̂_t + ε)

    Where:
        - θ_t: parameters at time step t
        - m_t, v_t: first and second moment estimates
        - m̂_t, v̂_t: bias-corrected moment estimates
        - α: learning rate (default: 0.001)
        - β₁, β₂: exponential decay rates (default: 0.9, 0.999)
        - ε: small constant for numerical stability (default: 1e-8)
        - t: time step

    Parameters:
        learning_rate: The learning rate (default: 0.001)
        beta1: Exponential decay rate for first moment (default: 0.9)
        beta2: Exponential decay rate for second moment (default: 0.999)
        epsilon: Small constant for numerical stability (default: 1e-8)

    Examples:
        >>> adam = Adam(learning_rate=0.01, beta1=0.9, beta2=0.999)
        >>> params = [1.0, 2.0]
        >>> grads1 = [0.1, 0.2]

        >>> # First update (with bias correction)
        >>> updated1 = adam.update(params, grads1)
        >>> len(updated1) == 2
        True
        >>> updated1[0] < params[0]  # Should decrease
        True

        >>> # Second update
        >>> grads2 = [0.05, 0.1]
        >>> updated2 = adam.update(updated1, grads2)
        >>> len(updated2) == 2
        True

        >>> # Test error handling
        >>> try:
        ...     Adam(beta1=1.5)
        ... except ValueError as e:
        ...     print("Caught expected error:", "beta1" in str(e).lower())
        Caught expected error: True

        >>> try:
        ...     Adam(beta2=1.0)  # beta2 must be < 1
        ... except ValueError as e:
        ...     print("Caught expected error:", "beta2" in str(e).lower())
        Caught expected error: True

        >>> # Test reset
        >>> adam.reset()
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
            learning_rate: Learning rate (must be positive)
            beta1: Exponential decay rate for first moment (must be in [0, 1))
            beta2: Exponential decay rate for second moment (must be in [0, 1))
            epsilon: Small constant for numerical stability (must be positive)

        Raises:
            ValueError: If any parameter is outside valid range
        """
        super().__init__(learning_rate)

        if not 0 <= beta1 < 1:
            raise ValueError(f"beta1 must be in [0, 1), got {beta1}")
        if not 0 <= beta2 < 1:
            raise ValueError(f"beta2 must be in [0, 1), got {beta2}")
        if epsilon <= 0:
            raise ValueError(f"epsilon must be positive, got {epsilon}")

        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

        # Internal state
        self._first_moment = None  # m_t
        self._second_moment = None  # v_t
        self._time_step = 0  # t (for bias correction)

    def update(
        self,
        parameters: Union[List[float], List[List[float]]],
        gradients: Union[List[float], List[List[float]]],
    ) -> Union[List[float], List[List[float]]]:
        """
        Update parameters using Adam rule.

        Performs Adam update with bias correction:
        m_t = β₁ * m_{t-1} + (1-β₁) * g_t
        v_t = β₂ * v_{t-1} + (1-β₂) * g_t²
        m̂_t = m_t / (1 - β₁^t)
        v̂_t = v_t / (1 - β₂^t)
        θ_{t+1} = θ_t - α * m̂_t / (√v̂_t + ε)

        Args:
            parameters: Current parameter values
            gradients: Gradients of loss function w.r.t. parameters

        Returns:
            Updated parameters

        Raises:
            ValueError: If parameters and gradients have different shapes
        """
        # Initialize moments if this is the first update
        if self._first_moment is None:
            self._first_moment = self._initialize_like(gradients)
            self._second_moment = self._initialize_like(gradients)

        # Increment time step
        self._time_step += 1

        # Bias correction terms
        bias_correction1 = 1 - self.beta1**self._time_step
        bias_correction2 = 1 - self.beta2**self._time_step

        def _adam_update_recursive(params, grads, first_moment, second_moment):
            # Handle scalar case
            if isinstance(params, (int, float)):
                if not isinstance(grads, (int, float)):
                    raise ValueError(
                        "Shape mismatch: parameter is scalar but gradient is not"
                    )

                # Update first moment: m = β₁ * m + (1-β₁) * g
                new_first_moment = self.beta1 * first_moment + (1 - self.beta1) * grads

                # Update second moment: v = β₂ * v + (1-β₂) * g²
                new_second_moment = self.beta2 * second_moment + (1 - self.beta2) * (
                    grads * grads
                )

                # Bias-corrected moments
                m_hat = new_first_moment / bias_correction1
                v_hat = new_second_moment / bias_correction2

                # Parameter update: θ = θ - α * m̂ / (√v̂ + ε)
                new_param = params - self.learning_rate * m_hat / (
                    math.sqrt(v_hat) + self.epsilon
                )

                return new_param, new_first_moment, new_second_moment

            # Handle list case
            if len(params) != len(grads):
                raise ValueError(
                    f"Shape mismatch: parameters length {len(params)} vs "
                    f"gradients length {len(grads)}"
                )

            new_params = []
            new_first_moments = []
            new_second_moments = []

            for p, g, m1, m2 in zip(params, grads, first_moment, second_moment):
                if isinstance(p, list) and isinstance(g, list):
                    # Recursive case for nested lists
                    new_p, new_m1, new_m2 = _adam_update_recursive(p, g, m1, m2)
                    new_params.append(new_p)
                    new_first_moments.append(new_m1)
                    new_second_moments.append(new_m2)
                elif isinstance(p, (int, float)) and isinstance(g, (int, float)):
                    # Base case for numbers

                    # Update moments
                    new_m1 = self.beta1 * m1 + (1 - self.beta1) * g
                    new_m2 = self.beta2 * m2 + (1 - self.beta2) * (g * g)

                    # Bias correction
                    m_hat = new_m1 / bias_correction1
                    v_hat = new_m2 / bias_correction2

                    # Update parameter
                    new_p = p - self.learning_rate * m_hat / (
                        math.sqrt(v_hat) + self.epsilon
                    )

                    new_params.append(new_p)
                    new_first_moments.append(new_m1)
                    new_second_moments.append(new_m2)
                else:
                    raise ValueError(
                        f"Shape mismatch: inconsistent types {type(p)} vs {type(g)}"
                    )

            return new_params, new_first_moments, new_second_moments

        # Perform the Adam update
        updated_params, self._first_moment, self._second_moment = (
            _adam_update_recursive(
                parameters, gradients, self._first_moment, self._second_moment
            )
        )

        return updated_params

    def _initialize_like(
        self, gradients: Union[List[float], List[List[float]]]
    ) -> Union[List[float], List[List[float]]]:
        """
        Initialize moments with same structure as gradients, filled with zeros.

        Args:
            gradients: Reference structure for initialization

        Returns:
            Zero-initialized structure with same shape as gradients
        """
        if isinstance(gradients, (int, float)):
            return 0.0

        moments = []
        for g in gradients:
            if isinstance(g, list):
                moments.append(self._initialize_like(g))
            else:
                moments.append(0.0)

        return moments

    def reset(self) -> None:
        """
        Reset the optimizer's internal state.

        This clears both moment estimates and resets the time step counter.
        Useful when beginning optimization on a new problem.
        """
        self._first_moment = None
        self._second_moment = None
        self._time_step = 0

    def __str__(self) -> str:
        """String representation of Adam optimizer."""
        return (
            f"Adam(learning_rate={self.learning_rate}, beta1={self.beta1}, "
            f"beta2={self.beta2}, epsilon={self.epsilon})"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example demonstrating Adam's performance on a challenging optimization problem
    print("\\nAdam Example: Rosenbrock Function Optimization")
    print("=" * 48)
    print("Function: f(x,y) = 100*(y-x²)² + (1-x)² (Rosenbrock)")
    print("This is a classic non-convex optimization test function.")
    print("Global minimum at (1, 1) with f(1,1) = 0")

    from .sgd import SGD
    from .adagrad import Adagrad

    # Initialize optimizers for comparison
    sgd = SGD(learning_rate=0.001)
    adagrad = Adagrad(learning_rate=0.01)
    adam = Adam(learning_rate=0.01)

    # Starting points (all same)
    x_sgd = [-1.0, 1.0]
    x_adagrad = [-1.0, 1.0]
    x_adam = [-1.0, 1.0]

    def rosenbrock(x, y):
        """Rosenbrock function: f(x,y) = 100*(y-x²)² + (1-x)²"""
        return 100 * (y - x * x) ** 2 + (1 - x) ** 2

    def rosenbrock_gradient(x, y):
        """Gradient of Rosenbrock function"""
        df_dx = -400 * x * (y - x * x) - 2 * (1 - x)
        df_dy = 200 * (y - x * x)
        return [df_dx, df_dy]

    print(f"\\nStarting point: x={x_adam[0]:.3f}, y={x_adam[1]:.3f}")
    print(f"Initial f(x,y): {rosenbrock(x_adam[0], x_adam[1]):.3f}")

    # Run optimization
    for i in range(200):
        # Calculate gradients for all optimizers
        grad_sgd = rosenbrock_gradient(x_sgd[0], x_sgd[1])
        grad_adagrad = rosenbrock_gradient(x_adagrad[0], x_adagrad[1])
        grad_adam = rosenbrock_gradient(x_adam[0], x_adam[1])

        # Update all optimizers
        x_sgd = sgd.update(x_sgd, grad_sgd)
        x_adagrad = adagrad.update(x_adagrad, grad_adagrad)
        x_adam = adam.update(x_adam, grad_adam)

        if i % 50 == 49:  # Print every 50 iterations
            f_sgd = rosenbrock(x_sgd[0], x_sgd[1])
            f_adagrad = rosenbrock(x_adagrad[0], x_adagrad[1])
            f_adam = rosenbrock(x_adam[0], x_adam[1])

            print(f"\\nStep {i + 1:3d}:")
            print(
                f"  SGD:     f = {f_sgd:10.3f}, x = ({x_sgd[0]:6.3f}, {x_sgd[1]:6.3f})"
            )
            print(
                f"  Adagrad: f = {f_adagrad:10.3f}, x = ({x_adagrad[0]:6.3f}, {x_adagrad[1]:6.3f})"
            )
            print(
                f"  Adam:    f = {f_adam:10.3f}, x = ({x_adam[0]:6.3f}, {x_adam[1]:6.3f})"
            )

    print(f"\\nFinal Results (target: x=1, y=1, f=0):")
    f_final_sgd = rosenbrock(x_sgd[0], x_sgd[1])
    f_final_adagrad = rosenbrock(x_adagrad[0], x_adagrad[1])
    f_final_adam = rosenbrock(x_adam[0], x_adam[1])

    print(
        f"SGD:     f = {f_final_sgd:.6f}, distance to optimum = {math.sqrt((x_sgd[0] - 1) ** 2 + (x_sgd[1] - 1) ** 2):.4f}"
    )
    print(
        f"Adagrad: f = {f_final_adagrad:.6f}, distance to optimum = {math.sqrt((x_adagrad[0] - 1) ** 2 + (x_adagrad[1] - 1) ** 2):.4f}"
    )
    print(
        f"Adam:    f = {f_final_adam:.6f}, distance to optimum = {math.sqrt((x_adam[0] - 1) ** 2 + (x_adam[1] - 1) ** 2):.4f}"
    )

    # Determine best performer
    best_loss = min(f_final_sgd, f_final_adagrad, f_final_adam)
    if best_loss == f_final_adam:
        print("\\n🏆 Adam achieved the best performance!")
    elif best_loss == f_final_adagrad:
        print("\\n🏆 Adagrad achieved the best performance!")
    else:
        print("\\n🏆 SGD achieved the best performance!")
