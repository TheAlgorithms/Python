# Implementing Newton Raphson method in Python
# Author: Saksham Gupta
#
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a functreal-valued ion
# The method can also be extended to complex functions
#
# Newton's Method - https://en.wikipedia.org/wiki/Newton's_method

from sympy import diff, lambdify, symbols
from sympy.functions import *  # noqa: F401, F403


def newton_raphson(
    function: str,
    starting_point: complex,
    variable: str = "x",
    precision: float = 10**-10,
    multiplicity: int = 1,
) -> complex:
    """Finds root from the 'starting_point' onwards by Newton-Raphson method
    Refer to https://docs.sympy.org/latest/modules/functions/index.html
    for usable mathematical functions

    >>> newton_raphson("sin(x)", 2)
    3.141592653589793
    >>> newton_raphson("x**4 -5", 0.4 + 5j)
    (-7.52316384526264e-37+1.4953487812212207j)
    >>> newton_raphson('log(y) - 1', 2, variable='y')
    2.7182818284590455
    >>> newton_raphson('exp(x) - 1', 10, precision=0.005)
    1.2186556186174883e-10
    >>> newton_raphson('cos(x)', 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Could not find root
    """

    x = symbols(variable)
    func = lambdify(x, function)
    diff_function = lambdify(x, diff(function, x))

    prev_guess = starting_point

    while True:
        if diff_function(prev_guess) != 0:
            next_guess = prev_guess - multiplicity * func(prev_guess) / diff_function(
                prev_guess
            )
        else:
            raise ZeroDivisionError("Could not find root") from None

        # Precision is checked by comparing the difference of consecutive guesses
        if abs(next_guess - prev_guess) < precision:
            return next_guess

        prev_guess = next_guess


# Let's Execute
if __name__ == "__main__":

    # Find root of trigonometric function
    # Find value of pi
    print(f"The root of sin(x) = 0 is {newton_raphson('sin(x)', 2)}")

    # Find root of polynomial
    # Find fourth Root of 5
    print(f"The root of x**4 - 5 = 0 is {newton_raphson('x**4 -5', 0.4 +5j)}")

    # Find value of e
    print(
        "The root of log(y) - 1 = 0 is ",
        f"{newton_raphson('log(y) - 1', 2, variable='y')}",
    )

    # Exponential Roots
    print(
        "The root of exp(x) - 1 = 0 is",
        f"{newton_raphson('exp(x) - 1', 10, precision=0.005)}",
    )

    # Find root of cos(x)
    print(f"The root of cos(x) = 0 is {newton_raphson('cos(x)', 0)}")
