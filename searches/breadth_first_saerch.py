# BFS algorithm in Python

"""
This is the implementation of the breadth-first search algorithm

For doctests run following commmand:
python3 -m doctest -v breadth_first_search.py

For manual testing run:
python3 breadth_first_search.py
"""

import collections
import unittest
import doctest

# BFS algorithm
"""
def function() -> None;
"""
def bfs(graph, root):
    """
    The graph in the function will take the values of the given nodes
    while root has the main node's value.
    """
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


"""
The graph has some values which are hard-codded and this graph has 0-3 index
having different nodes.

"""

if __name__ == "__main__":
    graph = {0: [3, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
    
    doctest.testmod()
    unittest.main()
"""
For Explanation visit: https://en.wikipedia.org/wiki/Breadth-first_search
"""
