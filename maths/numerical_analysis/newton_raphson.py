# Implementing Newton Raphson method in Python
# Author: Syed Haseeb Shah (github.com/QuantumNovice)
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a real-valued function
from __future__ import annotations

from decimal import Decimal

from sympy import diff, lambdify, symbols


def newton_raphson(func: str, a: float | Decimal, precision: float = 1e-10) -> float:
    """Finds root from the point 'a' onwards by Newton-Raphson method
    >>> newton_raphson("sin(x)", 2)
    3.1415926536808043
    >>> newton_raphson("x**2 - 5*x + 2", 0.4)
    0.4384471871911695
    >>> newton_raphson("x**2 - 5", 0.1)
    2.23606797749979
    >>> newton_raphson("log(x) - 1", 2)
    2.718281828458938
    """
    x = symbols("x")
    f = lambdify(x, func, "math")
    f_derivative = lambdify(x, diff(func), "math")
    x_curr = a
    while True:
        x_curr = Decimal(x_curr) - Decimal(f(x_curr)) / Decimal(f_derivative(x_curr))
        if abs(f(x_curr)) < precision:
            return float(x_curr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Find value of pi
    print(f"The root of sin(x) = 0 is {newton_raphson('sin(x)', 2)}")
    # Find root of polynomial
    print(f"The root of x**2 - 5*x + 2 = 0 is {newton_raphson('x**2 - 5*x + 2', 0.4)}")
    # Find value of e
    print(f"The root of log(x) - 1 = 0 is {newton_raphson('log(x) - 1', 2)}")
    # Find root of exponential function
    print(f"The root of exp(x) - 1 = 0 is {newton_raphson('exp(x) - 1', 0)}")
