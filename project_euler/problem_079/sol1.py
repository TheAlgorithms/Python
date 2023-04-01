"""
Project Euler Problem 79: https://projecteuler.net/problem=79

Passcode derivation

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.
...

"""
import itertools
import os


def solution() -> int:
    """
    Returns the shortest possible secret passcode of unknown length.

    >>> solution()
    73162890
    """
    with open(os.path.dirname(__file__) + "/p079_keylog.txt") as file:
        logins = [tuple(line.strip()) for line in file]

    unique_chars = {char for login in logins for char in login}

    for permutation in itertools.permutations(unique_chars):
        satisfied = True
        for login in logins:
            if not (
                permutation.index(login[0])
                < permutation.index(login[1])
                < permutation.index(login[2])
            ):
                satisfied = False
                break

        if satisfied:
            return int("".join(permutation))
            break

    return 0


if __name__ == "__main__":
    print(solution())
