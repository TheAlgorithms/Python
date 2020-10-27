def dfs(visited: list, graph: dict, start: str) -> list:
    """
    Returns a list of the visited nodes using a depth first search
    from inputed graph in alphabetical order.
    
    >>> graph = {'A' : ['B', 'C', 'D', 'G'], 'B' : ['A', 'C', 'F', 'G'], 
    'C' : ['A', 'B', 'D', 'E', 'F', 'G'], 'D' : ['A', 'C', 'E', 'F'], 
    'E' : ['C', 'D', 'F'], 'F' : ['B', 'C', 'D', 'E'], 'G' : ['A', 'B', 'C']}

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

# Scripting
    
lst1 = []
lst2 = []

graph1 = {'A' : ['B'], 'B' : ['A', 'D'], 'C' : ['D', 'E'], 'D' : ['B', 'C', 'E'], 'E' : ['C', 'D']}
graph2 = {'0' : ['1'], '1' : ['0', '3'], '2' : ['3', '4'], '3' : ['1', '2', '4'], '4' : ['2', '3']}

print(dfs(lst1, graph1, 'E'))
print(dfs(lst2, graph2, '2'))

# Can be used with any type of graph, but it must be a string set!!