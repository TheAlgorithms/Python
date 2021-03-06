"""
A bag contains one red disc and one blue disc. In a game of chance a player takes a
disc at random and its colour is noted. After each turn the disc is returned to the
bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red
discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly
11/120, and so the maximum prize fund the banker should allocate for winning in this
game would be £10 before they would expect to incur a loss. Note that any payout will
be a whole number of pounds and also includes the original £1 paid to play the game,
so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which
fifteen turns are played.


Solution:
    For each 15-disc sequence of red and blue for which there are more red than blue,
    we calculate the probability of that sequence and add it to the total probability
    of the player winning. The inverse of this probability gives an upper bound for
    the prize if the banker wants to avoid an expected loss.
"""

from itertools import product


def solution(num_turns: int = 15) -> int:
    """
    Find the maximum prize fund that should be allocated to a single game in which
    fifteen turns are played.
    >>> solution(4)
    10
    >>> solution(10)
    225
    """
    total_prob: float = 0.0
    prob: float
    num_blue: int
    num_red: int
    ind: int
    col: int
    series: tuple[int, ...]

    for series in product(range(2), repeat=num_turns):
        num_blue = series.count(1)
        num_red = num_turns - num_blue
        if num_red >= num_blue:
            continue
        prob = 1.0
        for ind, col in enumerate(series, 2):
            if col == 0:
                prob *= (ind - 1) / ind
            else:
                prob *= 1 / ind

        total_prob += prob

    return int(1 / total_prob)


if __name__ == "__main__":
    print(f"{solution() = }")
