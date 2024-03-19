"""
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approach of suming 'Equally Spaced Abscissas'

method 1:
"extended trapezoidal rule"

"""


def method_1(func, boundary, steps):
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
        y += h * f(func, i)
    y += (h / 2.0) * f(b)
    return y


def make_points(a, b, h):
    """
    Yields equally spaced points between a and b
    >>> x_i = make_points(0, 0.4, 0.1)
    >>> next(x_i)
    0.1
    >>> next(x_i)
    0.2
    >>> next(x_i)
    0.3
    >>> next(x_i)
    Traceback (most recent call last):
        ...
    StopIteration

    >>> x_i = make_points(0, 1, -0.2)
    >>> next(x_i)
    Traceback (most recent call last):
        ...
    ValueError: h must be positive

    >>> x_i = make_points(1,0,0.2)
    >>> next(x_i)
    Traceback (most recent call last):
        ...
    ValueError: a must be less than b
    """
    if h <= 0:
        raise ValueError("h must be positive")
    if a >= b:
        raise ValueError("a must be less than b")

    x = round(a + h, 10)
    while x <= (b - h):
        yield x
        x = round(x + h, 10)


def f(y, x):  # enter your function here
    """
    Returns the value of a lambda functiοn y at x
    >>> f(lambda x: x**2,2)
    4
    >>> f(lambda x: x**2,-1)
    1
    >>> f(lambda x: (x+1)/2,5)
    3.0
    >>> f(lambda x: (x+1)/2,0)
    0.5
    """
    return y(x)


def main():
    a = 0.0  # Lower bound of integration
    b = 1.0  # Upper bound of integration
    steps = 10.0  # define number of steps or resolution
    boundary = [a, b]  # define boundary of integration
    y = method_1(lambda x: x**2, boundary, steps)
    print(f"y = {y}")


if __name__ == "__main__":
    main()
