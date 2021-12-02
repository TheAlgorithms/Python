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
    for n in range(2,x):
        value *= n
    
    return value

def sine(
    x: float,
    accuracy: int = 85
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions#Trigonometric_functions

    Doctests:
    """

    sum = 0.0

    for n in range(accuracy):
        top = (-1)**n * pow(x, (2*n)+1)
        bottom = factorial((2*n)+1)
        sum += float(top) / float(bottom)
        
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
    print(sine(2*pi))