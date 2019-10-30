"""Logarithm function"""


def log(x, base=10):
    """
    This function returns the log value of a given number.
    The default base is 10, but users can set that to whatever they'd like

    >>> log(64, base=2)
    6

    >>> log(1000)
    3

    """
    n = 0
    while True:
        n += 1
        if base ** n == x:
            return n
            break


def test_log():
    assert log(64), 6
    assert log(1000, 10), 3


if __name__ == "__main__":
    x = 64
    base = 2
    res_expected = 6
    res_actual = log(x, base)
    if res_expected == res_actual:
        print(
            f"The log of {x} base {base} is {res_actual} versus {res_expected} expected."
        )
