# tests/test_sieve_of_atkin.py
import pytest
from maths.sieve_of_atkin import sieve_of_atkin


def test_small_primes():
    assert sieve_of_atkin(10) == [2, 3, 5, 7]


def test_invalid_limit():
    with pytest.raises(ValueError):
        sieve_of_atkin(1)
