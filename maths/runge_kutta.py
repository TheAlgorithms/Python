import numpy as np


def runge_kutta(f, y0, x0, h, x_end):
    """
    Calculate the numeric solution at each step to the ODE f(x, y) using RK4

    https://en.wikipedia.org/wiki/Runge-Kutta_methods

    Arguments:
    f -- The ode as a function of x and y
    y0 -- the initial value for y
    x0 -- the initial value for x
    h -- the stepsize
    x_end -- the end value for x

    >>> # the exact solution is math.exp(x)
    >>> def f(x, y):
    ...     return y
    >>> y0 = 1
    >>> y = runge_kutta(f, y0, 0.0, 0.01, 5)
    >>> y[-1]
    148.41315904125113
    """
    N = int(np.ceil((x_end - x0) / h))
    y = np.zeros((N + 1,))
    y[0] = y0
    x = x0

    for k in range(N):
        k1 = f(x, y[k])
        k2 = f(x + 0.5 * h, y[k] + 0.5 * h * k1)
        k3 = f(x + 0.5 * h, y[k] + 0.5 * h * k2)
        k4 = f(x + h, y[k] + h * k3)
        y[k + 1] = y[k] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h

    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
