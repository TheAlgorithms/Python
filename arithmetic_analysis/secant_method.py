# Implementing Secant method in Python
# https://en.wikipedia.org/wiki/Secant_method
# Author: dimgrichr


from math import exp
from typing import Callable

RealFunc = Callable[[float], float]  # type alias for real -> real function


def secant_method(
    func: RealFunc, lower_bound: float, upper_bound: float, repeats: int
) -> float:
    """
    >>> secant_method(lambda x: 8 * x - 2 * exp(-x), 1, 3, 2)
    0.2139409276214589
    >>> secant_method(lambda x: x ** 3 - 2 * x - 5, -3, 3, 10)
    2.094546116969569
    >>> secant_method(lambda x: x ** 3 - 1, 0, 5, 5)
    0.07992494940223759
    >>> secant_method(lambda x: x ** 3 - 1, 0, 5, 500)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Could not find root
    """
    for _ in range(repeats):
        value = func(upper_bound)
        numerator = value * (upper_bound - lower_bound)
        denominator = value - func(lower_bound)
        if denominator == 0.0:
            raise ZeroDivisionError("Could not find root")
        lower_bound, upper_bound = upper_bound, upper_bound - numerator / denominator

    return upper_bound


def f(x: float) -> float:
    """
    >>> f(5)
    39.98652410600183
    """
    return 8 * x - 2 * exp(-x)


print(f"The solution is: {secant_method(f, 1, 3, 2)}")
