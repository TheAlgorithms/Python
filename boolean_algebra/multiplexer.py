# https://www.electrically4u.com/solved-problems-on-multiplexer/


def mux(input0: int, input1: int, select: int) -> int:
    """
    Implement a 2-to-1 Multiplexer.

    :param input0: The first input value (0 or 1).
    :param input1: The second input value (0 or 1).
    :param select: The select signal (0 or 1) to choose between input0 and input1.
    :return: The output based on the select signal.

    >>> mux(0, 1, 0)
    0
    >>> mux(0, 1, 1)
    1
    >>> mux(1, 0, 0)
    1
    >>> mux(1, 0, 1)
    0
    """
    if select == 0:
        return input0
    elif select == 1:
        return input1
    else:
        raise ValueError("Select signal must be 0 or 1")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
