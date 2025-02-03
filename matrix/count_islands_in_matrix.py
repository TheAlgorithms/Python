# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


class Matrix:  # Public class to implement a graph
    def __init__(self, row: int, col: int, graph: list[list[bool]]) -> None:
        """
        Initialise matrix with number of rows, columns, and graph

        >>> m = Matrix(4, 3, [[True, False, False, False], [True, False, True, False], [False, False, True, True]])
        >>> m.ROW
        4
        >>> m.COL
        3
        >>> m.graph
        [[True, False, False, False], [True, False, True, False], [False, False, True, True]]
        """
        self.ROW = row
        self.COL = col
        self.graph = graph

    def is_safe(self, i: int, j: int, visited: list[list[bool]]) -> bool:
        """
        Checks if the cell (i, j) can be visited

        >>> visited = [[False, False, False], [False, False, False], [False, False, False]]
        >>> m = Matrix(3, 3, [[True, False, False], [False, False, True], [False, False, True]])
        >>> m.is_safe(0, 0, visited)
        True
        >>> m.is_safe(0, 2, visited)
        False
        >>> m.is_safe(-1, 2, visited)
        False
        >>> m.is_safe(1, 5, visited)
        False
        """
        return (
            0 <= i < self.ROW
            and 0 <= j < self.COL
            and not visited[i][j]
            and self.graph[i][j]
        )

    def diffs(self, i: int, j: int, visited: list[list[bool]]) -> None:
        """
        Checking all 8 elements surrounding nth element

        >>> visited = [[False, False, False], [False, False, False], [False, False, False]]
        >>> m = Matrix(3, 3, [[True, True, False], [False, True, False], [True, False, True]])
        >>> m.diffs(0, 0, visited)
        >>> visited
        [[True, True, False], [False, True, False], [False, False, False]]
        """
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]  # Coordinate order
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True  # Make those cells visited
        for k in range(8):
            if self.is_safe(i + row_nbr[k], j + col_nbr[k], visited):
                self.diffs(i + row_nbr[k], j + col_nbr[k], visited)

    def count_islands(self) -> int:
        """
        Counts the number of islands in the matrix

        >>> m = Matrix(3, 4, [[True, True, False, False], [False, True, False, True], [True, False, False, True]])
        >>> m.count_islands()
        3
        >>> m2 = Matrix(3, 3, [[True, True, False], [True, False, False], [False, False, True]])
        2
        """
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] is False and self.graph[i][j] == 1:
                    self.diffs(i, j, visited)
                    count += 1
        return count
