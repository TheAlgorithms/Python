import math

from geometry.shapes.shape_types.closed_shapes import ClosedShape


class Circle(ClosedShape):

    """
    a structure which represents a
    geometrical circle on a 2D surface

    >>> circle_one = Circle(5)
    >>> circle_one.get_diameter()
    10
    >>> circle_one.perimeter()
    31.41592653589793
    >>> circle_one.is_similar(None)
    Traceback (most recent call last):
    NotImplementedError: Not Implemented
    >>> circle_one.split()
    Traceback (most recent call last):
    NotImplementedError: Not Implemented
    >>> circle_one.max_parts(54)
    1486.0
    >>> circle_one.max_parts(7)
    29.0
    >>> circle_one.max_parts(22.5)
    265.375
    >>> circle_one.max_parts(-222)
    -1
    >>> circle_one.max_parts("-222")
    Traceback (most recent call last):
    TypeError: num_cuts must be a numeric value.
    """

    def __init__(self, radius: float) -> None:
        self.radius = radius
        self.origin = 0

    def get_diameter(self) -> float:
        return self.radius * 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * (self.radius**2)

    def is_similar(self, compared_shape: ClosedShape) -> bool:
        raise NotImplementedError("Not Implemented")

    def split(self) -> float:
        raise NotImplementedError("Not Implemented")

    def max_parts(self, num_cuts: float) -> float:
        """
        returns the maximum amount of
        parts a circle can be divided
        by if cut 'num_cuts' times
        """

        if not isinstance(num_cuts, (int, float)):
            raise TypeError("num_cuts must be a numeric value.")
        return ((num_cuts + 2 + num_cuts**2) * 0.5) if num_cuts >= 0 else -1
