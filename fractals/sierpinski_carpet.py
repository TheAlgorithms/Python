"""
The Sierpinski carpet is a plane fractal first described by Wacław Sierpiński
in 1916.  It is a two-dimensional generalisation of the Cantor set and a close
relative of the Sierpinski triangle.

Construction
    Start from a filled square.  Divide it into a 3x3 grid of nine equal
    sub-squares and remove the central one.  Then apply the same procedure
    recursively to each of the eight remaining sub-squares, forever.

A convenient way to decide whether a single cell of the ``3**n x 3**n`` grid is
filled (part of the carpet) or empty (a hole) is to look at the base-3 digits
of its row and column indices: the cell is a hole if and only if, at some
level, both the row digit and the column digit are equal to ``1`` (the centre
of that 3x3 block).

This module builds the carpet purely with integer arithmetic, so every
function is deterministic and can be verified with doctests -- no plotting or
turtle graphics required.

Reference: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_carpet
"""


def is_filled(row: int, col: int) -> bool:
    """
    Return ``True`` when the cell at (``row``, ``col``) belongs to the carpet
    and ``False`` when it falls inside one of the removed central squares.

    The result is independent of the fractal depth: a cell is a hole as soon as
    any pair of matching base-3 digits equals ``(1, 1)``.

    >>> is_filled(0, 0)
    True
    >>> is_filled(1, 1)  # the very first central square is removed
    False
    >>> is_filled(4, 4)  # centre of the centre block -> still a hole
    False
    >>> is_filled(0, 4)
    True
    >>> [is_filled(1, col) for col in range(3)]
    [True, False, True]

    Negative coordinates make no sense for a grid index.

    >>> is_filled(-1, 0)
    Traceback (most recent call last):
        ...
    ValueError: row and col must be non-negative, got (-1, 0)
    """
    if row < 0 or col < 0:
        msg = f"row and col must be non-negative, got ({row}, {col})"
        raise ValueError(msg)
    while row > 0 or col > 0:
        if row % 3 == 1 and col % 3 == 1:
            return False
        row //= 3
        col //= 3
    return True


def generate_carpet(depth: int, filled: str = "#", hole: str = " ") -> list[str]:
    """
    Build the Sierpinski carpet of the given ``depth`` as a list of strings.

    A depth of ``0`` is a single filled cell; each extra level multiplies the
    side length by three.

    >>> generate_carpet(0)
    ['#']
    >>> for line in generate_carpet(1):
    ...     print(line)
    ###
    # #
    ###
    >>> for line in generate_carpet(2, filled="X", hole="."):
    ...     print(line)
    XXXXXXXXX
    X.XX.XX.X
    XXXXXXXXX
    XXX...XXX
    X.X...X.X
    XXX...XXX
    XXXXXXXXX
    X.XX.XX.X
    XXXXXXXXX
    >>> generate_carpet(-1)
    Traceback (most recent call last):
        ...
    ValueError: depth must be non-negative, got -1
    """
    if depth < 0:
        msg = f"depth must be non-negative, got {depth}"
        raise ValueError(msg)
    size = 3**depth
    return [
        "".join(filled if is_filled(row, col) else hole for col in range(size))
        for row in range(size)
    ]


def count_filled_cells(depth: int) -> int:
    """
    Return how many cells are filled in a carpet of the given ``depth``.

    Each level keeps eight of the nine sub-squares, so the count is ``8**depth``.
    Verifying this closed form against a brute-force scan is a nice sanity check.

    >>> [count_filled_cells(depth) for depth in range(4)]
    [1, 8, 64, 512]
    >>> all(
    ...     count_filled_cells(depth)
    ...     == sum(line.count("#") for line in generate_carpet(depth))
    ...     for depth in range(4)
    ... )
    True
    """
    if depth < 0:
        msg = f"depth must be non-negative, got {depth}"
        raise ValueError(msg)
    return 8**depth


def main() -> None:
    for line in generate_carpet(3):
        print(line)


if __name__ == "__main__":
    main()
