from typing import List
import heapq
from copy import deepcopy


class UniformCostSearch:
    def __init__(self, current, final, grid):
        self.m = len(grid[0])
        self.n = len(grid)

    # diagonal clockwise
    dxy1 = [
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
    ]
    # diagonal anti-clockwise
    dxy2 = [
        (-1, -1),
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (-1, 1),
    ]

    # start point and end point on same row and column right side
    dxy3 = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (-1, 1),
    ]
    # start point and end point on same row and column left side
    dxy4 = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]
    # start point and end point on same column and row down side
    dxy5 = [
        (1, 0),
        (0, 1),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]
    # start point and end point on same column and row up side
    dxy6 = [
        (0, -1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    def get_shortest_path(self, start, end, dist, dxy):
        shortest_path = []
        curr_node = end
        while curr_node != start:
            shortest_path.append(curr_node)
            row, col = curr_node
            min_cell = float("inf")
            next_cell = None
            for dr, dc in dxy:
                if (
                    0 <= row + dr < self.m
                    and 0 <= col + dc < self.n
                    and [row + dr, col + dc] not in shortest_path
                ):
                    if dist[row + dr][col + dc] <= min_cell:
                        min_cell = dist[row + dr][col + dc]
                        next_cell = [row + dr, col + dc]
            curr_node = next_cell
        shortest_path.append(start)
        return shortest_path

    def ucs(self, current, final, grid, prev, dxy, goal_answer):
        dist = [[float("inf") for _ in range(self.m)] for _ in range(self.n)]
        visited = [[0 for _ in range(self.m)] for _ in range(self.n)]

        x = current[0]
        y = current[1]
        dist[x][y] = 0
        final_cnt = 0
        heap = [(0, x, y)]
        while heap:
            d, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            visited[x][y] = 1
            if [x, y] in final:
                idxs = [ix for ix, iy in enumerate(final) if iy == [x, y]]
                if len(idxs) > 1:
                    return None
                if goal_answer[idxs[0]] == 10**8:
                    final_cnt += 1
                if goal_answer[idxs[0]] > d:
                    goal_answer[idxs[0]] = d
                if final_cnt == len(final):
                    path = self.get_shortest_path(current, final[0], dist, dxy)
                    return path
            for dx, dy in dxy:
                if (
                    0 <= x + dx < self.m
                    and 0 <= y + dy < self.n
                    and grid[x + dx][y + dy] != 1
                ):
                    weight = 1
                    diagonal_weight = 1.414
                    if (
                        (dx == -1 and dy == -1)
                        or (dx == 1 and dy == 1)
                        or (dx == 1 and dy == -1)
                        or (dx == -1 and dy == 1)
                    ):
                        new_dist = d + diagonal_weight
                    else:
                        new_dist = d + weight
                    if new_dist < dist[x + dx][y + dy]:
                        dist[x + dx][y + dy] = new_dist
                        prev[x + dx][y + dy] = (x, y)
                        heapq.heappush(heap, (new_dist, x + dx, y + dy))

    def your_algorithm(
        self, start_point: List[int], end_point: List[int], grid: List[List[int]]
    ) -> List[int]:
        prev = [[None for _ in range(self.m)] for _ in range(self.n)]
        dxy = []
        if start_point[1] - end_point[1] == 0 and start_point[0] - end_point[0] < 0:
            dxy = self.dxy5
        elif start_point[1] - end_point[1] == 0 and start_point[0] - end_point[0] > 0:
            dxy = self.dxy6
        elif start_point[0] - end_point[0] == 0 and start_point[1] - end_point[1] < 0:
            dxy = self.dxy4
        elif start_point[0] - end_point[0] == 0 and start_point[1] - end_point[1] > 0:
            dxy = self.dxy3
        elif start_point[0] - end_point[0] > 0:
            dxy = self.dxy2
        elif start_point[0] - end_point[0] < 0:
            dxy = self.dxy1
        goal_answer = []
        for cell in end_point:
            goal_answer.append(10**8)
        path = self.ucs(start_point, [end_point], grid, prev, dxy, goal_answer)
        return path


def run():
    executed_object = UniformCostSearch(
        [0, 7],
        [19, 17],
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
    )
    path_result = executed_object.your_algorithm(
        [0, 7],
        [19, 17],
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
    )
    print(path_result)


if __name__ == "__main__":
    run()
