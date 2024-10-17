#!/usr/bin/env python3

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


def test_example_input():
    num_vertices = 3
    graph = [
        [float("inf"), float("inf"), float("inf")],
        [float("inf"), float("inf"), float("inf")],
        [float("inf"), float("inf"), float("inf")],
    ]
    for i in range(num_vertices):
        graph[i][i] = 0.0
    graph[0][1] = 2
    graph[1][0] = 1
    expected = [
        [0, 2, float("inf")],
        [1, 0, float("inf")],
        [float("inf"), float("inf"), 0],
    ]
    dist, _ = floyd_warshall(graph, num_vertices)
    assert dist == expected


if __name__ == "__main__":
    pytest.main()


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
