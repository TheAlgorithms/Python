"""
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approach of summing 'Equally Spaced Abscissas'
"""

from collections.abc import Callable, Iterator


def trapezoidal_rule(
    f: Callable[[float], float], boundary: list[float], steps: int
) -> float:
    """
    "extended trapezoidal rule"
    int(f) = dx/2 * (f1 + 2f2 + ... + fn)

    >>> def func(x): return x ** 2
    >>> abs(trapezoidal_rule(func, [0, 1], 10) - 0.335) < 1e-9
    True

    >>> def func(x): return 1
    >>> abs(trapezoidal_rule(func, [0, 10], 100) - 10.0) < 1e-9
    True

    >>> def func(x): return x
    >>> trapezoidal_rule(func, [0, 1], 1)
    0.5

    >>> trapezoidal_rule(func, [], 10)  # Empty boundary list
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    >>> trapezoidal_rule(func, [0, 1], 0)  # Steps as zero
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    >>> trapezoidal_rule(func, ['0', '1'], 10)  # Boundary values as strings
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'str' and 'str'

    Parameters:
    - f (Callable[[float], float]): The function to be integrated.
    - boundary (list of float): A two-element list specifying the lower and upper bounds
     of the integration interval.
    - steps (int): The number of steps (trapezoids) to divide the interval into.

    Returns:
    - float: The estimated value of the integral over the specified interval.
    """
    h = (boundary[1] - boundary[0]) / steps
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    y = 0.0
    y += (h / 2.0) * f(a)
    for i in x_i:
        y += h * f(i)
    y += (h / 2.0) * f(b)
    return y


def make_points(a: float, b: float, h: float) -> Iterator[float]:
    """
    Generate points within the interval (a, b) with a step size of h.

    The generator function yields a sequence of points starting from `a + h` to `b - h`.
    It is used to generate the x-values at which the function `f` will be evaluated,
    for the purpose of numerical integration using methods like the trapezoidal rule.

    Parameters:
    - a (float): The lower bound of the interval.
    - b (float): The upper bound of the interval.
    - h (float): The step size between each point in the interval.

    Yields:
    - float: The next point in the sequence within the interval (a, b).

    Examples:
    >>> list(make_points(0, 10, 2))
    [2, 4, 6]
    >>> list(make_points(1, 5, 1))
    [2, 3]
    >>> list(make_points(-2, 2, 1))
    [-1, 0]
    """
    x = a + h
    while x < (b - h):
        yield x
        x = x + h


if __name__ == "__main__":
    import doctest

    doctest.testmod()
