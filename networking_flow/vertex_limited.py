# Max-Flow reduction for vertex-limited networks (rather than edge-limited)
"""
Reduces a network that has vertex capacities into a network with edge capacities so that Ford-Fulkerson will work.
Explanation: https://en.wikipedia.org/wiki/Maximum_flow_problem#Maximum_flow_with_vertex_capacities
"""

def vertex_limited(graph, limits):
    max_flow_graph = [[0 for i in range(2*len(graph))] for j in range(2*len(graph))]
    
    # Give all directed edges infinite capacity
    for src_vertex in range(len(graph)):
        for dest_vertex in range(len(graph[0])):
            if (graph[src_vertex][dest_vertex] == 1):
                max_flow_graph[src_vertex][dest_vertex] = float('inf')

    # Expand all vertices into two vertices
    for src_vertex in range(len(graph)):
        # move all outbound edges of the vertex to the new vertex
        max_flow_graph[src_vertex + len(graph)] = max_flow_graph[src_vertex] 
        max_flow_graph[src_vertex] = [0 for i in range(len(max_flow_graph))]

        # create edge with capacity equal to the vertex's limit from original to the new vertex
        max_flow_graph[src_vertex][src_vertex + len(graph)] = limits[src_vertex]

    return max_flow_graph


# Test Case

from ford_fulkerson import ford_fulkerson

limits = [29, 12, 14, 20, 7, 29]
graph = [ # rows are source, columns are destination
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

mf_graph = vertex_limited(graph, limits)
print(mf_graph) # prints graph reduced to a standard flow network
print(ford_fulkerson(mf_graph, 0, len(mf_graph)-1)) # max flow should be 19