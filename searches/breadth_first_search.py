"""
Python implementation of the breadth-first search algorithm for pathfinding.

Find an explanation of this algorithm here: 
https://en.wikipedia.org/wiki/Breadth-first_search

Also included is a simple node class, maze generation and maze visualisation
to show the results of the algorithm.

For doctest testing run: python3 -m doctest -v breadth_first_search.py

For manual testing and visualisation run: python3 breadth_first_search.py
"""
import random
import queue


class Node:
    """
    Objects of this class make up the grid (2d array) which will be
    traversed by the algorithm.
    """

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.neighbours = []

    def __str__(self):
        return f"Node ({self.row}, {self.col})"

    def update_neighbours(self, i: int, j: int, grid: list) -> None:
        """
        Appends adjacent nodes which are not walls to self.neighbours.
        """

        if i > 0 and grid[i - 1][j].value:
            self.neighbours.append(grid[i - 1][j])
        if i < len(grid) - 1 and grid[i + 1][j].value:
            self.neighbours.append(grid[i + 1][j])
        if j > 0 and grid[i][j - 1].value:
            self.neighbours.append(grid[i][j - 1])
        if j < len(grid) - 1 and grid[i][j + 1].value:
            self.neighbours.append(grid[i][j + 1])

    def make_path(self):
        self.value = "x"

    def make_start(self):
        self.value = "S"
        return self

    def make_end(self):
        self.value = "E"
        return self


def random_value():
    """
    Used for very simple maze generation, every 1 in 4 nodes becomes a
    wall.

    This is done just so the algorithm has some obstacles to get around.

    Examples:
    >>> rand = random_value()
    >>> rand in [" ", None]
    True

    >>> rand = random_value()
    >>> rand in ["", 0, "hello"]
    False
    """

    return random.choices([" ", None], weights=[4, 1])[0]


def make_grid(size: int, random_maze=True) -> list:
    """
    Returns a list containing lists of nodes (the grid).

    Option to just have a grid with no walls generated
    by giving the second parameter as False.

    Examples:
    >>> grid = make_grid(2)
    >>> print(grid[1][1])
    Node (1, 1)

    >>> grid = make_grid(16)
    >>> print(grid[0][0])
    Node (0, 0)

    >>> grid = make_grid(4)
    >>> len(grid) == len(grid[0]) == 4
    True

    >>> len(make_grid(0))
    0

    >>> grid = make_grid(3, False)
    >>> grid[0][0].value
    ' '
    """

    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            value = random_value() if random_maze else " "
            row.append(Node(value, i, j))
        grid.append(row)
    return grid


def print_grid(grid: list, message: str) -> None:
    """
    Prints out the grid so the maze and the algorithm can be visualised.
    """

    key = "\nKey: \n|=wall S=start E=end x=path"
    print(f"{key}\n\n{message}\n", "_" * len(grid))
    for row in grid:
        print()
        for node in row:
            if node.value:
                print(node.value, end="")
            else:
                print("|", end="")
    print("\n", "_" * len(grid))


def construct_path(path: dict, current: Node, start: Node) -> None:
    """
    Takes a dictionary, path, and makes all nodes along the shortest
    path into path nodes.

    Only called if the end node was reached.

    Examples:
    >>> grid = make_grid(2, False)
    >>> start = grid[1][1]
    >>> path = {grid[0][0]: grid[1][0], grid[1][0]: grid[1][1]}
    >>> construct_path(path, grid[0][0], grid[1][1])
    >>> grid[1][0].value
    'x'
    >>> grid[0][0].value
    ' '

    >>> grid = make_grid(4, False)
    >>> start = grid[2][3]
    >>> path = {grid[1][2]: grid[1][3], grid[1][3]: grid[2][3]}
    >>> construct_path(path, grid[1][2], grid[2][3])
    >>> grid[1][3].value
    'x'
    >>> grid[0][0].value
    ' '
    """

    while path.get(current, None):
        current = path[current]
        if current is start:
            break
        current.make_path()


def breadth_first_search(grid, start, end):
    """
    Searches every traversible node outwards from the starting
    node until the end node is reached.

    This algorithm ensures the shortest path.

    Examples:
    >>> grid = make_grid(4, False)
    >>> start, end = grid[1][1], grid[2][2]
    >>> breadth_first_search(grid, start, end)
    True

    >>> grid = make_grid(25, False)
    >>> start, end = grid[24][24], grid[0][0]
    >>> breadth_first_search(grid, start, end)
    True

    >>> grid = make_grid(100, False)
    >>> start, end = grid[0][99], grid[99][0]
    >>> breadth_first_search(grid, start, end)
    True

    >>> grid = make_grid(10, False)
    >>> for row in grid: row[5].value = None
    >>> start, end = grid[9][9], grid[0][0]
    >>> breadth_first_search(grid, start, end)
    False
    """
    open_set = queue.Queue()
    open_set.put(start)

    # Will be used to construct the best path using the construct_path function
    path = {node: None for row in grid for node in row if node.value}

    while not open_set.empty():
        current = open_set.get()

        if current is end:
            construct_path(path, current, start)
            return True

        current.update_neighbours(current.row, current.col, grid)
        for neighbour in current.neighbours:
            if path[neighbour]:
                continue

            open_set.put(neighbour)
            path[neighbour] = current

    return False


if __name__ == "__main__":

    # **CHANGE THESE VARIABLES FOR DIFFERENT RESULTS**
    size = 50  # grid = size x size 2d array
    x1, y1 = 1, 1  # Sets the starting node to grid[x1][y1]
    x2, y2 = 48, 48  # Sets ending node to grid[x2][y2]

    # Grid generation
    grid = make_grid(size)
    start = grid[x1][y1].make_start()
    end = grid[x2][y2].make_end()

    # Output
    print_grid(grid, "Maze before:")
    if breadth_first_search(grid, start, end):
        print_grid(grid, "Maze after:")
    else:
        print("No path was found :(")
