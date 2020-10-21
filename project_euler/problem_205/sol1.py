"""
Project Euler Problem 205: https://projecteuler.net/problem=205

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
Peter and Colin roll their dice and compare totals: the highest total wins. The result
is a draw if the totals are equal.
What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded
to seven decimal places in the form 0.abcdefg

In the solution for all possible permutations of each player's dice points the sum of
points and number of occurrences are calculated. The number of occurrences are divided
by number of dice draws to get their probability.
Then for each permutation of the possible dice sum per draw between the two players the
 probabilities each time where Peter wins are added up to calculate the solution.
To generate the permutations 'itertools.product' is used.

"""

from itertools import product


def probability_of_sums(dice_max_points: int = 6, dice_number: int = 6) -> (list, list):
    """
    Returns the list of possible sums and their probabilities of dice_number dices with
    numbers from dice_min to dice_max

    >>> probability_of_sums(dice_max_points=5, dice_number=2)
    ([2, 3, 4, 5, 6, 7, 8, 9, 10], \
[0.04, 0.08, 0.12, 0.16, 0.2, 0.16, 0.12, 0.08, 0.04])

    """

    sums = []
    counter = []
    for dices in product(range(1, dice_max_points + 1), repeat=dice_number):
        s = sum(dices)
        if s not in sums:  # sum has not occurred, set count to 1
            sums.append(s)
            counter.append(1)
        else:  # sum has occurred, increment sum by 1
            idx = sums.index(s)
            counter[idx] += 1
    total = sum(counter)
    probability = [_t / total for _t in counter]

    return sums, probability


def solution(
    peter_dice_points: int = 4,
    peter_dice_number: int = 9,
    colin_dice_points: int = 6,
    colin_dice_number: int = 6,
) -> float:
    """
    Returns the probability of Peter winning in dice game with nine four-sided
    dice (1, 2, 3, 4 points) against Colin who has six six-sided dice (1, 2, 3, 4, 5,
    6). Winner of a match is who has more total points.
    Algorithm calculates the possible point sums for each player and their
    probabilities. Peter's probability to win is summed up from all the permutations
    where he has more points than Colin.

    >>> solution(peter_dice_points=6, peter_dice_number=5,
    ...          colin_dice_points=5, colin_dice_number=6)
    0.4241348

    """

    peter_wins = 0
    colin_wins = 0
    draw = 0
    for sums_peter, probabilities_peter in zip(
        *probability_of_sums(peter_dice_points, peter_dice_number)
    ):
        for sums_colin, probabilities_colin in zip(
            *probability_of_sums(colin_dice_points, colin_dice_number)
        ):
            p_branch = probabilities_peter * probabilities_colin
            if sums_peter > sums_colin:
                peter_wins += p_branch
            elif sums_colin > sums_peter:
                colin_wins += p_branch
            else:
                draw += p_branch

    return round(peter_wins, 7)


if __name__ == "__main__":
    print(f"{solution() = }")
