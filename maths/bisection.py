"""Given a function f(x) on floating number x and two numbers ‘a’ and ‘b’
such that f(a)*f(b) < 0 and f(x) is continuous in [a, b]. Here f(x) represents algebraic or transcendental equation.
Find root of function in interval [a, b] (Or find a value of x such that f(x) is 0)
"""
import doctest


def equation(x: int) -> float:
    return 10 - x * x


def bisection(a: int, b: int) -> float:
    """
    >>> bisection(-2,5)
    3.1611328125
    >>> bisection(0, 6)
    3.158203125
    >>> bisection(2,3)
    False
    """
    c = False
    # Bolzano theory in order to find if there is a root between a and b
    if equation(a) * equation(b) >= 0:
        return c

    half = a
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


if __name__ == '__main__':
    print(bisection(-2, 5))
    print(bisection(0, 6))
    print(bisection(2, 3))
    doctest.testmod()
