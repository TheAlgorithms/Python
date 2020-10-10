import numpy as np


def runge_kutta(f, y0, x0, h, x_end):
    """
    Calculate the numeric solution at each step to the ODE f(x, y) using:

    Runge-Kutta Fourth Order Method (RK4)

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
        f1 = f(x, y[k])
        f2 = f(x + 0.5 * h, y[k] + 0.5 * h * f1)
        f3 = f(x + 0.5 * h, y[k] + 0.5 * h * f2)
        f4 = f(x + h, y[k] + h * f3)
        y[k + 1] = y[k] + (1 / 6) * h * (f1 + 2 * f2 + 2 * f3 + f4)
        x += h

    return y

def butchers_runge_kutta(f, y0, x0, h, x_end):
    """
     Calculate the numeric solution at each step to the ODE f(x, y) using:

     Butcher's Fifth Order Runge-Kutta Method

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
     >>> y = butchers_runge_kutta(f, y0, 0.0, 0.01, 5)
     >>> y[-1]
     148.41315910258956
     """

    N = int(np.ceil((x_end - x0) / h))
    y = np.zeros((N + 1,))
    y[0] = y0
    x = x0

    for k in range(N):
        f1 = f(x, y[k])
        f2 = f(x + ((1/4) * h), y[k] + ((1/4) * h * f1))
        f3 = f(x + ((1/4) * h), y[k] + ((1/8) * h * f1) + ((1/8) * h * f2))
        f4 = f(x + ((1/2) * h), y[k] - ((1/2) * h * f2) + (h * f3))
        f5 = f(x + ((3/4) * h), y[k] + ((3/16) * h * f1) + ((9/16) * h * f4))
        f6 = f(x + h,
               y[k] - ((3/7) * h * f1) + ((2/7) * h * f2) +
               ((12/7) * h * f3) - ((12/7) * h * f4) + ((8/7) * h * f5))

        y[k + 1] = y[k] + (1 / 90) * h * (7*f1 + 32*f3 + 12*f4 + 32*f5 + 7*f6)

        x += h

    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    