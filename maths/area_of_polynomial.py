"""
Approximates the area of a polynomial given from the user using the trapezoidal rule
"""

def input_polynomial() -> list[float]:
    """
    This function takes the order of the polynomial and 
    its coefficients as inputs from the user
    and returns a list of coefficients.
    """
    m = int(input("Enter order of polynomial: "))
    arr = []
    for j in range(m, -1, -1):
        a_j = float(input(f"Enter coefficient of a[{j}]: "))
        arr.append(a_j)
    return arr

def evaluate(arr: list[float], x: float) -> float:
    """
    This function takes a list of coefficients 
    and a value of x as inputs and returns 
    the value of the polynomial at that point.
    
    >>> arr = [5]
    >>> f"{evaluate(arr,2)}
    '5'
    >>> arr = [5,1]
    >>> f"{evaluate(arr,2)}
    '11'
    """
    y = 0
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
    :param fnc: a list which defines a curve
    :param x_start: left end point to indicate the start of line segment
    :param x_end: right end point to indicate end of line segment
    :param steps: an accuracy gauge; more steps increases the accuracy
    :return: a float representing the length of the curve

    >>> def f(x):
    ...    return 5
    >>> f"{trapezoidal_area(f, 12.0, 14.0, 1000):.3f}"
    '10.000'
    >>> def f(x):
    ...    return 9*x**2
    >>> f"{trapezoidal_area(f, -4.0, 0, 10000):.4f}"
    '192.0000'
    >>> f"{trapezoidal_area(f, -4.0, 4.0, 10000):.4f}"
    '384.0000'
    """
    # This function takes a list of coefficients, 
    # start and end points on the x-axis, 
    # and the number of steps as inputs
    # and returns the area under the curve 
    # between those points using the trapezoidal rule.
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
    # In the main block, the code takes inputs for the polynomial, start and end points on the x-axis,
    # and calculates the area under the curve for different numbers of steps.
    f = input_polynomial()
    print("The given function is :")
    for j in range(len(f)-1):
        print(f"{f[j]}*x^{len(f)-j-1}", end=" + ")
    print(f"{f[-1]}*x^{0}")

    x1 = float(input("Enter the value of x_start : "))
    x2 = float(input("Enter the value of x_end : "))

    print(f"The area between the curve, x = {x1}, x = {x2} and the x axis is:")
    i = 10
    while i <= 100_000:
        area = trapezoidal_area(f, x1, x2, i)
        print(f"with {i} steps: area = {area:.4f} sq units")
        i *= 10
