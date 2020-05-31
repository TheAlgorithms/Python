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
    total_sum = 0
    temp_sum = 0
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
        name = str(file.readlines()[0])
        name = name.replace('"', "").split(",")

    name.sort()
    for i in range(len(name)):
        for j in name[i]:
            temp_sum += ord(j) - ord("A") + 1
        total_sum += (i + 1) * temp_sum
        temp_sum = 0
    return total_sum


if __name__ == "__main__":
    print(solution())
