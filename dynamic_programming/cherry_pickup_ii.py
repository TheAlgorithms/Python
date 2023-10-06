"""
You are given a rows x cols matrix grid representing a field of
cherries where grid[i][j] represents the
number of cherries that you can
collect from the (i, j) cell.

You have two robots that can
collect cherries for you:

Robot #1 is located at the top-left
corner (0, 0), and
Robot #2 is located at the
top-right corner (0, cols - 1).

Return the maximum number of cherries
collection using both robots by
following the rules below:

1. From a cell (i, j), robots can move to cell
   (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
2. When any robot passes through a cell,
   picks up all cherries,
   and the cell becomes an empty cell.
3. When both robots stay in the same cell,
   only one takes the cherries.
4. Both robots cannot move outside
   of the grid at any moment.
5. Both robots should reach the bottom row in grid.

Problem Statement:-
   https://leetcode.com/problems/cherry-pickup-ii

"""
from collections import defaultdict


class Solution:
    def __init__(self):
        self.dp: defaultdict[int] = defaultdict(int)

    def cherry_pickup(self, grid: list[list[int]]) -> int:
        return self.recurse(grid, 0, 0, len(grid[0]) - 1)

    def recurse(self, grid, row, column1, column2):
        # Reached the end
        if row == len(grid):
            return 0

        if row == len(grid):
            return 0

        # Both robots can't share same tile
        if column1 == column2:
            return float("-inf")

        if (
            0 <= row < len(grid)
            and 0 <= column1 < len(grid[0])
            and 0 <= column2 < len(grid[0])
        ):
            res = 0
            for y1 in [column1 - 1, column1, column1 + 1]:
                for y2 in [column2 - 1, column2, column2 + 1]:
                    if self.dp.get((row + 1, y1, y2)):
                        val = self.dp[(row + 1, y1, y2)]
                    else:
                        val = self.recurse(grid, row + 1, y1, y2)
                    res = max(res, val)

            self.dp[(row, column1, column2)] = (
                grid[row][column1] + grid[row][column2] + res
            )
            return grid[row][column1] + grid[row][column2] + res

        return float("-inf")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 3]]

    solution = Solution()
    result = solution.cherry_pickup(grid)
    print(result)  # Output: 19
