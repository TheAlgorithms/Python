"""
Project Euler Problem 90: https://projecteuler.net/problem=90
Cube digit pairs:

Each of the six faces on a cube has a different digit (0 to 9) written on it;
the same is done to a second cube.
In fact, by carefully choosing the digits on both cubes it is possible to display
all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.
For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube
and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that
an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all
nine square numbers to be displayed; otherwise it would be impossible to obtain 09.
In determining a distinct arrangement we are interested in the digits on each cube,
not the order.
{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets
in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9}
for the purpose of forming 2-digit numbers.
How many distinct arrangements of the two cubes allow for all of the
square numbers to be displayed?
"""

from itertools import permutations, combinations


def set_to_bit(bit_tuple: tuple) -> int:
    """
    returns bit representation of a given iterable, preferably tuple.
    @param t - tuple representing the 1 bits
    >>> set_to_bit((0,1))
    3
    >>> set_to_bit((1,3))
    10
    """
    res = 0
    for i in bit_tuple:
        res |= 1 << i
    return res


def is_bit_set(number: int, bit: int) -> bool:
    """
    checks if a given bit is 1 in the given number (work around for 6 and 9)
    @param number - the number/set to search in
    @param bit - the index to look for
    >>> is_bit_set(10, 1)
    True
    >>> is_bit_set(64, 9)
    True
    """
    if bit == 6 or bit == 9:
        return bool((1 << 6 & number) or (1 << 9 & number))
    return bool(1 << bit & number)


def validate_cubes(cubes: tuple, sq: list) -> bool:
    """
    verifies whether or not the selected combination of cubes is valid,
    by iterating through all square values.
    @param cubes - tuple of cubes represented by numbers (having six 1 bits (0-9))
    @param sq - list of squares to validate
    >>> validate_cubes((63,), ['4'])
    True
    """
    for s in sq:
        res = False
        for p in permutations(s):
            cur_res = True
            for i, c in enumerate(map(int, p)):
                cur_res = cur_res and is_bit_set(cubes[i], c)
            res = res or cur_res
        if not res:
            return False
    return True


def solution(squares: int = 9, number_of_dice: int = 2) -> int:
    """
    returns the solution of problem 90 using helper functions
    e.g 1217 for the default argument values
    >>> solution(3, 1)
    55
    >>> solution(7, 2)
    2365
    """
    sq = [str(i ** 2).zfill(number_of_dice) for i in range(1, squares + 1)]
    all_dices = [set_to_bit(c) for c in combinations(range(10), 6)]
    dices = [p for p in combinations(all_dices, number_of_dice)]

    return len([d for d in dices if validate_cubes(d, sq)])


if __name__ == "__main__":
    print(f"{solution()}")
