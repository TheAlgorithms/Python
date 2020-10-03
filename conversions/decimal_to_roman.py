"""Convert decimal numeral into roman numeral."""
ROMAN = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


def decimal_to_roman(num: int) -> str:
    r"""
    Given a decimal numeral, convert it to roman numeral.
    https://en.wikipedia.org/wiki/ROMAN
    >>> tests1 = {1: "I", 5: "V", 15: "XV", 29: "XXIX", 113: "CXIII"}
    >>> tests2 = {470: "CDLXX", 867: "DCCCLXVII", 3511: "MMMDXI", 4000: "NONE"}
    >>> all(decimal_to_roman(key) == value for key, value in tests1.items())
    True
    >>> all(decimal_to_roman(key) == value for key, value in tests2.items())
    True
    """
    # validating input
    if not (0 < num < 4000):
        return "NONE"

    num = str(num)  # to iterate over digits
    roman = []
    append = roman.append
    for i, d in enumerate(num):
        d = int(d)
        if not d:  # if d == 0 nothing to be done
            continue

        # to calculate effective value of d in num e.g. 2 in 1205 has
        # place = 100, so effective value is 200
        place = 10 ** (len(num) - i - 1)

        # checking if there is a reserved representation for this effective
        # value
        if d * place in ROMAN:
            append(ROMAN[d * place])

        # checking if there is a non-trivial representation for this effective
        # value e.g. 4 is "IV" not "IIII"
        elif (d + 1) * place in ROMAN:
            append(ROMAN[place])
            append(ROMAN[(d + 1) * place])
        else:
            # making some trivial checks
            if d > 5:
                try:
                    append(ROMAN[5 * place])
                    d -= 5
                except KeyError:
                    break
            while d:
                try:
                    append(ROMAN[place])
                    d -= 1
                except KeyError:
                    break
    return "".join(roman) if roman else "NONE"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
