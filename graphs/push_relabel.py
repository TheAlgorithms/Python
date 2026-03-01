"""
Push-Relabel Algorithm for Maximum Flow

More efficient than Ford-Fulkerson for dense graphs.
Uses preflow and height functions.

Time Complexity: O(V²√E) or O(V³) for basic implementation
Space Complexity: O(V²)
"""

from typing import List, Optional


class PushRelabel:
    """
    Push-Relabel (Goldberg-Tarjan) maximum flow algorithm.
    """
    
    def __init__(self, n: int):
        self.n = n
        self.capacity: List[List[int]] = [[0] * n for _ in range(n)]
        self.flow: List[List[int]] = [[0] * n for _ in range(n)]
        self.height = [0] * n
        self.excess = [0] * n
    
    def add_edge(self, u: int, v: int, cap: int) -> None:
        self.capacity[u][v] += cap
    
    def push(self, u: int, v: int) -> bool:
        """
        Push flow from u to v if possible.
        """
        residual = self.capacity[u][v] - self.flow[u][v]
        if residual <= 0 or self.height[u] <= self.height[v] or self.excess[u] <= 0:
            return False
        
        push_flow = min(self.excess[u], residual)
        self.flow[u][v] += push_flow
        self.flow[v][u] -= push_flow
        self.excess[u] -= push_flow
        self.excess[v] += push_flow
        return True
    
    def relabel(self, u: int) -> None:
        """
        Relabel vertex u to enable future pushes.
        """
        min_height = float('inf')
        for v in range(self.n):
            residual = self.capacity[u][v] - self.flow[u][v]
            if residual > 0:
                min_height = min(min_height, self.height[v])
        
        if min_height < float('inf'):
            self.height[u] = min_height + 1
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute maximum flow using push-relabel.
        
        Returns:
            Maximum flow value
        
        Example:
            >>> pr = PushRelabel(6)
            >>> edges = [(0,1,16), (0,2,13), (1,2,10), (1,3,12),
            ...          (2,4,14), (3,2,9), (3,5,20), (4,3,7), (4,5,4)]
            >>> for u,v,c in edges: pr.add_edge(u,v,c)
            >>> pr.max_flow(0, 5)
            23
        """
        n = self.n
        
        # Initialize preflow
        self.height[source] = n
        
        for v in range(n):
            cap = self.capacity[source][v]
            if cap > 0:
                self.flow[source][v] = cap
                self.flow[v][source] = -cap
                self.excess[v] = cap
                self.excess[source] -= cap
        
        # Process vertices with excess
        active = [v for v in range(n) if v != source and v != sink and self.excess[v] > 0]
        
        while active:
            u = active.pop()
            
            pushed = False
            for v in range(n):
                if self.push(u, v):
                    if v != source and v != sink and self.excess[v] == self.excess[u] + 1:
                        active.append(v)
                    pushed = True
                    if self.excess[u] == 0:
                        break
            
            if self.excess[u] > 0:
                if not pushed:
                    self.relabel(u)
                active.append(u)
        
        return self.excess[sink]


if __name__ == "__main__":
    import doctest
    doctest.testmod()