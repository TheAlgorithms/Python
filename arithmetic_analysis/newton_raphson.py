# Implementing Newton Raphson method in Python
# Author: Syed Haseeb Shah (github.com/QuantumNovice)
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a real-valued function
from decimal import Decimal
from math import *  # noqa: F401, F403

from sympy import diff


def newton_raphson(func: str, x: int, precision: int = 10 ** -10) -> float:
    """Finds root of func by Newton-Raphson method starting at x.
    >>> newton_raphson("sin(x)", 2)
    3.1415926536808043
    >>> newton_raphson("x**2 - 5*x +2", 0.4)
    0.4384471871911695
    >>> newton_raphson("x**2 - 5", 0.1)
    2.23606797749979
    >>> newton_raphson("log(x)- 1", 2)
    2.718281828458938
    """

    while True:
        # Evaluates f in x until it becomes "0" (the value given by the precision)

        x = Decimal(x) - (Decimal(eval(func)) / Decimal(eval(str(diff(func)))))
        # The next value of x. x_0 + f(x) / f'(x)

        if abs(eval(func)) < precision:
            # The algorithm stops when f(x) ~= 0 (precision)
            return float(x)


# Let's Execute
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # Find root of trigonometric function (value of pi)
    print(f"One root of sin(x) = 0 is {newton_raphson('sin(x)', 2)}")

    # Find root of polynomial
    print(f"One root of x**2 - 5*x + 2 = 0 is {newton_raphson('x**2 - 5*x + 2', 0.4)}")

    # Exponential Roots
    print(f"One root of log(x) - 1 = 0 is {newton_raphson('log(x) - 1', 2)}")
    print(f"One root of exp(x) - 1 = 0 is {newton_raphson('exp(x) - 1', 0)}")
