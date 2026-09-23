def padovan_sequence(n: int) -> int:
    """
    Return the n-th term of the Padovan Sequence.
    The Padovan sequence is the sequence of integers P(n) defined by the initial values
    P(0) = P(1) = P(2) = 1 and the recurrence relation P(n) = P(n-2) + P(n-3).

    https://en.wikipedia.org/wiki/Padovan_sequence

    :param n: The index of the term to return.
    :return: The n-th term of the Padovan Sequence.

    >>> padovan_sequence(0)
    1
    >>> padovan_sequence(1)
    1
    >>> padovan_sequence(2)
    1
    >>> padovan_sequence(3)
    2
    >>> padovan_sequence(4)
    2
    >>> padovan_sequence(5)
    3
    >>> padovan_sequence(10)
    12
    >>> padovan_sequence(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n <= 2:
        return 1

    p_prev_3, p_prev_2, p_prev_1 = 1, 1, 1

    for _ in range(3, n + 1):
        curr = p_prev_2 + p_prev_3
        p_prev_3, p_prev_2, p_prev_1 = p_prev_2, p_prev_1, curr

    return p_prev_1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("Doctests passed!")
