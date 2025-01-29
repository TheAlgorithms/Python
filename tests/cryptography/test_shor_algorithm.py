import pytest
from algorithms.cryptography.shor_algorithm import shor_algorithm

@pytest.mark.parametrize("N, expected_factors", [
    (15, (3, 5)),
    (21, (3, 7)),
    (35, (5, 7)),
    (55, (5, 11)),
])
def test_shor_algorithm(N, expected_factors):
    factors = shor_algorithm(N)
    assert sorted(factors) == sorted(expected_factors), f"Failed for N={N}"
