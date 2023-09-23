from __future__ import annotations

def solve_maze(maze: list[list[int]]) -> bool:
    """
    This method solves the "rat in maze" problem.
    In this problem, we have an n by n matrix, a start point, and an end point.
    We want to go from the start to the end. In this matrix, ones represent walls,
    and zeros represent paths we can use.
    
    Parameters:
        maze (2D matrix): The maze where 1 represents walls, and 0 represents paths.
    
    Returns:
        bool: True if a solution exists, False otherwise.
    
    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [1, 0, 1, 0, 1],
    ...         [0, 0, 1, 0, 0],
    ...         [1, 0, 0, 1, 0]]
    >>> solve_maze(maze)
    True
    Path:
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
    >>> solve_maze(maze)
    False
    No solution exists!
    """
    size = len(maze)
    # We need to create a solution object to save the path.
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    solved = run_maze(maze, 0, 0, solutions)
    
    if solved:
        print("Path:")
        for row in solutions:
            print(row)
    else:
        print("No solution exists!")
    return solved

def run_maze(maze: list[list[int]], i: int, j: int, solutions: list[list[int]]) -> bool:
    """
    This method is recursive, starting from (i, j) and going in one of four directions:
    up, down, left, right.
    If a path is found to the destination, it returns True; otherwise, it returns False.
    
    Parameters:
        maze (2D matrix): The maze where 1 represents walls, and 0 represents paths.
        i, j (int): Coordinates in the matrix.
        solutions (2D matrix): Solution matrix to save the path.
    
    Returns:
        bool: True if a path is found, False otherwise.
    """
    size = len(maze)
    # Final checkpoint.
    if i == j == (size - 1):
        solutions[i][j] = 1
        return True

    lower_flag = (0 <= i < size) and (0 <= j < size)  # Check bounds

    if lower_flag:
        # Check for already visited and blocked points.
        block_flag = (solutions[i][j] == 0) and (maze[i][j] == 0)
        if block_flag:
            # Mark as visited.
            solutions[i][j] = 1

            # Try different 
            # directions
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
