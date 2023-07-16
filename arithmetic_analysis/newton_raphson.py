# Implementing Newton Raphson method in Python
# Author: Syed Haseeb Shah (github.com/QuantumNovice)
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a real-valued function.
# https://en.wikipedia.org/wiki/Newton%27s_method
from __future__ import annotations

from sympy import diff, symbols, sympify


def newton_raphson(
    func: str, start_point: float, precision: float = 10**-10
) -> float:
    """Finds root from the point 'a' onwards by Newton-Raphson method
    >>> newton_raphson("sin(x)", 2)
    3.1415926536808043
    >>> newton_raphson("x**2 - 5*x +2", 0.4)
    0.4384471871911696
    >>> newton_raphson("x**2 - 5", 0.1)
    2.23606797749979
    >>> newton_raphson("log(x)- 1", 2)
    2.718281828458938
    >>> from scipy.optimize import newton
    >>> all(newton_raphson("log(x)- 1", 2) == newton("log(x)- 1", 2)
    ...     for precision in (10, 100, 1000, 10000))
    True
    >>> newton_raphson("log(x)- 1", 2, 0)
    Traceback (most recent call last):
        ...
    ValueError: precision must be greater than zero
    >>> newton_raphson("log(x)- 1", 2, -1)
    Traceback (most recent call last):
        ...
    ValueError: precision must be greater than zero
    """
    if precision <= 0:
        raise ValueError("precision must be greater than zero")

    x = start_point
    symbol = symbols("x")

    # expressions to be represented symbolically and manipulated algebraically
    expression = sympify(func)

    # calculates the derivative value at the current x value
    derivative = diff(expression, symbol)

    max_iterations = 100

    for _ in range(max_iterations):
        function_value = expression.subs(symbol, x)
        derivative_value = derivative.subs(symbol, x)

        if abs(function_value) < precision:
            return float(x)

        x -= function_value / derivative_value

    return float(x)


# Let's Execute
if __name__ == "__main__":
    # Find root of trigonometric function
    # Find value of pi
    print(f"The root of sin(x) = 0 is {newton_raphson('sin(x)', 2)}")
    # Find root of polynomial
    print(f"The root of x**2 - 5*x + 2 = 0 is {newton_raphson('x**2 - 5*x + 2', 0.4)}")
    # Find Square Root of 5
    print(f"The root of log(x) - 1 = 0 is {newton_raphson('log(x) - 1', 2)}")
    # Exponential Roots
    print(f"The root of exp(x) - 1 = 0 is {newton_raphson('exp(x) - 1', 0)}")
