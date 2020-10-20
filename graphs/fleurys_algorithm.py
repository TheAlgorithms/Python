from collections import defaultdict


class Graph:
    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v) -> None:
        """
        Function to add edges to the graph
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def rmv_edge(self, u, v) -> None:
        """
        Remove u-v edge from the graph
        """
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def dfs_count(self, v, visited) -> int:
        """
        A DFS based function to count reachable vertices from v
        """
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count = count + self.dfs_count(i, visited)
        return count

    def is_valid_next_edge(self, u, v) -> bool:
        """
        The function to check if edge u-v can be considered as next edge in
         Euler Tour
        """

        if len(self.graph[u]) == 1:
            return True
        else:
            visited = [False] * self.v
            count1 = self.dfs_count(u, visited)

            self.rmv_edge(u, v)
            visited = [False] * self.v
            count2 = self.dfs_count(u, visited)

            self.add_edge(u, v)

            return count1 <= count2

    def print_euler_util(self, u) -> None:
        """
        To print the elular tour
        """
        for v in self.graph[u]:
            if self.is_valid_next_edge(u, v):
                print("%d-%d " % (u, v)),
                self.rmv_edge(u, v)
                self.print_euler_util(v)

    def print_euler_tour(self) -> None:
        """
        The main function that print Eulerian Trail. It first finds an odd
        degree vertex (if there is any) and then calls printEulerUtil()
        to print the path
        """
        u = 0
        for i in range(self.v):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        print("\n")
        self.print_euler_util(u)


if __name__ == "__main__":
    """
    Driver code
    """
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.print_euler_tour()

    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.print_euler_tour()

    graph = Graph(5)
    graph.add_edge(1, 0)
    graph.add_edge(0, 2)
    graph.add_edge(2, 1)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)
    graph.add_edge(3, 2)
    graph.add_edge(3, 1)
    graph.add_edge(2, 4)
    graph.print_euler_tour()
