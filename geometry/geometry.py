from __future__ import annotations

import math
from dataclasses import dataclass, field
from types import NoneType
from typing import Self

# Building block classes


@dataclass
class Angle:
    """
    An Angle in degrees (unit of measurement)

    >>> Angle()
    Angle(degrees=90)
    >>> Angle(45.5)
    Angle(degrees=45.5)
    >>> Angle(-1)
    Traceback (most recent call last):
        ...
    TypeError: degrees must be a numeric value between 0 and 360.
    >>> Angle(361)
    Traceback (most recent call last):
        ...
    TypeError: degrees must be a numeric value between 0 and 360.
    """

    degrees: float = 90

    def __post_init__(self) -> None:
        if not isinstance(self.degrees, (int, float)) or not 0 <= self.degrees <= 360:
            raise TypeError("degrees must be a numeric value between 0 and 360.")

    def to_radians(self) -> float:
        """
        >>> Angle(90).to_radians()
        1.5707963267948966
        """
        return math.radians(self.degrees)

    @classmethod
    def from_radians(cls, radians: float) -> Angle:
        """
        >>> Angle.from_radians(math.pi / 2)
        Angle(degrees=90.0)
        """
        degrees = math.degrees(radians) % 360  # Normalize to 0-360
        return cls(degrees)


@dataclass
class Side:
    """
    A side of a two dimensional Shape such as Polygon, etc.
    adjacent_sides: a list of sides which are adjacent to the current side
    angle: the angle in degrees between each adjacent side
    length: the length of the current side in meters

    >>> Side(5)
    Side(length=5, angle=Angle(degrees=90), next_side=None)
    >>> Side(5, Angle(45.6))
    Side(length=5, angle=Angle(degrees=45.6), next_side=None)
    >>> Side(5, Angle(45.6), Side(1, Angle(2)))  # doctest: +ELLIPSIS
    Side(length=5, angle=Angle(degrees=45.6), next_side=Side(length=1, angle=Angle(d...
    >>> Side(-1)
    Traceback (most recent call last):
        ...
    TypeError: length must be a positive numeric value.
    >>> Side(5, None)
    Traceback (most recent call last):
        ...
    TypeError: angle must be an Angle object.
    >>> Side(5, Angle(90), "Invalid next_side")
    Traceback (most recent call last):
        ...
    TypeError: next_side must be a Side or None.
    """

    length: float
    angle: Angle = field(default_factory=Angle)
    next_side: Side | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.length, (int, float)) or self.length <= 0:
            raise TypeError("length must be a positive numeric value.")
        if not isinstance(self.angle, Angle):
            raise TypeError("angle must be an Angle object.")
        if not isinstance(self.next_side, (Side, NoneType)):
            raise TypeError("next_side must be a Side or None.")


@dataclass
class Ellipse:
    """
    A geometric Ellipse on a 2D surface

    >>> Ellipse(5, 10)
    Ellipse(major_radius=5, minor_radius=10)
    >>> Ellipse(5, 10) is Ellipse(5, 10)
    False
    >>> Ellipse(5, 10) == Ellipse(5, 10)
    True
    """

    major_radius: float
    minor_radius: float

    @property
    def area(self) -> float:
        """
        >>> Ellipse(5, 10).area
        157.07963267948966
        """
        return math.pi * self.major_radius * self.minor_radius

    @property
    def perimeter(self) -> float:
        """
        >>> round(Ellipse(5, 10).perimeter, 10)
        48.4422410807
        """
        a, b = max(self.major_radius, self.minor_radius), min(
            self.major_radius, self.minor_radius
        )
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return math.pi * (a + b) * (1 + 3 * h / (10 + math.sqrt(4 - 3 * h)))

    @property
    def eccentricity(self) -> float:
        """
        >>> Ellipse(5, 10).eccentricity
        0.8660254037844386
        >>> Circle(5).eccentricity
        0.0
        """
        a, b = max(self.major_radius, self.minor_radius), min(
            self.major_radius, self.minor_radius
        )
        return math.sqrt(1 - (b / a) ** 2)


