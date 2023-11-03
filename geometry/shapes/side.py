from dataclasses import dataclass

from geometry.angles.angle import Angle


@dataclass
class Side:

    """
    represents a side of a shape [such as polygon, e.t.c.]
    adjacent_sides: a list of sides which are adjacent to the current side
    angle: the angle between adjacent sides
    """

    adjacent_sides: list[float]
    angle: Angle
    length: float
