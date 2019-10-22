import numpy as np


def explicit_euler(ode_func, y0, x0, stepsize, x_end):
    """
    Calculate numeric solution at each step to an ODE using Euler's Method

    https://en.wikipedia.org/wiki/Euler_method

    Arguments:
    ode_func -- The ode as a function of x and y
    y0 -- the initial value for y
    x0 -- the initial value for x
    stepsize -- the increment value for x
    x_end -- the end value for x

    >>> # the exact solution is math.exp(x)
    >>> def f(x, y):
    ...     return y
    >>> y0 = 1
    >>> y = explicit_euler(f, y0, 0.0, 0.01, 5)
    >>> y[-1]
    144.77277243257308
    """
    N = int(np.ceil((x_end - x0) / stepsize))
    y = np.zeros((N + 1,))
    y[0] = y0
    x = x0

    for k in range(N):
        y[k + 1] = y[k] + stepsize * ode_func(x, y[k])
        x += stepsize

    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
