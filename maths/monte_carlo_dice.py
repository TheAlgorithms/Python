import random
from typing import List

class Dice:
    NUM_SIDES = 6

    def __init__(self):
        """ Initialize a six sided dice """
        self.sides = list(range(1, Dice.NUM_SIDES + 1))

    def roll(self):
        return random.choice(self.sides)

    def _str_(self):
        return "Fair Dice"


def throw_dice(num_throws: int, num_dice: int=2) -> List[float]:
    """
    Return probability list of all possible sums when throwing dice.

    >>> random.seed(0)
    >>> throw_dice(10, 1)
    [10.0, 0.0, 30.0, 50.0, 10.0, 0.0]
    >>> throw_dice(100, 1)
    [19.0, 17.0, 17.0, 11.0, 23.0, 13.0]
    >>> throw_dice(1000, 1)
    [18.8, 15.5, 16.3, 17.6, 14.2, 17.6]
    >>> throw_dice(10000, 1)
    [16.35, 16.89, 16.93, 16.6, 16.52, 16.71]
    >>> throw_dice(10000, 2)
    [2.74, 5.6, 7.99, 11.26, 13.92, 16.7, 14.44, 10.63, 8.05, 5.92, 2.75]
    """
    dices = [Dice() for i in range(num_dice)]
    count_of_sum = [0] * (len(dices) * Dice.NUM_SIDES + 1)
    for i in range(num_throws):
        count_of_sum[sum([dice.roll() for dice in dices])] += 1
    probability = [round((count * 100) / num_throws, 2) for count in count_of_sum]
    return probability[num_dice:]  # remove probability of sums that never appear


if __name__ == "__main__":
    import doctest

    doctest.testmod()
