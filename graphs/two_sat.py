"""
2-SAT (2-Satisfiability) Solver

Solves boolean satisfiability problems with 2 literals per clause.
Uses strongly connected components (Kosaraju's or Tarjan's).

Time Complexity: O(V + E) = O(n) where n is number of variables
Space Complexity: O(V + E)
"""

from typing import List, Tuple, Optional
from collections import defaultdict


class TwoSAT:
    """
    2-SAT solver using strongly connected components.

    Variable i is represented as:
    - 2*i: False literal (¬x_i)
    - 2*i+1: True literal (x_i)
    """

    def __init__(self, n: int):
        self.n = n  # Number of variables
        self.graph: defaultdict[int, List[int]] = defaultdict(list)
        self.rev_graph: defaultdict[int, List[int]] = defaultdict(list)

    def _var(self, i: int, val: bool) -> int:
        """Get literal index: 2*i for False, 2*i+1 for True."""
        return 2 * i + (1 if val else 0)

    def add_or(self, i: int, val_i: bool, j: int, val_j: bool) -> None:
        """
        Add clause (x_i = val_i) OR (x_j = val_j).

        Implications: ¬a → b and ¬b → a
        """
        a = self._var(i, val_i)
        b = self._var(j, val_j)
        not_a = a ^ 1
        not_b = b ^ 1

        # Add implication edges
        self.graph[not_a].append(b)
        self.graph[not_b].append(a)
        self.rev_graph[b].append(not_a)
        self.rev_graph[a].append(not_b)

    def add_implication(self, i: int, val_i: bool, j: int, val_j: bool) -> None:
        """Add implication: (x_i = val_i) → (x_j = val_j)."""
        a = self._var(i, val_i)
        b = self._var(j, val_j)
        self.graph[a].append(b)
        self.rev_graph[b].append(a)

    def add_nand(self, i: int, val_i: bool, j: int, val_j: bool) -> None:
        """Add constraint: NOT ((x_i = val_i) AND (x_j = val_j))."""
        self.add_or(i, not val_i, j, not val_j)

    def solve(self) -> Optional[List[bool]]:
        """
        Solve the 2-SAT problem.

        Returns:
            List of boolean assignments if satisfiable, None otherwise

        Example:
            >>> ts = TwoSAT(3)
            >>> ts.add_or(0, True, 1, False)   # x0 OR ¬x1
            >>> ts.add_or(1, True, 2, True)    # x1 OR x2
            >>> ts.add_or(0, False, 2, False)  # ¬x0 OR ¬x2
            >>> ts.solve()
            [True, True, False]
        """
        n = 2 * self.n

        # Kosaraju's algorithm
        visited = [False] * n
        order = []

        def dfs1(u: int):
            visited[u] = True
            for v in self.graph[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)

        for u in range(n):
            if not visited[u]:
                dfs1(u)

        # Reverse DFS
        component = [-1] * n
        current_comp = 0

        def dfs2(u: int):
            component[u] = current_comp
            for v in self.rev_graph[u]:
                if component[v] == -1:
                    dfs2(v)

        for u in reversed(order):
            if component[u] == -1:
                dfs2(u)
                current_comp += 1

        # Check satisfiability: x and ¬x must be in different components
        assignment = [False] * self.n
        for i in range(self.n):
            true_lit = self._var(i, True)
            false_lit = self._var(i, False)

            if component[true_lit] == component[false_lit]:
                return None  # Unsatisfiable

            # Assign based on topological order (higher component = later in topo sort)
            assignment[i] = component[true_lit] > component[false_lit]

        return assignment


def solve_2sat(
    n: int, clauses: List[Tuple[int, bool, int, bool]]
) -> Optional[List[bool]]:
    """
    Convenience function for 2-SAT.

    Args:
        n: Number of variables
        clauses: List of (var1, val1, var2, val2) representing (x1=val1) OR (x2=val2)

    Returns:
        Assignment if satisfiable, None otherwise
    """
    solver = TwoSAT(n)
    for i, vi, j, vj in clauses:
        solver.add_or(i, vi, j, vj)
    return solver.solve()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
