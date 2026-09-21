"""
RMSprop (Root Mean Square Propagation) optimizer implementation.

RMSprop is an adaptive learning rate optimizer that maintains a moving
average of squared gradients to normalize the gradient. It was proposed
by Geoffrey Hinton in his Coursera course on Neural Networks.

Key idea: Instead of using a fixed learning rate, RMSprop adapts the
learning rate for each parameter by dividing by a running average of
recent gradient magnitudes.

Update rules:
    v(t) = rho * v(t-1) + (1 - rho) * gradient^2
    param = param - (learning_rate / sqrt(v(t) + epsilon)) * gradient

Where:
    v(t)          = moving average of squared gradients
    rho           = decay factor (typically 0.9)
    learning_rate = step size
    epsilon       = small value to avoid division by zero

Reference: https://en.wikipedia.org/wiki/Stochastic_gradient_descent#RMSProp

>>> rmsprop([0.0], [0.1], 0.01)  # doctest: +ELLIPSIS
[-0.031...]
>>> rmsprop([1.0, -1.0], [0.5, -0.5], 0.01)  # doctest: +ELLIPSIS
[0.968..., -0.968...]
"""

import math


def rmsprop(
    params: list[float],
    gradients: list[float],
    learning_rate: float,
    rho: float = 0.9,
    epsilon: float = 1e-8,
    moving_avg: list[float] | None = None,
) -> list[float]:
    """
    Perform one step of the RMSprop optimization algorithm.

    :param params: Current parameter values to be updated.
    :param gradients: Gradients of the loss with respect to each parameter.
    :param learning_rate: Step size for the update (must be positive).
    :param rho: Decay factor for the moving average (default 0.9).
    :param epsilon: Small constant to avoid division by zero (default 1e-8).
    :param moving_avg: Running average of squared gradients. Updated in
                       place each call. Initialized to zeros if not provided.
    :return: Updated parameter values after one RMSprop step.

    :raises ValueError: If params and gradients have different lengths.
    :raises ValueError: If learning_rate, rho, or epsilon are out of range.

    >>> rmsprop([0.0], [0.0], 0.01)
    [0.0]
    >>> rmsprop([1.0], [0.0], 0.01)
    [1.0]
    >>> len(rmsprop([1.0, 2.0, 3.0], [0.1, 0.2, 0.3], 0.01)) == 3
    True
    >>> rmsprop([1.0], [0.5], learning_rate=0.01)  # doctest: +ELLIPSIS
    [0.968...]
    """
    if len(params) != len(gradients):
        msg = (
            f"params and gradients must have the same length, "
            f"got {len(params)} and {len(gradients)}"
        )
        raise ValueError(msg)
    if learning_rate <= 0:
        msg = f"learning_rate must be positive, got {learning_rate}"
        raise ValueError(msg)
    if not 0.0 <= rho < 1.0:
        msg = f"rho must be in [0, 1), got {rho}"
        raise ValueError(msg)
    if epsilon <= 0:
        msg = f"epsilon must be positive, got {epsilon}"
        raise ValueError(msg)

    # Initialize moving average of squared gradients to zeros
    if moving_avg is None:
        moving_avg = [0.0] * len(params)

    updated_params = []
    for i, (param, grad) in enumerate(zip(params, gradients)):
        # Update moving average IN PLACE so state persists across calls
        moving_avg[i] = rho * moving_avg[i] + (1 - rho) * grad**2
        # Compute adaptive update
        param = param - (learning_rate / math.sqrt(moving_avg[i] + epsilon)) * grad
        updated_params.append(param)

    return updated_params


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("RMSprop Optimizer Demo")
    print("=" * 40)
    print("Minimizing f(x) = x^2  (minimum at x = 0)")
    print("Gradient: f'(x) = 2x | Learning rate: 0.1\n")

    param = [5.0]
    moving_avg = [0.0]

    print(f"{'Step':>6} | {'param':>12} | {'f(x)':>12}")
    print("-" * 38)
    print(f"{'0':>6} | {param[0]:>12.6f} | {param[0] ** 2:>12.6f}")

    for step in range(1, 101):
        gradient = [2 * param[0]]
        param = rmsprop(param, gradient, learning_rate=0.1, moving_avg=moving_avg)
        if step % 20 == 0:
            print(f"{step:>6} | {param[0]:>12.6f} | {param[0] ** 2:>12.8f}")

    print(f"\nConverged to x = {param[0]:.8f}  (true minimum = 0.0)")
