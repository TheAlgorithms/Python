"""
Project Euler Problem 100: https://projecteuler.net/problem=100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

References:
- https://www.mathblog.dk/project-euler-100-blue-discs-two-blue/
"""

def solution(blue_discs: int, total_discs: int) -> int:
    """
    Finds number of blue discs
    1st parameter is the total blue discs
    2nd parameter is the total number of discs
    
    >>> soultion(15, 21)
    756872327473
    """
    target = 1000000000000
    while(total_discs < target):
        btemp = 3 * blue_discs + 2 * total_discs - 2
        ntemp = 4 * blue_discs + 3 * total_discs - 3
        blue_discs = btemp
        total_discs = ntemp
    return blue_discs

if __name__ == "__main__":
    print("number of blue discs ", solution(15, 21))