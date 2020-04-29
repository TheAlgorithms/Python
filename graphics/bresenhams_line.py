# https://en.wikipedia.org/wiki/Bresenham's_line_algorithm

from typing import Tuple, List, Callable, Optional

#                (x,   y)
Vector2D  = Tuple[int, int]
Vectors2D = List[Vector2D]

# returns 1 or -1, value is used to increment 
# x by 1 (right) or -1 (left)
# y by 1 (down) or  -1 (up)
get_increment_value: Callable[[int], int] = lambda delta: int((delta > 0) - (delta < 0))

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
        >>> line.end_vec
        (7, 5)
        >>> line.end_vec = (7, 12)
        >>> line.vectors
        [(0, 0), (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6), (4, 7), (5, 8), (5, 9), (6, 10), (6, 11), (7, 12)]
        """
        # list to hold all vectors on the line
        self.vectors:     Vectors2D = []
        # initial start and end vectors
        self.__start_vec: Vector2D  = start_vec
        self.__end_vec:   Vector2D  = end_vec
        self.__set_private_variables()
        # initiate the algorithm
        self.__append_line_vectors()

    # recalculate the vectors on the line each time
    # start_vec or end_vec is changed
    
    @property
    def start_vec(self) -> Vector2D:
        return self.__start_vec
    @start_vec.setter
    def start_vec(self, new_start_vec: Vector2D) -> None:
        self.__start_vec = new_start_vec
        self.__set_private_variables()
        self.vectors.clear()
        self.__append_line_vectors()

    @property
    def end_vec(self) -> Vector2D:
        return self.__end_vec
    @end_vec.setter
    def end_vec(self, new_end_vec: Vector2D) -> None:
        self.__end_vec = new_end_vec
        self.__set_private_variables()
        self.vectors.clear()
        self.__append_line_vectors()
    
    def __set_private_variables(self) -> None:
        """
        sets private variables each time start or end vec is changed
        these variables are only used internally
        """
        self.__x0:      int       = self.start_vec[0]
        self.__y0:      int       = self.start_vec[1]
        self.__x1:      int       = self.end_vec[0]
        self.__y1:      int       = self.end_vec[1]
        self.__delta_x: int       = self.__x1 - self.__x0
        self.__delta_y: int       = self.__y1 - self.__y0
        self.__x_inc:   int       = get_increment_value(self.__delta_x)
        self.__y_inc:   int       = get_increment_value(self.__delta_y)

        self.__delta_x = abs(self.__delta_x) * 2
        self.__delta_y = abs(self.__delta_y) * 2

    def __append_line_vectors(self) -> None:
        """
        initiates the algorithm, by appending the first vector
        and finding the appropiate axis to follow
        decision variable is used to decide to either append the 
        lower bound or the upper bound pixel on the approximate line
        """
        self.vectors.append((self.__x0, self.__y0))
        decision: int
        if (self.__delta_x >= self.__delta_y):
            decision = self.__delta_y - int(self.__delta_x / 2)
            self.__move_along_x(decision)
        else:
            decision = self.__delta_x - int(self.__delta_y / 2)
            self.__move_along_y(decision)

    def __move_along_x(self, decision: int) -> None:
        while (self.__x0 != self.__x1):
            if (decision >= 0):
                decision -= self.__delta_x
                self.__y0 += self.__y_inc
            decision += self.__delta_y
            self.__x0 += self.__x_inc
            self.vectors.append((self.__x0, self.__y0))

    def __move_along_y(self, decision: int) -> None:
        while (self.__y0 != self.__y1):
            if (decision >= 0):
                decision -= self.__delta_y
                self.__x0 += self.__x_inc
            decision += self.__delta_x
            self.__y0 += self.__y_inc
            self.vectors.append((self.__x0, self.__y0))

if __name__ == "__main__":
    import doctest
    doctest.testmod()