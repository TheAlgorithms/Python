"""
Given an two dimensional binary matrix grid. An island is a group of 1's (representing
land) connected 4-directionally (horizontal or vertical.) You may assume all four edges
of the grid are surrounded by water.  The area of an island is the number of cells with
a value 1 in the island. Return the maximum area of an island in a grid. If there is no
island, return 0.
"""

matrix = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]


def is_safe(row: int, col: int, rows: int, cols: int) -> bool:
    """
    Checking whether coordinate (row, col) is valid or not.

    >>> is_safe(0, 0, 5, 5)
    True
    >>> is_safe(-1,-1, 5, 5)
    False
    """
    return 0 <= row < rows and 0 <= col < cols


def depth_first_search(row: int, col: int, seen: set, mat: list[list[int]]) -> int:
    """
    Returns the current area of the island

    >>> depth_first_search(0, 0, set(), matrix)
    0
    """
    rows = len(mat)
    cols = len(mat[0])
    if is_safe(row, col, rows, cols) and (row, col) not in seen and mat[row][col] == 1:
        seen.add((row, col))
        return (
            1
            + depth_first_search(row + 1, col, seen, mat)
            + depth_first_search(row - 1, col, seen, mat)
            + depth_first_search(row, col + 1, seen, mat)
            + depth_first_search(row, col - 1, seen, mat)
        )
    else:
        return 0


def find_max_area(mat: list[list[int]]) -> int:
    """
    Finds the area of all islands and returns the maximum area.

    >>> find_max_area(matrix)
    6
    """
    seen: set = set()

    max_area = 0
    for row, line in enumerate(mat):
        for col, item in enumerate(line):
            if item == 1 and (row, col) not in seen:
                # Maximizing the area
                max_area = max(max_area, depth_first_search(row, col, seen, mat))
    return max_area


if __name__ == "__main__":
    import doctest

    print(find_max_area(matrix))  # Output -> 6

    """
    Explanation:
    We are allowed to move in four directions (horizontal or vertical) so the possible
    in a matrix if we are at x and y position the possible moving are

    Directions are [(x, y+1), (x, y-1), (x+1, y), (x-1, y)] but we need to take care of
    boundary cases as well which are x and y can not be smaller than 0 and greater than
    the number of rows and columns respectively.

    Visualization
    mat = [
        [0,0,A,0,0,0,0,B,0,0,0,0,0],
        [0,0,0,0,0,0,0,B,B,B,0,0,0],
        [0,C,C,0,D,0,0,0,0,0,0,0,0],
        [0,C,0,0,D,D,0,0,E,0,E,0,0],
        [0,C,0,0,D,D,0,0,E,E,E,0,0],
        [0,0,0,0,0,0,0,0,0,0,E,0,0],
        [0,0,0,0,0,0,0,F,F,F,0,0,0],
        [0,0,0,0,0,0,0,F,F,0,0,0,0]
    ]

    For visualization, I have defined the connected island with letters
    by observation, we can see that
        A island is of area 1
        B island is of area 4
        C island is of area 4
        D island is of area 5
        E island is of area 6 and
        F island is of area 5

    it has 6 unique islands of mentioned areas
    and the maximum of all of them is 6 so we return 6.
    """

    doctest.testmod()
