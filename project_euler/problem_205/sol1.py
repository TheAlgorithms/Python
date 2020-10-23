"""
Project Euler Problem 205: https://projecteuler.net/problem=205

Problem:
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
Peter and Colin roll their dice and compare totals: the highest total wins. 
The result is a draw if the totals are equal.
What is the probability that Pyramidal Pete beats Cubic Colin? 
Give your answer rounded to seven decimal places in the form 0.abcdefg

Solution:
Made all possible rolls and put sum of rolls in a list and then sorted.
Iterated through 6-sided dice and compared to 4-sided dice to count how many more
possibilities great than given roll. Divide that by all possible rolls.

"""

from itertools import product

def solution():
    """
    >>> solution()
    0.5731441
    """

    #makes dice possibilities
    four_sided = list(product(range(1,5), repeat=9))
    six_sided = list(product(range(1,7), repeat=6))

    count = 0

    sums_four_sided = []
    sums_six_sided = []

    #adding sums of dice
    for total_of_four in four_sided:
        sums_four_sided.append(sum(total_of_four))      
    for total_of_six in six_sided :
        sums_six_sided.append(sum(total_of_six))

    #sorting to make easier to compare
    sums_four_sided.sort()
    sums_six_sided.sort()

    #comparing sums and than subtracting the rest to shorten time
    for sum_1 in sums_six_sided:
        for num, sum_2 in enumerate(sums_four_sided):
            if sum_2 > sum_1:
                count += (len(sums_four_sided) - num)
                break

    return format(count/(len(sums_six_sided)*len(sums_four_sided)), '.7')


if __name__ == "__main__":
    print(f"{solution() = }")
