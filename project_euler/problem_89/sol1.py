"""
Project Euler Problem 89
https://projecteuler.net/problem=89

For a number written in Roman numerals to be considered valid there are basic rules
which must be followed. Even though the rules allow some numbers to be expressed in
more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number
sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example
is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one
thousand numbers written in valid, but not necessarily minimal, Roman numerals; see
About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four
consecutive identical units.
"""

import os

symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def parse_roman_numerals(numerals: str) -> int:
    """
    Converts a string of roman numerals to an integer.
    e.g.
    >>> parse_roman_numerals("LXXXIX")
    89
    >>> parse_roman_numerals("IIII")
    4
    """

    num = 0

    i = 0
    while i < len(numerals) - 1:
        value = symbols[numerals[i]]
        next_value = symbols[numerals[i + 1]]
        if value < next_value:
            num -= value
        else:
            num += value
        i += 1
    num += symbols[numerals[i]]

    return num


def generate_roman_numerals(num: int) -> str:
    """
    Generates a string of roman numerals for a given integer.
    e.g.
    >>> generate_roman_numerals(89)
    'LXXXIX'
    >>> generate_roman_numerals(4)
    'IV'
    """

    numerals = ""

    m = num // 1000
    numerals += m * "M"
    num %= 1000

    c = num // 100
    if c == 9:
        numerals += "CM"
        c -= 9
    elif c == 4:
        numerals += "CD"
        c -= 4
    if c >= 5:
        numerals += "D"
        c -= 5
    numerals += c * "C"
    num %= 100

    x = num // 10
    if x == 9:
        numerals += "XC"
        x -= 9
    elif x == 4:
        numerals += "XL"
        x -= 4
    if x >= 5:
        numerals += "L"
        x -= 5
    numerals += x * "X"
    num %= 10

    if num == 9:
        numerals += "IX"
        num -= 9
    elif num == 4:
        numerals += "IV"
        num -= 4
    if num >= 5:
        numerals += "V"
        num -= 5
    numerals += num * "I"

    return numerals


def solution(roman_numerals_filename: str = "/p089_roman.txt") -> int:
    """
    Calculates and returns the answer to project euler problem 89.

    Answer:
    >>> solution("/numeralcleanup_test.txt")
    16
    """

    savings = 0

    file1 = open(os.path.dirname(__file__) + roman_numerals_filename, "r")
    lines = file1.readlines()
    for line in lines:
        original = line.strip()
        num = parse_roman_numerals(original)
        shortened = generate_roman_numerals(num)
        savings += len(original) - len(shortened)

    return savings


if __name__ == "__main__":

    print(solution())
