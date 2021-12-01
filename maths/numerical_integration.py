"""
Approximates the area under the curve using many different 
methods of numerical integration. For more information on 
numerical integration see here:

https://en.wikipedia.org/wiki/Numerical_integration

The methods used are described in order from least 
accurate to most accurate:
1. Right endpoint rule
2. Left endpoint rule
3. Midpoint rule
4. Simpson's rule
5. Trapezoidal rule

For those looking to implement an algorithm for 
integration, the trapezoidal rule is the best fit. 
Generally, if your steps are equal to the size of 
your interval * 10,000, it will yield a fairly accurate
algorithm for a definite integral
"""
from __future__ import annotations

from typing import Callable

def right_endpt_rule(
    fnc: Callable[[int | float], int | float],
    x_start: int | float,
    x_end: int | float,
    steps: int = 100,
) -> float:
    
    """
    Construct a rectangle on each subinterval, the height of 
    the rectangle is determined by the function value at the 
    right endpoint of the subinterval. The rectangle width 
    is the length of the function (x_end-x_start)/steps. By 
    summing the area of each of these rectangles, we are 
    approximating the area underneath the curve

    Doctests:
    >>> def f(x):
    ...    return x**2

    >>> right_endpt_rule(f, 0, 1, 4)
    0.46875
    """
    area = 0.0
    dx = (x_end - x_start) / steps

    # For the RIGHT endpoint rule, we start at the 
    # right-hand side of each reactangle 
    # so our starting point must be x_start+dx
    i = x_start + dx

    # Looping through each subinterval 
    # till the end of the interval
    while i < x_end:
        # Calculate the height of rectangle
        height = fnc(i)
        # Calculate the area of rectangle and 
        # add it to our total area
        area += (height*dx)

        # Increment to the next subinterval
        i += dx

    return area

def left_endpt_rule(
    fnc: Callable[[int | float], int | float],
    x_start: int | float,
    x_end: int | float,
    steps: int = 100,
) -> float:

    """
    Construct a rectangle on each subinterval, the height of 
    the rectangle is determined by the function value at the 
    left endpoint of the subinterval. The rectangle width 
    is the length of the function (x_end-x_start)/steps. By 
    summing the area of each of these rectangles, we are 
    approximating the area underneath the curve
    
    Doctests:
    >>> def f(x):
    ...    return x**2

    >>> left_endpt_rule(f, 1, 5, 4)
    30.0
    """
    area = 0.0
    dx = (x_end - x_start) / steps

    # For the LEFT endpoint rule, we start at the 
    # left-hand side of each reactangle 
    # so our starting point must be x_start
    i = x_start

    # Looping through each subinterval 
    # till the end of the interval
    while i <= x_end-dx:
        # Calculate the height of rectangle
        height = fnc(i)
        # Calculate the area of rectangle and 
        # add it to our total area
        area += (height*dx)

        # Increment to the next subinterval
        i += dx

    return area

def midpoint_rule(
    fnc: Callable[[int | float], int | float],
    x_start: int | float,
    x_end: int | float,
    steps: int = 100,
) -> float:

    """
    Construct a rectangle on each subinterval, the height of 
    the rectangle is determined by the function value at the 
    midpoint of the subinterval. The rectangle width 
    is the length of the function (x_end-x_start)/steps. By 
    summing the area of each of these rectangles, we are 
    approximating the area underneath the curve

    Doctests:
    >>> def f(x):
    ...    return x**2

    >>> midpoint_rule(f, 1, 5, 4)
    41.0
    """
    area = 0.0
    dx = (x_end - x_start) / steps

    # For the midpoint rule, we start at the 
    # middle of each sub-interval 
    # so our starting point must be (x_start + (x_start+dx))/2
    # i.e. the average of the left point and the right point
    i = (x_start + (x_start+dx))/2

    # Looping through each subinterval 
    # till the end of the interval
    while i <= x_end:
        # Calculate the height of rectangle
        height = fnc(i)
        # Calculate the area of rectangle and 
        # add it to our total area
        area += (height*dx)

        # Increment to the next subinterval
        i += dx

    return area

