def double_factorial_recursive(n: int) -> int:
    """
    Compute double factorial using recursive method.
    Recursion can be costly for large numbers.

    To learn about the theory behind this algorithm:
    https://en.wikipedia.org/wiki/Double_factorial

    >>> from math import prod
    >>> all(double_factorial_recursive(i) == prod(range(i, 0, -2)) for i in range(20))
    True
    >>> double_factorial_recursive(0.1)
    Traceback (most recent call last):
        ...
    ValueError: double_factorial_recursive() only accepts integral values
    >>> double_factorial_recursive(-1)
    Traceback (most recent call last):
        ...
    ValueError: double_factorial_recursive() not defined for negative values
    """
    if not isinstance(n, int):
        raise ValueError("double_factorial_recursive() only accepts integral values")
    if n < 0:
        raise ValueError("double_factorial_recursive() not defined for negative values")
    return 1 if n <= 1 else n * double_factorial_recursive(n - 2)


def double_factorial_iterative(num: int) -> int:
    """
    Compute double factorial using iterative method.

    To learn about the theory behind this algorithm:
    https://en.wikipedia.org/wiki/Double_factorial

    >>> from math import prod
    >>> all(double_factorial_iterative(i) == prod(range(i, 0, -2)) for i in range(20))
    True
    >>> double_factorial_iterative(0.1)
    Traceback (most recent call last):
        ...
    ValueError: double_factorial_iterative() only accepts integral values
    >>> double_factorial_iterative(-1)
    Traceback (most recent call last):
        ...
    ValueError: double_factorial_iterative() not defined for negative values
    """
    if not isinstance(num, int):
        raise ValueError("double_factorial_iterative() only accepts integral values")
    if num < 0:
        raise ValueError("double_factorial_iterative() not defined for negative values")
    value = 1
    for i in range(num, 0, -2):
        value *= i
    return value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
