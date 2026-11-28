import pytest

from graphs.depth_first_search import depth_first_search


def build_linear_graph(node_count: int) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for i in range(node_count - 1):
        graph[str(i)] = [str(i + 1)]
    graph[str(node_count - 1)] = []
    return graph


@pytest.mark.parametrize("node_count", [100, 50000])
def test_depth_first_search_large_linear_graph(node_count: int) -> None:
    graph = build_linear_graph(node_count)
    visited = depth_first_search(graph, "0")
    assert len(visited) == node_count