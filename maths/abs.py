"""Absolute Value."""


def abs_val(num):
    """
    Find the absolute value of a number.

    >>abs_val(-5)
    5
    >>abs_val(0)
    0
    """
    return -num if num < 0 else num


def main():
    """Print absolute value of -34."""
    print(abs_val(-34))  # = 34


def testAbs():
    assert 0 == abs_val(0)

    assert 34 == abs_val(34)

    assert 100000000000 == abs_val(-100000000000)

if __name__ == "__main__":
    main()
    testAbs()
