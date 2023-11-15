from geometry.angles.angle import Angle
from geometry.shapes.side import Side

from .polygon import Polygon


class Rectangle(Polygon):
    """
    a structure which represents a
    geometrical rectangle on a 2D surface

    >>> rectangle_one = Rectangle(5, 10)
    >>> rectangle_one.perimeter()
    30
    >>> rectangle_one.area()
    50
    >>> rectangle_one.is_similar(None)
    Traceback (most recent call last):
    NotImplementedError: Not Implemented
    >>> rectangle_one.split()
    Traceback (most recent call last):
    NotImplementedError: Not Implemented
    """

    def __init__(self, short_side_length: float, long_side_length: float) -> None:
        super().__init__()
        self.short_side = Side([], Angle(90), short_side_length)
        self.long_side = Side([], Angle(90), long_side_length)
        super().add_side(self.short_side)
        super().add_side(self.long_side)

    def perimeter(self) -> float:
        return (self.short_side.length + self.long_side.length) * 2

    def area(self) -> float:
        return self.short_side.length * self.long_side.length

    def is_similar(self, compared_shape: Polygon) -> bool:
        raise NotImplementedError("Not Implemented")

    def split(self) -> float:
        raise NotImplementedError("Not Implemented")
