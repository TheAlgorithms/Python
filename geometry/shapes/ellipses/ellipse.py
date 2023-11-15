import math

from geometry.shapes.shape_types.closed_shapes import ClosedShape


class Ellipse(ClosedShape):

    """
    a structure which represents a
    geometrical ellipse on a 2D surface

    >>> ellipse_one = Ellipse(5, 10)
    >>> ellipse_one.perimeter()
    47.12388980384689
    >>> ellipse_one.is_similar(None)
    Traceback (most recent call last):
    NotImplementedError: Not Implemented
    >>> ellipse_one.split()
    Traceback (most recent call last):
    NotImplementedError: Not Implemented
    """

    def __init__(self, major_radius: float, minor_radius: float) -> None:
        self.major_radius: float = major_radius
        self.minor_radius: float = minor_radius

    def perimeter(self) -> float:
        return math.pi * (self.major_radius + self.minor_radius)

    def area(self) -> float:
        return math.pi * self.major_radius * self.minor_radius

    def is_similar(self, compared_shape: ClosedShape) -> bool:
        raise NotImplementedError("Not Implemented")

    def split(self) -> float:
        raise NotImplementedError("Not Implemented")
