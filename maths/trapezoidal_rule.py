"""
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approach of suming 'Equally Spaced Abscissas'

method 1:
"extended trapezoidal rule"
int(f) = dx/2 * (f1 + 2f2 + ... + fn)

"""


def method_1(boundary, steps):
    """
    Apply the extended trapezoidal rule to approximate the integral of function f(x)
    over the interval defined by 'boundary' with the number of 'steps'.

    Args:
        boundary (list of floats): A list containing the start and end values [a, b].
        steps (int): The number of steps or subintervals.
    Returns:
        float: Approximation of the integral of f(x) over [a, b].
    Examples:
    >>> method_1([0, 1], 10)
    0.3349999999999999
    """
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
    Generates points between 'a' and 'b' with step size 'h', excluding the end points.
    Args:
        a (float): Start value
        b (float): End value
        h (float): Step size
    Examples:
    >>> list(make_points(0, 10, 2.5))
    [2.5, 5.0, 7.5]

    >>> list(make_points(0, 10, 2))
    [2, 4, 6, 8]

    >>> list(make_points(1, 21, 5))
    [6, 11, 16]

    >>> list(make_points(1, 5, 2))
    [3]

    >>> list(make_points(1, 4, 3))
    []
    """
    x = a + h
    while x <= (b - h):
        yield x
        x = x + h


def f(x):  # enter your function here
    """
    Example:
    >>> f(2)
    4
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
