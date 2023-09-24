from __future__ import annotations


def solve_maze(maze: list[list[int]]) -> bool:
    """
    This method solves the "rat in maze" problem.
    Parameters :
        maze(2D matrix) : maze
    Returns:
        Return: True if the maze has a solution or False if it does not.
    Description:
        This method navigates through a maze represented as an n by n matrix,
        starting from a specified source cell (default: top-left corner) and 
        aiming to reach a destination cell (default: bottom-right corner).
        The maze consists of walls (0s) and open paths (1s).
        By providing custom row and column values, the source and destination cells can be adjusted.
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

    Note:
        In the output maze, the ones (1s) represent one of the possible
        paths from the source to the destination.

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
    No solution exists!
    False

    >>> maze = [[0, 1],
    ...         [1, 0]]
    >>> solve_maze(maze)
    No solution exists!
    False
    """
    # We need to create solution object to save path.
    size = len(maze)
    source_row=0
    source_column=0
    destination_row=size-1
    destination_column=size-1
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    solved = run_maze(maze, source_row, source_column,destination_row,
                      destination_column, solutions)
    if solved:
        print("\n".join(str(row) for row in solutions))
    else:
        print("No solution exists!")
    return solved


def run_maze(maze: list[list[int]], i: int, j: int,destination_row:int,
             destination_column:int, solutions: list[list[int]]) -> bool:
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
    if i == destination_row and  j == destination_column:
        solutions[i][j] = 1
        return True

    lower_flag = (not i < 0) and (not j < 0)  # Check lower bounds
    upper_flag = (i < size) and (j < size)  # Check upper bounds

    if lower_flag and upper_flag:
        # check for already visited and block points.
        block_flag = (not solutions[i][j]) and (not maze[i][j])
        if block_flag:
            # check visited
            solutions[i][j] = 1

            # check for directions
            if (
                run_maze(maze, i + 1, j,destination_row,
                            destination_column, solutions)
                or run_maze(maze, i, j + 1,destination_row,
                            destination_column, solutions)
                or run_maze(maze, i - 1, j,destination_row,
                            destination_column, solutions)
                or run_maze(maze, i, j - 1,destination_row,
                            destination_column, solutions)
            ):
                return True

            solutions[i][j] = 0
            return False
    return False



if __name__ == "__main__":
    import doctest

    doctest.testmod()
