def print_matrix(matrix):
    """
    This method takes matrix as parameter and print the solution
    In this matrix 1 s are the path to the destination.
    Parameters :
        matrix(2D matrix) : matrix
    """
    for i in matrix:
        print(i)


def fill_matrix(matrix, i, j):
    """
    This method just fills matrix i, j with value
    Parameters :
        matrix(2D matrix) : matrix
        i, j : coordinates of the matrix.
    """
    matrix[i][j] = 1


def solveMaze(maze, size):
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
    """
    # We need to create solution object to save path.
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    flag = runmaze(maze, size, 0, 0, solutions)
    if flag:
        print_matrix(solutions)
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
"""


def runmaze(maze, size, i, j, solutions):
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
            if runmaze(maze, size, i + 1, j, solutions):
                return True

            if runmaze(maze, size, i, j + 1, solutions):
                return True

            if runmaze(maze, size, i - 1, j, solutions):
                return True

            if runmaze(maze, size, i, j - 1, solutions):
                return True

            solutions[i][j] = 0
            return False


def main():
    maze = [
        [0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
    ]
    size = 5
    solveMaze(maze, size)


if __name__ == "__main__":
    main()
