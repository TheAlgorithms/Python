import sys
from collections import defaultdict


class Heap:
    def __init__(self):
        self.node_position = []

    def get_position(self, vertex):
        return self.node_position[vertex]

    def set_position(self, vertex, pos):
        self.node_position[vertex] = pos

    def top_to_bottom(self, heap, start, size, positions):
        if start > size // 2 - 1:
            return
        else:
            if 2 * start + 2 >= size:
                m = 2 * start + 1
            else:
                if heap[2 * start + 1] < heap[2 * start + 2]:
                    m = 2 * start + 1
                else:
                    m = 2 * start + 2
            if heap[m] < heap[start]:
                temp, temp1 = heap[m], positions[m]
                heap[m], positions[m] = heap[start], positions[start]
                heap[start], positions[start] = temp, temp1

                temp = self.get_position(positions[m])
                self.set_position(positions[m], self.get_position(positions[start]))
                self.set_position(positions[start], temp)

                self.top_to_bottom(heap, m, size, positions)

    # Update function if value of any node in min-heap decreases
    def bottom_to_top(self, val, index, heap, position):
        temp = position[index]

        while index != 0:
            if index % 2 == 0:
                parent = int((index - 2) / 2)
            else:
                parent = int((index - 1) / 2)

            if val < heap[parent]:
                heap[index] = heap[parent]
                position[index] = position[parent]
                self.set_position(position[parent], index)
            else:
                heap[index] = val
                position[index] = temp
                self.set_position(temp, index)
                break
            index = parent
        else:
            heap[0] = val
            position[0] = temp
            self.set_position(temp, 0)

    def heapify(self, heap, positions):
        start = len(heap) // 2 - 1
        for i in range(start, -1, -1):
            self.top_to_bottom(heap, i, len(heap), positions)

    def delete_minimum(self, heap, positions):
        temp = positions[0]
        heap[0] = sys.maxsize
        self.top_to_bottom(heap, 0, len(heap), positions)
        return temp


def prisms_algorithm(l):
    """
    >>> l = {0: [[1, 1], [3, 3]],
    ...      1: [[0, 1], [2, 6], [3, 5], [4, 1]],
    ...      2: [[1, 6], [4, 5], [5, 2]],
    ...      3: [[0, 3], [1, 5], [4, 1]],
    ...      4: [[1, 1], [2, 5], [3, 1], [5, 4]],
    ...      5: [[2, 2], [4, 4]]}
    >>> prisms_algorithm(l)
    [(0, 1), (1, 4), (4, 3), (4, 5), (5, 2)]
    """

    heap = Heap()

    visited = [0 for i in range(len(l))]
    nbr_tv = [-1 for i in range(len(l))]  # Neighboring Tree Vertex of selected vertex
    # Minimum Distance of explored vertex with neighboring vertex of partial tree
    # formed in graph
    distance_tv = []  # Heap of Distance of vertices from their neighboring vertex
    positions = []

    for x in range(len(l)):
        p = sys.maxsize
        distance_tv.append(p)
        positions.append(x)
        heap.node_position.append(x)

    tree_edges = []
    visited[0] = 1
    distance_tv[0] = sys.maxsize
    for x in l[0]:
        nbr_tv[x[0]] = 0
        distance_tv[x[0]] = x[1]
    heap.heapify(distance_tv, positions)

    for _ in range(1, len(l)):
        vertex = heap.delete_minimum(distance_tv, positions)
        if visited[vertex] == 0:
            tree_edges.append((nbr_tv[vertex], vertex))
            visited[vertex] = 1
            for v in l[vertex]:
                if visited[v[0]] == 0 and v[1] < distance_tv[heap.get_position(v[0])]:
                    distance_tv[heap.get_position(v[0])] = v[1]
                    heap.bottom_to_top(
                        v[1], heap.get_position(v[0]), distance_tv, positions
                    )
                    nbr_tv[v[0]] = vertex
    return tree_edges


if __name__ == "__main__":  # pragma: no cover
    # < --------- Prims Algorithm --------- >
    n = int(input("Enter number of vertices: ").strip())
    e = int(input("Enter number of edges: ").strip())
    adjlist = defaultdict(list)
    for x in range(e):
        l = [int(x) for x in input().strip().split()]
        adjlist[l[0]].append([l[1], l[2]])
        adjlist[l[1]].append([l[0], l[2]])
    print(prisms_algorithm(adjlist))
