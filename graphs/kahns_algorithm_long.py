# Finding longest distance in Directed Acyclic Graph using KahnsAlgorithm
# https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
from collections import deque


def longest_distance(graph: dict[int, list[int]]) -> int:
    """
    Return the number of vertices on the longest path in a directed acyclic graph.

    The graph is an adjacency list whose keys are the vertices 0 to n - 1.
    A graph with no vertices has a longest distance of 0.

    >>> longest_distance({0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7],
    ...                   5: [6], 6: [7], 7: []})
    5
    >>> longest_distance({0: [1], 1: [2], 2: []})
    3
    >>> longest_distance({0: [1, 2], 1: [3], 2: [3], 3: []})
    3
    >>> longest_distance({0: [], 1: [], 2: []})
    1
    >>> longest_distance({0: []})
    1
    >>> longest_distance({})
    0
    """
    indegree = [0] * len(graph)
    queue: deque[int] = deque()
    long_dist = [1] * len(graph)

    for values in graph.values():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.popleft()
        for x in graph[vertex]:
            indegree[x] -= 1

            long_dist[x] = max(long_dist[x], long_dist[vertex] + 1)

            if indegree[x] == 0:
                queue.append(x)

    return max(long_dist, default=0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Adjacency list of Graph
    graph = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
    print(longest_distance(graph))