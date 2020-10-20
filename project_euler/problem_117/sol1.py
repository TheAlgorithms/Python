"""
Project Euler Problem 104: https://projecteuler.net/problem=117
Using a combination of grey square tiles and oblong tiles chosen from:
red tiles (measuring two units), green tiles (measuring three units),
and blue tiles (measuring four units), it is possible to tile a row
measuring five units in length in exactly fifteen different ways.

How many ways can a row n units long be filled with.
Compute n = 0 manually as a base case.
 - Now assume n >= 1. Look at the leftmost item and sum up the possibilities.
 - Black square (n>=1): Rest of the row can be anything of length n-1. Add ways[n-1].
 - Red tile     (n>=2): Rest of the row can be anything of length n-2. Add ways[n-2].
 - Green tile   (n>=3): Rest of the row can be anything of length n-3. Add ways[n-3].
 - Blue tile    (n>=4): Rest of the row can be anything of length n-4. Add ways[n-4].
"""


def _calculate(length: int) -> str:
    """
    A small helper function for the recursion, mainly to have
    a clean interface for the solution() function below.

    >>> _calculate(12)
    '1490'
    >>> _calculate(15)
    '10671'
    >>> _calculate(41)
    '274423830033'
    """
    ways = [1] + [0] * length
    for n in range(1, len(ways)):
        ways[n] += sum(ways[max(n - 4, 0) : n])
    return str(ways[-1])


def solution(length: int = 50) -> str:
    """
    This function is used for finding how many units long be filled with

    >>> solution()
    '100808458960497'
    >>> solution(25)
    '7555935'
    """
    return _calculate(length)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{solution()}")
