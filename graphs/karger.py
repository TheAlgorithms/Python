"""
An implementation of Karger's Algorithm for partitioning a graph with a certain probability of finding the minimum edge cut.
"""

import random
from typing import Dict, List, Set, Tuple


# Adjacency list representation of this graph:
# https://en.wikipedia.org/wiki/File:Single_run_of_Karger%E2%80%99s_Mincut_algorithm.svg
TEST_GRAPH = {
    '1': ['2', '3', '4', '5'],
    '2': ['1', '3', '4', '5'],
    '3': ['1', '2', '4', '5', '10'],
    '4': ['1', '2', '3', '5', '6'],
    '5': ['1', '2', '3', '4', '7'],
    '6': ['7', '8', '9', '10', '4'],
    '7': ['6', '8', '9', '10', '5'],
    '8': ['6', '7', '9', '10'],
    '9': ['6', '7', '8', '10'],
    '10': ['6', '7', '8', '9', '3']
}


def partition_graph(graph: Dict[ str, List[str] ]) -> Set[ Tuple[str, str] ]:
    """
    Partitions a graph using Karger's Algorithm. Implemented from pseudocode found here:
    https://en.wikipedia.org/wiki/Karger%27s_algorithm.
    NOTE: This function involves random choices, meaning it will not give consistent outputs.
    
    Args:
        graph: A dictionary containing adacency lists for the graph. Nodes must be strings.
    
    Returns:
        The cutset of the cut found by Karger's Algorithm.

    >>> graph = {'0':['1'], '1':['0']}
    >>> partition_graph(graph)
    {('0', '1')}
    """
    # Dict that maps contracted nodes to a list of all the nodes it "contains."
    contracted_nodes = {node: {node} for node in graph}

    graph_copy = {node: graph[node][:] for node in graph}

    while len(graph_copy) > 2:

        # Choose a random edge.
        u = random.choice(list(graph_copy.keys()))
        v = random.choice(graph_copy[u])

        # Contract edge (u, v) to new node uv
        uv = u + v
        uv_neighbors = list(set(graph_copy[u] + graph_copy[v]))
        uv_neighbors.remove(u)
        uv_neighbors.remove(v)
        graph_copy[uv] = uv_neighbors
        for neighbor in uv_neighbors:
            graph_copy[neighbor].append(uv)

        contracted_nodes[uv] = set()
        for contracted_node in contracted_nodes[u]:
            contracted_nodes[uv].add(contracted_node)
        for contracted_node in contracted_nodes[v]:
            contracted_nodes[uv].add(contracted_node)

        # Remove nodes u and v.
        del graph_copy[u]
        del graph_copy[v]
        for neighbor in uv_neighbors:
            if u in graph_copy[neighbor]:
                graph_copy[neighbor].remove(u)
            if v in graph_copy[neighbor]:
                graph_copy[neighbor].remove(v)

    # Find cutset.
    cutset = set()
    groups = [contracted_nodes[node] for node in graph_copy]
    print(groups)
    for node in groups[0]:
        for neighbor in graph[node]:
            if neighbor in groups[1]:
                cutset.add((node, neighbor))
    return cutset

if __name__ == "__main__":
    print(partition_graph(TEST_GRAPH))
