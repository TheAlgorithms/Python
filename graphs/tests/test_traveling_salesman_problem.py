from graphs.traveling_salesman_problem import tsp_brute_force, tsp_dp, tsp_greedy


def sample_graph_1() -> list[list[int]]:
    return [
        [0, 29, 20],
        [29, 0, 15],
        [20, 15, 0],
    ]


def sample_graph_2() -> list[list[int]]:
    return [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]


def test_brute_force() -> None:
    graph = sample_graph_1()
    assert tsp_brute_force(graph) == 64


def test_dp() -> None:
    graph = sample_graph_1()
    assert tsp_dp(graph) == 64


def test_greedy() -> None:
    graph = sample_graph_1()
    # The greedy algorithm does not guarantee an optimal solution;
    # it is necessary to verify that its output is an integer greater than 0.
    # An approximate solution cannot be represented by '==',
    # and can only ensure that the result is reasonable.
    result = tsp_greedy(graph)
    assert isinstance(result, int)
    assert result >= 64


def test_dp_larger_graph() -> None:
    graph = sample_graph_2()
    assert tsp_dp(graph) == 80


def test_brute_force_larger_graph() -> None:
    graph = sample_graph_2()
    assert tsp_brute_force(graph) == 80


def test_greedy_larger_graph() -> None:
    graph = sample_graph_2()
    result = tsp_greedy(graph)
    assert isinstance(result, int)
    assert result >= 80
