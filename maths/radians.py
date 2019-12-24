from math import pi
'''

Coverts the given angle from degrees to radians
https://en.wikipedia.org/wiki/Radian
'''
def radians(degree):

    """
    >>> radians(180)
    3.141592653589793
    >>> radians(92)
    1.6057029118347832
    >>> radians(274)
    4.782202150464463
    """

    return degree / (180/pi)


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    