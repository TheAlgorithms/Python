ROMAN = [
    (1000000, "M_"), (900000, "C_M_"), (500000, "D_"), (400000, "C_D_"),
    (100000, "C_"), (90000, "X_C_"), (50000, "L_"), (40000, "X_L_"),
    (10000, "X_"), (9000, "I_X_"), (5000, "V_"), (4000, "I_V_"),
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
def roman_to_int(roman: str) -> int:
    """
    Convert a Roman numeral to an integer, supporting Vinculum notation
    (underscore _ represents 1000 times).

    LeetCode No. 13 Roman to Integer:
    Given a Roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.

    Reference: https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500,
    ...          "MMMCMXCIX": 3999, "I_V_": 4000, "X_": 10000, "M_": 1000000}
    >>> all(roman_to_int(key) == value for key, value in tests.items())
    True
    """
    vals = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "I_": 1000, "V_": 5000, "X_": 10000, "L_": 50000, "C_": 100000,
        "D_": 500000, "M_": 1000000
    }

    i, total = 0, 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in vals:
            total += vals[roman[i:i+2]]
            i += 2
        else:
            total += vals[roman[i]]
            i += 1
    return total


def int_to_roman(number: int) -> str:
    """
    Convert an integer to a Roman numeral, supporting Vinculum notation
    (underscore _ represents 1000 times).

    Given an integer, convert it to a Roman numeral.

    Reference:https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500,
    ...          "MMMCMXCIX": 3999, "I_V_": 4000, "X_": 10000, "M_": 1000000}
    >>> all(int_to_roman(value) == key for key, value in tests.items())
    True
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Input must be a positive integer greater than 0")

    result = []
    for arabic, roman in ROMAN:
        factor, number = divmod(number, arabic)
        result.append(roman * factor)
        if number == 0:
            break
    return "".join(result)

   if __name__ == "__main__":
       import doctest
       doctest.testmod()