def simpsons_rule(
    fnc: Callable[[int | float], int | float],
    x_start: int | float,
    x_end: int | float,
    steps: int = 100,
) -> float:

    """
    For simpson's rule, there must be an even number of subintervals.
    The exact derivation for this rule is complicated; the motivated 
    can find an explanation here:
    https://en.wikipedia.org/wiki/Simpson%27s_rule

    Note that this is NOT the Simpson's 1/3 rule or the simpson's 3/8th
    rule. The algrorithm employed is the general form which allows for an
    arbitrary amount of steps

    Doctests:
    >>> def f(x):
    ...    return x**2

    >>> simpsons_rule(f, 1, 5, 4)
    41.33333333333333
    """

    # Steps must be even
    if steps % 2 != 0:
        steps += 1

    dx = (x_end - x_start) / steps
    sum = 0.0

    # Loop from begining of interval to end of interval 
    # and sum up according to simpsons rule
    i = x_start
    counter = 1
    while i <= x_end:
        
        # If interval is at beginning or end, 
        # it doesn't have a multiplier
        if i == x_start or i == x_end:
            sum += fnc(i)

        # If interval is an odd number (the first, third,
        # fifth, ...), then the multiplier is 4
        elif counter % 2 == 0:
            sum += (4*fnc(i))

        # If interval is an even number (the second, 
        # fourth, ...), then the multiplier is 2
        else:
            sum += (2*fnc(i))
        
        # Increment our interval and counter
        i += dx
        counter += 1
    
    # Simpson's rule also says that the area is dx/3 * sum
    return (dx/3) * sum

def trapezoidal_area(
    fnc: Callable[[int | float], int | float],
    x_start: int | float,
    x_end: int | float,
    steps: int = 100,
) -> float:

    """
    Treats curve as a collection of linear lines and sums the area of the
    trapezium shape they form
    :param fnc: a function which defines a curve
    :param x_start: left end point to indicate the start of line segment
    :param x_end: right end point to indicate end of line segment
    :param steps: an accuracy gauge; more steps increases the accuracy
    :return: a float representing the length of the curve

    >>> def f(x):
    ...    return 5
    >>> '%.3f' % trapezoidal_area(f, 12.0, 14.0, 1000)
    '10.000'

    >>> def f(x):
    ...    return 9*x**2
    >>> '%.4f' % trapezoidal_area(f, -4.0, 0, 10000)
    '192.0000'

    >>> '%.4f' % trapezoidal_area(f, -4.0, 4.0, 10000)
    '384.0000'
    """
    x1 = x_start
    fx1 = fnc(x_start)
    area = 0.0

    for i in range(steps):

        # Approximates small segments of curve as linear and solve
        # for trapezoidal area
        x2 = (x_end - x_start) / steps + x1
        fx2 = fnc(x2)
        area += abs(fx2 + fx1) * (x2 - x1) / 2

        # Increment step
        x1 = x2
        fx1 = fx2
    return area     

if __name__ == "__main__":

    # Define a function for testing
    def f(x):
        return x ** 3

    print("f(x) = x^3")
    print("The area between the curve, x = 0, x = 5 and the x axis is:")

    # Test each approximation with a variety of intervals
    i = 10
    while i <= 100000:
        r_area = right_endpt_rule(f, 0, 5, i)
        l_area = left_endpt_rule (f, 0, 5, i)
        m_area = midpoint_rule   (f, 0, 5, i)
        t_area = trapezoidal_area(f, 0, 5, i)
        s_area = simpsons_rule   (f, 0, 5, i)
        print(f"Right endpoint rule ({i} steps): \t {r_area}")
        print(f"Left endpoint rule ({i} steps):  \t {l_area}")
        print(f"Midpoint rule ({i} steps):       \t {m_area}")
        print(f"Simpson's rule ({i} steps):      \t {s_area}")
        print(f"Trapezoidal rule ({i} steps):    \t {t_area}\n")

        i *= 10

    def g(x):
        return x**2
    
    print(simpsons_rule(g, 1, 5, 4))