"""
Given a n by n board where n is of form 2k where k >= 1 (Basically n is a power of 2 with minimum value as 2).
The board has one missing cell (of size 1 x 1). Fill the board using L shaped tiles.
A L shaped tile is a 2 x 2 square with one cell of size 1×1 missing.

This problem can be solved using Divide and Conquer. Below is the recursive algorithm.

// n is size of given square, p is location of missing cell
Tile(int n, Point p)

1) Base case: n = 2, A 2 x 2 square with one cell missing is nothing
   but a tile and can be filled with a single tile.

2) Place a L shaped tile at the center such that it does not cover
   the n/2 * n/2 subsquare that has a missing square. Now all four
   subsquares of size n/2 x n/2 have a missing cell (a cell that doesn't
   need to be filled).  See figure 2 below.

3) Solve the problem recursively for following four. Let p1, p2, p3 and
   p4 be positions of the 4 missing cells in 4 squares.
   a) Tile(n/2, p1)
   b) Tile(n/2, p2)
   c) Tile(n/2, p3)
   d) Tile(n/2, p3)

"""
import numpy as np

tile_count = 0


def place(grid: np.array, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> None:
    """
    place the L shaped tile in given three squares (x1, y1), (x2, y2), (x3, y3)
    """
    global tile_count
    tile_count += 1
    grid[x1][y1] = tile_count
    grid[x2][y2] = tile_count
    grid[x3][y3] = tile_count


def tile(grid: np.array, n: int, x: int, y: int) -> None:
    """
    n is size of given square, (x, y) is location of missing cell
    Tile(int n, int x, int y)

    1) Base case: n = 2, A 2 x 2 square with one cell missing is nothing
    but a tile and can be filled with a single tile.

    2) Place a L shaped tile at the center such that it does not cover
    the n/2 * n/2 subsquare that has a missing square. Now all four
    subsquares of size n/2 x n/2 have a missing cell (a cell that doesn't
    need to be filled).

    3) Solve the problem recursively for following four. Let p1, p2, p3 and
    p4 be positions of the 4 missing cells in 4 squares.
    a) Tile(n/2, p1)
    b) Tile(n/2, p2)
    c) Tile(n/2, p3)
    d) Tile(n/2, p3)
    """
    global tile_count
    r = 0
    c = 0

    # base case
    if n == 2:
        tile_count += 1
        for i in range(n):
            for j in range(n):
                if grid[x + i][y + j] == 0:
                    grid[x + i][y + j] = tile_count
        return 0

    # step 2
    for i in range(x, x + n):
        for j in range(y, y + n):
            if grid[i][j] != 0:
                r = i
                c = j

    if r < x + n / 2 and c < y + n / 2:
        place(
            grid,
            x + int(n / 2),
            y + int(n / 2) - 1,
            x + int(n / 2),
            y + int(n / 2),
            x + int(n / 2) - 1,
            y + int(n / 2),
        )

    elif r >= x + int(n / 2) and c < y + int(n / 2):
        place(
            grid,
            x + int(n / 2) - 1,
            y + int(n / 2),
            x + int(n / 2),
            y + int(n / 2),
            x + int(n / 2) - 1,
            y + int(n / 2) - 1,
        )

    elif r < x + int(n / 2) and c >= y + int(n / 2):
        place(
            grid,
            x + int(n / 2),
            y + int(n / 2) - 1,
            x + int(n / 2),
            y + int(n / 2),
            x + int(n / 2) - 1,
            y + int(n / 2) - 1,
        )

    elif r >= x + int(n / 2) and c >= y + int(n / 2):
        place(
            grid,
            x + int(n / 2) - 1,
            y + int(n / 2),
            x + int(n / 2),
            y + int(n / 2) - 1,
            x + int(n / 2) - 1,
            y + int(n / 2) - 1,
        )

    # step 3
    tile(grid, int(n / 2), x, y + int(n / 2))
    tile(grid, int(n / 2), x, y)
    tile(grid, int(n / 2), x + int(n / 2), y)
    tile(grid, int(n / 2), x + int(n / 2), y + int(n / 2))


def tiling(size_of_grid: int, missing_cell_x: int, missing_cell_y: int) -> np.array:
    """
    Runtime: O(len(input_string)*len(pattern))

    Arguments
    --------
    size_of_grid: int, any size of the grid
    missing_cell_x: int, x coordinate of the missing piece
    missing_cell_y: int, y coordinate of the missing piece

    Returns
    -------
    grid: the final grid

    Examples
    ---------
     >>> tiling(4, 0, 0)
     array([[-1.,  3.,  2.,  2.],
          [ 3.,  3.,  1.,  2.],
          [ 4.,  1.,  1.,  5.],
          [ 4.,  4.,  5.,  5.]])
     >>> tiling(4, 3, 3)
     array([[ 3.  3.  2.  2.]
        [ 3.  1.  1.  2.]
        [ 4.  1.  5.  5.]
        [ 4.  4.  5. -1.]])
     >>> tiling(2, 1, 1)
     array([[ 1.  1.]
        [ 1. -1.]])

    """
    grid = np.zeros((size_of_grid, size_of_grid))

    grid[missing_cell_x][missing_cell_y] = -1

    tile(grid, size_of_grid, 0, 0)

    return grid


if __name__ == "__main__":
    print(tiling(8, 0, 0))
