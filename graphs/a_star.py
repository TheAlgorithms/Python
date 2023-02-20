from __future__ import annotations

DIRECTIONS = [
    [-1, 0],  # up
    [0, -1],  # left
    [1, 0],  # down
    [0, 1],  # right
]


# function to search the path
def search(
    grid: list[list[int]],
    init: list[int],
    goal: list[int],
    cost: int,
    heuristic: list[list[int]],
) -> tuple[list[list[int]], list[list[int]]]:
    """
    A* search algorithm
    
    Args:
        grid (list[list[int]]): coordinates of the destination
        init (list[int]): initial coordinate of the subject
        goal (list[int]): coordinate of the destination
        cost (int): the cost of each movement
        heuristic (list[list[int]]): map. each grid stores the heuristic to the goal

    Raises:
        ValueError: Illegal input

    Returns:
        tuple[list[list[int]], list[list[int]]]: optimal path and corresponding actions.
    
    >>> search(grid1, init1, goal1, cost1, heuristic1)
    ([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [3, 3], [2, 3], [2, 4], [2, 5], [3, 5], [4, 5]], [[0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 3, 3], [2, 0, 0, 0, 0, 2], [2, 3, 3, 3, 0, 2]])
    >>> search(grid2, init2, goal2, cost2, heuristic2)
    Traceback (most recent call last):
     ...
    ValueError: Algorithm is unable to find solution
    >>> search(grid3, init3, goal3, cost3, heuristic3)
    ([[0, 4], [1, 4], [1, 5], [2, 5], [3, 5], [4, 5], [4, 4], [4, 3], [4, 2], [3, 2], [2, 2], [1, 2], [1, 1]], [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 2, 3], [0, 0, 0, 3, 0, 2], [0, 0, 0, 0, 0, 2], [1, 1, 1, 1, 1, 2]])
    >>> search(grid4, init4, goal4, cost4, heuristic4)
    ([[2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [5, 6], [4, 6], [3, 6], [2, 6], [2, 5], [2, 4], [2, 3], [2, 2], [1, 2], [1, 1]], [[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 1, 0], [2, 0, 2, 0, 0, 1, 0], [2, 3, 0, 1, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [2, 3, 3, 3, 3, 3, 3]])
    """
    closed = [
        [0 for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]  # the reference grid
    closed[init[0]][init[1]] = 1
    action = [
        [0 for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]  # the action grid

    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]  # cost from starting cell to destination cell
    cell = [[f, g, x, y]]

    found = False  # flag that is set when search is complete

    while not found:
        if len(cell) == 0:
            raise ValueError("Algorithm is unable to find solution")
        else:  # to choose the least costliest action so as to move closer to the goal
            found = expand(cell, goal, grid, closed, action, heuristic, cost)
                            
    path = backtrack(goal, action, init)
    
    return path, action

def expand(cell, goal, grid, closed, action, heuristic, cost) -> bool:
    """
    Expand the searching tree, return true if the goal can be found in this expansion.

    Args:
        cell (list[list[int]]): priority queue of the possible movements, sorted by (previous cost + heuristic)
        goal (list[int]): coordinates of the destination
        grid (list[list[int]]): map
        closed (list[list[int]]): map. 1 represents this place has been visited
        action (list[list[int]]): map. each grid records the action brings the subject here
        heuristic (list[list[int]]): map. each grid stores the heuristic to the goal
        cost (int): the cost of each movement

    Returns:
        bool: If the goal can be found in this expansion.
    """
    cell.sort()
    cell.reverse()
    next_cell = cell.pop()
    x = next_cell[2]
    y = next_cell[3]
    g = next_cell[1]
    if x == goal[0] and y == goal[1]:
        return True
    else:
        for i in range(len(DIRECTIONS)):  # to try out different valid actions
            x2 = x + DIRECTIONS[i][0]
            y2 = y + DIRECTIONS[i][1]
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                    g2 = g + cost
                    f2 = g2 + heuristic[x2][y2]
                    cell.append([f2, g2, x2, y2])
                    closed[x2][y2] = 1
                    action[x2][y2] = i
        return False


def backtrack(goal, action, init) -> list[list[int]]:
    """
    Get the optimal path according to the action history.

    Args:
        goal (list[int]): coordinates of the destination
        action (list[list[int]]): action history
        init (list[int]): initial coordinate of the subject

    Returns:
        list[list[int]]: optimal path
    """
    invpath = []
    x = goal[0]
    y = goal[1]
    invpath.append([x, y])  # we get the reverse path from here
    while x != init[0] or y != init[1]:
        x2 = x - DIRECTIONS[action[x][y]][0]
        y2 = y - DIRECTIONS[action[x][y]][1]
        x = x2
        y = y2
        invpath.append([x, y])

    path = []
    for i in range(len(invpath)):
        path.append(invpath[len(invpath) - 1 - i])
    return path

# test1 input
grid1 = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
]
init1 = [0, 0]
goal1 = [len(grid1) - 1, len(grid1[0]) - 1]
cost1 = 1
heuristic1 = [[0 for row in range(len(grid1[0]))] for col in range(len(grid1))]
for i in range(len(grid1)):
    for j in range(len(grid1[0])):
        heuristic1[i][j] = abs(i - goal1[0]) + abs(j - goal1[1])
        if grid1[i][j] == 1:
            # added extra penalty in the heuristic map
            heuristic1[i][j] = 99
            
# test2 input
grid2 = [
    [0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
]
init2 = [0, 0]
goal2 = [len(grid1) - 1, len(grid1[0]) - 1]
cost2 = 1
heuristic2 = [[0 for row in range(len(grid2[0]))] for col in range(len(grid2))]
for i in range(len(grid2)):
    for j in range(len(grid2[0])):
        heuristic2[i][j] = abs(i - goal2[0]) + abs(j - goal2[1])
        if grid2[i][j] == 1:
            # added extra penalty in the heuristic map
            heuristic2[i][j] = 99
            
# test3 input
grid3 = [
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
]
init3 = [0, 4]
goal3 = [1, 1]
cost3 = 1
heuristic3 = [[0 for row in range(len(grid3[0]))] for col in range(len(grid3))]
for i in range(len(grid3)):
    for j in range(len(grid3[0])):
        heuristic3[i][j] = abs(i - goal3[0]) + abs(j - goal3[1])
        if grid3[i][j] == 1:
            # added extra penalty in the heuristic map
            heuristic3[i][j] = 99

# test4 input
grid4 = [
    [0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
init4 = [2, 0]
goal4 = [1, 1]
cost4 = 1
heuristic4 = [[0 for row in range(len(grid4[0]))] for col in range(len(grid4))]
for i in range(len(grid4)):
    for j in range(len(grid4[0])):
        heuristic4[i][j] = abs(i - goal4[0]) + abs(j - goal4[1])
        if grid4[i][j] == 1:
            # added extra penalty in the heuristic map
            heuristic4[i][j] = 99


if __name__ == "__main__":
    import doctest

    doctest.testmod()
