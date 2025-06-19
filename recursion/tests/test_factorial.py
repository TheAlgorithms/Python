import pytest

from recursion.factorial import factorial


def test_factorial_valid_inputs() -> None:
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_invalid_input() -> None:
    with pytest.raises(ValueError):
        factorial(-1)
