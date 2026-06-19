#!/usr/bin/env python3
"""
Auto-fix script for TheAlgorithms/Python PR ruff errors.
Run from repo root: python fix_ruff_errors.py
"""

from pathlib import Path


def fix_floyd_warshall():
    p = Path("graphs/floyd_warshall.py")
    text = p.read_text()
    text = text.replace(
        "current = next_node[current][end]  # type: ignore",
        "current = next_node[current][end]  # type: ignore[assignment]",
    )
    p.write_text(text)
    print("fixed graphs/floyd_warshall.py")


def fix_ford_fulkerson():
    p = Path("graphs/ford_fulkerson.py")
    text = p.read_text()
    text = text.replace(
        "u = parent[s]  # type: ignore", "u = parent[s]  # type: ignore[assignment]"
    )
    p.write_text(text)
    print("fixed graphs/ford_fulkerson.py")


def fix_heavy_light_decomposition():
    p = Path("graphs/heavy_light_decomposition.py")
    text = p.read_text()
    old = """        # Same chain now
        l, r = self.pos[u], self.pos[v]
        if l > r:
            l, r = r, l
        segment = self.base_array[l : r + 1]"""
    new = """        # Same chain now
        left_idx, right_idx = self.pos[u], self.pos[v]
        if left_idx > right_idx:
            left_idx, right_idx = right_idx, left_idx
        segment = self.base_array[left_idx : right_idx + 1]"""
    text = text.replace(old, new)
    p.write_text(text)
    print("fixed graphs/heavy_light_decomposition.py")


def fix_hopcroft_karp():
    p = Path("graphs/hopcroft_karp.py")
    text = p.read_text()

    text = text.replace(
        'self.dist[u] = float("inf")  # type: ignore',
        'self.dist[u] = float("inf")  # type: ignore[assignment]',
        1,
    )
    text = text.replace(
        'if pair_v is not None and self.dist[pair_v] == float("inf"):  # type: ignore',
        'if pair_v is not None and self.dist[pair_v] == float("inf"):  # type: ignore[operator]',
    )
    text = text.replace(
        'self.dist[u] = float("inf")  # type: ignore',
        'self.dist[u] = float("inf")  # type: ignore[assignment]',
    )

    old = """                if self.pair_u[u] is None:
                    if self.dfs(u):
                        matching += 1"""
    new = """                if self.pair_u[u] is None and self.dfs(u):
                    matching += 1"""
    text = text.replace(old, new)

    old = """        print(
            f"Hopcroft-Karp: {n}x{m}, {edges} edges, matching={result}, time={elapsed:.3f}s"
        )"""
    new = """        print(
            f"Hopcroft-Karp: {n}x{m}, {edges} edges, "
            f"matching={result}, time={elapsed:.3f}s"
        )"""
    text = text.replace(old, new)

    p.write_text(text)
    print("fixed graphs/hopcroft_karp.py")


def fix_max_bipartite_independent_set():
    p = Path("graphs/max_bipartite_independent_set.py")
    text = p.read_text()

    text = text.replace(
        "# Minimum vertex cover = (U - Z) \u222a (V \u2229 Z)",
        "# Minimum vertex cover = (U - Z) union (V intersect Z)",
    )
    text = text.replace(
        "# Maximum independent set = Z \u222a (V - Z) = complement of min vertex cover",
        "# Maximum independent set = Z union (V - Z) = complement of min vertex cover",
    )
    text = text.replace(
        'dist[u] = float("inf")  # type: ignore',
        'dist[u] = float("inf")  # type: ignore[assignment]',
        1,
    )
    text = text.replace(
        'if pu is not None and dist[pu] == float("inf"):  # type: ignore',
        'if pu is not None and dist[pu] == float("inf"):  # type: ignore[operator]',
    )
    text = text.replace(
        'dist[u] = float("inf")  # type: ignore',
        'dist[u] = float("inf")  # type: ignore[assignment]',
    )

    p.write_text(text)
    print("fixed graphs/max_bipartite_independent_set.py")


def fix_push_relabel():
    p = Path("graphs/push_relabel.py")
    text = p.read_text()

    old = "v for v in range(n) if v != source and v != sink and self.excess[v] > 0"
    new = "v for v in range(n) if v not in (source, sink) and self.excess[v] > 0"
    text = text.replace(old, new)

    old = """                    if (
                        v != source
                        and v != sink
                        and self.excess[v] == self.excess[u] + 1
                    ):"""
    new = """                    if (
                        v not in (source, sink)
                        and self.excess[v] == self.excess[u] + 1
                    ):"""
    text = text.replace(old, new)

    p.write_text(text)
    print("fixed graphs/push_relabel.py")


def fix_test_graph_algorithms():
    p = Path("graphs/tests/test_graph_algorithms.py")
    text = p.read_text()

    text = text.replace(
        "dist, next_node = floyd_warshall(graph)",
        "_dist, next_node = floyd_warshall(graph)",
    )
    text = text.replace("result = hk.max_matching()", "hk.max_matching()")

    p.write_text(text)
    print("fixed graphs/tests/test_graph_algorithms.py")


if __name__ == "__main__":
    print("Applying auto-fixes for ruff errors...\n")
    fix_floyd_warshall()
    fix_ford_fulkerson()
    fix_heavy_light_decomposition()
    fix_hopcroft_karp()
    fix_max_bipartite_independent_set()
    fix_push_relabel()
    fix_test_graph_algorithms()
    print("\nAll fixes applied! Run 'ruff check graphs/' to verify.")
