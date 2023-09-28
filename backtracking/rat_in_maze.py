from __future__ import annotations


def solve_maze(
    maze: list[list[int]],
    source_row: int,
    source_column: int,
    destination_row: int,
    destination_column: int,
) -> bool:
    """
        This method solves the "rat in maze" problem.
        Parameters :
            - maze(2D matrix) : maze
            - source_row (int): The row index of the starting point.
            - source_column (int): The column index of the starting point.
            - destination_row (int): The row index of the destination point.
            - destination_column (int): The column index of the destination point.
        Returns:
            Return: True if the maze has a solution or False if it does not.
        Description:
            This method navigates through a maze represented as an n by n matrix,
    <<<<<<< HEAD
            starting from a specified source cell  and
            aiming to reach a destination cell.
    =======
            starting from a specified source cell (default: top-left corner) and
            aiming to reach a destination cell (default: bottom-right corner).
    >>>>>>> origin/new_branch
            The maze consists of walls (1s) and open paths (0s).
            By providing custom row and column values, the source and destination
            cells can be adjusted.
        >>> maze = [[0, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0],
        ...         [1, 0, 1, 0, 1],
        ...         [0, 0, 1, 0, 0],
        ...         [1, 0, 0, 1, 0]]
        >>> solve_maze(maze,0,0,len(maze)-1,len(maze)-1)
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
        >>> solve_maze(maze,0,0,len(maze)-1,len(maze)-1)
        [1, 0, 0, 0, 0]
        [1, 0, 0, 0, 0]
        [1, 0, 0, 0, 0]
        [1, 0, 0, 0, 0]
        [1, 1, 1, 1, 1]
        True

        >>> maze = [[0, 0, 0],
        ...         [0, 1, 0],
        ...         [1, 0, 0]]
        >>> solve_maze(maze,0,0,len(maze)-1,len(maze)-1)
        [1, 1, 1]
        [0, 0, 1]
        [0, 0, 1]
        True

        >>> maze = [[1, 0, 0],
        ...         [0, 1, 0],
        ...         [1, 0, 0]]
        >>> solve_maze(maze,0,1,len(maze)-1,len(maze)-1)
        [0, 1, 1]
        [0, 0, 1]
        [0, 0, 1]
        True

        >>> maze = [[1, 1, 0, 0, 1, 0, 0, 1],
        ...         [1, 0, 1, 0, 0, 1, 1, 1],
        ...         [0, 1, 0, 1, 0, 0, 1, 0],
        ...         [1, 1, 1, 0, 0, 1, 0, 1],
        ...         [0, 1, 0, 0, 1, 0, 1, 1],
        ...         [0, 0, 0, 1, 1, 1, 0, 1],
        ...         [0, 1, 0, 1, 0, 1, 1, 1],
        ...         [1, 1, 0, 0, 0, 0, 0, 1]]
        >>> solve_maze(maze,0,2,len(maze)-1,2)
        [0, 0, 1, 1, 0, 0, 0, 0]
        [0, 0, 0, 1, 1, 0, 0, 0]
        [0, 0, 0, 0, 1, 0, 0, 0]
        [0, 0, 0, 1, 1, 0, 0, 0]
        [0, 0, 1, 1, 0, 0, 0, 0]
        [0, 0, 1, 0, 0, 0, 0, 0]
        [0, 0, 1, 0, 0, 0, 0, 0]
        [0, 0, 1, 0, 0, 0, 0, 0]
        True


        >>> maze = [[1, 0, 0],
        ...         [0, 1, 1],
        ...         [1, 0, 0]]
        >>> solve_maze(maze,0,1,len(maze)-1,len(maze)-1)
        No solution exists!
        False

        >>> maze = [[0, 1],
        ...         [1, 0]]
        >>> solve_maze(maze,0,0,len(maze)-1,len(maze)-1)
        No solution exists!
        False

        >>> maze = [[0, 1],
        ...         [1, 0]]
        >>> solve_maze(maze,2,0,len(maze)-1,len(maze)-1)
        Invalid source coordinates
        False

        >>> maze = [[1, 0, 0],
        ...         [0, 1, 1],
        ...         [1, 0, 0]]
        >>> solve_maze(maze,0,1,len(maze),len(maze)-1)
        Invalid destination coordinates
        False
    """
    size = len(maze)
    # Check if source and destination coordinates are Invalid.
    if not (0 <= source_row <= size - 1 and 0 <= source_column <= size - 1):
        print("Invalid source coordinates")
        return False
    elif not (0 <= destination_row <= size - 1 and 0 <= destination_column <= size - 1):
        print("Invalid destination coordinates")
        return False
    # We need to create solution object to save path.
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    solved = run_maze(
        maze, source_row, source_column, destination_row, destination_column, solutions
    )
    if solved:
        print("\n".join(str(row) for row in solutions))
    else:
        print("No solution exists!")
    return solved


def run_maze(
    maze: list[list[int]],
    i: int,
    j: int,
    destination_row: int,
    destination_column: int,
    solutions: list[list[int]],
) -> bool:
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
    if i == destination_row and j == destination_column and maze[i][j] == 0:
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
                run_maze(maze, i + 1, j, destination_row, destination_column, solutions)
                or run_maze(
                    maze, i, j + 1, destination_row, destination_column, solutions
                )
                or run_maze(
                    maze, i - 1, j, destination_row, destination_column, solutions
                )
                or run_maze(
                    maze, i, j - 1, destination_row, destination_column, solutions
                )
            ):
                return True

            solutions[i][j] = 0
            return False
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
