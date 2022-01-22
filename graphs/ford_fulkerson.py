"""
 An implementation of the Ford-Fulkerson algorithm that finds the maximum flow in a network.
"""


class MyGraph:

    def __init__(self, graph):
        """
        Constructor for graph: passing in an instance of graph & getting rows in graph
        :param graph:
        """
        self.graph = graph
        self.ROW = len(graph)

    def ford_fulkerson(self, src, sink):
        """
        Calculates the max flow in a network from a source vertex (s) to sink vertex (t) using the Ford-Fulkerson algorithm.
        Implemented from pseudocode found here: https://brilliant.org/wiki/ford-fulkerson-algorithm/.
        """

        # Flow starts at a value of 0
        max_flow = 0
        
        # Stores the path & is populated by breadth_first_search function
        path = self.ROW * [-1]

        # Augments flow along the path (ensures some path from source vertex to sink vertex is found)
        while self.breadth_first_search(path, src, sink):
            temp = sink
            # Calculates max flow in the path
            flow = float("Inf")

            while temp != src:
                # Calculates minimum residual capacity
                flow = min(flow, self.graph[path[temp]][temp])
                temp = path[temp]

            # Adds flow of path to cumulative flow to get max
            max_flow += flow

            # Updates all edges (residual capacity)
            row = sink
            while row != src:
                col = path[row]
                # Max-flow min-cut theorem: forward flow = -backward flow for edges so the flow is preserved
                # Forward direction residual capacities
                self.graph[row][col] += flow
                # Backward direction residual capacities
                self.graph[col][row] -= flow
                row = path[row]

        # Returns max flow value calculated from algorithm
        return max_flow

    def breadth_first_search(self, path, src, sink):
        """
        Checks if a path exists from the source vertex to the sink vertex using standard BFS algorithm.
        Implemented from pseudocode found here: https://en.wikipedia.org/wiki/Breadth-first_search.
        """
        # Starts with each vertex marked as "not visited"
        visited_node = self.ROW * [False]

        # Uses queue for breadth-first search (BFS)
        bfs_queue = [src]

        # Changes source vertex to visited ("True")
        visited_node[src] = True

        while bfs_queue:
            # Takes off the front vertex in queue
            front = bfs_queue.pop(0)

            # Gets adjacent vertices of front vertex
            for i, value in enumerate(self.graph[front]):
                if value > 0 and not visited_node[i]:
                    path[i] = front
                    # Mark vertex as visited if not yet visited
                    visited_node[i] = True
                    # Add vertex to queue
                    bfs_queue.append(i)

        # True if path exists from s (source vertex) to t (sink vertex)
        if visited_node[sink]:
            return True
        else:
            return False


if __name__ == "__main__":
    # Sample graph to test algorithm on -- from https://www.programiz.com/dsa/ford-fulkerson-algorithm
    TEST_GRAPH = [[0, 8, 0, 0, 3, 0],
                  [0, 0, 9, 0, 0, 0],
                  [0, 0, 0, 0, 7, 2],
                  [0, 0, 0, 0, 0, 5],
                  [0, 0, 7, 4, 0, 0],
                  [0, 0, 0, 0, 0, 0]]

    graph = MyGraph(TEST_GRAPH)

    # Source vertex (s)
    s = 0
    # Sink vertex (t)
    t = 5

    # Ultimate output print statement -- call our algorithm
    print(f"The maximum flow in this network from source vertex {s} to sink vertex {t} is {graph.ford_fulkerson(s, t)}.")
    # Prints: The maximum flow in this network from source vertex 0 to sink vertex 5 is 6.