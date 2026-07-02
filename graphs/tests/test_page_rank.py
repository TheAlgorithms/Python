import math

from graphs.page_rank import Node, page_rank


def add_edge(nodes, source, destination):
    nodes[destination].add_inbound(nodes[source].name)
    nodes[source].add_outbound(nodes[destination].name)


def test_page_rank_scores_are_normalized():
    nodes = [Node("A"), Node("B"), Node("C")]
    add_edge(nodes, 0, 1)
    add_edge(nodes, 0, 2)
    add_edge(nodes, 1, 2)
    add_edge(nodes, 2, 0)

    ranks = page_rank(nodes, max_iter=100)

    assert math.isclose(sum(ranks.values()), 1.0, abs_tol=1e-8)


def test_page_rank_handles_dangling_nodes():
    nodes = [Node("A"), Node("B"), Node("C")]
    add_edge(nodes, 0, 1)
    add_edge(nodes, 1, 2)

    ranks = page_rank(nodes, max_iter=100)

    assert math.isclose(sum(ranks.values()), 1.0, abs_tol=1e-8)
    assert math.isclose(ranks["C"], 0.474412, rel_tol=1e-5)
    assert ranks["C"] > ranks["B"] > ranks["A"]
