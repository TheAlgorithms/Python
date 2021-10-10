"""

Calculates the nth number in Sylvester's sequence

Source:
    https://en.wikipedia.org/wiki/Sylvester%27s_sequence

"""


def sylvester(number: int) -> int:
    """
    :param number: nth number to calculate in the sequence
    :return: the nth number in Sylvester's sequence

    >>> sylvester(8)
    113423713055421844361000443

    >>> sylvester(-1)
    Traceback (most recent call last):
    ...
    ValueError: The input value of [n=-1] has to be > 0

    >>> sylvester(8.0)
    Traceback (most recent call last):
    ...
    AssertionError: The input value of [n=8.0] is not an integer
    """
    assert isinstance(number, int), f"The input value of [n={number}] is not an integer"

    if number == 1:
        return 2
    elif number < 1:
        raise ValueError(f"The input value of [n={number}] has to be > 0")
    else:
        num = sylvester(number - 1)
        lower = num - 1
        upper = num
        return lower * upper + 1


if __name__ == "__main__":
    print(f"The 8th number in Sylvester's sequence: {sylvester(8)}")
