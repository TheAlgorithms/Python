def fill_matrix(matrix, i, j):
    """
    This method just fills matrix i, j with value
    Parameters :
        matrix(2D matrix) : matrix
        i, j : coordinates of the matrix.
    """
    matrix[i][j] = 1


def solveMaze(maze):
    """
    This method solves rat in maze algorithm.
    In this problem we have n by n matrix and we have start point and end point
    we want to go from source to distination. In this matrix 0 are block paths
    1 are open paths we can use.
    Parameters :
        maze(2D matrix) : maze
        size : size of our maze(square)
    Returns:
        This method returns true and array if solution found otherwise false and None

    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [1, 0, 1, 0, 1],
    ...         [0, 0, 1, 0, 0],
    ...         [1, 0, 0, 1, 0]]
    >>> solveMaze(maze)
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 0, 1, 1]
    [0, 0, 0, 0, 1]

    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 0, 0, 0, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 0, 0, 0, 0]]
    >>> solveMaze(maze)
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]

    >>> maze = [[0, 0, 0],
    ...         [0, 1, 0],
    ...         [1, 0, 0]]
    >>> solveMaze(maze)
    [1, 1, 1]
    [0, 0, 1]
    [0, 0, 1]

    >>> maze = [[0, 1, 0],
    ...         [0, 1, 0],
    ...         [1, 0, 0]]
    >>> solveMaze(maze)
    Solution does not exists!

    >>> maze = [[0, 1],
    ...         [1, 0]]
    >>> solveMaze(maze)
    Solution does not exists!
    """
    size = len(maze)
    # We need to create solution object to save path.
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    solved = runmaze(maze, 0, 0, solutions)

    if solved:
        result = "".join(str(row) + "\n" for row in solutions)
        print(result[: len(result) - 1])  # For last \n
    else:
        print("Solution does not exists!")


"""
This method is recursive method which starts from i and j
and goes with 4 direction option up, down, left, right
if path found to destination it breaks and return True
otherwise False
Parameters:
    maze(2D matrix) : maze
    size : size of our maze(square)
    i, j : coordinates of matrix
    solutions(2D matrix) : solutions
Returns:
    Boolean if path is found True, Otherwise False.

    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [1, 0, 1, 0, 1],
    ...         [0, 0, 1, 0, 0],
    ...         [1, 0, 0, 1, 0]]
    >>> solveMaze(maze)
    True

    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 0, 0, 0, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 0, 0, 0, 0]]
    >>> solveMaze(maze)
    True

    >>> maze = [[0, 0, 0],
    ...         [0, 1, 0],
    ...         [1, 0, 0]]
    >>> solveMaze(maze)
    True

    >>> maze = [[0, 1, 0],
    ...         [0, 1, 0],
    ...         [1, 0, 0]]
    >>> solveMaze(maze)
    False

    >>> maze = [[0, 1],
    ...         [1, 0]]
    >>> solveMaze(maze)
    False
"""


def runmaze(maze, i, j, solutions):
    size = len(maze)
    # Final check point.
    if (i == (size - 1)) and (j == (size - 1)):
        fill_matrix(solutions, i, j)
        return True

    lower_flag = (not (i < 0)) and (not (j < 0))  # Check lower bounds
    upper_flag = (i < size) and (j < size)  # Check upper bounds

    if lower_flag and upper_flag:
        # check for already visited and block points.
        block_flag = (not (solutions[i][j])) and (not (maze[i][j]))
        if block_flag:
            # check visited
            fill_matrix(solutions, i, j)

            # check for directions
            if runmaze(maze, i + 1, j, solutions):
                return True

            if runmaze(maze, i, j + 1, solutions):
                return True

            if runmaze(maze, i - 1, j, solutions):
                return True

            if runmaze(maze, i, j - 1, solutions):
                return True

            solutions[i][j] = 0
            return False


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
