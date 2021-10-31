"""
Problem 205 Dice Game: https://projecteuler.net/problem=205

Description:

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
Peter and Colin roll their dice and compare totals: the highest total wins.
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg

Solution:

The probability that, for a fixed n, the sum of the dice is exactly n is given by
`number of combinations such that sum is n` / `number of total combinations`.
That probability is computed with two helper functions:
count_four_sided() and count_six_sided().

Given a fixed n, between 7 and 36,
the player with the four sided dice wins if and only if the sum
of the nine dice is bigger than the same of six dice.
We can compute this probability as:
(1 - P(sum of four sided < n)) * P(sum of six sided = n).

In conclusion,
the final solution is obtained as the sum of the probabilities that the
player with the four sided dice wins, for any 7 <= n <= 36.


Time: 2.3 sec
"""
from itertools import product


def count_four_sided(n: int, D_4={}) -> int:
    """
    It returns the number of combinations of nine four-sided dice such that
    the sum of the dice is exactly n.
    It also returns D_4, in order to speed up computation time.
    >>> count_four_sided(8)
    (0, {8: 0})
    >>> count_four_sided(16)
    (4950, {8: 0, 16: 4950})
    >>> count_four_sided(35)
    (9, {8: 0, 16: 4950, 35: 9})
    """
    if n in D_4.keys():
        return D_4[n], D_4
    else:
        dice = [[n for n in range(1, 5)]] * 9
        sums = [sum(item) for item in product(*dice)]
        D_4[n] = sums.count(n)
        return D_4[n], D_4


def count_six_sided(n: int, D_6={}) -> int:
    """
    It returns the number of combinations of six six-sided dice such that
    the sum of the dice is exactly n.
    >>> count_six_sided(8)
    (21, {8: 21})
    >>> count_six_sided(16)
    (2247, {8: 21, 16: 2247})
    >>> count_six_sided(35)
    (6, {8: 21, 16: 2247, 35: 6})
    """
    if n in D_6.keys():
        return D_6[n], D_6
    else:
        dice = [[n for n in range(1, 7)]] * 6
        sums = [sum(item) for item in product(*dice)]
        D_6[n] = sums.count(n)
        return D_6[n], D_6


def prob_win_four_sided(n: int, D_4={}, D_6={}) -> float:
    """
    Given a number 7 <= n <= 36,
    it returns the exact probability that the sum obtained with nine four-sided dice
    is bigger that the sum obtained with six six-sided dice.
    >>> prob_win_four_sided(8)
    (0.00045010288065843606, {7: 0, 8: 0}, {8: 21})
    >>> prob_win_four_sided(10)
    (0.0027005142635769305, {7: 0, 8: 0, 9: 1, 10: 9}, {8: 21, 10: 126})
    """
    tot_6, D_6 = count_six_sided(n, D_6)
    p_6 = tot_6 * (1 / 6) ** 6
    p_win = 1
    for i in range(7, n + 1):
        tot_4, D_4 = count_four_sided(i, D_4)
        p_win -= tot_4 * (1 / 4) ** 9
    return p_win * p_6, D_4, D_6


def solution() -> float:
    """
    It return the probability that the sum of of nine four-sided dice is
    bigger than the sum of six six-sided dice.
    The final answer is given as a float with 7 decimal digits.
    """
    D_4, D_6 = {}, {}
    probability = 0
    for n in range(6, 37):
        p_n, D_4, D_6 = prob_win_four_sided(n, D_4, D_6)
        probability += p_n
    return round(probability, 7)


if __name__ == "__main__":
    print(f"{solution() = }")
