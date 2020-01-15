import math


def fx(x: float, a: float) -> float:
    return math.pow(x, 2) - a


def fx_derivative(x: float) -> float:
    return 2 * x


def get_initial_point(a: float) -> float:
    start = 2.0

    while start <= a:
        start = math.pow(start, 2)

    return start


def square_root_iterative(
    a: float, max_iter: int = 9999, tolerance: float = 0.00000000000001
) -> float:
    """
    Sqaure root is aproximated using Newtons method.
    https://en.wikipedia.org/wiki/Newton%27s_method
    
    >>> all(abs(square_root_iterative(i)-math.sqrt(i)) <= .00000000000001  for i in range(0, 500))
    True
    
    >>> square_root_iterative(-1)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    >>> square_root_iterative(4)
    2.0

    >>> square_root_iterative(3.2)
    1.788854381999832

    >>> square_root_iterative(140)
    11.832159566199232
    """

    if a < 0:
        raise ValueError("math domain error")

    value = get_initial_point(a)

    for i in range(max_iter):
        prev_value = value
        value = value - fx(value, a) / fx_derivative(value)
        if abs(prev_value - value) < tolerance:
            return value

    return value


if __name__ == "__main__":
    from doctest import testmod

    testmod()
