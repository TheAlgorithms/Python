from functools import lru_cache


@lru_cache
def bell_number(n: int) -> int:
    """
    Calculate the Bell Number for a given integer n.

    :param n: The integer for which to calculate the Bell Number.
    :return: The Bell Number for the given integer n.

    >>> bell_number(5)
    52
    >>> bell_number(0)
    1
    >>> bell_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: Number should not be negative.
    """
    if n < 0:
        raise ValueError("Number should not be negative.")

    if n == 0:
        return 1

    # Initialize the Bell Number for n=1
    bell_n = [0] * (n + 1)
    bell_n[0] = 1

    for i in range(1, n + 1):
        bell_n[i] = 0
        for j in range(i):
            bell_n[i] += bell_n[j]

    return bell_n[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
