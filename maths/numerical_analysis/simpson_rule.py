"""
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approach of summing 'Equally Spaced Abscissas'

method 2:
"Simpson Rule"

"""


def method_2(boundary: list[int], steps: int) -> float:
    # "Simpson Rule"
    # int(f) = delta_x/2 * (b-a)/3*(f1 + 4f2 + 2f_3 + ... + fn)
    """
    Calculate the definite integral of a function using Simpson's Rule.
    :param boundary: A list containing the lower and upper bounds of integration.
    :param steps: The number of steps or resolution for the integration.
    :return: The approximate integral value.

    >>> round(method_2([0, 2, 4], 10), 10)
    2.6666666667
    >>> round(method_2([2, 0], 10), 10)
    -0.2666666667
    >>> round(method_2([-2, -1], 10), 10)
    2.172
    >>> round(method_2([0, 1], 10), 10)
    0.3333333333
    >>> round(method_2([0, 2], 10), 10)
    2.6666666667
    >>> round(method_2([0, 2], 100), 10)
    2.5621226667
    >>> round(method_2([0, 1], 1000), 10)
    0.3320026653
    >>> round(method_2([0, 2], 0), 10)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Number of steps must be greater than zero
    >>> round(method_2([0, 2], -10), 10)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Number of steps must be greater than zero
    """
    if steps <= 0:
        raise ZeroDivisionError("Number of steps must be greater than zero")

    h = (boundary[1] - boundary[0]) / steps
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    y = 0.0
    y += (h / 3.0) * f(a)
    cnt = 2
    for i in x_i:
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i)
        cnt += 1
    y += (h / 3.0) * f(b)
    return y


def make_points(a, b, h):
    x = a + h
    while x < (b - h):
        yield x
        x = x + h


def f(x):  # enter your function here
    y = (x - 0) * (x - 0)
    return y


def main():
    a = 0.0  # Lower bound of integration
    b = 1.0  # Upper bound of integration
    steps = 10.0  # number of steps or resolution
    boundary = [a, b]  # boundary of integration
    y = method_2(boundary, steps)
    print(f"y = {y}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
