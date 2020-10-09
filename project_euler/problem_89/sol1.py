"""
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

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains
one thousand numbers written in valid, but not necessarily minimal, Roman numerals;
see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four
consecutive identical units.
"""

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(s: str) -> int:
    """
    Convert romanan numeral to integer.
    >>> roman_to_int("XVI")
    16
    >>> roman_to_int("XLIX")
    49
    >>> roman_to_int("MDCVI")
    1606
    """
    ret = 0
    idx = 0
    while idx < len(s) - 1:
        one = s[idx]
        two = s[idx + 1]
        if VALUES[one] < VALUES[two]:
            ret += VALUES[two] - VALUES[one]
            idx += 2
        else:
            ret += VALUES[one]
            idx += 1
    if idx == len(s) - 1:
        ret += VALUES[s[-1]]
    return ret


def int_to_roman(
    n: int, canD: bool = True, canL: bool = True, canV: bool = True
) -> str:
    """
    Recursively convert an integer to minimal Roman numeral form.
    >>> int_to_roman(16)
    'XVI'
    >>> int_to_roman(49)
    'XLIX'
    >>> int_to_roman(1606)
    'MDCVI'
    """
    if n >= 1000:
        return "M" + int_to_roman(n - 1000, canD, canL, canV)
    elif n >= 900:
        return "CM" + int_to_roman(n - 900, canD, canL, canV)
    elif n >= 500 and canD:
        return "D" + int_to_roman(n - 500, False, canL, canV)
    elif n >= 400 and canD:
        return "CD" + int_to_roman(n - 400, False, canL, canV)
    elif n >= 100:
        return "C" + int_to_roman(n - 100, canD, canL, canV)
    elif n >= 90:
        return "XC" + int_to_roman(n - 90, canD, canL, canV)
    elif n >= 50:
        return "L" + int_to_roman(n - 50, canD, False, canV)
    elif n >= 40:
        return "XL" + int_to_roman(n - 40, canD, False, canV)
    elif n >= 10:
        return "X" + int_to_roman(n - 10, canD, canL, canV)
    elif n >= 9:
        return "IX" + int_to_roman(n - 9, canD, canL, canV)
    elif n >= 5:
        return "V" + int_to_roman(n - 5, canD, canL, False)
    elif n >= 4:
        return "IV" + int_to_roman(n - 4, canD, canL, False)
    elif n >= 1:
        return "I" + int_to_roman(n - 1, canD, canL, False)
    else:
        return ""


def gains(word: str) -> int:
    """
    Calculate the number of character saved by writing a roman integer in its
    minimal form.
    >>> gains("MMMDLXVIIII")
    3
    >>> gains("MDCCCXXIIII")
    2
    >>> gains("MMCXCVI")
    0
    """
    return len(word) - len(int_to_roman(roman_to_int(word)))


def solution() -> int:
    #    with open("_p089_roman.txt", "r") as f:
    #        words = f.read().split("\n")

    from .data import WORDS

    return sum(gains(word.strip()) for word in WORDS)


if __name__ == "__main__":
    print(solution())
