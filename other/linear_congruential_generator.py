__author__ = "Tobias Carryer"

from time import time


class LinearCongruentialGenerator:
    """
    A pseudorandom number generator.
    """

    def __init__(self, multiplier, increment, modulo, seed=int(time())):
        """
        These parameters are saved and used when nextNumber() is called.

        modulo is the largest number that can be generated (exclusive). The most
        efficient values are powers of 2. 2^32 is a common value.
        """
        self.multiplier = multiplier
        self.increment = increment
        self.modulo = modulo
        self.seed = seed

    def next_number(self):
        """
        The smallest number that can be generated is zero.
        The largest number that can be generated is modulo-1. modulo is set in the constructor.
        """
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulo
        return self.seed


if __name__ == "__main__":
    # Show the LCG in action.
    lcg = LinearCongruentialGenerator(1664525, 1013904223, 2 << 31)
    while True:
        print(lcg.next_number())
