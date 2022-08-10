import numpy as np


def runge_kutta4(f, y0, h, t):
    """
    Calculate on step of the ODE f(x, y) using Runge-Kutta method

    # https://en.wikipedia.org/wiki/Runge-Kutta_methods

    @param f: function of the form f(x, y)
        The ode as a function of t and y
    @param y0: float or array like
        the initial value for y
    @param t: float 
        the time value for the solution
    @param h: float
        the stepsize
    @return: float or array like 
        the solution at time t

    >>> def f(y, t):
    ...     return y
    >>> y0, a, b, h = 1, 0, 5, 0.01
    >>> nstep = int(np.ceil((b - a) / h))
    >>> y = np.zeros((nstep + 1,))
    >>> y[0] = y0
    >>> t = a
    >>> for k in range(nstep):
    ...    y[k + 1] = runge_kutta4(f, y[k], h, t)
    ...    t += h

    >>> y[-1]
    148.41315904125125

    >>> np.exp(b)
    148.4131591025766


    """
    k1 = f(y0, t)
    k2 = f(y0 + 0.5 * h * k1, t + 0.5 * h)
    k3 = f(y0 + 0.5 * h * k2, t + 0.5 * h)
    k4 = f(y0 + h * k3, t + h)
    y0 += h / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)

    return y0


def bogacki_shampine(f, y0, h,  t):
    """
    Calculate on step of the ODE f(x, y) using Bogacki-Shampine method

    https://en.wikipedia.org/wiki/Bogacki%E2%80%93Shampine_method

    @param f: function of the form f(x, y)
        The ode as a function of t and y
    @param y0: float or array like
        the initial value for y
    @param h: float
        the stepsize
    @return: float or array like
        the solution at time t

    >>> def f(y, t):
    ...     return y
    >>> y0, a, b, h = 1, 0, 5, 0.01
    >>> nstep = int(np.ceil((b - a) / h))
    >>> y = np.zeros((nstep + 1,))
    >>> y[0] = y0
    >>> t = a
    >>> for k in range(nstep):
    ...    y[k + 1] = bogacki_shampine(f, y[k], h, t)
    ...    t += h

    >>> y[-1]
    148.41312842949924

    >>> np.exp(b)
    148.4131591025766
    """

    k1 = f(y0, t)
    k2 = f(y0 + 0.5 * h * k1, t + 0.5 * h)
    k3 = f(y0 + 0.75 * h * k2, t + 0.75 * h)
    y0 += h / 9.0 * (2.0 * k1 + 3.0 * k2 + 4.0 * k3)

    return y0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
