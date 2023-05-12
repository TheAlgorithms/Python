"""
Animating Conway's Game of Life on Python

For more information, see:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
https://conwaylife.com/wiki/

Usage:
  - $python3 gol.py <url:str>
  - $python3 gol.py <grid_size:int>
"""


import re
import sys

import matplotlib as mlb
import matplotlib.pyplot as plt
import numpy as np
import requests
from matplotlib.animation import FuncAnimation


def update(_: int, img: mlb.image.AxesImage, grid: np.ndarray) -> mlb.image.AxesImage:
    """
    The core "algorithm" of the code

    :param _: The frame number (unused)
    :param img:
    :param grid:
    """
    # Avoid interim changes that affect the outcome
    new_grid = grid.copy()
    rows, cols = grid.shape

    # Apply rules to all cells expect those on the margins
    for i in range(rows):
        for j in range(cols):
            # Use % (modulus operator) to make indices wrap around
            xr = np.r_[i - 1 : i + 2] % rows
            xc = np.r_[j - 1 : j + 2] % cols
            alive_neighbors = int(
                np.sum(grid[np.ix_(xr, xc)]) - grid[i][j]
            )  # Sum of the 8 cells surrounding it

            # 3 alive neighbors cause dead cells to become alive
            if not grid[i][j] and alive_neighbors == 3:
                new_grid[i][j] = 1

            # Alive cells with too many or too few neighbors die
            elif grid[i][j] and alive_neighbors not in (2, 3):
                new_grid[i][j] = 0
    grid[:] = new_grid[:]

    img.set_data(grid)
    return img


def parse_grid_url(target_url: str) -> np.ndarray:
    """
    Get text file online via url. Parse into 2D np.ndarray.

    Works for text files with "." as a 0 and "O" as a 1, ie
    those found on conwaylife.com/wiki/
    """
    response = requests.get(target_url)
    data = response.text

    # Find where the data starts and get data
    idx = min([data.find(i) for i in ["..", "O.", ".O", "OO"]])
    new = data[idx:].split()

    cols = len(new[0])
    rows = len(new)

    binary = {".": 0, "O": 1}
    grid = np.zeros((rows, cols))
    for i, j in enumerate(new):
        grid[i] = [binary[k] for k in j]

    return grid


def main() -> None:
    # Input is given
    if len(sys.argv) == 2:
        cli_arg = sys.argv[1]
    else:
        # Default URL
        cli_arg = "https://conwaylife.com/patterns/31p3onmerzenichsp64.cells"

    # If input is integer, create a randomly populated numpy grid of input size
    if match := re.match("^[0-9]+$", cli_arg):
        size = int(match[0])

        # Create a matrix of dims (size-2)x(size-2) randomly filled with bool values
        grid = np.random.randint(2, size=(size - 2, size - 2))

    # Interpret it as a URL
    else:
        grid = parse_grid_url(cli_arg)

    # Avoid IndexError by zero-padding twice
    grid = np.pad(grid, 2, mode="constant")

    fig, ax = plt.subplots()

    # Change interpolation to "nearest" to get rid of bluriness
    img = ax.imshow(grid, interpolation="lanczos", cmap="Greys")
    print(type(img))
    _anim = FuncAnimation(
        fig,
        update,
        fargs=(
            img,
            grid,
        ),
        frames=20,
        interval=50,
    )

    plt.show()


if __name__ == "__main__":
    main()
