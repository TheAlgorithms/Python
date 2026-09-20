import pytest

from graphs.graphs_floyd_warshall import floyd_warshall


def test_no_edges():
    graph = [
        [0, float("inf"), float("inf")],
        [float("inf"), 0, float("inf")],
        [float("inf"), float("inf"), 0],
    ]
    expected = [
        [0, float("inf"), float("inf")],
        [float("inf"), 0, float("inf")],
        [float("inf"), float("inf"), 0],
    ]
    dist, _ = floyd_warshall(graph, 3)
    assert dist == expected


def test_with_edges():
    graph = [[0, 3, float("inf")], [2, 0, float("inf")], [float("inf"), 7, 0]]
    expected = [[0, 3, float("inf")], [2, 0, float("inf")], [9, 7, 0]]
    dist, _ = floyd_warshall(graph, 3)
    assert dist == expected


def test_unreachable_vertices():
    graph = [
        [0, 1, float("inf")],
        [float("inf"), 0, 2],
        [float("inf"), float("inf"), 0],
    ]
    expected = [[0, 1, 3], [float("inf"), 0, 2], [float("inf"), float("inf"), 0]]
    dist, _ = floyd_warshall(graph, 3)
    assert dist == expected


if __name__ == "__main__":
    pytest.main()
