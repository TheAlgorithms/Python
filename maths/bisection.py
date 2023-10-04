"""
Given a function on floating number f(x) and two floating numbers ‘a’ and ‘b’ such that
f(a) * f(b) < 0 and f(x) is continuous in [a, b].
Here f(x) represents algebraic or transcendental equation.
Find root of function in interval [a, b] (Or find a value of x such that f(x) is 0)

https://en.wikipedia.org/wiki/Bisection_method
"""


def equation(x: float) -> float:
    """
    >>> equation(5)
    -15
    >>> equation(0)
    10
    >>> equation(-5)
    -15
    >>> equation(0.1)
    9.99
    >>> equation(-0.1)
    9.99
    """
    return 10 - x * x


def bisection(a: float, b: float) -> float:
    """
    >>> bisection(-2, 5)
    3.1611328125
    >>> bisection(0, 6)
    3.158203125
    >>> bisection(2, 3)
    Traceback (most recent call last):
        ...
    ValueError: Wrong space!
    """
    # Bolzano theory in order to find if there is a root between a and b
    if equation(a) * equation(b) >= 0:
        raise ValueError("Wrong space!")

    c = a
    while (b - a) >= 0.01:
        # Find middle point
        c = (a + b) / 2
        # Check if middle point is root
        if equation(c) == 0.0:
            break
        # Decide the side to repeat the steps
        if equation(c) * equation(a) < 0:
            b = c
        else:
            a = c
    return c


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(bisection(-2, 5))
    print(bisection(0, 6))