class Circle(Ellipse):
    """
    A geometric Circle on a 2D surface

    >>> Circle(5)
    Circle(radius=5)
    >>> Circle(5) is Circle(5)
    False
    >>> Circle(5) == Circle(5)
    True
    >>> Circle(5).area
    78.53981633974483
    >>> Circle(5).perimeter
    31.41592653589793
    """

    def __init__(self, radius: float) -> None:
        super().__init__(radius, radius)
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"

    @property
    def diameter(self) -> float:
        """
        >>> Circle(5).diameter
        10
        """
        return self.radius * 2

    def max_parts(self, num_cuts: float) -> float:
        """
        Return the maximum number of parts that circle can be divided into if cut
        'num_cuts' times.

        >>> circle = Circle(5)
        >>> circle.max_parts(0)
        1.0
        >>> circle.max_parts(7)
        29.0
        >>> circle.max_parts(54)
        1486.0
        >>> circle.max_parts(22.5)
        265.375
        >>> circle.max_parts(-222)
        Traceback (most recent call last):
            ...
        TypeError: num_cuts must be a positive numeric value.
        >>> circle.max_parts("-222")
        Traceback (most recent call last):
            ...
        TypeError: num_cuts must be a positive numeric value.
        """
        if not isinstance(num_cuts, (int, float)) or num_cuts < 0:
            raise TypeError("num_cuts must be a positive numeric value.")
        return (num_cuts + 2 + num_cuts**2) * 0.5


@dataclass
class Polygon:
    """
    An abstract class which represents Polygon on a 2D surface.

    >>> Polygon()
    Polygon(sides=[])
    >>> polygon = Polygon()
    >>> polygon.add_side(Side(5)).get_side(0)
    Side(length=5, angle=Angle(degrees=90), next_side=None)
    >>> polygon.get_side(1)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> polygon.set_side(0, Side(10)).get_side(0)
    Side(length=10, angle=Angle(degrees=90), next_side=None)
    >>> polygon.set_side(1, Side(10))
    Traceback (most recent call last):
        ...
    IndexError: list assignment index out of range
    """

    sides: list[Side] = field(default_factory=list)

    def add_side(self, side: Side) -> Self:
        """
        >>> polygon = Polygon()
        >>> _ = polygon.add_side(Side(5, Angle(90)))
        >>> _ = polygon.add_side(Side(10, Angle(90)))
        >>> polygon.sides[0].next_side == polygon.sides[1]
        True
        """
        if self.sides:
            self.sides[-1].next_side = side
        self.sides.append(side)
        return self

    def get_side(self, index: int) -> Side:
        """
        >>> Polygon().get_side(0)
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        >>> Polygon().add_side(Side(5)).get_side(-1)
        Side(length=5, angle=Angle(degrees=90), next_side=None)
        """
        return self.sides[index]

    def set_side(self, index: int, side: Side) -> Self:
        """
        >>> Polygon().set_side(0, Side(5))
        Traceback (most recent call last):
            ...
        IndexError: list assignment index out of range
        >>> Polygon().add_side(Side(5)).set_side(0, Side(10))
        Polygon(sides=[Side(length=10, angle=Angle(degrees=90), next_side=None)])
        """
        self.sides[index] = side
        return self

    def get_vertices(self) -> list[tuple[float, float]]:
        """
        >>> rect = Rectangle(5, 10)
        >>> vertices = rect.get_vertices()
        >>> len(vertices)
        5
        >>> vertices[0]
        (0.0, 0.0)
        >>> vertices[1]
        (5.0, 0.0)
        """
        if not self.sides:
            return []
        vertices = [(0.0, 0.0)]
        x, y = 0.0, 0.0
        direction = 0.0  # Initial direction in radians

        for side in self.sides:
            x += side.length * math.cos(direction)
            y += side.length * math.sin(direction)
            vertices.append((x, y))
            # Turn by exterior angle (180 - interior)
            turn = math.pi - side.angle.to_radians()
            direction += turn

        # Check closure (tolerance for float precision)
        if (
            math.hypot(
                vertices[-1][0] - vertices[0][0], vertices[-1][1] - vertices[0][1]
            )
            > 1e-6
        ):
            raise ValueError("Polygon does not close back to starting point")
        return vertices

    def perimeter(self) -> float:
        """
        >>> Rectangle(5, 10).perimeter()
        30
        """
        return sum(side.length for side in self.sides)

    def area(self) -> float:
        """
        >>> Rectangle(5, 10).area()
        50
        """
        vertices = self.get_vertices()
        if len(vertices) < 3:
            return 0.0
        n = len(vertices)
        a = 0.0
        for i in range(n):
            j = (i + 1) % n
            a += vertices[i][0] * vertices[j][1]
            a -= vertices[j][0] * vertices[i][1]
        return abs(a) / 2.0


