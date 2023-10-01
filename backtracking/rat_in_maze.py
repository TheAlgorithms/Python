from __future__ import annotations


def solve_maze(maze: list[list[int]]) -> bool:
    """
    This method solves the "rat in maze" problem.
    In this problem we have some n by n matrix, a start point and an end point.
    We want to go from the start to the end. In this matrix zeroes represent walls
    and ones paths we can use.
    Parameters :
        maze(2D matrix) : maze
    Returns:
        Return: True if the maze has a solution or False if it does not.
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
    No solution exists!
    False

    >>> maze = [[0, 1],
    ...         [1, 0]]
    >>> solve_maze(maze)
    No solution exists!
    False
    """
    size = len(maze)
    # We need to create a solution object to save the path.
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
    If a path is found to the destination, it returns True; otherwise, it returns False.
    Parameters:
        maze(2D matrix) : maze
        i, j : coordinates of the matrix
        solutions(2D matrix) : solutions
    Returns:
        Boolean if the path is found, True; Otherwise, False.
    """
    size = len(maze)
    # Final checkpoint.
    if i == j == (size - 1):
        solutions[i][j] = 1
        return True

    # Check bounds
    if (
        i >= 0
        and j >= 0
        and i < size
        and j < size
        and solutions[i][j] == 0
        and maze[i][j] == 1
    ):
        solutions[i][j] = 1

        # Explore in four directions: up, down, left, right
        if (
            run_maze(maze, i + 1, j, solutions)
            or run_maze(maze, i, j + 1, solutions)
            or run_maze(maze, i - 1, j, solutions)
            or run_maze(maze, i, j - 1, solutions)
        ):
            return True

        # If none of the directions lead to a solution, backtrack by marking the current position as 0
        solutions[i][j] = 0

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
