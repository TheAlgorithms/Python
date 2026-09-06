from graphs.connected_components import connected_components


def test_connected_components_empty_graph():
    assert connected_components({}) == []
