"""
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same
is done to a second cube. By placing the two cubes side-by-side in different positions
we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:
￼
In fact, by carefully choosing the digits on both cubes it is possible to display all
of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube
and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an
arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square
numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not
the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last
example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of
forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to
be displayed?
"""


from itertools import combinations


def test_arrangement(die1: set, die2: set) -> bool:
    """
    Check if an arrangement of two dice can represent all 1- and 2- digit squares.
    >>> test_arrangement({0, 5, 6, 7, 8, 9},{1, 2, 3, 4, 6, 7})
    True
    >>> test_arrangement({0, 5, 6, 7, 8, 9},{1, 2, 3, 4, 5, 7})
    False
    """
    if 6 in die1:
        die1.add(9)
    elif 9 in die1:
        die1.add(6)

    if 6 in die2:
        die2.add(9)
    elif 9 in die2:
        die2.add(6)

    for i in range(1, 10):
        square = i * i
        a, b = square // 10, square % 10
        if not ((a in die1 and b in die2) or (b in die1 and a in die2)):
            return False

    return True


def solution() -> int:
    """
    Return the number of distinct arrangement of two dice which allow for all 1-
    and 2- digit square numbers to be displayed.
    """
    s = set()

    for die1 in combinations(range(10), 6):
        die1_set = set(die1)
        for die2 in combinations(range(10), 6):
            if die2 < die1:
                continue
            die2_set = set(die2)
            if test_arrangement(die1_set, die2_set):
                die1 = tuple(sorted(die1))
                die2 = tuple(sorted(die2))
                tmp = tuple(sorted([die1, die2]))
                s.add(tmp)

    return len(s)


if __name__ == "__main__":
    print(solution())
