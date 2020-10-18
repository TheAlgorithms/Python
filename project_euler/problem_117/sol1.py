"""
Project Euler Problem 104: https://projecteuler.net/problem=117
Using a combination of grey square tiles and oblong tiles chosen from:
red tiles (measuring two units), green tiles (measuring three units),
and blue tiles (measuring four units), it is possible to tile a row
measuring five units in length in exactly fifteen different ways.

How many ways can a row n units long be filled with
"""


def solution(length: int = 50) -> str:
    """
    >>> solution(50)
    '100808458960497'
    """
    ways = [1] + [0] * length
    for n in range(1, len(ways)):
        ways[n] += sum(ways[max(n-4, 0):n])
    return str(ways[-1])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{solution()}")
