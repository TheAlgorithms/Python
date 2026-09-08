"""
A NOR Gate is a logic gate in boolean algebra which results in false(0) if any of the
inputs is 1, and True(1) if all inputs are 0.
Following is the truth table of a NOR Gate:
    Truth Table of NOR Gate:
    | Input 1  | Input 2  |  Output  |
    |    0     |    0     |    1     |
    |    0     |    1     |    0     |
    |    1     |    0     |    0     |
    |    1     |    1     |    0     |

    Code provided by Akshaj Vishwanathan
https://www.geeksforgeeks.org/logic-gates-in-python
"""

from collections.abc import Callable


def nor_gate(input_1: int, input_2: int) -> int:
    """
    >>> nor_gate(0, 0)
    1
    >>> nor_gate(0, 1)
    0
    >>> nor_gate(1, 0)
    0
    >>> nor_gate(1, 1)
    0
    >>> nor_gate(0.0, 0.0)
    1
    >>> nor_gate(0, -7)
    0
    """
    return int(input_1 == input_2 == 0)


def truth_table(func: Callable) -> str:
    """
    >>> print(truth_table(nor_gate))
    Truth Table of NOR Gate:
    | Input 1  | Input 2  |  Output  |
    |    0     |    0     |    1     |
    |    0     |    1     |    0     |
    |    1     |    0     |    0     |
    |    1     |    1     |    0     |
    """

    def make_table_row(items: list | tuple) -> str:
        """
        >>> make_table_row(("One", "Two", "Three"))
        '|   One    |   Two    |  Three   |'
        """
        return f"| {' | '.join(f'{item:^8}' for item in items)} |"

    return "\n".join(
        (
            "Truth Table of NOR Gate:",
            make_table_row(("Input 1", "Input 2", "Output")),
            *[make_table_row((i, j, func(i, j))) for i in (0, 1) for j in (0, 1)],
        )
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(truth_table(nor_gate))
