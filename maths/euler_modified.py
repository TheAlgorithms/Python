from typing import Callable

import numpy as np


def euler_modified(
    ode_func: Callable, y0: float, x0: float, step_size: float, x_end: float
) -> np.array:
    """
    Calculate solution at each step to an ODE using Euler's Modified Method
    The Euler is straightforward to implement, but can't give accurate solutions.
    So, they Proposed some changes to improve the accuracy

    https://en.wikipedia.org/wiki/Euler_method

    Arguments:
    ode_func -- The ode as a function of x and y
    y0 -- the initial value for y
    x0 -- the initial value for x
    stepsize -- the increment value for x
    x_end -- the end value for x

    >>> # the exact solution is math.exp(x)
    >>> def f1(x, y):
    ...     return -2*x*(y**2)
    >>> y = euler_modified(f1, 1.0, 0.0, 0.2, 1.0)
    >>> y[-1]
    0.503338255442106
    >>> import math
    >>> def f2(x, y):
    ...     return -2*y + (x**3)*math.exp(-2*x)
    >>> y = euler_modified(f2, 1.0, 0.0, 0.1, 0.3)
    >>> y[-1]
    0.5525976431951775
    """
    N = int(np.ceil((x_end - x0) / step_size))
    y = np.zeros((N + 1,))
    y[0] = y0
    x = x0

    for k in range(N):
        y_get = y[k] + step_size * ode_func(x, y[k])
        y[k + 1] = y[k] + (
            (step_size / 2) * (ode_func(x, y[k]) + ode_func(x + step_size, y_get))
        )
        x += step_size

    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
