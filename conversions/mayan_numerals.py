"""
Conversion of numbers from the decimal number system to the vigecimal numeral system
used by the Mayans in their time.

Available Functions:
-> From int to mayan.
-> From mayan to int.

USAGE :
-> Import this file into their respective project.
-> Use the function mayan_to_int() for conversion of numbers in the Mayan system to decimal.
-> Parameters :
    -> mayan_levels[] : The Mayan numbers arranged according to their level (determined by their
                        position in the arrangement), the zero symbol can be include.
-> Or use the function int_to_mayan() for conversion of decimal numbers to the Mayan system. The zero
    symbol is not include in the return array.
-> Parameters :
    -> number : The decimal number to convert in the Mayan system.

REFERENCES :
-> Wikipedia reference: https://en.wikipedia.org/wiki/Maya_numerals
-> Wikipedia reference: https://en.wikipedia.org/wiki/Positional_notation
-> https://courses.lumenlearning.com/waymakermath4libarts/chapter/the-mayan-numeral-system/

"""

SYMBOLS = {
    "o": 0,
    ".": 1,
    "..": 2,
    "...": 3,
    "....": 4,
    "|": 5,
    ".|": 6,
    "..|": 7,
    "...|": 8,
    "....|": 9,
    "||": 10,
    ".||": 11,
    "..||": 12,
    "...||": 13,
    "....||": 14,
    "|||": 15,
    ".|||": 16,
    "..|||": 17,
    "...|||": 18,
    "....|||": 19,
}


def mayan_to_int(mayan_levels: list[str]) -> int:
    """
    Conversion from mayan to decimal
    >>> mayan_to_int(["o", ".", "..||"])
    32
    >>> mayan_to_int([".", ".", "....|"])
    429
    >>> mayan_to_int(["..||", ".|||", "|"])
    5125
    >>> mayan_to_int(["IX", "|||||", "....."])
    Traceback (most recent call last):
        ...
    ValueError: Invalid 'symbol' value: 'IX',  Supported values are:
    o, ., .., ..., ...., |, .|, ..|, ...|, ....|, ||, .||, ..||, ...||, ....||, |||, .|||, ..|||, ...|||, ....|||
    """

    decimal_number = 0
    levels = len(mayan_levels)

    for index in range(levels):
        symbol = mayan_levels[index]

        if symbol not in SYMBOLS:
            raise ValueError(
                f"Invalid 'symbol' value: {symbol!r},  Supported values are:\n"
                + ", ".join(list(SYMBOLS))
            )

        level_value = SYMBOLS[symbol]
        power = levels - (index + 1)

        decimal_number += level_value * (20**power)

    return decimal_number


def int_to_mayan(number: int) -> list[str]:
    """
    Conversion from decimal to mayan.
    >>> int_to_mayan(32)
    ['.', '..||']
    >>> int_to_mayan(429)
    ['.', '.', '....|']
    >>> int_to_mayan(5125)
    ['..||', '.|||', '|']
    >>> int_to_mayan(-10)
    Traceback (most recent call last):
        ...
    ValueError: Invalid 'number' value: -10,  Supported values greater than zero (positives).
    """

    if number < 0:
        raise ValueError(
            f"Invalid 'number' value: {number!r},  Supported values greater than zero (positives)."
        )

    mayan_levels = []

    levels = get_levels(number)
    remainder = number

    for index in range(levels):
        power = levels - (index + 1)

        quotient = int(remainder / (20**power))
        remainder = number % (20**power)

        mayan_levels.append(list(SYMBOLS)[quotient])

    return mayan_levels


def get_levels(number: int) -> int:
    quotient = number
    levels = 0

    while quotient >= 1:
        quotient = quotient / 20
        levels += 1

    return levels


if __name__ == "__main__":
    import doctest

    doctest.testmod()
