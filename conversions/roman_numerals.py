ROMAN = [
    (1000000, "M_"),
    (900000, "C_M_"),
    (500000, "D_"),
    (400000, "C_D_"),
    (100000, "C_"),
    (90000, "X_C_"),
    (50000, "L_"),
    (40000, "X_L_"),
    (10000, "X_"),
    (9000, "I_X_"),
    (5000, "V_"),
    (4000, "I_V_"),
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


def roman_to_int(roman):
    vals = {roman: arabic for arabic, roman in ROMAN}
    i, total = 0, 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i + 1] == "_":
            total += vals[roman[i] + "_"]
            i += 2
        else:
            total += vals[roman[i]]
            i += 1
    return total


def int_to_roman(number):
    if not isinstance(number, int) or number <= 0:
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
