""" The radian is the standard unit of angular measure, used in many areas of mathematics. An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle; one radian is just under 57.3 degrees (when the arc length is equal to the radius). """


def degree_to_radian(degree: int, ndigits: int = 2) -> float:
    """
    Convert a given value from degree to radian and round it to 2 decimal places.
    >>> degree_to_radian(90, 3)
    1.571
    >>> degree_to_radian(23, 2)
    0.40
    >>> degree_to_radian("degree")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to int: 'degree'
    """
    pi=22/7
    return round(degree*(pi/180), ndigits)



if __name__ == "__main__":

    import doctest

    doctest.testmod()
