"""Absolute Value."""


def abs_val(num: float) -> float:
    """
    Find the absolute value of a number.

    >>> abs_val(-5.1)
    5.1
    >>> abs_val(-5) == abs_val(5)
    True
    >>> abs_val(0)
    0
    """
    return -num if num < 0 else num


def test_abs_val():
    """
    >>> test_abs_val()
    """
    assert 0 == abs_val(0)
    assert 34 == abs_val(34)
    assert 100000000000 == abs_val(-100000000000)


if __name__ == "__main__":
    print(abs_val(-34))  # --> 34
