## A* Search Algorithm in Python
- Given an adjacency list and a heuristic function for a directed graph, implement the A* search algorithm to find the shortest path from a start node to a goal node.

`Examples:`
```bash
Input:
Start Node: A
Goal Node: F
Nodes: A, B, C, D, E, F
Edges with weights:
(A, B, 1), (A, C, 4),
(B, D, 3), (B, E, 5),
(C, F, 2),
(D, F, 1), (D, E, 1),
(E, F, 2)
Output: A -> B -> D -> F
Explanation: The A* search algorithm is applied to find the shortest path from node A to node F in the given graph. The path found is A -> B -> D -> F, with a total cost of 5.



Input:
Start Node: A
Goal Node: E
Nodes: A, B, C, D, E
Edges with weights:
(A, B, 3), (A, C, 5),
(B, D, 2), (B, E, 6),
(C, E, 1),
(D, E, 4)
Output: A -> B -> D -> E
Explanation: The A* search algorithm is applied to find the shortest path from node A to node E in the given graph. The path found is A -> B -> D -> E, with a total cost of 9.
```
#### What is A* Search Algorithm?
- The ***A* search algorithm*** is a popular ***pathfinding algorithm*** used in many applications, including video games, robotics, and route planning. A* is an extension of Dijkstra’s algorithm and uses heuristics to improve the efficiency of the search by prioritizing paths that are likely to be closer to the goal.

#### How A* Search Algo works?
- Here’s how the A* search algorithm works:

`Initialization:`
- Start with an open list containing the start node.
- Start with an empty closed list.

`While the open list is not empty:`
- Select the node with the lowest f value from the open list. - This node is the current node.
- If the current node is the goal node, the path has been found; reconstruct the path and return it.
- Move the current node to the closed list.
- For each neighbor of the current node:
    - If the neighbor is in the closed list or is a wall, skip it.
    - If the neighbor is not in the open list:
        - Compute its g value (cost from the start node to the current node plus the cost from the current node to the neighbor).
        - Compute its h value (heuristic estimate of the cost from the neighbor to the goal).
        - Add it to the open list with f=g+h and set the parent of the neighbor to the current node.
    - If the neighbor is already in the open list:
        - If the new g value is lower than the current g value, update the neighbor’s g and f values and update its parent to the current node.

`If the open list is empty:`
- The goal is unreachable; return failure.

***`A_start_search.py`***
```bash
# Python program for A* Search Algorithm
import math
import heapq

# Define the Cell class


class Cell:
    def __init__(self):
      # Parent cell's row index
        self.parent_i = 0
    # Parent cell's column index
        self.parent_j = 0
 # Total cost of the cell (g + h)
        self.f = float('inf')
    # Cost from start to this cell
        self.g = float('inf')
    # Heuristic cost from this cell to destination
        self.h = 0


# Define the size of the grid
ROW = 9
COL = 10

# Check if a cell is valid (within the grid)


def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# Check if a cell is unblocked


def is_unblocked(grid, row, col):
    return grid[row][col] == 1

# Check if a cell is the destination


def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Calculate the heuristic value of a cell (Euclidean distance to destination)


def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

# Trace the path from source to destination


def trace_path(cell_details, dest):
    print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
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


def a_star_search(grid, src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
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
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
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
                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
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


def main():
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
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    # Define the source and destination
    src = [8, 0]
    dest = [0, 0]

    # Run the A* search algorithm
    a_star_search(grid, src, dest)


if __name__ == "__main__":
    main()
```
***`output:`***
```bash
The destination cell is found
The Path is 
-> (8, 0) -> (7, 0) -> (6, 0) -> (5, 0) -> (4, 1) -> (3, 2) -> (2, 1) -> (1, 0) -> (0, 0) 
```

- ***Time Complexity:*** O(E log V), where E is the number of edges and V is the number of vertices, due to the use of the priority queue.
- ***Auxiliary Space:*** O(V), where V is the number of vertices in the grid.

