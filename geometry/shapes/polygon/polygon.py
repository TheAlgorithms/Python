from geometry.shapes.shape_types.closed_shapes import ClosedShape
from geometry.shapes.shape_types.intersecting_self_shapes import IntersectSelfShape
from geometry.shapes.side import Side
from typing import TypeVar

PolygonType = TypeVar("PolygonType", bound="Polygon")


class Polygon(ClosedShape, IntersectSelfShape):

    """
    an abstract class which represents a
    set of polygons on a 2D surface

    >>> from geometry.angles.angle import Angle
    >>> polygon_one = Polygon()
    >>> side_length = 15
    >>> angle_degrees = 60
    >>> side_one = Side([], Angle(angle_degrees), side_length)
    >>> side_two = Side([], Angle(angle_degrees), side_length)
    >>> side_three = Side([], Angle(angle_degrees), side_length)
    >>> side_one.adjacent_sides.append(side_two)
    >>> side_one.adjacent_sides.append(side_three)
    >>> side_two.adjacent_sides.append(side_three)
    >>> side_two.adjacent_sides.append(side_one)
    >>> side_three.adjacent_sides.append(side_one)
    >>> side_three.adjacent_sides.append(side_two)
    >>> polygon_one.add_side(side_one)
    >>> polygon_one.add_side(side_two)
    >>> polygon_one.add_side(side_three)
    >>> polygon_one.set_side(0, side_one)
    >>> polygon_one.set_side(1, side_two)
    >>> polygon_one.set_side(2, side_three)
    >>> side_one_data = polygon_one.get_side(0)
    >>> print(side_one_data.length)
    15
    >>> print(side_one_data.angle.degrees)
    60
    >>> polygon_one.area()

    >>> polygon_one.is_similar(None)

    >>> polygon_one.split()

    >>> polygon_one.perimeter()

    """

    def __init__(self) -> None:
        self.sides: list[Side] = []

    def get_side(self, index: int) -> Side:
        return self.sides[index]

    def set_side(self, index: int, side: Side) -> None:
        self.sides[index] = side

    def add_side(self, side: Side) -> None:
        self.sides.append(side)

    def area(self) -> float:
        pass

    def is_similar(self, compared_shape: PolygonType) -> bool:
        pass

    def perimeter(self) -> float:
        pass

    def split(self) -> float:
        pass
