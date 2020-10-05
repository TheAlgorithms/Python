import math

def hypotenuse(side1:float, side2:float):
    """
    Calculating the hypotenuse of a right triangle using Pythagorean Theorem

    https://en.wikipedia.org/wiki/Pythagorean_theorem

    Arguments:
    side1 - one of the co-sides of the right angle (or the side a as if it is in like the wikipedia page)
    side2 - other one of the co-sides of the right angle (or the side b as if it is in like the wikipedia page)

    returns the hypotenuse of the triangle with the given side lengths

    side lenghts must be positive so the module converts it to positive automatially
    
    examples:
    >>> hypotenuse(3, 4)
    ...     5.0
    >>> hypotenuse(12, -5)
    ...     13.0
    >>> hypotenuse(-6, -8)
    ...     10.0
    """
    a = abs(side1)
    b = abs(side2)
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    