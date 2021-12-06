"""
The 6 normal trig functions and their inverses. In theory, I could 
have used a CORDIC algorithm https://en.wikipedia.org/wiki/CORDIC
but this requires a load of pre-calculated values stored in some
list. In keeping with the spirit of what this repository aims to
achieve, I decided to use a taylor series expansion so that everything
is clear

Note also that we only need to create a maclaurin expansion for sin(x)
and cos(x). Using trig identities, we can bootstrap our way into the 
other 4 trignometric functions.
https://en.wikipedia.org/wiki/List_of_trigonometric_identities
"""
from math import copysign, log, pi

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
    
    # Sometimes when we shift the angle around a lot we get a negative 
    # result and things break down a bit if that's the case
    if x < 0:
        x *= -1

    # This summation is supposed to be infinite but computers are 
    # discrete systems. Note that with 85 iterations, this accurately 
    # computes sin to a degree that is useful for most applications
    for n in range(accuracy):
        numerator = (-1)**n * pow(x, (2*n)+1)
        denominator = factorial((2*n)+1)
        sum += float(numerator) / float(denominator)

    # Because of the way this taylor seriees works, we sometimes 
    # get numbers so small that they are practically 0 (instead of 0)
    if sum < 1E-15:
        sum = 0.0

    return sum

def cosine(
    x: float,
    accuracy: int = 85
) -> float:
    """
    Algorithm used: taylor series
    https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    Doctests:
    """

    # Value to be returned
    sum = 0.0
    
    # Because of the way this taylor series works, we need 
    # to flip the sign after the sum has been computed
    is_negative = False

    # Python imposed limitation
    if accuracy > 85:
        accuracy = 85
    
    # We can reduce our range of angles to just 
    # be from [0, 2pi] because trig functions are periodic
    x = x%(2*pi)

    # If our intial angle is in the second or third 
    # quadrant, mark the answer as negative
    if x <= pi and x > (pi/2):
        is_negative = True

    # We can further reduce our range of inputs to just [0, pi]
    if x > (pi) and pi < (2*pi):
        # Move the value to the equivalent value in [0, pi]
        x -= pi

    # And we can once again reduce the range of inputs to [0, pi/2]
    if x >= (pi/2):
        # Move the angle to it's equivelent angle in [0, pi/2]
        x = pi-x
    
    # This summation is supposed to be infinite but computers are 
    # discrete systems. Note that with 85 iterations, this accurately 
    # computes cosine to a degree that is useful for most applications. 
    # Note also that the first term of this series will always be one. 
    # This causes a problem with changing the sign of the output. We 
    # will need to use a flag for that instead
    for n in range(accuracy):
        numerator = (-1)**n * pow(x, (2*n))
        denominator = factorial(2*n)
        sum += float(numerator) / float(denominator)

    # Because of the way this taylor seriees works, we sometimes 
    # get numbers so small that they are practically 0 (instead of 0)
    if sum < 1E-15:
        sum = 0.0
    
    # Flag for flipping the sign
    if is_negative:
        sum *= -1
    
    return sum

def tangent(x: float) -> float:
    """
    Algorithm used: trignometric identity
    https://en.wikipedia.org/wiki/List_of_trigonometric_identities

    Doctests:
    """

    # There are a handful of angles where tan(x) is undefined 
    # and we need to approriately handle that.
    try:
        return sine(x)/cosine(x)
    except ZeroDivisionError:
        pass

def cosecant(x: float) -> float:
    """
    Algorithm used: The definition of cosecant is 1/sin(x)

    Doctests:
    """

    # Note that csc(x) is undefined when sin(x) = 0
    try:
        return 1/sine(x)
    except ZeroDivisionError:
        pass

def secant(
    x: float,
    accuracy: int = 100
) -> float:
    """
    Algorithm used: The definition of secant is 1/cos(x)

    Doctests:
    """

    # Note that sec(x) is undefinde when cos(x) = 0
    try:
        return 1/cosine(x)
    except ZeroDivisionError:
        pass

def cotangent(x: float) -> float:
    """
    Algorithm used: The defintion of cotangent is 1/tan(x)

    Doctests:
    """
    try:
        return 1/tangent(x)
    except ZeroDivisionError:
        pass

if __name__ == "__main__":

    # Test every 30 degrees

    counter = 0
    angle = 0.0
    while counter < 12:
        
        # Test each trig function at a variety of angles
        print(f"sin({angle}) = {sine(angle)}")
        print(f"cos({angle}) = {cosine(angle)}")
        print(f"tan({angle}) = {tangent(angle)}")
        print(f"cosecant({angle}) = {cosecant(angle)}")
        print(f"secant({angle}) = {secant(angle)}")
        print(f"cotangent({angle}) = {cotangent(angle)}\n")

        angle += (pi/3)
        counter+=1