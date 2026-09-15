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
    >>> roman_to_int("iii")
    3
    >>> roman_to_int("")
    Traceback (most recent call last):
        ...
    ValueError: Input cannot be an empty string
    >>> roman_to_int("MIX-abc")
    Traceback (most recent call last):
        ...
    ValueError: Invalid Roman numeral character: -
    """
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = roman.upper()
    if not roman:
        raise ValueError("Input cannot be an empty string")
    for char in roman:
        if char not in vals:
            msg = f"Invalid Roman numeral character: {char}"
            raise ValueError(msg)

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
    Given an integer, convert it to a roman numeral.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    >>> all(int_to_roman(value) == key for key, value in tests.items())
    True
    >>> int_to_roman(0)
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer between 1 and 3999
    >>> int_to_roman(-5)
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer between 1 and 3999
    >>> int_to_roman(4000)
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer between 1 and 3999
    >>> int_to_roman(1.5)  # type: ignore[arg-type]
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer between 1 and 3999
    """
    if not isinstance(number, int) or not (0 < number < 4000):
        raise ValueError("Input must be an integer between 1 and 3999")

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
