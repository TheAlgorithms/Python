"""
https://en.wikipedia.org/wiki/Bidirectional_search
"""

import time
from typing import List, Tuple

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],  # 0 are free path whereas 1's are obstacles
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
]

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # up, left, down, right


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

    def __init__(self, pos_x, pos_y, goal_x, goal_y, g_cost, parent):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_y, pos_x)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.g_cost = g_cost
        self.parent = parent
        self.h_cost = self.calculate_heuristic()
        self.f_cost = self.g_cost + self.h_cost

    def calculate_heuristic(self) -> float:
        """
        The heuristic here is the Manhattan Distance
        Could elaborate to offer more than one choice
        """
        dy = abs(self.pos_x - self.goal_x)
        dx = abs(self.pos_y - self.goal_y)
        return dx + dy

    def __lt__(self, other):
        return self.f_cost < other.f_cost


class AStar:
    def __init__(self, start, goal):
        self.start = Node(start[1], start[0], goal[1], goal[0], 0, None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], 99999, None)

        self.open_nodes = [self.start]
        self.closed_nodes = []

        self.reached = False

        self.path = [(self.start.pos_y, self.start.pos_x)]
        self.costs = [0]

    def search(self):
        while self.open_nodes:
            # Open Nodes are sorted using __lt__
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)

            if current_node.pos == self.target.pos:
                self.reached = True
                self.path = self.retrace_path(current_node)
                break

            self.closed_nodes.append(current_node)
            successors = self.get_successors(current_node)

            for child_node in successors:
                if child_node in self.closed_nodes:
                    continue

                if child_node not in self.open_nodes:
                    self.open_nodes.append(child_node)
                else:
                    # retrieve the best current path
                    better_node = self.open_nodes.pop(self.open_nodes.index(child_node))

                    if child_node.g_cost < better_node.g_cost:
                        self.open_nodes.append(child_node)
                    else:
                        self.open_nodes.append(better_node)

        if not (self.reached):
            print("No path found")

    def get_successors(self, parent: Node) -> List[Node]:
        """
        Returns a list of successors (both in the grid and free spaces)
        """
        successors = []
        for action in delta:
            pos_x = parent.pos_x + action[1]
            pos_y = parent.pos_y + action[0]
            if not (0 < pos_x < len(grid[0]) - 1 and 0 < pos_y < len(grid) - 1):
                continue

            if grid[pos_y][pos_x] != 0:
                continue

            node_ = Node(
                pos_x,
                pos_y,
                self.target.pos_y,
                self.target.pos_x,
                parent.g_cost + 1,
                parent,
            )
            successors.append(node_)
        return successors

    def retrace_path(self, node: Node) -> List[Tuple[int]]:
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


class BidirectionalAStar:
    def __init__(self, start, goal):
        self.fwd_astar = AStar(start, goal)
        self.bwd_astar = AStar(goal, start)
        self.reached = False
        self.path = self.fwd_astar.path

    def search(self):
        while self.fwd_astar.open_nodes or self.bwd_astar.open_nodes:
            self.fwd_astar.open_nodes.sort()
            self.bwd_astar.open_nodes.sort()
            current_fwd_node = self.fwd_astar.open_nodes.pop(0)
            current_bwd_node = self.bwd_astar.open_nodes.pop(0)

            if current_bwd_node.pos == current_fwd_node.pos:
                self.reached = True
                self.retrace_bidirectional_path(current_fwd_node, current_bwd_node)
                break

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
                        # retrieve the best current path
                        better_node = astar.open_nodes.pop(
                            astar.open_nodes.index(child_node)
                        )

                        if child_node.g_cost < better_node.g_cost:
                            astar.open_nodes.append(child_node)
                        else:
                            astar.open_nodes.append(better_node)

    def retrace_bidirectional_path(
        self, fwd_node: Node, bwd_node: Node
    ) -> List[Tuple[int]]:
        fwd_path = self.fwd_astar.retrace_path(fwd_node)
        bwd_path = self.bwd_astar.retrace_path(bwd_node)
        fwd_path.reverse()
        path = fwd_path + bwd_path
        return path


# all coordinates are given in format [y,x]
init = (0, 0)
goal = (len(grid) - 1, len(grid[0]) - 1)
for elem in grid:
    print(elem)

start_time = time.time()
a_star = AStar(init, goal)
a_star.search()
end_time = time.time() - start_time
print(f"AStar execution time = {end_time:f} seconds")

bd_start_time = time.time()
bidir_astar = BidirectionalAStar(init, goal)
bidir_astar.search()
bd_end_time = time.time() - bd_start_time
print(f"BidirectionalAStar execution time = {bd_end_time:f} seconds")
