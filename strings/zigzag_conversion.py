from __future__ import annotations


def zigzag_convert(s: str, num_rows: int) -> str:
    """
    Convert a string to zigzag pattern and read it row by row.

    The string is written in a zigzag pattern on num_rows rows:
    - Characters at index 0, num_rows, 2*num_rows, ... go to row 0
    - Characters at index 1, num_rows+1, 2*num_rows+1, ... go to row 1
    - And so on until row num_rows-1
    - Then the direction reverses (going up)

    Args:
        s: The input string to convert
        num_rows: Number of rows in the zigzag pattern

    Returns:
        The string read row by row from top to bottom

    >>> zigzag_convert("PAYPALISHIRING", 3)
    'PAHNAPLSIIGYIR'
    >>> zigzag_convert("PAYPALISHIRING", 4)
    'PINALSIGYAHRPI'
    >>> zigzag_convert("A", 1)
    'A'
    >>> zigzag_convert("AB", 1)
    'BA'
    """
    if num_rows == 1 or num_rows >= len(s):
        return s

    rows: list[list[str]] = [[] for _ in range(num_rows)]
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row].append(char)
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
        if going_down:
            current_row += 1
        else:
            current_row -= 1

    return "".join("".join(row) for row in rows)


if __name__ == "__main__":
    import doctest

    doctest.testmod()