"""
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approach of suming 'Equally Spaced Abscissas'

method 1:
"extended trapezoidal rule"

"""


def method_1(boundary, steps):
    """
    Compute the integral using the extended trapezoidal rule.

    Doctest:
    >>> method_1([0.0, 1.0], 10.0)
    0.3349999999999999
    """
    # "extended trapezoidal rule"
    # int(f) = dx/2 * (f1 + 2f2 + ... + fn)

    h = (boundary[1] - boundary[0]) / steps
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    y = 0.0
    y += (h / 2.0) * f(a)
    for i in x_i:
        # print(i)
        y += h * f(i)
    y += (h / 2.0) * f(b)
    return y


def make_points(a, b, h):
    """
    Generate the points.

    Doctest:
    >>> result = list(make_points(0.0, 1.0, 0.1))
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [0.1, 0.2, 0.30000000000000004, 0.4, 0.5,
     0.6, 0.7, 0.7999999999999999, 0.8999999999999999]
    """

    x = a + h

    while x < (b - h):
        yield x
        x = x + h


def f(x):  # enter your function here
    """
    Doctest:
    >>> f(2)
    4
    >>> f(3)
    9
    """
    y = (x - 0) * (x - 0)
    return y


def main():
    a = 0.0  # Lower bound of integration
    b = 1.0  # Upper bound of integration
    steps = 10.0  # define number of steps or resolution
    boundary = [a, b]  # define boundary of integration
    y = method_1(boundary, steps)
    print(f"y = {y}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
