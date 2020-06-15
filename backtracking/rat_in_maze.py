def solve_maze(maze: list) -> bool:
    """
    This method solves rat in maze algorithm.
    In this problem we have n by n matrix and we have start point and end point
    we want to go from source to distination. In this matrix 0 are block paths
    1 are open paths we can use.
    Parameters :
        maze(2D matrix) : maze
    Returns:
        Return: True is maze has a solution or False if it does not.
    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [1, 0, 1, 0, 1],
    ...         [0, 0, 1, 0, 0],
    ...         [1, 0, 0, 1, 0]]
    >>> solve_maze(maze)
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 0, 1, 1]
    [0, 0, 0, 0, 1]
    True

    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 0, 0, 0, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 0, 0, 0, 0]]
    >>> solve_maze(maze)
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]
    True

    >>> maze = [[0, 0, 0],
    ...         [0, 1, 0],
    ...         [1, 0, 0]]
    >>> solve_maze(maze)
    [1, 1, 1]
    [0, 0, 1]
    [0, 0, 1]
    True

    >>> maze = [[0, 1, 0],
    ...         [0, 1, 0],
    ...         [1, 0, 0]]
    >>> solve_maze(maze)
    Solution does not exists!
    False

    >>> maze = [[0, 1],
    ...         [1, 0]]
    >>> solve_maze(maze)
    Solution does not exists!
    False
    """
    size = len(maze)
    # We need to create solution object to save path.
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    solved = run_maze(maze, 0, 0, solutions)
    if solved:
        print("\n".join(str(row) for row in solutions))
    else:
        print("Solution does not exists!")
    return solved


def run_maze(maze, i, j, solutions):
    """
    This method is recursive method which starts from i and j
    and goes with 4 direction option up, down, left, right
    if path found to destination it breaks and return True
    otherwise False
    Parameters:
        maze(2D matrix) : maze
        i, j : coordinates of matrix
        solutions(2D matrix) : solutions
    Returns:
        Boolean if path is found True, Otherwise False.
    """
    size = len(maze)
    # Final check point.
    if i == j == (size - 1):
        solutions[i][j] = 1
        return True

    lower_flag = (not (i < 0)) and (not (j < 0))  # Check lower bounds
    upper_flag = (i < size) and (j < size)  # Check upper bounds

    if lower_flag and upper_flag:
        # check for already visited and block points.
        block_flag = (not (solutions[i][j])) and (not (maze[i][j]))
        if block_flag:
            # check visited
            solutions[i][j] = 1

            # check for directions
            if (run_maze(maze, i + 1, j, solutions) or
                run_maze(maze, i, j + 1, solutions) or
                run_maze(maze, i - 1, j, solutions) or
                run_maze(maze, i, j - 1, solutions)):
                return True

            solutions[i][j] = 0
            return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
