from __future__ import annotations


def solve_maze(maze: list[list[int]]) -> bool:
    """
    This method solves the "rat in maze" problem.
    In this problem, we have an n by n binary matrix where each
    cell in the matrix contains a value 0 or 1.
    In this matrix, 1 represents a valid path that can be
    followed to reach the end of the matrix,
    while 0 represents an obstacle.
    A path that the rat takes cannot include any cell that is an obstacle.
    The rat is allowed to move in 4 directions:
    UP, DOWN, LEFT, RIGHT.
    Given a starting point (0, 0) and an ending point (n-1, n-1),
    return True if it's possible for the rat to reach the ending point
    from the starting point or False otherwise.
    Parameters :
        maze(2D matrix) : maze
    Returns:
        Return: True if the maze has a solution or False if it does not.
        It also prints out the valid path from start to end with 1s
        representing the valid path
        if there’s a solution or “No solution exists!” if it does not.
    >>> maze = [[1, 0, 1, 0, 0],
    ...         [1, 1, 1, 1, 1],
    ...         [0, 1, 0, 1, 0],
    ...         [1, 1, 0, 1, 1],
    ...         [0, 1, 1, 0, 1]]
    >>> solve_maze(maze)
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 0, 1, 1]
    [0, 0, 0, 0, 1]
    True

    >>> maze = [[1, 0, 1, 0, 0],
    ...         [1, 1, 1, 1, 1],
    ...         [1, 1, 1, 1, 0],
    ...         [1, 1, 1, 1, 1],
    ...         [1, 1, 1, 1, 1]]
    >>> solve_maze(maze)
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]
    True

    >>> maze = [[1, 1, 1],
    ...         [1, 0, 1],
    ...         [0, 1, 1]]
    >>> solve_maze(maze)
    [1, 1, 1]
    [0, 0, 1]
    [0, 0, 1]
    True

    >>> maze = [[1, 0, 1],
    ...         [1, 0, 1],
    ...         [0, 1, 1]]
    >>> solve_maze(maze)
    No solution exists!
    False

    >>> maze = [[1, 0],
    ...         [0, 1]]
    >>> solve_maze(maze)
    No solution exists!
    False
    """
    size = len(maze)
    # We need to create solution object to save path.
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    solved = run_maze(maze, 0, 0, solutions)
    if solved:
        print("\n".join(str(row) for row in solutions))
    else:
        print("No solution exists!")
    return solved


def run_maze(maze: list[list[int]], i: int, j: int, solutions: list[list[int]]) -> bool:
    """
    This method is recursive starting from (i, j) and going in one of four directions:
    up, down, left, right.
    If a path is found to destination it returns True otherwise it returns False.
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

    lower_flag = (not i < 0) and (not j < 0)  # Check lower bounds
    upper_flag = (i < size) and (j < size)  # Check upper bounds

    if lower_flag and upper_flag:
        # check for already visited and block points.
        block_flag = (not solutions[i][j]) and maze[i][j] == 1
        if block_flag:
            # check visited
            solutions[i][j] = 1

            # check for directions
            if (
                run_maze(maze, i + 1, j, solutions)
                or run_maze(maze, i, j + 1, solutions)
                or run_maze(maze, i - 1, j, solutions)
                or run_maze(maze, i, j - 1, solutions)
            ):
                return True

            solutions[i][j] = 0
            return False
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
