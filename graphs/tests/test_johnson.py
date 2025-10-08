import math

import pytest

from graphs.johnson import johnson


def test_johnson_basic():
    g = {
        0: [(1, 3), (2, 8), (4, -4)],
        1: [(3, 1), (4, 7)],
        2: [(1, 4)],
        3: [(0, 2), (2, -5)],
        4: [(3, 6)],
    }
    dist = johnson(g)
    assert math.isclose(dist[0][3], 2.0, abs_tol=1e-9)
    assert math.isclose(dist[3][2], -5.0, abs_tol=1e-9)


def test_johnson_negative_cycle():
    g2 = {0: [(1, 1)], 1: [(0, -3)]}
    with pytest.raises(ValueError):
        johnson(g2)
