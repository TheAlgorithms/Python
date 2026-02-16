"""
A Buffer Gate is a logic gate in boolean algebra which outputs the same value
as its input. It is used for signal isolation, increasing drive strength, or
introducing propagation delay in digital circuits.

In digital electronics, buffers are essential for:
- Isolating different circuit sections
- Increasing current drive capability  
- Preventing signal degradation
- Creating intentional delays in timing circuits

Following is the truth table of a Buffer Gate:
    ----------------------
    | Input  |  Output   |
    ----------------------
    |   0    |     0     |
    |   1    |     1     |
    ----------------------

Refer - https://en.wikipedia.org/wiki/Digital_buffer
"""


def buffer_gate(input_1: int) -> int:
    """
    Calculate output of a buffer gate

    >>> buffer_gate(0)
    0
    >>> buffer_gate(1)
    1
    """
    return int(bool(input_1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()