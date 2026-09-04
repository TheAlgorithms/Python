from __future__ import annotations

# Example input (matrix where mat[i][j] == 1 if person i knows person j)
mat = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1],
]

# Expected output for this input
expect = 1  # person at index 1 is the celebrity


def celebrity(mat: list[list[int]]) -> int:
    """
    Function to find the celebrity in a party.

    A celebrity is a person who is:
    - Known by everyone else
    - Knows no one else
    - At max there can be only one celebrity
    Args:
        mat: n x n matrix, where mat[i][j] == 1 if person i knows person j.

    Returns:
        Index of the celebrity if one exists, else -1.

    Example:
    >>> celebrity(mat) == expect
    True
    """
    n = len(mat)
    st: list[int] = list(range(n))  # push everybody in the stack

    # Find a potential celebrity
    while len(st) > 1:
        a = st.pop()
        b = st.pop()

        if mat[a][b]:
            st.append(b)  # a knows b so a can't be celebrity
        else:
            st.append(a)  # a doesn't know b so b can't be celebrity

    # Potential candidate
    c = st.pop()

    # Verify candidate
    for i in range(n):
        if i == c:
            continue
        if mat[c][i] or not mat[i][c]:
            return -1
    return c


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Celebrity is:", celebrity(mat))
