# The depth first search is a tree searching algorithm that outputs the final
# tree from a graph that is inputed. More explanation can be found here:
# https://en.wikipedia.org/wiki/Depth-first_search#:~:text=Depth%2Dfirst%20search%20(DFS),along%20each%20branch%20before%20backtracking.

def dfs(visited: list, graph: dict, start: str) -> list:
    """
    Returns a list of the visited nodes using a depth first search
    from inputed graph in alphabetical order.
    
    >>> graph = {'A' : ['B', 'C', 'D', 'G'], 'B' : ['A', 'C', 'F', 'G'], 'C' : ['A', 'B', 'D', 'E', 'F', 'G'], 'D' : ['A', 'C', 'E', 'F'], 'E' : ['C', 'D', 'F'], 'F' : ['B', 'C', 'D', 'E'], 'G' : ['A', 'B', 'C']}

    dfs(graph, 'A')

    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    >>> graph = {'A' : ['B'], 'B' : ['D'], 'C' : ['D', 'E'], 'D' : ['B'], 'E' : ['C', 'D']}

    dfs(graph, 'D')

    ['D', 'B', 'A', 'C', 'E']
    """

    if start not in visited:
        visited.append(start)
        for neighbour in graph[start]:
            dfs(visited, graph, neighbour)
    
    return visited
    
lst = []

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Can be used with any type of graph, but it must be a string set!!
