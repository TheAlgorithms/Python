"""
Ford-Fulkerson Algorithm with Edmonds-Karp Implementation

Maximum flow using BFS for shortest augmenting paths.
Edmonds-Karp: O(VE²) - polynomial time guarantee

Time Complexity: O(VE²)
Space Complexity: O(V²)
"""

from typing import List, Tuple, Optional
from collections import deque


class FordFulkerson:
    """
    Maximum flow using Ford-Fulkerson with Edmonds-Karp (BFS).
    """
    
    def __init__(self, n: int):
        self.n = n
        # Residual graph as adjacency matrix
        self.capacity: List[List[int]] = [[0] * n for _ in range(n)]
        self.flow: List[List[int]] = [[0] * n for _ in range(n)]
    
    def add_edge(self, u: int, v: int, cap: int) -> None:
        """Add directed edge with capacity."""
        self.capacity[u][v] += cap
    
    def bfs(self, source: int, sink: int) -> Tuple[bool, List[Optional[int]]]:
        """
        Find shortest augmenting path using BFS.
        
        Returns:
            Tuple of (found_path, parent_array)
        """
        parent: List[Optional[int]] = [None] * self.n
        parent[source] = -1
        queue = deque([source])
        
        while queue and parent[sink] is None:
            u = queue.popleft()
            
            for v in range(self.n):
                residual = self.capacity[u][v] - self.flow[u][v]
                if parent[v] is None and residual > 0:
                    parent[v] = u
                    queue.append(v)
        
        return parent[sink] is not None, parent
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute maximum flow from source to sink.
        
        Returns:
            Maximum flow value
        
        Example:
            >>> ff = FordFulkerson(6)
            >>> edges = [(0,1,16), (0,2,13), (1,2,10), (1,3,12), 
            ...          (2,4,14), (3,2,9), (3,5,20), (4,3,7), (4,5,4)]
            >>> for u,v,c in edges: ff.add_edge(u,v,c)
            >>> ff.max_flow(0, 5)
            23
        """
        total_flow = 0
        
        while True:
            found, parent = self.bfs(source, sink)
            if not found:
                break
            
            # Find minimum residual capacity along path
            path_flow = float('inf')
            s = sink
            while s != source:
                u = parent[s]  # type: ignore
                residual = self.capacity[u][s] - self.flow[u][s]
                path_flow = min(path_flow, residual)
                s = u
            
            # Update flow along path
            s = sink
            while s != source:
                u = parent[s]  # type: ignore
                self.flow[u][s] += path_flow
                self.flow[s][u] -= path_flow  # Reverse edge
                s = u
            
            total_flow += path_flow
        
        return total_flow
    
    def get_flow_edges(self) -> List[Tuple[int, int, int]]:
        """
        Get edges with positive flow.
        """
        edges = []
        for u in range(self.n):
            for v in range(self.n):
                if self.flow[u][v] > 0:
                    edges.append((u, v, self.flow[u][v]))
        return edges


def ford_fulkerson(capacity: List[List[int]], 
                   source: int, 
                   sink: int) -> int:
    """
    Convenience function for Ford-Fulkerson.
    
    Args:
        capacity: Capacity matrix
        source: Source vertex
        sink: Sink vertex
    
    Returns:
        Maximum flow
    """
    n = len(capacity)
    ff = FordFulkerson(n)
    ff.capacity = [row[:] for row in capacity]
    return ff.max_flow(source, sink)


if __name__ == "__main__":
    import doctest
    doctest.testmod()