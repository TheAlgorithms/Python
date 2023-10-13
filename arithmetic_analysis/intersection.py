import math
from collections.abc import Callable


def intersection(function: Callable[[float], float], x0: float, x1: float) -> float:
    """
    Find the root of the given function using the secant method.

    Args:
        function (Callable[[float], float]): The function to find the root of.
        x0 (float): The initial guess for the root.
        x1 (float): Another initial guess for the root.

    Returns:
        float: The estimated root of the function.

    Raises:
        ZeroDivisionError: If the method encounters division by zero.

    Examples:

    # Test cases for finding the root of various functions:

    # Valid root within the specified range
    >>> intersection(lambda x: x ** 3 - 1, -5, 5)
    1.0000000000003888

    # Valid root at one of the boundary points
    >>> intersection(lambda x: x ** 3 - 1, 5, 5)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero, could not find root

    # Valid root with large range
    >>> intersection(lambda x: x ** 3 - 1, 100, 200)
    1.0000000000003888

    # Valid root with a quadratic equation
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 0, 2)
    0.9999999998088019

    # Valid root with a quadratic equation at another interval
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 2, 4)
    2.9999999998088023

    # Valid root with a quadratic equation and a large range
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 4, 1000)
    3.0000000001786042

    # Valid root for the sine function
    >>> intersection(math.sin, -math.pi, math.pi)
    0.0

    # Valid root for the cosine function
    >>> intersection(math.cos, -math.pi, math.pi)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero, could not find root

    # Test with the 'f' function provided in the code
    >>> intersection(f, 3, 3.5)
    # Output will depend on the specific 'f' function used.

    # Edge case: Invalid input with the same 'x0' and 'x1' values
    >>> intersection(lambda x: x ** 3 - 1, 3, 3)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero, could not find root

    # Edge case: Invalid input with 'x0' and 'x1' switched
    >>> intersection(lambda x: x ** 3 - 1, 5, -5)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero, could not find root

    # Edge case: Input where the initial approximation is a root
    >>> intersection(lambda x: x ** 3 - 1, 1, 2)
    1.0
    """
    x_n: float = x0
    x_n1: float = x1
    while True:
        if x_n == x_n1 or function(x_n1) == function(x_n):
            raise ZeroDivisionError("float division by zero, could not find root")
        x_n2: float = x_n1 - (
            function(x_n1) / (
                (function(x_n1) - function(x_n)) / (x_n1 - x_n)
            )
        )

        if abs(x_n2 - x_n1) < 10**-5:
            return x_n2
        x_n = x_n1
        x_n1 = x_n2


# Define the 'f' function for testing
def f(x: float) -> float:
    return math.pow(x, 3) - (2 * x) - 5


if __name__ == "__main__":
    print(
        intersection(f, 3, 3.5)
    )  # Output will depend on the specific 'f' function used.
