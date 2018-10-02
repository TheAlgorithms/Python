"""
This is a pure python implementation of euler's method
For doctests run following command:
python -m doctest -v euler_method.py
or
python3 -m doctest -v euler_method.py
For manual testing run:
python euler_method.py
"""

from __future__ import print_function
import math


def euler(f, xa, xb, ya, n):
    """Solve a first order ODE using Euler's Method
    :param f: F(x,y) such that y'=F(x,y)
    :param xa: The initial value of x
    :param xb: The final value of x
    :param ya: The intial value of y
    :param n: The number of steps
    :return: A list of points approximating the differential equation
    Examples:
    >>> euler(lambda x, y: 2 - 2 * y - math.exp(-4 * x), 0, 0.5, 1, 5)
    [(0, 1), (0.1, 0.9), (0.2, 0.8529679953964361), (0.30000000000000004, 0.8374414999054267), (0.4, 0.8398337787331212), (0.5, 0.8516773711870314)]
    """
    h = (xb - xa) / float(n)
    x = xa
    y = ya
    result = [(x, y)]
    for _ in range(n):
        y += h * f(x, y)
        x += h
        result.append((x, y))
    return result


if __name__ == '__main__':
    f = lambda x, y: 2 - 2 * y - math.exp(-4 * x)
    xa = 0
    ya = 1
    xb = 0.5
    n = 5
    print(euler(f, xa, xb, ya, n))