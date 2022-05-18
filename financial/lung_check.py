"""
A pure python implementation of the lugh algortihm.

The lugh algortihm is a simple checksum formula
used to validate a variety of identification numbers, such as credit card numbers, 
IMEI numbers, SIM card numbers and more.

from: https://en.wikipedia.org/wiki/Luhn_algorithm

For doctests run following command:
python3 -m doctest -v lung_check.py

For manual testing run:
python3 lung_check.py

"""
def luhn_check(card_no: str) -> bool:
    """
    A pure python implementation of the lugh algortihm.

    :param card_no: a card number to be validated
    :return: True / False

    Examples:
    >>> luhn_check("7656449456")
    True
    >>> luhn_check("7626449456")
    False
    >>> luhn_check("7850889192")
    True
    """
    card_digits = len(str(card_no))
    luhn_sum = 0
    second = False

    for i in range(card_digits - 1, -1, -1):
        d = ord(card_no[i]) - ord('0')

        if (second == True):
            d = d * 2

        luhn_sum += d // 10
        luhn_sum += d % 10

        second = not second

    if (luhn_sum % 10 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    user_input = input("Enter a number:\n").strip()
    print(luhn_check(user_input))
