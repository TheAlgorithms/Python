import pytest

from maths.binomial_distribution import binomial_distribution


def test_large_number_of_trials() -> None:
    assert binomial_distribution(85, 171, 0.5) == pytest.approx(0.060749764626165485)
