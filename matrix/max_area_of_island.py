# Given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid.
# If there is no island, return 0.


class maximumAreaOfIsland:
    def __init__(self, mat: list[list[int]]) -> None:
        """
        Constructor to set the problem param.
        """
        self.mat = mat
        self.ROWS = len(mat)
        self.COLS = len(mat[0])
        self.seen = set()

    def is_safe(self, row: int, col: int) -> bool:
        """
        Checking weather co-ordinate (i,j) is valid or not.
        """
        return not (row < 0 or col < 0 or row >= self.ROWS or col >= self.COLS)

    def dfs(self, row: int, col: int) -> int:
        """
        Returns the current Area of island
        """
        if (
            self.is_safe(row, col)
            and (row, col) not in self.seen
            and self.mat[row][col] == 1
        ):
            self.seen.add((row, col))
            return (
                1
                + self.dfs(row + 1, col)
                + self.dfs(row - 1, col)
                + self.dfs(row, col + 1)
                + self.dfs(row, col - 1)
            )
        else:
            return 0

    def count_max_area(self) -> int:
        max_area = 0
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.mat[row][col] == 1 and (row, col) not in self.seen:
                    # Maximizing the area
                    max_area = max(max_area, self.dfs(row, col))

        return max_area


# Example 1:
mat = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]

maximum_area_1 = maximumAreaOfIsland(mat)

print(maximum_area_1.count_max_area())  # Output -> 6

"""
Explaination:
We are allowed to move 4-directionally (horizontal or vertical.) so the possible
in a matrix if we are at x and y possition the possible moveing are

>> directions = [(x,y+1),(x,y-1),(x+1,y),(x-1,y)] also we need to care of boundary cases as well
    which are x and y can not be smaller than 0 and greater than number of rows and colums respectively.


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

For visualization I have defined the connected island with alphabates.
by observation we can see that
    A island is of area 1
    B island is of area 4
    C island is of area 4
    D island is of area 5
    E island is of area 6 and
    F island is of area 5

it has 6 unique island's of mentioned area's
and maximum of all of them is 6 so we return 6.
"""


if __name__ == "__main__":
    import doctest

    doctest.testmod()