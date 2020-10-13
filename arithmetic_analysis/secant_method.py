# Implementing Secant method in Python
# Author: dimgrichr


from math import exp


def f(x):
    """
    >>> f(5)
    39.98652410600183
    """
    return 8 * x - 2 * exp(-x)


def secant_method(lower_bound, upper_bound, repeats):
    """
    >>> SecantMethod(1, 3, 2)
    0.2139409276214589
    """
    x0 = lower_bound
    x1 = upper_bound
    for i in range(0, repeats):
        x0, x1 = x1, x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    return x1


print(f"The solution is: {secant_method(1, 3, 2)}")