class Rectangle(Polygon):
    """
    A geometric rectangle on a 2D surface.

    >>> rectangle_one = Rectangle(5, 10)
    >>> rectangle_one.perimeter()
    30
    >>> rectangle_one.area()
    50
    >>> Rectangle(-5, 10)
    Traceback (most recent call last):
        ...
    TypeError: length must be a positive numeric value.
    """

    def __init__(self, short_side_length: float, long_side_length: float) -> None:
        super().__init__()
        self.short_side_length = short_side_length
        self.long_side_length = long_side_length
        self.post_init()

    def post_init(self) -> None:
        """
        >>> rect = Rectangle(5, 10)
        >>> len(rect.sides)
        4
        >>> rect.sides[0].length
        5
        """
        self.short_side = Side(self.short_side_length)
        self.long_side = Side(self.long_side_length)
        self.short_side_2 = Side(self.short_side_length)
        self.long_side_2 = Side(self.long_side_length)

        super().add_side(self.short_side)
        super().add_side(self.long_side)
        super().add_side(self.short_side_2)
        super().add_side(self.long_side_2)

    def perimeter(self) -> float:
        return (self.short_side.length + self.long_side.length) * 2

    def area(self) -> float:
        return self.short_side.length * self.long_side.length


@dataclass
class Square(Rectangle):
    """
    a structure which represents a
    geometrical square on a 2D surface
    >>> square_one = Square(5)
    >>> square_one.perimeter()
    20
    >>> square_one.area()
    25
    """

    def __init__(self, side_length: float) -> None:
        super().__init__(side_length, side_length)

    def perimeter(self) -> float:
        return super().perimeter()

    def area(self) -> float:
        return super().area()


class Triangle(Polygon):
    """
    A geometric triangle on a 2D surface.

    >>> tri = Triangle(3, 4, 5)
    >>> tri.perimeter()
    12
    >>> tri.area()
    6.0
    >>> Triangle(1, 2, 10)
    Traceback (most recent call last):
        ...
    ValueError: Sides must satisfy triangle inequality
    >>> Triangle(3, 4, 5, Angle(90), Angle(90), Angle(90))
    Traceback (most recent call last):
        ...
    ValueError: Triangle angles must sum to 180 degrees
    """

    def __init__(
        self,
        side_a: float,
        side_b: float,
        side_c: float,
        angle_a: Angle | None = None,
        angle_b: Angle | None = None,
        angle_c: Angle | None = None,
    ) -> None:
        super().__init__()

        # validate triangle inequality
        if not (
            side_a + side_b > side_c
            and side_a + side_c > side_b
            and side_b + side_c > side_a
        ):
            raise ValueError("Sides must satisfy triangle inequality")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        # calculate angles using cosines if not provided
        if angle_a is None:
            cos_a = (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
            angle_a = Angle.from_radians(math.acos(max(-1, min(1, cos_a))))

        if angle_b is None:
            cos_b = (side_a**2 + side_c**2 - side_b**2) / (2 * side_a * side_c)
            angle_b = Angle.from_radians(math.acos(max(-1, min(1, cos_b))))

        if angle_c is None:
            cos_c = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
            angle_c = Angle.from_radians(math.acos(max(-1, min(1, cos_c))))

        # validate angle sum
        angle_sum = angle_a.degrees + angle_b.degrees + angle_c.degrees
        if abs(angle_sum - 180) > 0.01:
            raise ValueError("Triangle angles must sum to 180 degrees")

        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c

        # add sides with their corresponding angles
        self.add_side(Side(side_a, angle_a))
        self.add_side(Side(side_b, angle_b))
        self.add_side(Side(side_c, angle_c))

    def perimeter(self) -> float:
        """
        >>> Triangle(3, 4, 5).perimeter()
        12
        """
        return self.side_a + self.side_b + self.side_c

    def area(self) -> float:
        """
        Calculate area using Heron's formula.

        >>> Triangle(3, 4, 5).area()
        6.0
        >>> round(Triangle(5, 5, 5).area(), 2)
        10.83
        """
        s = self.perimeter() / 2  # semi-perimeter
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return area


if __name__ == "__main__":
    __import__("doctest").testmod()
