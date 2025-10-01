"""Converts a given string to integer and float
This works with only Indian system of wording

 * Indian system uses crore, lakh, thousand and not million and billions

For the part after the decimal example ( .159 ):
     * Digit by digit ( .159 ) -> point one five nine is allowed
     * Anything else will throw an error

>>> to_int("Five")
5
>>> to_float("Five")
5.0

>>> to_int("One thousand five hundred and two")
1502
>>> to_float("One thousand five hundred and two")
1502.0

>>> to_int(
...     "Ninety nine crore three lakh seventy two thousand and six point one five nine"
... )
990372006

>>> to_float(
...     "Ninety nine crore three lakh seventy two thousand and six point one five nine"
... )
990372006.159

wikipedia explanation - https://en.wikipedia.org/wiki/Numeral_(linguistics)
"""


def to_int(word: str) -> int:
    if len(word.strip()) > 0:
        units = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
        }

        tens = {
            "ten": 10,
            "twenty": 20,
            "thirty": 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty": 80,
            "ninety": 90,
        }

        multipliers = {
            "hundred": 100,
            "thousand": 1_000,
            "lakh": 1_00_000,
            "crore": 1_00_00_000,
        }

        if "point" in word:
            word_lst = word.split("point")
            word = "".join(word_lst[:-1])

        words = (
            word.strip()
            .replace(" and", "")
            .replace("-", "")
            .replace("_", "")
            .lower()
            .split()
        )

        number = 0
        temp = 0

        for index, word in enumerate(words):
            if index == 0:
                if word in units:
                    temp += units[word]
                elif word in tens:
                    temp += tens[word]
                else:
                    temp += multipliers[word]
            elif index == (len(words) - 1):
                if word in units:
                    temp += units[word]
                    number += temp
                elif word in tens:
                    temp += tens[word]
                    number += temp
                else:
                    temp *= multipliers[word]
                    number += temp
            elif word in units:
                temp += units[word]
            elif word in tens:
                temp += tens[word]
            elif word in multipliers:
                temp *= multipliers[word]
                number += temp
                temp = 0

        if len(words) > 1:
            return number
        else:
            return temp
    else:
        raise ValueError("Empty input is not a valid number in words")


def to_float(word: str) -> float:
    units = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
    }

    all_words = (
        word.strip()
        .replace(" and", "")
        .replace("-", "")
        .replace("_", "")
        .lower()
        .split("point")
    )
    if len(all_words) > 1:
        word = all_words[0]
        after_point = all_words[1].split()

        integer_part = to_int(word)

        decimal_part = ""
        for num in after_point:
            if num in units:
                decimal_part += str(units[num])

        str_float = str(integer_part) + str(decimal_part)
        divider = "1" + ("0" * len(after_point))
        return int(str_float) / int(divider)

    else:
        return float(to_int(word))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # while True:
    #     word = input("Enter a number in words (q to quit) :- ").lower().strip()
    #     if word == "q":
    #         break
    #     else:
    #         integer = to_int(word)
    #         print(f"\nThe number in {type(integer)} --> {integer} ")
    #         floater = to_float(word)
    #         print(f"\nThe number in {type(floater)} --> {floater} ")
