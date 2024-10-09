"""
https://tr.wikipedia.org/wiki/Çift_yönlü_arama
"""

from __future__ import annotations

import time
from math import sqrt

# Yazar: K. Umut Araz (https://github.com/arazumut)

# 1 için manhattan, 0 için öklid
HEURISTIC = 0

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],  # 0 serbest yol, 1 engel
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
]

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # yukarı, sol, aşağı, sağ

TPosition = tuple[int, int]


class Node:
    """
    >>> k = Node(0, 0, 4, 3, 0, None)
    >>> k..heuristic_hesapla()
    5.0
    >>> n = Node(1, 4, 3, 4, 2, None)
    >>> n.heuristic_hesapla()
    2.0
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
        g_cost: int,
        parent: Node | None,
    ) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_y, pos_x)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.g_cost = g_cost
        self.parent = parent
        self.h_cost = self.heuristic_hesapla()
        self.f_cost = self.g_cost + self.h_cost

    def heuristic_hesapla(self) -> float:
        """
        A* için Heuristic
        """
        dy = self.pos_x - self.goal_x
        dx = self.pos_y - self.goal_y
        if HEURISTIC == 1:
            return abs(dx) + abs(dy)
        else:
            return sqrt(dy**2 + dx**2)

    def __lt__(self, other: Node) -> bool:
        return self.f_cost < other.f_cost


class AStar:
    """
    >>> astar = AStar((0, 0), (len(grid) - 1, len(grid[0]) - 1))
    >>> (astar.start.pos_y + delta[3][0], astar.start.pos_x + delta[3][1])
    (0, 1)
    >>> [x.pos for x in astar.get_successors(astar.start)]
    [(1, 0), (0, 1)]
    >>> (astar.start.pos_y + delta[2][0], astar.start.pos_x + delta[2][1])
    (1, 0)
    >>> astar.yolu_geri_al(astar.start)
    [(0, 0)]
    >>> astar.ara()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3),
     (4, 3), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6)]
    """

    def __init__(self, start: TPosition, goal: TPosition):
        self.start = Node(start[1], start[0], goal[1], goal[0], 0, None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], 99999, None)

        self.open_nodes = [self.start]
        self.closed_nodes: list[Node] = []

        self.reached = False

    def ara(self) -> list[TPosition]:
        while self.open_nodes:
            # Açık Düğümler __lt__ kullanılarak sıralanır
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)

            if current_node.pos == self.target.pos:
                return self.yolu_geri_al(current_node)

            self.closed_nodes.append(current_node)
            successors = self.get_successors(current_node)

            for child_node in successors:
                if child_node in self.closed_nodes:
                    continue

                if child_node not in self.open_nodes:
                    self.open_nodes.append(child_node)
                else:
                    # en iyi mevcut yolu al
                    better_node = self.open_nodes.pop(self.open_nodes.index(child_node))

                    if child_node.g_cost < better_node.g_cost:
                        self.open_nodes.append(child_node)
                    else:
                        self.open_nodes.append(better_node)

        return [self.start.pos]

    def get_successors(self, parent: Node) -> list[Node]:
        """
        Haleflerin listesini döndürür (hem gridde hem de serbest alanlarda)
        """
        successors = []
        for action in delta:
            pos_x = parent.pos_x + action[1]
            pos_y = parent.pos_y + action[0]
            if not (0 <= pos_x <= len(grid[0]) - 1 and 0 <= pos_y <= len(grid) - 1):
                continue

            if grid[pos_y][pos_x] != 0:
                continue

            successors.append(
                Node(
                    pos_x,
                    pos_y,
                    self.target.pos_y,
                    self.target.pos_x,
                    parent.g_cost + 1,
                    parent,
                )
            )
        return successors

    def yolu_geri_al(self, node: Node | None) -> list[TPosition]:
        """
        Başlangıç düğümüne kadar ebeveynlerden yolu geri al
        """
        current_node = node
        path = []
        while current_node is not None:
            path.append((current_node.pos_y, current_node.pos_x))
            current_node = current_node.parent
        path.reverse()
        return path


class BidirectionalAStar:
    """
    >>> bd_astar = BidirectionalAStar((0, 0), (len(grid) - 1, len(grid[0]) - 1))
    >>> bd_astar.fwd_astar.start.pos == bd_astar.bwd_astar.target.pos
    True
    >>> bd_astar.çift_yönlü_yolu_geri_al(bd_astar.fwd_astar.start,
    ...                                     bd_astar.bwd_astar.start)
    [(0, 0)]
    >>> bd_astar.ara()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4),
     (2, 5), (3, 5), (4, 5), (5, 5), (5, 6), (6, 6)]
    """

    def __init__(self, start: TPosition, goal: TPosition) -> None:
        self.fwd_astar = AStar(start, goal)
        self.bwd_astar = AStar(goal, start)
        self.reached = False

    def ara(self) -> list[TPosition]:
        while self.fwd_astar.open_nodes or self.bwd_astar.open_nodes:
            self.fwd_astar.open_nodes.sort()
            self.bwd_astar.open_nodes.sort()
            current_fwd_node = self.fwd_astar.open_nodes.pop(0)
            current_bwd_node = self.bwd_astar.open_nodes.pop(0)

            if current_bwd_node.pos == current_fwd_node.pos:
                return self.çift_yönlü_yolu_geri_al(
                    current_fwd_node, current_bwd_node
                )

            self.fwd_astar.closed_nodes.append(current_fwd_node)
            self.bwd_astar.closed_nodes.append(current_bwd_node)

            self.fwd_astar.target = current_bwd_node
            self.bwd_astar.target = current_fwd_node

            successors = {
                self.fwd_astar: self.fwd_astar.get_successors(current_fwd_node),
                self.bwd_astar: self.bwd_astar.get_successors(current_bwd_node),
            }

            for astar in [self.fwd_astar, self.bwd_astar]:
                for child_node in successors[astar]:
                    if child_node in astar.closed_nodes:
                        continue

                    if child_node not in astar.open_nodes:
                        astar.open_nodes.append(child_node)
                    else:
                        # en iyi mevcut yolu al
                        better_node = astar.open_nodes.pop(
                            astar.open_nodes.index(child_node)
                        )

                        if child_node.g_cost < better_node.g_cost:
                            astar.open_nodes.append(child_node)
                        else:
                            astar.open_nodes.append(better_node)

        return [self.fwd_astar.start.pos]

    def çift_yönlü_yolu_geri_al(
        self, fwd_node: Node, bwd_node: Node
    ) -> list[TPosition]:
        fwd_path = self.fwd_astar.yolu_geri_al(fwd_node)
        bwd_path = self.bwd_astar.yolu_geri_al(bwd_node)
        bwd_path.pop()
        bwd_path.reverse()
        path = fwd_path + bwd_path
        return path


if __name__ == "__main__":
    # tüm koordinatlar [y,x] formatında verilir
    init = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    for elem in grid:
        print(elem)

    start_time = time.time()
    a_star = AStar(init, goal)
    path = a_star.ara()
    end_time = time.time() - start_time
    print(f"AStar çalışma süresi = {end_time:f} saniye")

    bd_start_time = time.time()
    bidir_astar = BidirectionalAStar(init, goal)
    bd_end_time = time.time() - bd_start_time
    print(f"BidirectionalAStar çalışma süresi = {bd_end_time:f} saniye")
