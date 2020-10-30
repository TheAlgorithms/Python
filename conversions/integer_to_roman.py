def int_to_roman(number: int) -> str:
    """
    Convert integer to roman numerals
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> int_to_roman(3456)
    'MMMCDLVI'
    >>> int_to_roman(3999)
    'MMMCMXCIX'
    """
    vals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL":40, "X": 10, "IX": 9, "V": 5, "IV":4, "I": 1}
    roman_num = ""

    while number > 0:
        for i, r in vals.items():
            while number >= r:
                roman_num += i
                number -= r

    return roman_num

if __name__ == "__main__":
    import doctest

    doctest.testmod()
