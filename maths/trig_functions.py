"""
The 6 normal trig functions and their inverses. In theory, I could 
have used a CORDIC algorithm https://en.wikipedia.org/wiki/CORDIC
but this requires a load of pre-calculated values stored in some
list. In keeping with the spirit of what this repository aims to
achieve, I decided to use a taylor series expansion so that everything
is clear
"""
from math import pi

# A lot of the maclaurin series require 
# a factorial in their expressions. This
# is just a simple O(n) algo for factorial
def factorial(x: int) -> int:

    value = 1
    for i in range(1, x + 1):
        value *= i
    return value


def sine(
    x: float,
    accuracy: int = 85
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions#Trigonometric_functions

    Accuracy cannot exceed 85 for 
    this algorithm because python 
    runs into issues with converting 
    huge factorials into floats.
    Doctests:
    """

    # Value to be returned
    sum = 0.0
    
    # Python imposed limitation
    if accuracy > 85:
        accuracy = 85

    # We can reduce our range of angles to just 
    # be from [0, 2pi] because trig functions are periodic
    x = x%(2*pi)

    # We can further reduce our range of inputs to just [-pi/2, pi/2]
    if x > (pi/2) and pi < ((3*pi)/2):
        # Output must then be negative if it's in the second or third
        # quadrant
        sum *= -1
        # Move the value out of that quadrant
        x += pi

    # And we can once again reduce the range of inputs to [0, pi/2]
    if x >= ((3*pi)/2):
        x = (2*pi)-x


    for n in range(accuracy):
        numerator = (-1)**n * pow(x, (2*n)+1)
        denominator = factorial((2*n)+1)
        sum += float(numerator) / float (denominator)

    return sum

def cosine(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def tangent(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def cosecant(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def secant(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def cotangent(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def arc_sine(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def arc_cosine(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def arc_tangent(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def arc_cosecant(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def arc_secant(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

def arc_cotangent(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """
    pass

if __name__ == "__main__":

    # do some testing stuff
    print(sine(0))
    print(sine(pi/3))
    print(sine(pi/2))
    print(sine((3*pi)/4))
    print(sine(pi))
    print(sine((5*pi)/4))
    print(sine((3*pi)/2))
    print(sine((7*pi)/3))
    print(sine(2*pi))