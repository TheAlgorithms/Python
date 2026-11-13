"""Solve 2-SAT using an implication graph and Kosaraju's algorithm.

Each clause has two literals, such as ``(1, -2)`` for ``x1 OR NOT x2``.
A literal is a nonzero integer: positive for a variable and negative for its
negation. Variables are numbered from 1 to ``number_of_variables``.

A clause ``(a OR b)`` is equivalent to the implications ``NOT a -> b`` and
``NOT b -> a``. A formula is unsatisfiable exactly when some variable and
its negation belong to the same strongly connected component.

Time complexity: O(V + C), where V is the number of variables and C is the
number of clauses. Space complexity: O(V + C).

References:
    https://cp-algorithms.com/graph/2SAT.html
    https://en.wikipedia.org/wiki/2-satisfiability
"""

from itertools import combinations, combinations_with_replacement, product


def _implication_graph(
    number_of_variables: int, clauses: list[tuple[int, int]]
) -> tuple[list[list[int]], list[list[int]]]:
    """Build the forward and reverse graphs for the clauses.

    Each variable has two vertices: the positive literal at an even index
    and the negative literal at the next odd index. XOR 1 negates a literal.

    >>> _implication_graph(1, [(1, 1)])
    ([[], [0, 0]], [[1, 1], []])
    """
    vertex_count = 2 * number_of_variables
    graph: list[list[int]] = [[] for _ in range(vertex_count)]
    reversed_graph: list[list[int]] = [[] for _ in range(vertex_count)]

    for first, second in clauses:
        for literal in (first, second):
            if isinstance(literal, bool) or not isinstance(literal, int):
                msg = "Literals must be integers"
                raise TypeError(msg)
            if literal == 0 or abs(literal) > number_of_variables:
                msg = f"Literal {literal} is outside the range 1..{number_of_variables}"
                raise ValueError(msg)

        first_vertex = 2 * (abs(first) - 1) + (first < 0)
        second_vertex = 2 * (abs(second) - 1) + (second < 0)
        for source, target in (
            (first_vertex ^ 1, second_vertex),
            (second_vertex ^ 1, first_vertex),
        ):
            graph[source].append(target)
            reversed_graph[target].append(source)

    return graph, reversed_graph


def _kosaraju_components(
    graph: list[list[int]], reversed_graph: list[list[int]]
) -> list[int]:
    """Find strongly connected components using two iterative DFS passes.

    Both graphs must contain the same vertices and reversed edges.

    >>> _kosaraju_components([[1], [0]], [[1], [0]])
    [0, 0]
    """
    vertex_count = len(graph)
    visited = [False] * vertex_count
    finishing_order: list[int] = []

    # First pass: DFS finishing order in the original graph.
    # The explicit stack prevents recursion errors on long paths.
    for start in range(vertex_count):
        if visited[start]:
            continue
        visited[start] = True
        stack = [(start, 0)]
        while stack:
            vertex, edge_index = stack[-1]
            if edge_index == len(graph[vertex]):
                finishing_order.append(vertex)
                stack.pop()
                continue

            stack[-1] = (vertex, edge_index + 1)
            neighbor = graph[vertex][edge_index]
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append((neighbor, 0))

    # Second pass: visit the reversed graph in decreasing finishing order.
    components = [-1] * vertex_count
    component_id = 0
    for start in reversed(finishing_order):
        if components[start] != -1:
            continue
        components[start] = component_id
        stack_vertices = [start]
        while stack_vertices:
            vertex = stack_vertices.pop()
            for neighbor in reversed_graph[vertex]:
                if components[neighbor] == -1:
                    components[neighbor] = component_id
                    stack_vertices.append(neighbor)
        component_id += 1
    return components


def two_sat(
    number_of_variables: int, clauses: list[tuple[int, int]]
) -> list[bool] | None:
    """Return a satisfying assignment, or None if the 2-CNF formula is impossible.

    The returned list contains the truth values of x1, x2, ..., xN in order.
    For a satisfiable formula, more than one assignment may be valid.

    >>> two_sat(2, [(1, 2), (-1, 2), (1, -2)])
    [True, True]
    >>> two_sat(1, [(1, 1)])
    [True]
    >>> two_sat(1, [(-1, -1)])
    [False]
    >>> two_sat(1, [(1, 1), (-1, -1)]) is None
    True
    >>> two_sat(2, [(1, 2), (-1, 2), (1, -2), (-1, -2)]) is None
    True
    >>> two_sat(2, [(1, -1), (2, -2)])
    [True, True]
    >>> two_sat(0, [])
    []
    >>> two_sat(2, [])
    [True, True]
    >>> two_sat(2, [(0, 1)])
    Traceback (most recent call last):
    ...
    ValueError: Literal 0 is outside the range 1..2
    >>> two_sat(2, [(3, 1)])
    Traceback (most recent call last):
    ...
    ValueError: Literal 3 is outside the range 1..2
    >>> two_sat(-1, [])
    Traceback (most recent call last):
    ...
    ValueError: Number of variables must be nonnegative
    >>> two_sat(1, [(True, 1)])
    Traceback (most recent call last):
    ...
    TypeError: Literals must be integers
    """
    if isinstance(number_of_variables, bool) or not isinstance(
        number_of_variables, int
    ):
        msg = "Number of variables must be an integer"
        raise TypeError(msg)
    if number_of_variables < 0:
        msg = "Number of variables must be nonnegative"
        raise ValueError(msg)

    graph, reversed_graph = _implication_graph(number_of_variables, clauses)
    components = _kosaraju_components(graph, reversed_graph)

    assignment: list[bool] = []
    for variable in range(number_of_variables):
        positive = 2 * variable
        negative = positive ^ 1
        if components[positive] == components[negative]:
            return None
        assignment.append(components[positive] > components[negative])
    return assignment


def test_two_sat_against_brute_force() -> None:
    """Compare the solver with exhaustive truth tables for small formulas.

    This verifies both satisfiability and every returned assignment, not only
    the solver's ability to round-trip its own representation.

    >>> test_two_sat_against_brute_force()
    """
    for variable_count in (1, 2, 3):
        literals = [value for i in range(1, variable_count + 1) for value in (i, -i)]
        possible_clauses = list(combinations_with_replacement(literals, 2))
        for clause_count in range(4):
            for selected_clauses in combinations(possible_clauses, clause_count):
                clauses = list(selected_clauses)
                actual = two_sat(variable_count, clauses)
                expected_satisfiable = any(
                    all(
                        values[abs(a) - 1] == (a > 0) or values[abs(b) - 1] == (b > 0)
                        for a, b in clauses
                    )
                    for values in product((False, True), repeat=variable_count)
                )
                assert (actual is not None) == expected_satisfiable
                if actual is not None:
                    assert all(
                        actual[abs(a) - 1] == (a > 0) or actual[abs(b) - 1] == (b > 0)
                        for a, b in clauses
                    )

    # A long implication chain must not raise RecursionError.
    variable_count = 2_000
    long_chain = [(1, 1)]
    long_chain.extend((-i, i + 1) for i in range(1, variable_count))
    assert two_sat(variable_count, long_chain) == [True] * variable_count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
