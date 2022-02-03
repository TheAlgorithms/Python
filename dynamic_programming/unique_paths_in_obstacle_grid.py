from doctest import testmod
"""
We have a 2D grid with obstacles.
Starting form the top left corner we have to
find the no of unique paths to reach the bottom rightcorner
We can only move right or down
"""


def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    """
    >>> print(unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]))
    2
    >>> print(unique_paths_with_obstacles([[0,1],[0,0]]))
    1
    >>> print(unique_paths_with_obstacles([[0,1,0],[0,0,0],[0,0,1]]))
    0
    """

    # If the obstacle grid is not given as input
    if not obstacle_grid:
        return 0

    # If the starting tile is blocked there is no way to enter the grid
    if obstacle_grid[0][0] == 1:
        return 0

    rows = len(obstacle_grid)
    cols = len(obstacle_grid[0])

    # Creating a 2D list to memorise unique paths to a tile
    unique_paths = [[0 for col in range(cols)] for row in range(rows)]

    # There is only one way to reach the starting the tile
    unique_paths[0][0] = 1

    # Finding no of ways to reach all the tiles in top row
    for col in range(1, cols):
        if obstacle_grid[0][col] == 1:
            unique_paths[0][col] = 0
        else:
            unique_paths[0][col] = unique_paths[0][col - 1]

    # Finding no of ways to reach all the tiles in left most column
    for row in range(1, rows):
        if obstacle_grid[row][0] == 1:
            unique_paths[row][0] = 0
        else:
            unique_paths[row][0] = unique_paths[row - 1][0]

    # Calculating no of unique paths for rest of the tiles
    for row in range(1, rows):
        for col in range(1, cols):
            if obstacle_grid[row][col] == 1:
                unique_paths[row][col] = 0
            else:
                unique_paths[row][col] = (
                    unique_paths[row - 1][col] + unique_paths[row][col - 1]
                )

    return unique_paths[-1][-1]


if __name__ == "__main__":
    testmod(name="unique_paths_with_obstacles", verbose=True)
