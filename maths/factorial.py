"""
Factorial of a positive integer -- https://en.wikipedia.org/wiki/Factorial
"""


def factorial(number: int) -> int:
    """
    Calculate the factorial of specified number (n!).

    >>> import math
    >>> all(factorial(i) == math.factorial(i) for i in range(20))
    True
    >>> factorial(0.1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() only accepts integral values
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() not defined for negative values
    >>> factorial(1)
    1
    >>> factorial(6)
    720
    >>> factorial(0)
    1
    """
    if number != int(number):
        raise ValueError("factorial() only accepts integral values")
    if number < 0:
        raise ValueError("factorial() not defined for negative values")
    value = 1
    for i in range(1, number + 1):
        value *= i
    return value


def factorial_recursive(number: int) -> int:
    """
    Calculate the factorial of a number using recursion.

    >>> import math
    >>> all(factorial_recursive(i) == math.factorial(i) for i in range(10))
    True
    >>> factorial_recursive(0)
    1
    >>> factorial_recursive(5)
    120
    >>> factorial_recursive(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial_recursive() not defined for negative values
    """
    if number != int(number):
        raise ValueError("factorial_recursive() only accepts integral values")
    if number < 0:
        raise ValueError("factorial_recursive() not defined for negative values")
    if number in (0, 1):
        return 1
    return number * factorial_recursive(number - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
