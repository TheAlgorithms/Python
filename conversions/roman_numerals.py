ROMAN_NUMERALS = {
    1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
    90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
}

def roman_to_int(roman):
    result = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in ROMAN_NUMERALS:
            result += ROMAN_NUMERALS[roman[i:i+2]]
            i += 2
        else:
            result += ROMAN_NUMERALS[roman[i]]
            i += 1
    return result

def int_to_roman(number):
    result = ""
    for value, numeral in ROMAN_NUMERALS.items():
        while number >= value:
            result += numeral
            number -= value
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
