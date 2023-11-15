from abc import ABC, abstractmethod
from typing import TypeVar

ShapeType = TypeVar("ShapeType", bound="Shape")


class Shape(ABC):

    """
    interface which represents a geometrical shape
    at a global level
    """

    @abstractmethod
    def is_similar(self, compared_shape: ShapeType) -> bool:
        """
        a method for comparing with another shape,
        which also implements this interface
        """

    @abstractmethod
    def split(self) -> float:
        """
        a method for splitting a shape
        into a certain quantity of pieces,
        following a specific algorithm which returns
        the amount of pieces after splitting the shape

        note: in the future, a separate class might be created,
        which will represent a certain part of a shape, because of that
        the return type of this method might change
        """

    """
	to do: create a factory method for creating a specific shape
	@abstractmethod
	def create_shape(self):
		pass"""
