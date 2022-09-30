# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


class matrix:  # Public class to implement a graph
    def __init__(self, row: int, col: int, graph: list[list[bool]]) -> None:
        self.ROW = row
        self.COL = col
        self.graph = graph

    def is_safe(self, i: int, j: int, visited: list[list[bool]]) -> bool:
        return (
            0 <= i < self.ROW
            and 0 <= j < self.COL
            and not visited[i][j]
            and self.graph[i][j]
        )

    def diffs(self, i: int, j: int, visited: list[list[bool]]) -> None:
        # Checking all 8 elements surrounding nth element
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]  # Coordinate order
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True  # Make those cells visited
        for k in range(8):
            if self.is_safe(i + rowNbr[k], j + colNbr[k], visited):
                self.diffs(i + rowNbr[k], j + colNbr[k], visited)

    def count_islands(self) -> int:  # And finally, count all islands.
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] is False and self.graph[i][j] == 1:
                    self.diffs(i, j, visited)
                    count += 1
        return count
