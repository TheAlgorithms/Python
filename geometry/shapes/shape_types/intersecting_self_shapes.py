from abc import ABC, abstractmethod

from geometry.shapes.shape import Shape


class IntersectSelfShape(Shape, ABC):
    """
    an interface which represents polygons
    some of whose edges cross each other [self intersecting shapes]
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
