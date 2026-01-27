"""
Prints a number triangle pattern.

Example for n = 5:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


def number_triangle(n: int) -> None:
    """
    Prints a number triangle up to n rows.

    :param n: Number of rows
    """
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in range(1, i + 1)))


if __name__ == "__main__":
    number_triangle(5)
