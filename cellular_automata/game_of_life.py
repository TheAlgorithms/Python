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

import doctest
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
    For creating a nested list of boolean values,
    based on the size parameter provided

    Args:
        size: integer

    Returns:
        A nested list of boolean values

    Examples:
        >>> create_canvas(1)
        [[False]]
        >>> create_canvas(2)
        [[False, False], [False, False]]
        >>> create_canvas(3)
        [[False, False, False], [False, False, False], [False, False, False]]
        >>> create_canvas(0)
        []
        >>> create_canvas(-1)
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
    This function runs the rules of game through all points, and changes their
    status accordingly.(in the same canvas)

    Args:
        canvas : canvas of population to run the rules on.

    Returns:
        canvas of population after one step

    Example #1:
        >>> canvas=[[False, False, False], [False, False, False], [False, False, False]]
        >>> run(canvas)
        [[False, False, False], [False, False, False], [False, False, False]]

    Example #2:
        >>> canvas=[[True, False, False], [True, False, False], [False, False, False]]
        >>> run(canvas)
        [[False, False, False], [False, False, False], [False, False, False]]

    Example #3:
        >>> canvas=[[True, True, True], [True, False, False], [False, False, False]]
        >>> run(canvas)
        [[False, False, False], [False, False, False], [False, False, False]]

    Example #4:
        >>> canvas=[[True, False, False], [False, False, True], [False, True, False]]
        >>> run(canvas)
        [[False, False, False], [False, True, False], [False, False, False]]

    Example #5:
        >>> canvas=[[True, True, True], [True, True, True], [True, True, True]]
        >>> run(canvas)
        [[False, False, False], [False, False, False], [False, False, True]]
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
    Update canvas provided

    Args:
        pt: boolean
        neighbours: canvas

    Returns:
        Updated canvas

    Example #1:
    Tests pt = True, and alive < 2; expected 'alive' count = 0
        >>> pt=True
        >>> canvas=[[False, False, False], [False, False, False], [False, False, False]]
        >>> __judge_point(pt, canvas)
        False

    Example #2:
    Tests pt = True, and alive < 2; expected 'alive' count = 1
        >>> pt=True
        >>> canvas=[[True, False, False], [True, False, False], [False, False, False]]
        >>> __judge_point(pt, canvas)
        False

    Example #3:
    Tests pt = True, and alive 'in' 2
        >>> pt=True
        >>> canvas=[[True, True, True], [False, False, False], [False, False, False]]
        >>> __judge_point(pt, canvas)
        True

    Example #4:
    Tests pt = True, and alive 'in' 3
        >>> pt=True
        >>> canvas=[[True, True, True], [True, False, False], [False, False, False]]
        >>> __judge_point(pt, canvas)
        True

    Example #5:
    Tests pt = True, and alive > 3; expected 'alive' count = 4
        >>> pt=True
        >>> canvas=[[True, True, True], [True, False, False], [False, False, True]]
        >>> __judge_point(pt, canvas)
        False

    Example #6:
    Tests pt = False, and alive == 3
        >>> pt=False
        >>> canvas=[[True, False, False], [False, False, True], [False, True, False]]
        >>> __judge_point(pt, canvas)
        True

    Example #7:
    Tests pt = False, and alive != 3; expected 'alive' count = 0
        >>> pt=False
        >>> canvas=[[False, False, False], [False, False, False], [False, False, False]]
        >>> __judge_point(pt, canvas)
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

    doctest.testmod()
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
