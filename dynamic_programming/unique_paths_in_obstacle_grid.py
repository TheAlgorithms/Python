from doctest import testmod
"""
We have a 2D grid with obstacles.
Starting form the top left corner we have to
find the no of unique paths to reach the bottom rightcorner
We can only move right or down
"""


def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    """
    >>> print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    2
    >>> print(uniquePathsWithObstacles([[0,1],[0,0]]))
    1
    >>> print(uniquePathsWithObstacles([[0,1,0],[0,0,0],[0,0,1]]))
    0
    """

    # If the obstacle grid is not given as input
    if not obstacleGrid:
        return 0

    # If the starting tile is blocked there is no way to enter the grid
    if obstacleGrid[0][0] == 1:
        return 0

    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])

    # Creating a 2D list to memorise unique paths to a tile
    uniquePaths = [[0 for col in range(cols)] for row in range(rows)]

    # There is only one way to reach the starting the tile
    uniquePaths[0][0] = 1

    # Finding no of ways to reach all the tiles in top row
    for col in range(1, cols):
        if obstacleGrid[0][col] == 1:
            uniquePaths[0][col] = 0
        else:
            uniquePaths[0][col] = uniquePaths[0][col - 1]

    # Finding no of ways to reach all the tiles in left most column
    for row in range(1, rows):
        if obstacleGrid[row][0] == 1:
            uniquePaths[row][0] = 0
        else:
            uniquePaths[row][0] = uniquePaths[row - 1][0]

    # Calculating no of unique paths for rest of the tiles
    for row in range(1, rows):
        for col in range(1, cols):
            if obstacleGrid[row][col] == 1:
                uniquePaths[row][col] = 0
            else:
                uniquePaths[row][col] = (
                    uniquePaths[row - 1][col] + uniquePaths[row][col - 1]
                )

    return uniquePaths[-1][-1]


if __name__ == "__main__":
    testmod(name="uniquePathsWithObstacles", verbose=True)
