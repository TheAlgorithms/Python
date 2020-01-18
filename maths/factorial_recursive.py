def factorial(n: int) -> int:
    """
    Calculate the factorial of a positive integer
    https://en.wikipedia.org/wiki/Factorial

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
    """
    if not isinstance(n, int):
        raise ValueError("factorial() only accepts integral values")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
