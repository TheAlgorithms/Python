import pytest

from maths.sieve_of_atkin import sieve_of_atkin


def test_small_primes():
    assert sieve_of_atkin(10) == [2, 3, 5, 7]


def test_medium_primes():
    assert sieve_of_atkin(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_invalid_limit():
    with pytest.raises(ValueError):
        sieve_of_atkin(1)
