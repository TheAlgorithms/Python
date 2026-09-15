ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def roman_to_int(roman: str) -> int:
    """
    LeetCode No. 13 Roman to Integer
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    >>> all(roman_to_int(key) == value for key, value in tests.items())
    True
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


def int_to_roman(number: int) -> str:
    """
    Given an integer, convert it to a Roman numeral.
    Input must be an integer in the range 1 to 3999.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    >>> all(int_to_roman(value) == key for key, value in tests.items())
    True
    >>> int_to_roman(0)
    Traceback (most recent call last):
        ...
    ValueError: int_to_roman only accepts integers in the range 1 to 3999, got 0
    >>> int_to_roman(-1)
    Traceback (most recent call last):
        ...
    ValueError: int_to_roman only accepts integers in the range 1 to 3999, got -1
    >>> int_to_roman(4000)
    Traceback (most recent call last):
        ...
    ValueError: int_to_roman only accepts integers in the range 1 to 3999, got 4000
    >>> int_to_roman(True)
    Traceback (most recent call last):
        ...
    TypeError: int_to_roman only accepts integers, got bool
    """
    if not isinstance(number, int) or isinstance(number, bool):
        msg = f"int_to_roman only accepts integers, got {type(number).__name__}"
        raise TypeError(msg)
    if not 1 <= number <= 3999:
        msg = f"int_to_roman only accepts integers in the range 1 to 3999, got {number}"
        raise ValueError(msg)
    result = []
    for arabic, roman in ROMAN:
        (factor, number) = divmod(number, arabic)
        result.append(roman * factor)
        if number == 0:
            break
    return "".join(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
