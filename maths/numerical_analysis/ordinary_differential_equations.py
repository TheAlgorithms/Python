"""
Numerical methods for solving Ordinary Differential Equations (ODEs)
of the form y' = f(x, y).
This module implements the Euler method and Heun's method.

References:
- Euler Method: https://en.wikipedia.org/wiki/Euler_method
- Heun's Method: https://en.wikipedia.org/wiki/Heun%27s_method
"""

from collections.abc import Callable


def euler_method(
    differential_function: Callable[[float, float], float],
    x_initial: float,
    y_initial: float,
    step_size: float,
    total_steps: int,
) -> tuple[list[float], list[float]]:
    """
    Approximates the solution of a first-order ODE y' = f(x, y) using Euler's method.

    :param differential_function: The differential equation function f(x, y).
    :param x_initial: Initial value of x.
    :param y_initial: Initial value of y (y(x_initial) = y_initial).
    :param step_size: Step size.
    :param total_steps: Number of iterations to perform.
    :return: A tuple containing lists of x and y coordinates.

    >>> def f_ode(x: float, y: float) -> float: return y - x**2 + 1
    >>> x_vals, y_vals = euler_method(f_ode, 0.0, 0.5, 0.25, 2)
    >>> [round(i, 4) for i in x_vals]
    [0.0, 0.25, 0.5]
    >>> [round(i, 4) for i in y_vals]
    [0.5, 0.875, 1.3281]
    """
    x_estimates = [0.0] * (total_steps + 1)
    y_estimates = [0.0] * (total_steps + 1)
    x_estimates[0], y_estimates[0] = x_initial, y_initial

    for i in range(total_steps):
        y_estimates[i + 1] = (
            y_estimates[i]
            + differential_function(x_estimates[i], y_estimates[i]) * step_size
        )
        x_estimates[i + 1] = x_estimates[i] + step_size

    return x_estimates, y_estimates


def heuns_method(
    differential_function: Callable[[float, float], float],
    x_initial: float,
    y_initial: float,
    step_size: float,
    total_steps: int,
) -> tuple[list[float], list[float]]:
    """
    Approximates the solution of a first-order ODE y' = f(x, y) using Heun's method
    (also known as the improved Euler method).

    :param differential_function: The differential equation function f(x, y).
    :param x_initial: Initial value of x.
    :param y_initial: Initial value of y.
    :param step_size: Step size.
    :param total_steps: Number of iterations to perform.
    :return: A tuple containing lists of x and y coordinates.

    >>> def f_ode(x: float, y: float) -> float: return y - x**2 + 1
    >>> x_vals, y_vals = heuns_method(f_ode, 0.0, 0.5, 0.25, 2)
    >>> [round(i, 4) for i in y_vals]
    [0.5, 0.9141, 1.4114]
    """
    x_estimates = [0.0] * (total_steps + 1)
    y_estimates = [0.0] * (total_steps + 1)
    x_estimates[0], y_estimates[0] = x_initial, y_initial

    for i in range(total_steps):
        y_predictor = (
            y_estimates[i]
            + differential_function(x_estimates[i], y_estimates[i]) * step_size
        )
        x_estimates[i + 1] = x_estimates[i] + step_size
        y_estimates[i + 1] = (
            y_estimates[i]
            + (
                (
                    differential_function(x_estimates[i], y_estimates[i])
                    + differential_function(x_estimates[i + 1], y_predictor)
                )
                / 2.0
            )
            * step_size
        )

    return x_estimates, y_estimates


if __name__ == "__main__":
    import doctest

    doctest.testmod()
