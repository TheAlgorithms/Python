class Matrix:
    """
    Class to represent a 2D binary grid as a matrix and count the number of islands.
    An island is a group of connected 1s.
    We call cells with 1 "land" and cells with 0 "water".
    Connections can be vertical, horizontal, or diagonal.
    """

    def __init__(self, row: int, col: int, graph: list[list[bool]]) -> None:
        """
        Initialize the matrix.

        :param row: Number of rows
        :param col: Number of columns
        :param graph: 2D list representing the matrix (1 = land, 0 = water)

        >>> graph = [[1, 1, 0], [0, 1, 0], [1, 0, 0]]
        >>> m = Matrix(3, 3, graph)
        >>> m.ROW
        3
        >>> m.COL
        3
        >>> m.graph == graph
        True

        # Edge case: Empty matrix
        >>> empty = Matrix(0, 0, [])
        >>> empty.ROW
        0
        >>> empty.COL
        0
        >>> empty.graph
        []

        # Edge case: 1x1 matrix
        >>> single = Matrix(1, 1, [[1]])
        >>> single.ROW
        1
        >>> single.COL
        1
        >>> single.graph
        [[1]]
        """

        self.ROW = row
        self.COL = col
        self.graph = graph

    def is_safe(self, i: int, j: int, visited: list[list[bool]]) -> bool:
        """
        Check if a cell (i, j) is "safe".

        We consider a cell "safe" if:
        - It is within the bounds of the matrix
        - It has not been visited yet
        - It contains land (i.e., value is 1)

        :param i: row index
        :param j: column index
        :param visitied: 2D list indicating which cells we have visited
        :return: True if cell is safe, else False

        >>> m = Matrix(3, 3, [[1, 0, 0], [0, 0, 1], [0, 0, 0]])
        >>> visited = [[False]*3 for _ in range(3)]

        # Within bounds, unvisited, and value is 1 (land)
        >>> m.is_safe(0, 0, visited)
        True

        # Within bounds, unvisited, but value is 0 (water)
        >>> m.is_safe(0, 1, visited)
        False

        # Within bounds, land, but already visited
        >>> visited[0][0] = True
        >>> m.is_safe(0, 0, visited)
        False

        # Out of bounds
        >>> m.is_safe(3, 0, visited)
        False
        >>> m.is_safe(-1, 0, visited)
        False
        """

        return (
            0 <= i < self.ROW
            and 0 <= j < self.COL
            and not visited[i][j]
            and self.graph[i][j] == 1
        )

    def diffs(self, i: int, j: int, visited: list[list[bool]]) -> None:
        """
        Check the 8 cells connected to (i, j) and marks the land cells as visited.

        Depth-first search (DFS) to mark land cells connected to (i, j) as visited.

        :param i: Row index of current cell
        :param j: Column index of current cell
        :param visited: 2D list tracking visited cells

        >>> graph = [[1, 1, 0], [0, 1, 0], [0, 0, 0]]
        >>> m = Matrix(3, 3, graph)
        >>> visited = [[False] * 3 for _ in range(3)]
        >>> m.diffs(0, 0, visited)
        >>> visited[0][0] and visited[0][1] and visited[1][1]
        True
        >>> visited[2][2]
        False
        """

        # 8 possible movements (N, NE, E, SE, S, SW, W, NW)
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Make cells visited
        visited[i][j] = True
        for k in range(8):
            next_i, next_j = i + row_nbr[k], j + col_nbr[k]
            if self.is_safe(next_i, next_j, visited):
                self.diffs(next_i, next_j, visited)

    def count_islands(self) -> int:
        """
        Count the number of islands in the matrix.

        :return: Number of islands found

        >>> graph = [[1, 1, 0], [0, 1, 0], [1, 0, 0]]
        >>> m = Matrix(3, 3, graph)
        >>> m.count_islands()
        1

        >>> graph1 = [[1, 1, 0], [0, 0, 0], [1, 0, 0]]
        >>> m1 = Matrix(3, 3, graph1)
        >>> m1.count_islands()
        2

        >>> graph2 = [[0, 0, 0], [0, 0, 0]]
        >>> m2 = Matrix(2, 3, graph2)
        >>> m2.count_islands()
        0

        >>> graph3 = [[1]]
        >>> m3 = Matrix(1, 1, graph3)
        >>> m3.count_islands()
        1
        """
        visited = [[False for _ in range(self.COL)] for _ in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if not visited[i][j] and self.graph[i][j] == 1:
                    self.diffs(i, j, visited)
                    count += 1
        return count
