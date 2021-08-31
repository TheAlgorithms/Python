def double_factorial(n: int) -> int:
    """
    Compute double factorial using recursive method.
    Recursion can be costly for large numbers.

    To learn about the theory behind this algorithm:
    https://en.wikipedia.org/wiki/Double_factorial

    >>> import math
    >>> all(double_factorial(i) == math.prod(range(i, 0, -2)) for i in range(20))
    True
    >>> double_factorial(0.1)
    Traceback (most recent call last):
        ...
    ValueError: double_factorial() only accepts integral values
    >>> double_factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: double_factorial() not defined for negative values
    """
    if not isinstance(n, int):
        raise ValueError("double_factorial() only accepts integral values")
    if n < 0:
        raise ValueError("double_factorial() not defined for negative values")
    return 1 if n <= 1 else n * double_factorial(n - 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
