"""
Use the Secant method to solve Non-Linear/Transcendental Equations.
Author: Ravi kumar (@ ravi-ivar-7)
"""

from collections.abc import Callable

import numpy as np


def secant_method(
    equation: Callable,
    guess_1: float,
    guess_2: float,
    accuracy: float,
    iterations: int,
) -> float:
    """
    Solve a Non-Linear/Transcendental Equations using Secant Method.

    https://en.wikipedia.org/wiki/Secant_method

    args:
    equation: A Non-Linear/Transcendental Equation with one variable (x).
    guess_1: First guess for secant method.
    guess_2: Second guess for secant method.
    accuracy: Desired level of precision or tolerance.
    iterations: Method does not always guarantee root. Hence required some stopping criteria.

    Returns:
        Root of equation accurate upto given accuracy.

    >>> def eq(x):
    ...     return x**3 - 5*x + 1
    >>> secant_method(eq, 0, 1, .001, 10)
    0.2016398528913041

    >>> def eq(x):
    ...     return x**3 - 5*x + 1
    >>> secant_method(eq, 1, 0, .001, 10)
    0.2016338525316861

    >>> def eq(x):
    ...     return x**3 - 5*x + 1
    >>> secant_method(eq, 0, 0, .001, 10)
    Traceback (most recent call last):
        ...
    ValueError: Value of both guesses cannot be same.

    >>> def eq(x):
    ...     return x**3 - 5*x + 10
    >>> secant_method(eq, 1, 0, .001, 10)
    Traceback (most recent call last):
        ...
    ValueError: Secant method failed!
    """

    if guess_1 == guess_2:
        raise ValueError("Value of both guesses cannot be same.")

    x = np.zeros(
        (iterations + 2),
    )
    x[0] = guess_1
    x[1] = guess_2

    for i in range(iterations):
        x[i + 2] = x[i + 1] - (equation(x[i + 1]) * (x[i + 1] - x[i])) / (
            equation(x[i + 1]) - equation(x[i])
        )

        if abs(x[i + 2] - x[i + 1]) <= accuracy:
            return x[i + 2]

    raise ValueError("Secant method failed!")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
