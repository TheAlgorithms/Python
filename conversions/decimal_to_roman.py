"""Convert decimal numeral into roman numeral."""


def decimal_to_roman(num: int) -> str:
    """
    Given a decimal numeral, convert it to roman numeral.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {1: "I", 5: "V", 15: "XV", 29: "XXIX", 113: "CXIII",
                470: "CDLXX", 867: "DCCCLXVII", 3511: "MMMDXI", 4000: "NONE"}
    >>> all(decimal_to_roman(key) == value for key, value in tests.items())
    True
    """

    Roman_numerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

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
        if d * place in Roman_numerals:
            append(Roman_numerals[d * place])

        # checking if there is a non-trivial representation for this effective
        # value e.g. 4 is "IV" not "IIII"
        elif (d + 1) * place in Roman_numerals:
            append(Roman_numerals[place])
            append(Roman_numerals[(d + 1) * place])
        else:
            # making some trivial checks
            if d > 5:
                try:
                    append(Roman_numerals[5 * place])
                    d -= 5
                except KeyError:
                    break
            while d:
                try:
                    append(Roman_numerals[place])
                    d -= 1
                except KeyError:
                    break
    return "".join(roman) if roman else "NONE"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
