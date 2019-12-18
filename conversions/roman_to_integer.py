def roman_to_int(roman: str) -> int:
    """
    LeetCode No. 13 Roman to Integer
    Given a roman numeral, convert it to an integer. 
    Input is guaranteed to be within the range from 1 to 3999.
    >>> roman_to_int("III")
    3
    >>> roman_to_int("CLIV")
    154
    >>> roman_to_int("MMD")
    2500
    """
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    place = 0
    while place < len(roman):
        if (place + 1 < len(roman)) and (vals[roman[place]] < vals[roman[place + 1]]):
            total += vals[roman[place + 1]] - vals[roman[place]]
            place += 2
        else:
            total += vals[roman[place]]
            place += 1
    return total


if __name__ == "__main__":
    import doctest

    doctest.testmod()
