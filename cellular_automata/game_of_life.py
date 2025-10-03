"""Conway's Game Of Life, Author Anurag Kumar(mailto:anuragkumarak95@gmail.com)

Requirements:
  - numpy
  - random
  - time
  - matplotlib

Python:
  - 3.5

Usage:
  - $python3 game_of_life <canvas_size:int>

Game-Of-Life Rules:

 1.
 Any live cell with fewer than two live neighbours
 dies, as if caused by under-population.
 2.
 Any live cell with two or three live neighbours lives
 on to the next generation.
 3.
 Any live cell with more than three live neighbours
 dies, as if by over-population.
 4.
 Any dead cell with exactly three live neighbours be-
 comes a live cell, as if by reproduction.
"""

import random
import sys

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

usage_doc = "Usage of script: script_name <size_of_canvas:int>"

choice = [0] * 100 + [1] * 10
random.shuffle(choice)


def create_canvas(size: int) -> list[list[bool]]:
    """
    Create a square canvas of given size filled with False (dead cells).

    Args:
        size: The dimension of the square canvas

    Returns:
        A size x size 2D list of boolean values, all initialized to False

    >>> canvas = create_canvas(3)
    >>> len(canvas)
    3
    >>> len(canvas[0])
    3
    >>> all(all(not cell for cell in row) for row in canvas)
    True
    >>> create_canvas(1)
    [[False]]
    >>> create_canvas(0)
    []
    """
    canvas = [[False for i in range(size)] for j in range(size)]
    return canvas


def seed(canvas: list[list[bool]]) -> None:
    for i, row in enumerate(canvas):
        for j, _ in enumerate(row):
            canvas[i][j] = bool(random.getrandbits(1))


def run(canvas: list[list[bool]]) -> list[list[bool]]:
    """
    Run one generation of Conway's Game of Life on the canvas.

    Applies the Game of Life rules to all cells simultaneously to produce
    the next generation.

    Args:
        canvas: 2D list representing current state of cells

    Returns:
        2D list representing the next generation state

    >>> blinker = [[False, False, False, False, False],
    ...            [False, False, True, False, False],
    ...            [False, False, True, False, False],
    ...            [False, False, True, False, False],
    ...            [False, False, False, False, False]]
    >>> result = run(blinker)
    >>> result[2]
    [False, True, True, True, False]
    >>> run([[False, False, False], [False, False, False], [False, False, False]])
    [[False, False, False], [False, False, False], [False, False, False]]
    >>> block = [[False, False, False, False],
    ...          [False, True, True, False],
    ...          [False, True, True, False],
    ...          [False, False, False, False]]
    >>> run(block)[1]
    [False, True, True, False]
    """
    current_canvas = np.array(canvas)
    next_gen_canvas = np.array(create_canvas(current_canvas.shape[0]))
    for r, row in enumerate(current_canvas):
        for c, pt in enumerate(row):
            next_gen_canvas[r][c] = __judge_point(
                pt, current_canvas[r - 1 : r + 2, c - 1 : c + 2]
            )

    return next_gen_canvas.tolist()


def __judge_point(pt: bool, neighbours: list[list[bool]]) -> bool:
    """
    Apply Conway's Game of Life rules to determine the next state of a cell.

    Args:
        pt: Current state of the cell (True=alive, False=dead)
        neighbours: 3x3 grid including the cell and its 8 neighbors

    Returns:
        The next state of the cell

    Rules:
        1. Live cell with <2 live neighbours dies (under-population)
        2. Live cell with 2-3 live neighbours survives
        3. Live cell with >3 live neighbours dies (over-population)
        4. Dead cell with exactly 3 live neighbours becomes alive

    >>> __judge_point(
    ...     True, [[True, True, False], [False, True, False], [False, False, False]]
    ... )
    True
    >>> __judge_point(
    ...     True, [[True, False, False], [False, True, False], [False, False, False]]
    ... )
    False
    >>> __judge_point(
    ...     True, [[True, True, True], [True, True, False], [False, False, False]]
    ... )
    False
    >>> __judge_point(
    ...     False, [[True, True, False], [True, False, False], [False, False, False]]
    ... )
    True
    >>> __judge_point(
    ...     False, [[True, False, False], [False, False, False], [False, False, False]]
    ... )
    False
    """
    dead = 0
    alive = 0
    # finding dead or alive neighbours count.
    for i in neighbours:
        for status in i:
            if status:
                alive += 1
            else:
                dead += 1

    # handling duplicate entry for focus pt.
    if pt:
        alive -= 1
    else:
        dead -= 1

    # running the rules of game here.
    state = pt
    if pt:
        if alive < 2:
            state = False
        elif alive in {2, 3}:
            state = True
        elif alive > 3:
            state = False
    elif alive == 3:
        state = True

    return state


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception(usage_doc)

    canvas_size = int(sys.argv[1])
    # main working structure of this module.
    c = create_canvas(canvas_size)
    seed(c)
    fig, ax = plt.subplots()
    fig.show()
    cmap = ListedColormap(["w", "k"])
    try:
        while True:
            c = run(c)
            ax.matshow(c, cmap=cmap)
            fig.canvas.draw()
            ax.cla()
    except KeyboardInterrupt:
        # do nothing.
        pass
