# Title: Dijkstra's Algorithm for finding the single-source shortest path in a graph
# Author: Shubham Malik
# References: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import math
import sys
from collections import defaultdict


class PriorityQueue:
    """
    Priority queue class.
    For storing a vertex set to retrieve node with the lowest distance.
    Based on Min Heap.
    """

    def __init__(self) -> None:
        """
        Class constructor method.

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.cur_size
        0
        >>> priority_queue_test.array
        []
        >>> priority_queue_test.node_positions
        {}
        """
        self.cur_size = 0
        self.array = []
        self.node_positions = {}  # To store the pos of node in array

    def is_empty(self) -> bool:
        """
        Conditional boolean method to determine if the priority queue is empty or not.

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.is_empty()
        True
        >>> priority_queue_test.insert((2, 'A'))
        >>> priority_queue_test.is_empty()
        False
        """
        return self.cur_size == 0

    def min_heapify(self, idx) -> None:
        """
        Sorts the queue array so that the minimum element is root.

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.cur_size = 3
        >>> priority_queue_test.node_positions = {'A': 0, 'B': 1, 'C': 2}

        >>> priority_queue_test.array = [(5, 'A'), (10, 'B'), (15, 'C')]
        >>> priority_queue_test.min_heapify(0)
        >>> priority_queue_test.array
        [(5, 'A'), (10, 'B'), (15, 'C')]

        >>> priority_queue_test.array = [(10, 'A'), (5, 'B'), (15, 'C')]
        >>> priority_queue_test.min_heapify(0)
        >>> priority_queue_test.array
        [(5, 'B'), (10, 'A'), (15, 'C')]

        >>> priority_queue_test.array = [(10, 'A'), (15, 'B'), (5, 'C')]
        >>> priority_queue_test.min_heapify(0)
        >>> priority_queue_test.array
        [(5, 'C'), (15, 'B'), (10, 'A')]

        >>> priority_queue_test.array = [(10, 'A'), (5, 'B')]
        >>> priority_queue_test.cur_size = len(priority_queue_test.array)
        >>> priority_queue_test.node_positions = {'A': 0, 'B': 1}
        >>> priority_queue_test.min_heapify(0)
        >>> priority_queue_test.array
        [(5, 'B'), (10, 'A')]
        """
        left_child = self.left_child(idx)
        right_child = self.right_child(idx)

        smallest = idx

        if (
            left_child < self.cur_size
            and self.array[left_child][0] < self.array[idx][0]
        ):
            smallest = left_child

        if (
            right_child < self.cur_size
            and self.array[right_child][0] < self.array[smallest][0]
        ):
            smallest = right_child

        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def insert(self, tup) -> None:
        """
        Inserts a node into the Priority Queue.

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.insert((10, 'A'))
        >>> priority_queue_test.array
        [(10, 'A')]
        >>> priority_queue_test.insert((15, 'B'))
        >>> priority_queue_test.array
        [(10, 'A'), (15, 'B')]
        >>> priority_queue_test.insert((5, 'C'))
        >>> priority_queue_test.array
        [(5, 'C'), (10, 'A'), (15, 'B')]
        """
        self.node_positions[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])

    def extract_min(self) -> str:
        """
        Removes and returns the min element at top of priority queue.

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.array = [(10, 'A'), (15, 'B')]
        >>> priority_queue_test.cur_size = len(priority_queue_test.array)
        >>> priority_queue_test.node_positions = {'A': 0, 'B': 1}
        >>> priority_queue_test.insert((5, 'C'))
        >>> priority_queue_test.extract_min()
        'C'
        >>> priority_queue_test.array[0]
        (10, 'A')
        """
        min_node = self.array[0][1]
        self.array[0] = self.array[self.cur_size - 1]
        self.cur_size -= 1
        self.min_heapify(0)
        del self.node_positions[min_node]
        return min_node

    @staticmethod
    def left_child(i) -> int:
        """
        Returns the index of left child

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.left_child(0)
        1
        >>> priority_queue_test.left_child(1)
        3
        """
        return 2 * i + 1

    @staticmethod
    def right_child(i) -> int:
        """
        Returns the index of right child

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.right_child(0)
        2
        >>> priority_queue_test.right_child(1)
        4
        """
        return 2 * i + 2

    @staticmethod
    def parent_idx(i) -> int:
        """
        Returns the index of parent

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.parent_idx(2)
        1
        >>> priority_queue_test.parent_idx(4)
        2
        """
        return math.floor(i / 2)

    def swap(self, i, j) -> None:
        """
        Swaps array elements at indices i and j, update the pos{}

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.array = [(10, 'A'), (15, 'B')]
        >>> priority_queue_test.cur_size = len(priority_queue_test.array)
        >>> priority_queue_test.node_positions = {'A': 0, 'B': 1}
        >>> priority_queue_test.swap(0, 1)
        >>> priority_queue_test.array
        [(15, 'B'), (10, 'A')]
        >>> priority_queue_test.node_positions
        {'A': 1, 'B': 0}
        """
        self.node_positions[self.array[i][1]] = j
        self.node_positions[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def decrease_key(self, tup, new_d) -> None:
        """
        Decrease the key value for a given tuple, assuming the new_d is at most old_d.
        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.array = [(10, 'A'), (15, 'B')]
        >>> priority_queue_test.cur_size = len(priority_queue_test.array)
        >>> priority_queue_test.node_positions = {'A': 0, 'B': 1}
        >>> priority_queue_test.decrease_key((10, 'A'), 5)
        >>> priority_queue_test.array
        [(5, 'A'), (15, 'B')]
        """
        idx = self.node_positions[tup[1]]
        self.array[idx] = (new_d, tup[1])
        while idx > 0 and self.array[self.parent_idx(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.parent_idx(idx))
            idx = self.parent_idx(idx)


class Graph:
    """
    Graph class for computing Dijkstra's algorithm
    """

    def __init__(self, num_nodes) -> None:
        """
        Class constructor

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.num_nodes
        1
        >>> graph_test.dist_from_src
        [0]
        >>> graph_test.parent_idx
        [-1]
        >>> graph_test.get_adjacency_list()
        {}
        """
        self.adjacency_list = defaultdict(list)  # To store graph: u -> (v,w)
        self.num_nodes = num_nodes  # Number of nodes in graph
        self.dist_from_src = [
            0
        ] * self.num_nodes  # To store the distance from source vertex
        self.parent_idx = [-1] * self.num_nodes  # To store the path

    def get_adjacency_list(self) -> dict:
        """
        Returns the defaultdict adjacency_list converted to dict()
        """
        return dict(self.adjacency_list)

    def add_edge(self, u, v, w) -> None:
        """
        Add edge going from node u to v and v to u with weight w: u (w)-> v, v (w) -> u

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.add_edge(1, 2, 1)
        >>> graph_test.add_edge(2, 3, 2)
        >>> graph_test.get_adjacency_list()
        {1: [(2, 1)], 2: [(1, 1), (3, 2)], 3: [(2, 2)]}

        >>> graph_test.add_edge(2, 4, -1)
        Traceback (most recent call last):
        ...
        AssertionError: Dijkstra algorithm does not support negative edge weights!
        """
        assert w >= 0, "Dijkstra algorithm does not support negative edge weights!"
        self.adjacency_list[u].append((v, w))
        self.adjacency_list[v].append((u, w))

    def show_graph(self) -> None:
        """
        Show the graph: u -> v(w)

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.add_edge(1, 2, 1)
        >>> graph_test.show_graph()
        1 -> 2(1)
        2 -> 1(1)
        >>> graph_test.add_edge(2, 3, 2)
        >>> graph_test.show_graph()
        1 -> 2(1)
        2 -> 1(1) -> 3(2)
        3 -> 2(2)
        """
        for u in self.adjacency_list:
            print(
                u,
                "->",
                " -> ".join(str(f"{v}({w})") for v, w in self.adjacency_list[u]),
            )

    def dijkstra(self, src, is_show_distance=True) -> None:
        """
        Dijkstra algorithm

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        >>> graph_test.dist_from_src
        [0]

        >>> graph_test = Graph(3)
        >>> graph_test.add_edge(0, 1, 2)
        >>> graph_test.add_edge(1, 2, 2)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 2
        Node 2 has distance: 4
        >>> graph_test.dist_from_src
        [0, 2, 4]

        >>> graph_test = Graph(2)
        >>> graph_test.add_edge(0, 1, 2)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 2
        >>> graph_test.dist_from_src
        [0, 2]

        >>> graph_test = Graph(3)
        >>> graph_test.add_edge(0, 1, 2)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 2
        Node 2 has distance: 9223372036854775807
        >>> graph_test.dist_from_src
        [0, 2, 9223372036854775807]

        >>> graph_test = Graph(3)
        >>> graph_test.add_edge(0, 1, 2)
        >>> graph_test.add_edge(1, 2, 2)
        >>> graph_test.add_edge(0, 2, 1)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 2
        Node 2 has distance: 1
        >>> graph_test.dist_from_src
        [0, 2, 1]
        """
        self.dist_from_src = [
            sys.maxsize
        ] * self.num_nodes  # init with inf values for all node distances
        self.parent_idx = [-1] * self.num_nodes  # flush old junk values in par[]
        self.dist_from_src[src] = 0  # src is the source node

        priority_queue = PriorityQueue()
        priority_queue.insert((0, src))  # (dist from src, node)
        priority_queue_vertex_tracker = set(
            range(self.num_nodes)
        )  # track all vertices initially

        while not priority_queue.is_empty():
            u = (
                priority_queue.extract_min()
            )  # return node with the min dist from source

            if u in priority_queue_vertex_tracker:
                priority_queue_vertex_tracker.remove(
                    u
                )  # Remove u from tracker since it's extracted

            for v, w in self.adjacency_list[u]:
                new_dist = self.dist_from_src[u] + w

                if self.dist_from_src[v] > new_dist:
                    self.dist_from_src[v] = new_dist
                    self.parent_idx[v] = u

                    if (
                        v in priority_queue_vertex_tracker
                        and v in priority_queue.node_positions
                    ):
                        priority_queue.decrease_key(
                            (self.dist_from_src[v], v), new_dist
                        )
                        priority_queue_vertex_tracker.remove(v)
                    else:
                        priority_queue.insert((new_dist, v))

        if is_show_distance:
            self.show_distances(src)  # Show the shortest distances from src

    def show_distances(self, src) -> None:
        """
        Show the distances from src to all other nodes in a graph

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.show_distances(0)
        Distance from node: 0
        Node 0 has distance: 0
        """
        print(f"Distance from node: {src}")
        for u in range(self.num_nodes):
            print(f"Node {u} has distance: {self.dist_from_src[u]}")

    def show_path(self, src, dest):
        """
        Shows the shortest path from src to dest.
        WARNING: Use it *after* calling dijkstra.

        Examples:
        >>> graph_test = Graph(4)
        >>> graph_test.add_edge(0, 1, 1)
        >>> graph_test.add_edge(1, 2, 2)
        >>> graph_test.add_edge(2, 3, 3)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 1
        Node 2 has distance: 3
        Node 3 has distance: 6
        >>> graph_test.show_path(0, 3)
        ----Path to reach 3 from 0----
        0 -> 1 -> 2 -> 3
        Total cost of path:  6
        """
        path = []
        cost = 0
        temp = dest
        # Backtracking from dest to src
        while self.parent_idx[temp] != -1:
            path.append(temp)
            if temp != src:
                for v, w in self.adjacency_list[temp]:
                    if v == self.parent_idx[temp]:
                        cost += w
                        break
            temp = self.parent_idx[temp]
        path.append(src)
        path.reverse()

        print(f"----Path to reach {dest} from {src}----")
        for u in path:
            print(f"{u}", end="")
            if u != dest:
                print(" -> ", end="")

        print("\nTotal cost of path: ", cost)


if __name__ == "__main__":
    from doctest import testmod
    from timeit import timeit

    testmod()

    def init_test_graph():
        graph = Graph(9)
        graph.add_edge(0, 1, 4)
        graph.add_edge(0, 7, 8)
        graph.add_edge(1, 2, 8)
        graph.add_edge(1, 7, 11)
        graph.add_edge(2, 3, 7)
        graph.add_edge(2, 8, 2)
        graph.add_edge(2, 5, 4)
        graph.add_edge(3, 4, 9)
        graph.add_edge(3, 5, 14)
        graph.add_edge(4, 5, 10)
        graph.add_edge(5, 6, 2)
        graph.add_edge(6, 7, 1)
        graph.add_edge(6, 8, 6)
        graph.add_edge(7, 8, 7)
        return graph

    print("\nGraph prior to Dijkstra algorithm sorting:")
    test_graph = init_test_graph()
    test_graph.show_graph()

    num_runs = 1000
    timer_dijkstra = timeit(
        setup="graph = init_test_graph()",
        stmt="graph.dijkstra(0, False)",
        globals=globals(),
        number=num_runs,
    )
    print(f"\nDijkstra processing time: {timer_dijkstra:.5f} s for {num_runs} runs")

    print("\nGraph after Dijkstra algorithm sorting:")
    test_graph.dijkstra(src=0, is_show_distance=False)
    test_graph.show_graph()
