from .rectangle import Rectangle


class Square(Rectangle):
    """
    a structure which represents a
    geometrical square on a 2D surface

    >>> square_one = Square(5)
    >>> square_one.perimeter()
    20
    >>> square_one.area()
    25
    >>> square_one.is_similar(None)
    Traceback (most recent call last):
    NotImplementedError: Not Implemented
    >>> square_one.split()
    Traceback (most recent call last):
    NotImplementedError: Not Implemented
    """

    def __init__(self, side_length: float) -> None:
        super().__init__(side_length, side_length)

    def perimeter(self) -> float:
        return super().perimeter()

    def area(self) -> float:
        return super().area()

    def is_similar(self, compared_shape: Rectangle) -> bool:
        raise NotImplementedError("Not Implemented")

    def split(self) -> float:
        raise NotImplementedError("Not Implemented")
