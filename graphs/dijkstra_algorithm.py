# Title: Dijkstra's Algorithm for finding single source shortest path from scratch
# Author: Shubham Malik
# References: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import math
import sys

# For storing the vertex set to retrieve node with the lowest distance


class PriorityQueue:
    """Priority queue implementation based on Min Heap"""

    def __init__(self):
        self.cur_size = 0
        self.array = []
        self.pos = {}  # To store the pos of node in array

    def isEmpty(self):
        """Returns True if the PriorityQueue is empty, else False"""
        return self.cur_size == 0

    def min_heapify(self, idx):
        """
        Ensures element at idx is well placed on the heap after change

        Note:
            element can only change to have a lower rank

        Args:
            idx (int): index of the element that has changed
        """
        lc = self.left(idx)
        rc = self.right(idx)
        if lc < self.cur_size and self.array(lc)[0] < self.array(idx)[0]:
            smallest = lc
        else:
            smallest = idx
        if rc < self.cur_size and self.array(rc)[0] < self.array(smallest)[0]:
            smallest = rc
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def insert(self, tup):
        """
        Inserts an element in the Priority Queue

        Args:
            (rank (int), value): element to insert

        Note:
            Lower rank means higher priority

        """
        self.pos[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])

    def extract_min(self):
        """
        Removes and return the min element at the top of the Priority Queue

        Returns:
            Element with lowest rank (highest priority)

        """
        min_node = self.array[0][1]
        self.array[0] = self.array[self.cur_size - 1]
        self.cur_size -= 1
        self.min_heapify(1)
        del self.pos[min_node]
        return min_node

    def left(self, i):
        """
        Returns the index of the left child

        Args:
            i (int): index

        Returns:
            int: index of the left child

        """
        return 2 * i + 1

    def right(self, i):
        """
        Returns the index of the right child

        Args:
            i (int): index

        Returns:
            int: index of the right child

        """
        return 2 * i + 2

    def par(self, i):
        """
        Returns the index of parent

        Args:
            i (int): index

        Returns:
            int: the index of the parent

        """
        return math.floor(i / 2)

    def swap(self, i, j):
        """
        Swaps array elements at indices i and j

        Args:
            i, j (int): indices which values will be swapped

        Updates:
            self.pos

        """
        self.pos[self.array[i][1]] = j
        self.pos[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def decrease_key(self, tup, new_d):
        """
        Decreases rank of tup (increases priority)

        Note:
            Assumes new_d is lower than tup[0] (lower rank is higher priority)

        Args:
            tup (int, something): (rank, value) pair representing element
            new_d (int): new rank

        """
        idx = self.pos[tup[1]]
        # assuming the new_d is atmost old_d
        self.array[idx] = (new_d, tup[1])
        while idx > 0 and self.array[self.par(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.par(idx))
            idx = self.par(idx)


class Graph:
    """
    Implementation of undirected graph with dijkstra algorithm

    Args:
        num (int): number of nodes in the graph
                   nodes should be between 0 and (num-1)

    """

    def __init__(self, num):
        self.adjList = {}  # To store graph: u -> (v,w)
        self.num_nodes = num  # Number of nodes in graph
        # To store the distance from source vertex
        self.dist = [0] * self.num_nodes
        self.par = [-1] * self.num_nodes  # To store the path

    def add_edge(self, u, v, w):
        """
        Adds undirect edge u <-> v with weight w

        Args:
            u (int): node1
            v (int): node2
            w (int): weight

        Examples:
            >>> graph.add_edge(0, 1, 4)

            adds the edge 0 -> 1(4) and 1 -> 0(4)

        """
        # Check if u already in graph
        if u in self.adjList.keys():
            self.adjList[u].append((v, w))
        else:
            self.adjList[u] = [(v, w)]

        # Assuming undirected graph
        if v in self.adjList.keys():
            self.adjList[v].append((u, w))
        else:
            self.adjList[v] = [(u, w)]

    def show_graph(self):
        """
        Prints the graph to the screen

        Examples:
            >>> graph = Graph(3)
            >>> graph.add_edge(0, 1, 4)
            >>> graph.add_edge(0, 2, 8)
            >>> graph.show_graph()
            0 -> 1(4) -> 2(8)
            1 -> 0(4)
            2 -> 0(8)

        """
        for u in self.adjList:
            print(u, "->", " -> ".join(str(f"{v}({w})") for v, w in self.adjList[u]))

    def dijkstra(self, src):
        """
        Computes the shortest distances from src

        Args:
            src (int): source node

        Updates:
            self.dist: contains the shortest distances to src

        """
        # Flush old junk values in par[]
        self.par = [-1] * self.num_nodes
        # src is the source node
        self.dist[src] = 0
        Q = PriorityQueue()
        Q.insert((0, src))  # (dist from src, node)
        for u in self.adjList.keys():
            if u != src:
                self.dist[u] = sys.maxsize  # Infinity
                self.par[u] = -1

        while not Q.isEmpty():
            u = Q.extract_min()  # Returns node with the min dist from source
            # Update the distance of all the neighbours of u and
            # if their prev dist was INFINITY then push them in Q
            for v, w in self.adjList[u]:
                new_dist = self.dist[u] + w
                if self.dist[v] > new_dist:
                    if self.dist[v] == sys.maxsize:
                        Q.insert((new_dist, v))
                    else:
                        Q.decrease_key((self.dist[v], v), new_dist)
                    self.dist[v] = new_dist
                    self.par[v] = u

        # Show the shortest distances from src
        self.show_distances(src)

    def show_distances(self, src):
        """
        Prints the distances to src on the screen

        Examples:
            >>> graph = Graph(3)
            >>> graph.add_edge(0, 1, 4)
            >>> graph.add_edge(0, 2, 7)
            >>> graph.add_edge(1, 2, 2)
            >>> graph.dijkstra(0)
            >>> graph.show_distances(0)
            Distances from node: 0
            Node 0 has distance: 0
            Node 1 has distance: 4
            Node 2 has distance: 6

        """
        print(f"Distance from node: {src}")
        for u in range(self.num_nodes):
            print(f"Node {u} has distance: {self.dist[u]}")

    def show_path(self, src, dest):
        """
        Prints the shortest path from src to dest

        Args:
            src (int): source
            dest (int): destination

        WARNING: Use if *after* calling dijkstra

        Examples:
            >>> graph = Graph(3)
            >>> graph.add_edge(0, 1, 4)
            >>> graph.add_edge(0, 2, 7)
            >>> graph.add_edge(1, 2, 2)
            >>> graph.dijkstra(0)
            >>> graph.show_path(0, 2)
            ----Path to reach 2 from 0----
            0 -> 1 -> 2
            Total cost of path: 6

        """
        path = []
        cost = 0
        temp = dest
        # Backtracking from dest to src
        while self.par[temp] != -1:
            path.append(temp)
            if temp != src:
                for v, w in self.adjList[temp]:
                    if v == self.par[temp]:
                        cost += w
                        break
            temp = self.par[temp]
        path.append(src)
        path.reverse()

        print(f"----Path to reach {dest} from {src}----")
        for u in path:
            print(f"{u}", end=" ")
            if u != dest:
                print("-> ", end="")

        print("\nTotal cost of path: ", cost)


if __name__ == "__main__":
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
    graph.show_graph()
    graph.dijkstra(0)
    graph.show_path(0, 4)

# OUTPUT
# 0 -> 1(4) -> 7(8)
# 1 -> 0(4) -> 2(8) -> 7(11)
# 7 -> 0(8) -> 1(11) -> 6(1) -> 8(7)
# 2 -> 1(8) -> 3(7) -> 8(2) -> 5(4)
# 3 -> 2(7) -> 4(9) -> 5(14)
# 8 -> 2(2) -> 6(6) -> 7(7)
# 5 -> 2(4) -> 3(14) -> 4(10) -> 6(2)
# 4 -> 3(9) -> 5(10)
# 6 -> 5(2) -> 7(1) -> 8(6)
# Distance from node: 0
# Node 0 has distance: 0
# Node 1 has distance: 4
# Node 2 has distance: 12
# Node 3 has distance: 19
# Node 4 has distance: 21
# Node 5 has distance: 11
# Node 6 has distance: 9
# Node 7 has distance: 8
# Node 8 has distance: 14
# ----Path to reach 4 from 0----
# 0 -> 7 -> 6 -> 5 -> 4
# Total cost of path:  21
