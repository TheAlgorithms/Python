"""
Numerical methods for solving Ordinary Differential Equations (ODEs) of the form y' = f(x, y).
This module implements the Euler method and Heun's method.

References:
- Euler Method: https://en.wikipedia.org/wiki/Euler_method
- Heun's Method: https://en.wikipedia.org/wiki/Heun%27s_method

"""

from typing import Callable, List, Tuple


def euler_method(
    f: Callable[[float, float], float], x0: float, y0: float, h: float, steps: int
) -> Tuple[List[float], List[float]]:
    """
    Approximates the solution of a first-order ODE y' = f(x, y) using Euler's method.

    :param f: The differential equation function f(x, y).
    :param x0: Initial value of x.
    :param y0: Initial value of y (y(x0) = y0).
    :param h: Step size.
    :param steps: Number of iterations to perform.
    :return: A tuple containing lists of x and y coordinates.

    >>> def f_ode(x: float, y: float) -> float: return y - x**2 + 1
    >>> x_vals, y_vals = euler_method(f_ode, 0.0, 0.5, 0.25, 2)
    >>> [round(i, 4) for i in x_vals]
    [0.0, 0.25, 0.5]
    >>> [round(i, 4) for i in y_vals]
    [0.5, 0.875, 1.3281]
    """
    x = [0.0] * (steps + 1)
    y = [0.0] * (steps + 1)
    x[0], y[0] = x0, y0

    for i in range(steps):
        y[i + 1] = y[i] + f(x[i], y[i]) * h
        x[i + 1] = x[i] + h

    return x, y


def heuns_method(
    f: Callable[[float, float], float], x0: float, y0: float, h: float, steps: int
) -> Tuple[List[float], List[float]]:
    """
    Approximates the solution of a firs -order ODE y' = f(x, y) using Heun's method
    (also known as the improved Euler method).

    :param f: The differential equation function f(x, y).
    :param x0: Initial value of x.
    :param y0: Initial value of y.
    :param h: Step size.
    :param steps: Number of iterations to perform.
    :return: A tuple containing lists of x and y coordinates.

    >>> def f_ode(x: float, y: float) -> float: return y - x**2 + 1
    >>> x_vals, y_vals = heuns_method(f_ode, 0.0, 0.5, 0.25, 2)
    >>> [round(i, 4) for i in y_vals]
    [0.5, 0.9141, 1.4114]
    """
    x = [0.0] * (steps + 1)
    y = [0.0] * (steps + 1)
    x[0], y[0] = x0, y0

    for i in range(steps):
        y_predictor = y[i] + f(x[i], y[i]) * h
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + ((f(x[i], y[i]) + f(x[i + 1], y_predictor)) / 2.0) * h

    return x, y


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # example
    def example_ode(x: float, y: float) -> float:
        return y - x**2 + 1

    x_res, y_res = heuns_method(example_ode, 0.0, 0.5, 0.25, 4)
    print(f"Final heuns methot y value at x={x_res[-1]}: {round(y_res[-1], 4)}")
