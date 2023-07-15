import math


def convert(number: int) -> str:
    """
    Given a number return the number in words.

    >>> convert(123)
    'OneHundred,TwentyThree'
    """
    if number == 0:
        words = "Zero"
        return words
    else:
        digits = math.log10(number)
        digits = digits + 1
        singles = {}
        singles[0] = ""
        singles[1] = "One"
        singles[2] = "Two"
        singles[3] = "Three"
        singles[4] = "Four"
        singles[5] = "Five"
        singles[6] = "Six"
        singles[7] = "Seven"
        singles[8] = "Eight"
        singles[9] = "Nine"

        doubles = {}
        doubles[0] = ""
        doubles[2] = "Twenty"
        doubles[3] = "Thirty"
        doubles[4] = "Forty"
        doubles[5] = "Fifty"
        doubles[6] = "Sixty"
        doubles[7] = "Seventy"
        doubles[8] = "Eighty"
        doubles[9] = "Ninety"

        teens = {}
        teens[0] = "Ten"
        teens[1] = "Eleven"
        teens[2] = "Twelve"
        teens[3] = "Thirteen"
        teens[4] = "Fourteen"
        teens[5] = "Fifteen"
        teens[6] = "Sixteen"
        teens[7] = "Seventeen"
        teens[8] = "Eighteen"
        teens[9] = "Nineteen"

        placevalue = {}
        placevalue[2] = "Hundred,"
        placevalue[3] = "Thousand,"
        placevalue[5] = "Lakh,"
        placevalue[7] = "Crore,"

        temp_num = number
        words = ""
        counter = 0
        digits = int(digits)
        while counter < digits:
            current = temp_num % 10
            if counter % 2 == 0:
                addition = ""
                if counter in placevalue and current != 0:
                    addition = placevalue[counter]
                if counter == 2:
                    words = singles[current] + addition + words
                elif counter == 0:
                    if ((temp_num % 100) // 10) == 1:
                        words = teens[current] + addition + words
                        temp_num = temp_num // 10
                        counter += 1
                    else:
                        words = singles[current] + addition + words

                else:
                    words = doubles[current] + addition + words

            else:
                if counter == 1:
                    if current == 1:
                        words = teens[number % 10] + words
                    else:
                        addition = ""
                        if counter in placevalue:
                            addition = placevalue[counter]
                        words = doubles[current] + addition + words
                else:
                    addition = ""
                    if counter in placevalue:
                        if current == 0 and ((temp_num % 100) // 10) == 0:
                            addition = ""
                        else:
                            addition = placevalue[counter]
                    if ((temp_num % 100) // 10) == 1:
                        words = teens[current] + addition + words
                        temp_num = temp_num // 10
                        counter += 1
                    else:
                        words = singles[current] + addition + words
            counter += 1
            temp_num = temp_num // 10
    return words


if __name__ == "__main__":
    import doctest

    doctest.testmod()
