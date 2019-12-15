# Implementing Newton Raphson method in Python
# Author: Syed Haseeb Shah (github.com/QuantumNovice)
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a real-valued function

from decimal import Decimal
from math import *  # noqa: F821
from sympy import diff


def NewtonRaphson(func: str, a: int, precision=int: 10 ** -10) -> float:
    """ Finds root from the point 'a' onwards by Newton-Raphson method
    >>> NewtonRaphson("sin(x)", 2))
    3.141592653680804119362982272
    >>> NewtonRaphson("x**2 - 5*x +2", 0.4))
    0.4384471871911695062638833812
    >>> NewtonRaphson("x**2 - 5", 0.1))
    2.236067977499789696465261251
    >>> NewtonRaphson("log(x)- 1", 2))
    2.718281828458937968804105873
    """
    x = a
    while True:
        x = Decimal(x) - (Decimal(eval(func)) / Decimal(eval(str(diff(func)))))
        # This number dictates the accuracy of the answer
        if abs(eval(func)) < precision:
            return x


# Let's Execute
if __name__ == "__main__":
    # Find root of trigonometric function
    # Find value of pi
    print(f"The root of sin(x) = 0 is {NewtonRaphson('sin(x)', 2)}")
    # Find root of polynomial
    print(f"The root of x**2 - 5*x + 2 = 0 is {NewtonRaphson('x**2 - 5*x + 2', 0.4)}")
    # Find Square Root of 5
    print(f"The root of log(x) - 1 = 0 is {NewtonRaphson('log(x) - 1', 2)}")
    # Exponential Roots
    print(f"The root of exp(x) - 1 = 0 is {NewtonRaphson('exp(x) - 1', 0)}")
