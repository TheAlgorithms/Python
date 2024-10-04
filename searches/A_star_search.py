# Python program for A* Search Algorithm
import math
import heapq
from typing import List, Tuple

# Define the Cell class


class Cell:
    def __init__(self) -> None:
        # Parent cell's row index
        self.parent_i = 0
        # Parent cell's column index
        self.parent_j = 0
        # Total cost of the cell (g + h)
        self.f = float("inf")
        # Cost from start to this cell
        self.g = float("inf")
        # Heuristic cost from this cell to destination
        self.h = 0


# Define the size of the grid
ROW = 9
COL = 10

# Check if a cell is valid (within the grid)


def is_valid(row: int, col: int) -> bool:
    """
    Check if a cell is within the grid bounds.

    Args:
        row (int): The row index of the cell.
        col (int): The column index of the cell.

    Returns:
        bool: True if the cell is within bounds, False otherwise.

    Examples:
        >>> is_valid(5, 3)
        True
        >>> is_valid(9, 5)
        False
        >>> is_valid(-1, 0)
        False
    """
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# Check if a cell is unblocked


def is_unblocked(grid: List[List[int]], row: int, col: int) -> bool:
    """
    Check if a cell is unblocked in the grid.

    Args:
        grid (List[List[int]]): The grid representing the map.
        row (int): The row index of the cell.
        col (int): The column index of the cell.

    Returns:
        bool: True if the cell is unblocked (1), False if blocked (0).

    Examples:
        >>> grid = [
        ...     [1, 0, 1],
        ...     [1, 1, 0],
        ...     [0, 1, 1]
        ... ]
        >>> is_unblocked(grid, 0, 0)
        True
        >>> is_unblocked(grid, 0, 1)
        False
        >>> is_unblocked(grid, 2, 2)
        True
    """
    return grid[row][col] == 1


# Check if a cell is the destination


def is_destination(row: int, col: int, dest: Tuple[int, int]) -> bool:
    """
    Check if a cell is the destination.

    Args:
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        dest (Tuple[int, int]): The destination coordinates as (row, col).

    Returns:
        bool: True if the cell is the destination, False otherwise.

    Examples:
        >>> is_destination(3, 4, (3, 4))
        True
        >>> is_destination(2, 1, (3, 4))
        False
    """
    return row == dest[0] and col == dest[1]


# Calculate the heuristic value of a cell (Euclidean distance to destination)


def calculate_h_value(row: int, col: int, dest: Tuple[int, int]) -> float:
    """
    Calculate the heuristic value (Euclidean distance) from a cell to the destination.

    Args:
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        dest (Tuple[int, int]): The destination coordinates as (row, col).

    Returns:
        float: The Euclidean distance from the current cell to the destination.

    Examples:
        >>> calculate_h_value(0, 0, (3, 4))
        5.0
        >>> calculate_h_value(2, 1, (2, 1))
        0.0
        >>> calculate_h_value(1, 1, (4, 5))
        5.0
    """
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5


# Trace the path from source to destination


def trace_path(cell_details: List[List[Cell]], dest: Tuple[int, int]) -> None:
    """
    Trace and print the path from the source to the destination.

    Args:
        cell_details (List[List[Cell]]): A 2D list containing details of each cell.
        dest (Tuple[int, int]): The destination coordinates as (row, col).

    Returns:
        None

    Examples:
        >>> class Cell:
        ...     def __init__(self):
        ...         self.parent_i = 0
        ...         self.parent_j = 0
        >>> cell_details = [[Cell() for _ in range(2)] for _ in range(2)]
        >>> cell_details[1][1].parent_i = 0
        >>> cell_details[1][1].parent_j = 0
        >>> trace_path(cell_details, (1, 1))
        The Path is 
        -> (0, 0) -> (1, 1) 
    """
    print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (
        cell_details[row][col].parent_i == row
        and cell_details[row][col].parent_j == col
    ):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    # Add the source cell to the path
    path.append((row, col))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()


# Implement the A* search algorithm


def a_star_search(grid: List[List[int]], src: Tuple[int, int], dest: Tuple[int, int]) -> None:
    """
    Perform the A* search to find the shortest path from source to destination.

    Args:
        grid (List[List[int]]): The grid representing the map, where 1 is unblocked and 0 is blocked.
        src (Tuple[int, int]): The source coordinates as (row, col).
        dest (Tuple[int, int]): The destination coordinates as (row, col).

    Returns:
        None

    Examples:
        >>> grid = [
        ...     [1, 1, 1],
        ...     [1, 0, 1],
        ...     [1, 1, 1]
        ... ]
        >>> a_star_search(grid, (0, 0), (2, 2))
        The destination cell is found
        The Path is 
        -> (0, 0) -> (1, 1) -> (2, 2) 
        >>> a_star_search(grid, (0, 0), (1, 1))
        Source or the destination is blocked
    """
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(
        grid, dest[0], dest[1]
    ):
        print("Source or the destination is blocked")
        return

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return

    # Initialize the closed list (visited cells)
    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        # For each direction, check the successors
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # If the successor is valid, unblocked, and not visited
            if (
                is_valid(new_i, new_j)
                and is_unblocked(grid, new_i, new_j)
                and not closed_list[new_i][new_j]
            ):
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if (
                        cell_details[new_i][new_j].f == float("inf")
                        or cell_details[new_i][new_j].f > f_new
                    ):
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        # Update the cell details
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")


# Driver Code    

if __name__ == "__main__":
    """
    Run the A* search algorithm on a predefined grid.

    Returns:
        None

    Examples:
        >>> main()
        The destination cell is found
        The Path is
        -> (8, 0) -> (7, 1) -> (6, 0) -> (5, 1) -> (4, 0) -> (3, 1) -> (2, 0) -> (1, 1) -> (0, 0)
    """
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    ]

    # Define the source and destination
    src = (8, 0)
    dest = (0, 0)

    # Run the A* search algorithm
    a_star_search(grid, src, dest)

