# The depth first search is a tree searching algorithm that outputs the final
# tree from a graph that is inputed. More explanation can be found here:
# https://en.wikipedia.org/wiki/Depth-first_search#:~:text=Depth%2Dfirst%20search%20(DFS),along%20each%20branch%20before%20backtracking.

def depth_first_search(visited: list, graph: dict, start: str) -> list:
    """
    Returns a list of the visited nodes using a depth first search
    from inputed graph in alphabetical order.
    
    >>> lst = []
    graph = {'A' : ['B', 'C', 'D', 'G'], 'B' : ['A', 'C', 'F', 'G'], 'C' : ['A', 'B', 'D', 'E', 'F', 'G'], 'D' : ['A', 'C', 'E', 'F'], 'E' : ['C', 'D', 'F'], 'F' : ['B', 'C', 'D', 'E'], 'G' : ['A', 'B', 'C']}

    depth_first_search(lst, graph, 'A')

    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    >>> lst = []
    graph = {'A' : ['B'], 'B' : ['A', 'D'], 'C' : ['D', 'E'], 'D' : ['B', 'C', 'E'], 'E' : ['C', 'D']}

    depth_first_search(lst, graph, 'D')

    ['D', 'B', 'A', 'C', 'E']
    """

    if start not in visited:
        visited.append(start)
        for neighbour in graph[start]:
            depth_first_search(visited, graph, neighbour)
    
    return visited
    
lst = []

if __name__ == "__main__":
    import doctest
    doctest.testmod()
