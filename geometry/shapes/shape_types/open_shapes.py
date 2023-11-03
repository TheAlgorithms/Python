from abc import ABC, abstractmethod

from geometry.shapes.shape import Shape


class OpenShape(Shape, ABC):
    """
    an interface which represents shapes or figures
    with different starting and ending points [open shapes]
    more info: https://en.wikipedia.org/wiki/Polygon
    """

    @abstractmethod
    def is_similar(self, compared_shape):
        pass

    @abstractmethod
    def split(self):
        pass
