"""
Use the Runge-Kutta-Gill's method of order 4 to solve Ordinary Differential Equations.

https://www.geeksforgeeks.org/gills-4th-order-method-to-solve-differential-equations/
Author : Ravi Kumar
"""

from collections.abc import Callable
from math import sqrt

import numpy as np


def runge_kutta_gills(
    func: Callable[[float, float], float],
    x_initial: float,
    y_initial: float,
    step_size: float,
    x_final: float,
) -> np.ndarray:
    """
    Solve an Ordinary Differential Equations using Runge-Kutta-Gills Method of order 4.

    args:
    func: An ordinary differential equation (ODE) as function of x and y.
    x_initial: The initial value of x.
    y_initial: The initial value of y.
    step_size: The increment value of x.
    x_final: The final value of x.

    Returns:
        Solution of y at each nodal point

    >>> def f(x, y):
    ...     return (x-y)/2
    >>> y = runge_kutta_gills(f, 0, 3, 0.2, 5)
    >>> float(y[-1])
    3.4104259225717537

    >>> def f(x,y):
    ...     return x
    >>> y = runge_kutta_gills(f, -1, 0, 0.2, 0)
    >>> y
    array([ 0.  , -0.18, -0.32, -0.42, -0.48, -0.5 ])

    >>> def f(x, y):
    ...     return x + y
    >>> y = runge_kutta_gills(f, 0, 0, 0.2, -1)
    Traceback (most recent call last):
        ...
    ValueError: The final value of x must be greater than initial value of x.

    >>> def f(x, y):
    ...     return x
    >>> y = runge_kutta_gills(f, -1, 0, -0.2, 0)
    Traceback (most recent call last):
        ...
    ValueError: Step size must be positive.
    """
    if x_initial >= x_final:
        raise ValueError(
            "The final value of x must be greater than initial value of x."
        )

    if step_size <= 0:
        raise ValueError("Step size must be positive.")

    n = int((x_final - x_initial) / step_size)
    y = np.zeros(n + 1)
    y[0] = y_initial
    for i in range(n):
        k1 = step_size * func(x_initial, y[i])
        k2 = step_size * func(x_initial + step_size / 2, y[i] + k1 / 2)
        k3 = step_size * func(
            x_initial + step_size / 2,
            y[i] + (-0.5 + 1 / sqrt(2)) * k1 + (1 - 1 / sqrt(2)) * k2,
        )
        k4 = step_size * func(
            x_initial + step_size, y[i] - (1 / sqrt(2)) * k2 + (1 + 1 / sqrt(2)) * k3
        )

        y[i + 1] = y[i] + (k1 + (2 - sqrt(2)) * k2 + (2 + sqrt(2)) * k3 + k4) / 6
        x_initial += step_size
    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
