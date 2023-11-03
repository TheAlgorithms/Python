from abc import ABC, abstractmethod


class Shape(ABC):

    """
    interface which represents a geometrical shape
    at a global level
    """

    @abstractmethod
    def is_similar(self, compared_shape):
        """
        a method for comparing with another shape,
        which also implements this interface
        """

    @abstractmethod
    def split(self):
        """
        a method for splitting a shape
        into a certain quantity of pieces,
        following a specific algorithm
        """

    """
	to do: create a factory method for creating a specific shape
	@abstractmethod
	def create_shape(self):
		pass"""
