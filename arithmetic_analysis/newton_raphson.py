# Implementing Newton Raphson method in Python
# Author: Syed Haseeb Shah (github.com/QuantumNovice)
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a real-valued function
from __future__ import annotations

from sympy import diff, symbols, sympify


def newton_raphson(func: str, a: float, precision: float = 10**-10) -> float:
    """Finds root from the point 'a' onwards by Newton-Raphson method
    >>> newton_raphson("sin(x)", 2)
    3.1415926536808043
    >>> newton_raphson("x**2 - 5*x +2", 0.4)
    0.4384471871911696
    >>> newton_raphson("x**2 - 5", 0.1)
    2.23606797749979
    >>> newton_raphson("log(x)- 1", 2)
    2.718281828458938
    """
    x = a
    symbol = symbols("x")
    # expressions to be represented symbolically and manipulated algebraically
    exp = sympify(func)
    # calculate the derivative value at the current x value
    exp_diff = diff(exp, symbol)
    maximum_iterations = 100

    for _ in range(maximum_iterations):
        val = exp.subs(symbol, x)
        diff_val = exp_diff.subs(symbol, x)

        if abs(val) < precision:
            return float(x)

        x = x - (val / diff_val)

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
