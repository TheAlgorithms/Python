# Implementing Newton Raphson method in Python
# Author: Syed Haseeb Shah (github.com/QuantumNovice)
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a real-valued function
from __future__ import annotations

from scipy.optimize import newton
from sympy import diff, lambdify, symbols, sympify


def newton_raphson(
    func: str, a: float, precision: float = 10**-10
) -> float:
    """Finds root from the point 'a' onwards by Newton-Raphson method
    >>> newton_raphson("sin(x)", 2)
    3.141592653589793
    >>> newton_raphson("x**2 - 5*x +2", 0.4)
    0.43844718719116976
    >>> newton_raphson("x**2 - 5", 0.1)
    2.23606797749979
    >>> newton_raphson("log(x)- 1", 2)
    2.7182818284590455
    """
    symbol = symbols('x')
    exp = sympify(func)
    exp_diff = diff(exp, symbol)

    exp_func = lambdify(symbol, exp)
    f_diff_func = lambdify(symbol, exp_diff)

    res = newton(exp_func, a, fprime=f_diff_func, tol=precision)
    return res


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
