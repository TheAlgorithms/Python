import math
from collections.abc import Callable


def intersection(function: Callable[[float], float], x0: float, x1: float) -> float:
    """
    function is the f we want to find its root
    x0 and x1 are two random starting points
    >>> intersection(lambda x: x ** 3 - 1, -5, 5)
    0.9999999999954654
    >>> intersection(lambda x: x ** 3 - 1, 5, 5)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero, could not find root
    >>> intersection(lambda x: x ** 3 - 1, 100, 200)
    1.0000000000003888
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 0, 2)
    0.9999999998088019
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 2, 4)
    2.9999999998088023
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 4, 1000)
    3.0000000001786042
    >>> intersection(math.sin, -math.pi, math.pi)
    0.0
    >>> intersection(math.cos, -math.pi, math.pi)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero, could not find root
    """
    x_n: float = x0
    x_n1: float = x1
    while True:
        if x_n == x_n1 or function(x_n1) == function(x_n):
            raise ZeroDivisionError("float division by zero, could not find root")
        x_n2: float = x_n1 - (
            function(x_n1) / ((function(x_n1) - function(x_n)) / (x_n1 - x_n))
        )
        if abs(x_n2 - x_n1) < 10**-5:
            return x_n2
        x_n = x_n1
        x_n1 = x_n2


def f(x: float) -> float:
    """
    function is f(x) = x^3 - 2x - 5
    >>> f(2)
    -1.0
    """
    return math.pow(x, 3) - (2 * x) - 5


if __name__ == "__main__":
    print(intersection(f, 3, 3.5))
