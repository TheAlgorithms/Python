# Given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid.
# If there is no island, return 0.


class matrix:
    def __init__(self, mat) -> None:
        """
        Constructor to set the problem param.
        """
        self.mat = mat
        self.ROWS = len(mat)
        self.COLS = len(mat[0])
        self.seen = set()

    def is_safe(self, i, j):
        """
        Checking weather co-ordinate (i,j) is valid or not.
        """
        return not (i < 0 or j < 0 or i >= self.ROWS or j >= self.COLS)

    def dfs(self, i, j):
        """
        Returns the current Area of island
        """
        if self.is_safe(i, j) and (i, j) not in self.seen and self.mat[i][j] == 1:
            self.seen.add((i, j))
            return (
                1
                + self.dfs(i + 1, j)
                + self.dfs(i - 1, j)
                + self.dfs(i, j + 1)
                + self.dfs(i, j - 1)
            )
        else:
            return 0

    def count_max_area(self) -> int:
        max_area = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.mat[i][j] == 1 and (i, j) not in self.seen:
                    # Maximizing the area
                    max_area = max(max_area, self.dfs(i, j))

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

maximum_area_1 = matrix(mat)

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
