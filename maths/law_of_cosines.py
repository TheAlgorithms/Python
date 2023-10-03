# url: https://en.wikipedia.org/wiki/Law_of_cosines


import math

def law_of_cosines(a: float, b: float, angle_c: float) -> float:
    """
    Calculate the length of the third side of a triangle using the Law of Cosines.

    :param a: The length of side 'a' (float).
    :param b: The length of side 'b' (float).
    :param angle_c: The measure of angle 'C' in degrees (float).
    
    :return: The length of side 'c' (float).
    
    >>> law_of_cosines(5, 7, 60)
    5.830951894845301
    >>> law_of_cosines(3, 4, 90)
    5.0
    """
    # Convert the angle from degrees to radians
    angle_c_radians = math.radians(angle_c)
    
    # Use the Law of Cosines formula
    c_squared = a**2 + b**2 - 2 * a * b * math.cos(angle_c_radians)
    
    # Take the square root to find the length of side 'c'
    c = math.sqrt(c_squared)
    
    return c

if __name__ == "__main__":
    import doctest
    doctest.testmod()

