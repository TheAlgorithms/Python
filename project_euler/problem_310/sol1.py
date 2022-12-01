"""
Project Euler Problem 310: https://projecteuler.net/problem=310

Alice and Bob play the game Nim Square.
Nim Square is just like ordinary three-heap normal play Nim, but
the players may only remove a square number of stones from a heap.
The number of stones in the three heaps is represented by the ordered
triple (a,b,c).
If 0 <= a <= b <= c <= 29 then the number of losing positions for the
next player is 1160.

Find the number of losing positions for the next player if
0 <= a <= b <= c <= 100,000.


Solution explanation:

Following from the references below (Sprague-Grundy theorem), three
piles of stones containing a, b, c is a losing state if their grundy
values have an xor sum of 0 i.e. grundy[a] ^ grundy[b] ^ grundy[c] == 0

The grundy values can be defined as:
  - grundy[0] = 0 (No moves for the first player. Second player wins by default)
  - grundy[i] = MEX(grundy[i - j * j] for all j such that j * j <= i) (from the
    definition of Sprague-Grundy theorem. MEX is the "minimal excludant" of the set)

The problem reduces to finding count of numbers i, j, k satisfying:
  - i <= j <= k
  - grundy[i] ^ grundy[j] ^ grundy[k] == 0

This can be done naively in O(n^3) time after finding grundy values but it is
too slow for solving the constraints of this problem. The observation here is
to use frequency counting of the grundy values and calculate the count of
numbers satisfying the property mathematically.

Algorithm:
- Calculate the frequency F of each grundy value

- Iterate over all triplets of possible grundy values grundy_i, grundy_j,
  grundy_k such that grundy_i <= grundy_j <= grundy_k

- Calculate contribution of each possible triplet using combinatorics to the
  number of losing states:
  - Case 1: grundy_i < grundy_j < grundy_k
    Contributes a total of F[grundy_i] * F[grundy_j] * F[grundy_k] losing states

  - Case 2: grundy_i == grundy_j < grundy_k
    There are n * (n + 1) / 2 distinct pairs to choose with same grundy_i/grundy_j
    values
    Contributes a total of (F[grundy_i] * (F[grundy_j] + 1) / 2) * F[grundy_k]
    losing states

  - Case 3: grundy_i < grundy_j == grundy_k
    There are n * (n + 1) / 2 distinct pairs to choose with same grundy_j/grundy_k
    values
    Contributes a total of F[grundy_i] * (F[grundy_j] * (F[grundy_k] + 1) / 2)
    losing states

  - Case 4: grundy_i == grundy_j == grundy_k
    There are n * (n + 1) * (n + 2) / 6 distinct triplets to choose with same
    grundy_i/grundy_j/grundy_k values
    Contributes a total of F[grundy_i] * (F[grundy_j] + 1) * (F[grundy_k] + 2) / 6
    losing states


References:
- https://en.wikipedia.org/wiki/Nim
- https://en.wikipedia.org/wiki/Sprague-Grundy_theorem
- https://cp-algorithms.com/game_theory/sprague-grundy-nim.html
- https://en.wikipedia.org/wiki/Mex_(mathematics)
"""


def solution(limit: int = 100000) -> int:
    """
    This function computes the number of losing positions in the game of
    Nim Square given that there are three heaps containing a, b, c stones
    respectively and 0 <= a <= b <= c <= limit.

    >>> solution(29)
    1160
    >>> solution(100)
    25582
    >>> solution(69420)
    964859030953
    """

    # Safe upper bound for possible grundy values
    # Can be observed by printing values for a large limit
    grundy_limit = 100

    limit += 1
    grundy = [0] * limit

    # Compute the grundy values
    for i in range(1, limit):
        moves = [False] * grundy_limit
        j = 1

        while j * j <= i:
            moves[grundy[i - j * j]] = True
            j += 1

        grundy[i] = moves.index(False)

    freq = [0] * grundy_limit

    # Compute frequency of grundy values
    for g in grundy:
        freq[g] += 1

    losing_positions_count = 0

    # Use mathematical intuition and combinatorics to calculate contribution
    # of every triplet of grundy values to the count of losing states
    for grundy_i in range(grundy_limit):
        for grundy_j in range(grundy_i, grundy_limit):
            for grundy_k in range(grundy_j, grundy_limit):
                xor_sum = grundy_i ^ grundy_j ^ grundy_k
                x, y, z = freq[grundy_i], freq[grundy_j], freq[grundy_k]

                # We require xor_sum to be 0 to calculate losing states
                # as explained in references
                if xor_sum:
                    continue

                if grundy_i < grundy_j < grundy_k:
                    losing_positions_count += x * y * z
                elif grundy_i == grundy_j and grundy_j < grundy_k:
                    losing_positions_count += ((x * (y + 1)) // 2) * z
                elif grundy_i < grundy_j and grundy_j == grundy_k:
                    losing_positions_count += x * (y * (z + 1) // 2)
                else:
                    losing_positions_count += x * (y + 1) * (z + 2) // 6

    return losing_positions_count


if __name__ == "__main__":
    print(f"{solution() = }")
