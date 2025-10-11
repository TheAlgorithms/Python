# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///

import pytest

from maths.factorial import factorial, factorial_recursive


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_zero(function):
    assert function(0) == 1


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_positive_integers(function):
    assert function(1) == 1
    assert function(5) == 120
    assert function(7) == 5040


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_large_number(function):
    assert function(10) == 3628800


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_negative_number(function):
    with pytest.raises(ValueError):
        function(-3)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
