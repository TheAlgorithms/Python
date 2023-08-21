"""
Langton's ant

@ https://en.wikipedia.org/wiki/Langton%27s_ant
@ https://upload.wikimedia.org/wikipedia/commons/0/09/LangtonsAntAnimated.gif
"""

from functools import partial

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

WIDTH = 80
HEIGHT = 80


class LangtonsAnt:
    """
    Represents the main LangonsAnt algorithm.

    >>> la = LangtonsAnt(2, 2)
    >>> la.board
    [[True, True], [True, True]]
    >>> la.ant_position
    (1, 1)
    """

    def __init__(self, width: int, height: int) -> None:
        # Each square is either True or False where True is white and False is black
        self.board = [[True] * width for _ in range(height)]
        self.ant_position: tuple[int, int] = (width // 2, height // 2)

        # Initially pointing left (similar to the the wikipedia image)
        # (0 = 0° | 1 = 90° | 2 = 180 ° | 3 = 270°)
        self.ant_direction: int = 3

    def move_ant(self, axes: plt.Axes | None, display: bool, _frame: int) -> None:
        """
        Performs three tasks:
            1. The ant turns either clockwise or anti-clockwise according to the colour
            of the square that it is currently on. If the square is white, the ant
            turns clockwise, and if the square is black the ant turns anti-clockwise
            2. The ant moves one square in the direction that it is currently facing
            3. The square the ant was previously on is inverted (White -> Black and
            Black -> White)

        If display is True, the board will also be displayed on the axes

        >>> la = LangtonsAnt(2, 2)
        >>> la.move_ant(None, True, 0)
        >>> la.board
        [[True, True], [True, False]]
        >>> la.move_ant(None, True, 0)
        >>> la.board
        [[True, False], [True, False]]
        """
        directions = {
            0: (-1, 0),  # 0°
            1: (0, 1),  # 90°
            2: (1, 0),  # 180°
            3: (0, -1),  # 270°
        }
        x, y = self.ant_position

        # Turn clockwise or anti-clockwise according to colour of square
        if self.board[x][y] is True:
            # The square is white so turn 90° clockwise
            self.ant_direction = (self.ant_direction + 1) % 4
        else:
            # The square is black so turn 90° anti-clockwise
            self.ant_direction = (self.ant_direction - 1) % 4

        # Move ant
        move_x, move_y = directions[self.ant_direction]
        self.ant_position = (x + move_x, y + move_y)

        # Flip colour of square
        self.board[x][y] = not self.board[x][y]

        if display and axes:
            # Display the board on the axes
            axes.get_xaxis().set_ticks([])
            axes.get_yaxis().set_ticks([])
            axes.imshow(self.board, cmap="gray", interpolation="nearest")

    def display(self, frames: int = 100_000) -> None:
        """
        Displays the board without delay in a matplotlib plot
        to visually understand and track the ant.

        >>> _ = LangtonsAnt(WIDTH, HEIGHT)
        """
        fig, ax = plt.subplots()
        # Assign animation to a variable to prevent it from getting garbage collected
        self.animation = FuncAnimation(
            fig, partial(self.move_ant, ax, True), frames=frames, interval=1
        )
        plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    LangtonsAnt(WIDTH, HEIGHT).display()
