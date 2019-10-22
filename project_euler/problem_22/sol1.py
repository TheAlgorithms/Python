# -*- coding: latin-1 -*-
"""
Name scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import os


def solution():
    """Returns the total of all the name scores in the file.

    >>> solution()
    871198282
    """
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
        names = str(file.readlines()[0])
        names = names.replace('"', "").split(",")

    names.sort()

    name_score = 0
    total_score = 0

    for i, name in enumerate(names):
        for letter in name:
            name_score += ord(letter) - 64

        total_score += (i + 1) * name_score
        name_score = 0
    return total_score


if __name__ == "__main__":
    print(solution())
