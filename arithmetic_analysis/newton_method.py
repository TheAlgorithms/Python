"""Newton's Method."""

# Newton's Method - https://en.wikipedia.org/wiki/Newton%27s_method
from typing import Callable

RealFunc = Callable[[float], float]  # type alias for a real -> real function


# function: f(x)
# derivative: f'(x)
def newton(
    function: RealFunc,
    derivative: RealFunc,
    starting_int: int,
) -> float:
    """Calculates one root of function by Newton's method starting at x0 = starting_point
    >>> newton(lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x ** 2 - 2, 3)
    2.0945514815423474
    >>> newton(lambda x: x ** 3 - 1, lambda x: 3 * x ** 2, -2)
    1.0
    >>> newton(lambda x: x ** 3 - 1, lambda x: 3 * x ** 2, -4)
    1.0000000000000102
    >>> import math
    >>> newton(math.sin, math.cos, 1)
    0.0
    >>> newton(math.sin, math.cos, 2)
    3.141592653589793
    >>> newton(math.cos, lambda x: -math.sin(x), 2)
    1.5707963267948966
    >>> newton(math.cos, lambda x: -math.sin(x), 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Could not find root
    """
    prev_guess = float(starting_int)  # sets the starting point for the algorithm
    while True:
        try:
            # Calculates the next point based on x = x0 - f(x) / f'(x)
            next_guess = prev_guess - function(prev_guess) / derivative(prev_guess)
        except ZeroDivisionError:
            raise ZeroDivisionError("Could not find root") from None

        if abs(prev_guess - next_guess) < 10 ** -5:
            # The algorithm stops when the difference between the last 2 guesses are
            # less than the fixed presition of 10 ** -5
            return next_guess
        prev_guess = next_guess


def main():
    def f(x: float) -> float:
        return (x ** 3) - (2 * x) - 5

    def f1(x: float) -> float:
        return 3 * (x ** 2) - 2

    print(newton(f, f1, 3))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
