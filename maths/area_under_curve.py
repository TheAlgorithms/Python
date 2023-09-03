"""
Approximates the area under the curve using the trapezoidal rule
"""
from __future__ import annotations


def evaluate(arr: list[float], x: float) -> float:
    """
    This function takes a list of coefficients
    and a value of x as inputs and returns
    the value of the polynomial at that point.
    :param arr: a list containing coefficients
    :param x: value of x

    >>> arr = [5]
    >>> f"{evaluate(arr,2)}"
    '5.0'
    >>> arr = [5,1]
    >>> f"{evaluate(arr,2)}"
    '11.0'
    """
    y = 0.0
    for i in range(len(arr)):
        y += arr[i] * (x ** (len(arr) - i - 1))
    return y


def trapezoidal_area(
    fnc: list[float],
    x_start: float,
    x_end: float,
    steps: int = 100,
) -> float:
    """
    Treats curve as a collection of linear lines and sums the area of the
    trapezium shape they form
    :param fnc: a list which defines a curve of polynomial
    :param x_start: left end point to indicate the start of line segment
    :param x_end: right end point to indicate end of line segment
    :param steps: an accuracy gauge; more steps increases the accuracy
    :return: a float representing the length of the curve

    >>> f = [5.0]
    >>> f"{trapezoidal_area(f, 12.0, 14.0, 1000):.3f}"
    '10.000'
    >>> f = [9.0,0.0,0.0]
    >>> f"{trapezoidal_area(f, -4.0, 0, 10000):.4f}"
    '192.0000'
    >>> f"{trapezoidal_area(f, -4.0, 4.0, 10000):.4f}"
    '384.0000'
    """
    dx = (x_end - x_start) / steps
    area = 0.0
    for i in range(steps):
        x1 = x_start + i * dx
        x2 = x_start + (i + 1) * dx
        fx1 = evaluate(fnc, x1)
        fx2 = evaluate(fnc, x2)
        area += abs((fx2 + fx1) * dx / 2)
    return area


if __name__ == "__main__":
    m = int(input("Enter order of polynomial: ").strip())
    f = []
    for j in range(m, -1, -1):
        a_j = float(input(f"Enter coefficient of a[{j}]: ").strip())
        f.append(a_j)

    print("The given function is :")
    for j in range(len(f) - 1):
        print(f"{f[j]}*x^{len(f)-j-1}", end=" + ")
    print(f"{f[-1]}*x^{0}")

    x1 = float(input("Enter the value of x_start : "))
    x2 = float(input("Enter the value of x_end : "))

    # print(f"The area between the curve, x = {x1}, x = {x2} and the x axis is:")
    # i = 10
    # while i <= 100000:
    #     print(f"with {i} steps: area = {trapezoidal_area(f, x1, x2, i):.4f}")
    #     i *= 10
    print(evaluate(f, x1))
