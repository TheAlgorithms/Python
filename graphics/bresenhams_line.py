# https://en.wikipedia.org/wiki/Bresenham's_line_algorithm

from typing import Tuple, List, Any, Optional

#                (x,   y)
Vector2D = Tuple[int, int]
Vectors2D = List[Vector2D]


class BresenhamLine:
    """
    This implementation yields a list of 2-dimensional vectors, which can be used
    to plot a close approximation to a straight line between two points
    """

    def __init__(self, start_vec: Vector2D, end_vec: Vector2D) -> None:
        """
            start_vec: start vector of the line
            end_vec  : end   vector of the line

        >>> line = BresenhamLine((0, 0), (7, 5))
        >>> line.vectors
        [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 4), (7, 5)]

        >>> line.set_end_vec((7, 12))
        True

        >>> line.vectors
        [(0, 0), (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6), (4, 7), (5, 8), (5, 9), (6, 10), (6, 11), (7, 12)]

        >>> line.set_end_vec(100)
        Traceback (most recent call last):
        TypeError: "end_vec" must be an indexable type, not type <class 'int'>

        >>> line.set_start_vec((2, "a"))
        Traceback (most recent call last):
        ValueError: "start_vec" must contain two integers, not (2, 'a')
        """
        self.vectors: Vectors2D = []
        self.__start_vec: Vector2D = (0, 0)
        self.__end_vec: Vector2D = (0, 0)
        if self._validate_input(start_vec, end_vec):
            self._set_private_variables(start_vec, end_vec)
            self._append_line_vectors()

    @property
    def start_vec(self) -> Vector2D:
        return self.__start_vec

    def set_start_vec(self, new_start_vec: Vector2D) -> bool:
        """
            new_start_vec: new start vector of the line
        return true if new value is set and new line vectors appended

        >>> line = BresenhamLine((0, 0), (100, 100))
        >>> line.set_start_vec((42, 42))
        True

        >>> line.set_start_vec(42)
        Traceback (most recent call last):
        TypeError: "start_vec" must be an indexable type, not type <class 'int'>
        """
        var_set: bool = False
        if self._validate_input(new_start_vec, self.__end_vec):
            self._set_private_variables(start_vec=new_start_vec)
            var_set = True
        return self._append_line_vectors() and var_set

    @property
    def end_vec(self) -> Vector2D:
        return self.__end_vec

    def set_end_vec(self, new_end_vec: Vector2D) -> bool:
        """
            new_end_vec: new end vector of the line
        return true if new value is set and new line vectors appended

        >>> line = BresenhamLine((0, 0), (100, 100))
        >>> line.set_end_vec((50, 67))
        True

        >>> line.set_end_vec((50, "b"))
        Traceback (most recent call last):
        ValueError: "end_vec" must contain two integers, not (50, 'b')
        """
        var_set: bool = False
        if self._validate_input(self.__start_vec, new_end_vec):
            self._set_private_variables(end_vec=new_end_vec)
            var_set = True
        return self._append_line_vectors() and var_set

    def _append_line_vectors(self) -> bool:
        """
        Initiates the algorithm, by appending the first vector
        and by finding the deltas between the pair of x and y points

        returns true or false using the logic that the length of the final vector list
                must be equal to the highest delta of the x or y points, plus one
        
        >>> line = BresenhamLine((257, 211), (52, 58))
        >>> line._set_private_variables()

        >>> line._append_line_vectors()
        True

        >>> line.set_start_vec((100, 100))
        True

        >>> line._append_line_vectors()
        False
        """
        self.vectors.clear()
        self.vectors.append((self.__x0, self.__y0))
        self.vectors.extend(self._get_line_vectors())
        x_diff: int = abs(self.end_vec[0] - self.start_vec[0])
        y_diff: int = abs(self.end_vec[1] - self.start_vec[1])
        return (x_diff + 1 == len(self.vectors)) or (y_diff + 1 == len(self.vectors))

    def _get_line_vectors(self) -> Vectors2D:
        """
        return a list of vectors, not including the initial point, on the approximate line 

        >>> line = BresenhamLine((0, 0), (7, 5))
        >>> line._set_private_variables()

        >>> line._get_line_vectors()
        [(1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 4), (7, 5)]
        """
        line_vectors: Vectors2D = []
        decision: int
        if self.__delta_x >= self.__delta_y:
            decision = self.__delta_y - int(self.__delta_x / 2)
            while self.__x0 != self.__x1:
                if decision >= 0:
                    decision -= self.__delta_x
                    self.__y0 += self.__y_inc
                decision += self.__delta_y
                self.__x0 += self.__x_inc
                line_vectors.append((self.__x0, self.__y0))
        else:
            decision = self.__delta_x - int(self.__delta_y / 2)
            while self.__y0 != self.__y1:
                if decision >= 0:
                    decision -= self.__delta_y
                    self.__x0 += self.__x_inc
                decision += self.__delta_x
                self.__y0 += self.__y_inc
                line_vectors.append((self.__x0, self.__y0))
        return line_vectors

    def _validate_input(self, first_arg: Any, second_arg: Any) -> bool:
        """
            first_arg : first  argument of the BresenhamLine(first_arg, second_arg) call
            second_arg: second argument of the BresenhamLine(first_arg, second_arg) call
        return true if all tests are passed for both arguments, otherwise raise an exception

        >>> line = BresenhamLine((0, 0), (0, 0))

        >>> line._validate_input((50, 100), (350, 350))
        True

        >>> line._validate_input((50, 100), 100)
        Traceback (most recent call last):
        TypeError: "end_vec" must be an indexable type, not type <class 'int'>
        """
        if not is_indexable(first_arg):
            raise TypeError(
                f'"start_vec" must be an indexable type, not type {type(first_arg)}'
            )
        if not is_indexable(second_arg):
            raise TypeError(
                f'"end_vec" must be an indexable type, not type {type(second_arg)}'
            )
        if not is_int(first_arg[0]) or not is_int(first_arg[1]):
            raise ValueError(f'"start_vec" must contain two integers, not {first_arg}')
        if not is_int(second_arg[0]) or not is_int(second_arg[1]):
            raise ValueError(f'"end_vec" must contain two integers, not {second_arg}')
        return True

    def _set_private_variables(
        self, start_vec: Optional[Vector2D] = None, end_vec: Optional[Vector2D] = None
    ) -> None:
        """
        set private variables each time start or end vec is changed
        these variables are only for internal usage
        """
        if start_vec:
            self.__start_vec = start_vec
        if end_vec:
            self.__end_vec = end_vec
        self.__x0: int = int(self.start_vec[0])
        self.__y0: int = int(self.start_vec[1])
        self.__x1: int = int(self.end_vec[0])
        self.__y1: int = int(self.end_vec[1])
        self.__delta_x: int = self.__x1 - self.__x0
        self.__delta_y: int = self.__y1 - self.__y0
        self.__x_inc: int = int((self.__delta_x > 0) - (self.__delta_x < 0))
        self.__y_inc: int = int((self.__delta_y > 0) - (self.__delta_y < 0))
        self.__delta_x = abs(self.__delta_x) * 2
        self.__delta_y = abs(self.__delta_y) * 2


def is_indexable(arg: Any) -> bool:
    """
        arg     : the argument itself that should be tested
    return true if object is indexable with at least two items

    >>> is_indexable((10, 10))
    True

    >>> is_indexable(10)
    False
    """
    try:
        arg[0]
        arg[1]
    except TypeError:
        return False
    except IndexError:
        return False
    return True


def is_int(arg: Any) -> bool:
    """
        arg     : the argument itself that should be tested
    return true if object is or can be converted into an int

    >>> is_int((10, 10))
    False

    >>> is_int("10")
    True
    """
    try:
        int(arg)
    except TypeError:
        return False
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
