"""
Signum function -- https://en.wikipedia.org/wiki/Sign_function
"""


def signum(num: float) -> int:
    """
    Applies signum function on the number

    Custom test cases:
    >>> signum(-20)
    -1
    >>> signum(20)
    1
    >>> signum(0)
    0
    >>> signum("a")
    0
    >>> signum([])
    0
    >>> signum(-10)
    -1
    >>> signum(10)
    1
    """
    if num < 0:
        return -1
    return 1 if num else 0


def test_signum() -> None:
    """
    Tests the signum function
    """
    assert signum(5) == 1
    assert signum(-5) == -1
    assert signum(0) == 0
    assert signum(10.5) == 1
    assert signum(-10.5) == -1
    assert signum(1e-6) == 1
    assert signum(-1e-6) == -1
    assert signum(123456789) == 1
    assert signum(-123456789) == -1


if __ame__ == "__main":
    print(signum(12))
    print(signum(-12))
    print(signum(0))
