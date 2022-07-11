from collections.abc import Callable

import numpy as np


def explicit_euler(
    ode_func: Callable, y0: float, x0: float, step_size: float, x_end: float
) -> np.ndarray:
    """Calculate numeric solution at each step to an ODE using Euler's Method

    For reference to Euler's method refer to https://en.wikipedia.org/wiki/Euler_method.

    Args:
        ode_func (Callable):  The ordinary differential equation
            as a function of x and y.
        y0 (float): The initial value for y.
        x0 (float): The initial value for x.
        step_size (float): The increment value for x.
        x_end (float): The final value of x to be calculated.

    Returns:
        np.ndarray: Solution of y for every step in x.

    >>> # the exact solution is math.exp(x)
    >>> def f(x, y):
    ...     return y
    >>> y0 = 1
    >>> y = explicit_euler(f, y0, 0.0, 0.01, 5)
    >>> y[-1]
    144.77277243257308
    """
    N = int(np.ceil((x_end - x0) / step_size))
    y = np.zeros((N + 1,))
    y[0] = y0
    x = x0

    for k in range(N):
        y[k + 1] = y[k] + step_size * ode_func(x, y[k])
        x += step_size

    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
