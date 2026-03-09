"""
Python program to show how to interpolate and evaluate a polynomial
using Neville's method.
Neville's method evaluates a polynomial that passes through a
given set of x and y points for a particular x value (x0) using the
Newton polynomial form.
Reference:
    https://rpubs.com/aaronsc32/nevilles-method-polynomial-interpolation
"""


def neville_interpolate(x_points: list, y_points: list, x0: int) -> list:
    """
       Interpolate and evaluate a polynomial using Neville's method.
       Arguments:
           x_points, y_points: Iterables of x and corresponding y points through
            which the polynomial passes.
           x0: The value of x to evaluate the polynomial for.
       Return Value: A list of the approximated value and the Neville iterations
           table respectively.
    >>> import pprint
    >>> neville_interpolate((1,2,3,4,6), (6,7,8,9,11), 5)[0]
    10.0
    >>> pprint.pprint(neville_interpolate((1,2,3,4,6), (6,7,8,9,11), 99)[1])
    [[0, 6, 0, 0, 0],
     [0, 7, 0, 0, 0],
     [0, 8, 104.0, 0, 0],
     [0, 9, 104.0, 104.0, 0],
     [0, 11, 104.0, 104.0, 104.0]]
    >>> neville_interpolate((1,2,3,4,6), (6,7,8,9,11), 99)[0]
    104.0
    >>> neville_interpolate((1,2,3,4,6), (6,7,8,9,11), '')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'str' and 'int'
    """
    n = len(x_points)
    q = [[0] * n for i in range(n)]
    for i in range(n):
        q[i][1] = y_points[i]

    for i in range(2, n):
        for j in range(i, n):
            q[j][i] = (
                (x0 - x_points[j - i + 1]) * q[j][i - 1]
                - (x0 - x_points[j]) * q[j - 1][i - 1]
            ) / (x_points[j] - x_points[j - i + 1])

    return [q[n - 1][n - 1], q]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
