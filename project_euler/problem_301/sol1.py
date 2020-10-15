"""
Project Euler Problem 301: https://projecteuler.net/problem=301

Problem Statement:
Nim is a game played with heaps of stones, where two players take
it in turn to remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of
Nim, which works as follows:
- At the start of the game there are three heaps of stones.
- On each player's turn, the player may remove any positive
  number of stones from any single heap.
- The first player unable to move (because no stones remain) loses.

If (n1, n2, n3) indicates a Nim position consisting of heaps of size
n1, n2, and n3, then there is a simple function, which you may look up
or attempt to deduce for yourself, X(n1, n2, n3) that returns:
- zero if, with perfect strategy, the player about to
  move will eventually lose; or
- non-zero if, with perfect strategy, the player about
  to move will eventually win.

For example X(1,2,3) = 0 because, no matter what the current player does,
the opponent can respond with a move that leaves two heaps of equal size,
at which point every move by the current player can be mirrored by the
opponent until no stones remain; so the current player loses. To illustrate:
- current player moves to (1,2,1)
- opponent moves to (1,0,1)
- current player moves to (0,0,1)
- opponent moves to (0,0,0), and so wins.

For how many positive integers n <= 2^30 does X(n,2n,3n) = 0?
"""


def x(n: int, n2: int, n3: int) -> int:
    """
    Returns:
    - zero if, with perfect strategy, the player about to
      move will eventually lose; or
    - non-zero if, with perfect strategy, the player about
      to move will eventually win.

    >>> x(1, 2, 3)
    0
    >>> x(3, 6, 9)
    12
    >>> x(8, 16, 24)
    0
    >>> x(11, 22, 33)
    60
    >>> x(1000, 2000, 3000)
    3968
    """
    return n ^ n2 ^ n3


def solution(n: int = 2 ** 10) -> int:
    """
    For a given integer n <= 2^30, returns how many Nim games are lost.
    >>> solution(2)
    2
    >>> solution(2 ** 10)
    144
    """
    lossCount = 0
    for i in range(1, n + 1):
        if x(i, 2 * i, 3 * i) == 0:
            lossCount += 1

    return lossCount


if __name__ == "__main__":
    print(solution())
