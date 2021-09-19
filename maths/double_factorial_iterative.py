def double_factorial(num: int) -> int:
    """
    Compute double factorial using iterative method.

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
    if not isinstance(num, int):
        raise ValueError("double_factorial() only accepts integral values")
    if num < 0:
        raise ValueError("double_factorial() not defined for negative values")
    value = 1
    for i in range(num, 0, -2):
        value *= i
    return value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
