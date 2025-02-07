# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


class Matrix:  # Public class to implement a graph
    def __init__(self, graph: list[list[bool]]) -> None:
        """
        Initialise matrix with number of rows, columns, and graph.

        >>> m = Matrix([[True, False, False, False],
        ...              [True, False, True, False],
        ...              [False, False, True, True]])
        >>> m.ROW
        3
        >>> m.COL
        4
        >>> m.graph
        [[True, False, False, False],
        ...[True, False, True, False],
        ...[False, False, True, True]]
        """
        self.graph = graph
        self.ROW = len(graph)
        self.COL = len(graph[0])

    def is_safe(self, i: int, j: int, visited: list[list[bool]]) -> bool:
        """
        >>> visited = [[False, False, False],
        ...             [False, False, False],
        ...             [False, False, False]]
        >>> m = Matrix([[True, False, False],
        ...              [False, False, True],
        ...              [False, False, True]])
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
        Checking all 8 elements surrounding nth element.

        >>> visited = [[False, False, False],
        ...             [False, False, False],
        ...             [False, False, False]]
        >>> m = Matrix([[True, True, False],
        ...              [False, True, False],
        ...              [True, False, True]])
        >>> m.diffs(0, 0, visited)
        >>> visited
        [[True, True, False],
        ...[False, True, False],
        ...[True, False, True]]
        """
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]  # Coordinate order
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True  # Make those cells visited
        for k in range(8):
            if self.is_safe(i + row_nbr[k], j + col_nbr[k], visited):
                self.diffs(i + row_nbr[k], j + col_nbr[k], visited)

    def count_islands(self) -> int:
        """
        >>> m = Matrix([[True, True, False, False],
        ...              [False, True, False, True],
        ...              [True, False, False, True]])
        >>> m.count_islands()
        2
        >>> m2 = Matrix([[True, True, False],
        ...               [True, False, False],
        ...               [False, False, True]])
        >>> m2.count_islands()
        2
        """
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if not visited[i][j] and self.graph[i][j]:
                    self.diffs(i, j, visited)
                    count += 1
        return count
