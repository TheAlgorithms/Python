"""
https://en.wikipedia.org/wiki/Best-first_search#Greedy_BFS
"""

from __future__ import annotations

Path = list[tuple[int, int]]

# 0's are free path whereas 1's are obstacles
TEST_GRIDS = [
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
    ],
    [
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ],
]

delta = ([-1, 0], [0, -1], [1, 0], [0, 1])  # up, left, down, right


class Node:
    """
    >>> k = Node(0, 0, 4, 5, 0, None)
    >>> k.calculate_heuristic()
    9
    >>> n = Node(1, 4, 3, 4, 2, None)
    >>> n.calculate_heuristic()
    2
    >>> l = [k, n]
    >>> n == l[0]
    False
    >>> l.sort()
    >>> n == l[0]
    True
    """

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        goal_x: int,
        goal_y: int,
        g_cost: float,
        parent: Node | None,
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_y, pos_x)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.g_cost = g_cost
        self.parent = parent
        self.f_cost = self.calculate_heuristic()

    def calculate_heuristic(self) -> float:
        """
        The heuristic here is the Manhattan Distance
        Could elaborate to offer more than one choice
        """
        dx = abs(self.pos_x - self.goal_x)
        dy = abs(self.pos_y - self.goal_y)
        return dx + dy

    def __lt__(self, other) -> bool:
        return self.f_cost < other.f_cost

    def __eq__(self, other) -> bool:
        return self.pos == other.pos


class GreedyBestFirst:
    """
    >>> grid = TEST_GRIDS[2]
    >>> gbf = GreedyBestFirst(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))
    >>> [x.pos for x in gbf.get_successors(gbf.start)]
    [(1, 0), (0, 1)]
    >>> (gbf.start.pos_y + delta[3][0], gbf.start.pos_x + delta[3][1])
    (0, 1)
    >>> (gbf.start.pos_y + delta[2][0], gbf.start.pos_x + delta[2][1])
    (1, 0)
    >>> gbf.retrace_path(gbf.start)
    [(0, 0)]
    >>> gbf.search()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3),
     (4, 4)]
    """

    def __init__(
        self, grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]
    ):
        self.grid = grid
        self.start = Node(start[1], start[0], goal[1], goal[0], 0, None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], 99999, None)

        self.open_nodes = [self.start]
        self.closed_nodes: list[Node] = []

        self.reached = False

    def search(self) -> Path | None:
        """
        Search for the path,
        if a path is not found, only the starting position is returned
        """
        while self.open_nodes:
            # Open Nodes are sorted using __lt__
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)

            if current_node.pos == self.target.pos:
                self.reached = True
                return self.retrace_path(current_node)

            self.closed_nodes.append(current_node)
            successors = self.get_successors(current_node)

            for child_node in successors:
                if child_node in self.closed_nodes:
                    continue

                if child_node not in self.open_nodes:
                    self.open_nodes.append(child_node)

        if not self.reached:
            return [self.start.pos]
        return None

    def get_successors(self, parent: Node) -> list[Node]:
        """
        Returns a list of successors (both in the grid and free spaces)
        """
        return [
            Node(
                pos_x,
                pos_y,
                self.target.pos_x,
                self.target.pos_y,
                parent.g_cost + 1,
                parent,
            )
            for action in delta
            if (
                0 <= (pos_x := parent.pos_x + action[1]) < len(self.grid[0])
                and 0 <= (pos_y := parent.pos_y + action[0]) < len(self.grid)
                and self.grid[pos_y][pos_x] == 0
            )
        ]

    def retrace_path(self, node: Node | None) -> Path:
        """
        Retrace the path from parents to parents until start node
        """
        current_node = node
        path = []
        while current_node is not None:
            path.append((current_node.pos_y, current_node.pos_x))
            current_node = current_node.parent
        path.reverse()
        return path


if __name__ == "__main__":
    for idx, grid in enumerate(TEST_GRIDS):
        print(f"==grid-{idx + 1}==")

        init = (0, 0)
        goal = (len(grid) - 1, len(grid[0]) - 1)
        for elem in grid:
            print(elem)

        print("------")

        greedy_bf = GreedyBestFirst(grid, init, goal)
        path = greedy_bf.search()
        if path:
            for pos_x, pos_y in path:
                grid[pos_x][pos_y] = 2

            for elem in grid:
                print(elem)
