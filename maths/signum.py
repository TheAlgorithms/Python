"""
Signum function

Refer - https://en.wikipedia.org/wiki/Sign_function
"""


def signum(num):
    """
    Applies signum function on the number

    >>> signum(-10)
    -1
    >>> signum(10)
    1
    >>> signum(0)
    0
    """
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0


def test_signum():
    """
    Tests the signum function
    """
    assert signum(5) == 1
    assert signum(-5) == -1
    assert signum(0) == 0


if __name__ == "__main__":
    print(signum(12))
    print(signum(-12))
    print(signum(0))
