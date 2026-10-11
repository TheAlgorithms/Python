import math
def volume_of_cylinder(radius: float, height: float) -> float:
    """
    Calculate the volume of a cylinder.
    Formula: pi * radius^2 * height
    Examples:
    >>> volume_of_cylinder(3.0, 5.0)
    141.37
    >>> volume_of_cylinder(2.5, 4.0)
    78.54
    >>> volume_of_cylinder(0.0, 5.0)
    0.0
    """
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    volume = math.pi * (radius ** 2) * height
    return round(volume, 2)
if __name__ == "__main__":
    import doctest
    doctest.testmod()