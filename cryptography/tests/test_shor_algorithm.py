import pytest
from cryptography.shor_algorithm import shor_classical


def test_small_composite():
    factors = shor_classical(15)
    assert set(factors) == {3, 5}


def test_medium_composite():
    factors = shor_classical(21)
    assert set(factors) == {3, 7}


def test_even_number():
    factors = shor_classical(18)
    assert set(factors) == {2, 9}


def test_prime_number():
    result = shor_classical(13)
    assert isinstance(result, str)
    assert "prime" in result.lower()


def test_invalid_input():
    result = shor_classical(1)
    assert isinstance(result, str)
    assert "failure" in result.lower()


def test_larger_composite_number():
    result = shor_classical(91)
    assert isinstance(result, (tuple, str))
    if isinstance(result, tuple):
        assert all(isinstance(x, int) for x in result)
