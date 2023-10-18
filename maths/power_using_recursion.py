"""
== Raise base to the power of exponent using recursion ==
    Input -->
        Enter the base: 3
        Enter the exponent: 4
    Output  -->
        3 to the power of 4 is 81
    Input -->
        Enter the base: 2
        Enter the exponent: 0
    Output -->
        2 to the power of 0 is 1
"""
import pytest


def power(base: int, exponent: int) -> float:
    """
    Calculate the power of a base raised to an exponent.

    Examples:
    >>> power(3, 4)  # Positive exponent
    81
    >>> power(2, 0)  # Zero exponent
    1
    >>> power(5, -3)  # Negative exponent
    0.008
    >>> all(power(base, exponent) == pow(base, exponent)
    ...     for base in range(-10, 10) for exponent in range(10))  # Check against built-in pow() function
    True
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)


@pytest.mark.parametrize("base, exponent", [(1, 2), (2, 3), (3, 4)])
def test_power_positive_exponent(base, exponent):
    assert power(base, exponent) == pow(base, exponent)


@pytest.mark.parametrize("base, exponent", [(1, -2), (2, -3), (3, -4)])
def test_power_negative_exponent(base, exponent):
    assert power(base, exponent) == 1 / pow(base, -exponent)


def test_power_zero_exponent():
    assert power(1, 0) == 1
    assert power(2, 0) == 1
    assert power(3, 0) == 1


def test_power_with_non_integer_exponent():
    assert power(2, 0.5) == pytest.approx(1.4142135623730951)
    assert power(5, -1.5) == pytest.approx(0.4)
    assert power(3, 1.3) == pytest.approx(5.916079783099617)


def test_power_raises_type_error():
    with pytest.raises(TypeError):
        power("abc", 2)
    with pytest.raises(TypeError):
        power(2, "def")


def test_power_raises_value_error():
    witSh pytest.raises(ValueError):
        power(2, -10)
