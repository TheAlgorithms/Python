def roman_to_int(s: str) -> int:
    # Store roman numbers in a dictionary
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    conversion = 0
    # iterate through the string
    for i in range(len(s)):
        if i < len(s) - 1:
            if roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                conversion = conversion - roman_numerals[s[i]]
            else:
                conversion = conversion + roman_numerals[s[i]]
        else:
            conversion = conversion + roman_numerals[s[i]]
    return conversion


if __name__ == "__main__":
    print(roman_to_int("XIV"))  # Should be 14
    print(roman_to_int("MCMXCIV"))  # Should be 1994
