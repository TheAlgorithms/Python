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

References:
  = https://en.wikipedia.org/wiki/Nim
"""


def solution(exponent: int = 30) -> int:
    """
    For any given exponent x >= 0, 1 <= n <= 2^x.
    This function returns how many Nim games are lost given that
    each Nim game has three heaps of the form (n, 2*n, 3*n).
    >>> solution(0)
    1
    >>> solution(2)
    3
    >>> solution(10)
    144
    """

    # Following the reference from wikipedia, one can come to the conclusion that
    # this problem boils down finding count of numbers `n` satisfying
    #   - F(n): XOR(n, XOR(2 * n, 3 * n)) == 0
    #
    # Naively searching for `n` satisfying the above equation is too slow however
    # there's a clever observation that can be made.
    #
    # A number `n` satisfies this equality if none of its 1-bits are adjacent.
    # Our new problem can be defined as
    #   - G(m): number of numbers with non-adjacent 1-bits up to 2^m
    #
    # The problem reduces to a simple counting problem where Dynamic Programming
    # can be applied.
    #
    # Define `dp[i][bit]` as the number of numbers satisfying G when `bit`'th bit
    # is set to `i`
    #   - `i`: {0, 1}
    #   - `bit`: {0, 1, ..., max_bits}
    #
    # Example:
    # - `dp[0][4]`: number of numbers satisfying F when 4'th bit is set to 0
    # - `dp[1][3]`: number of numbers satisfying F when 3'rd bit is set to 1

    dp = [[0] * (exponent + 1) for _ in range(2)]

    # Base Cases
    dp[0][0] = 1
    dp[1][0] = 0

    # Transitions
    for bit in range(1, exponent + 1):
        dp[0][bit] = dp[0][bit - 1] + dp[1][bit - 1]
        dp[1][bit] = dp[0][bit - 1]

    return dp[0][-1] + dp[1][-1]

    # The code above can be optimized to not allocate extra memory at all
    # dp0: int = 1
    # dp1: int = 1
    # for bit in range(1, exponent + 1):
    #     dp0, dp1 = dp0 + dp1, dp0
    # return dp0 + dp1


if __name__ == "__main__":
    print(f"{solution() = }")
