from abc import ABC, abstractmethod

from geometry.shapes.shape import Shape


class ClosedShape(Shape, ABC):
    """
    an interface which represents shapes
    that start and end at the same point [closed shape]
    more info: https://en.wikipedia.org/wiki/Polygon
    """

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def is_similar(self, compared_shape: Shape) -> bool:
        pass

    @abstractmethod
    def split(self) -> float:
        pass
