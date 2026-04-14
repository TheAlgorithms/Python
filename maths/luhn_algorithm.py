"""
Luhn Algorithm — credit card number validation.

The Luhn algorithm (also known as the "modulus 10" or "mod 10" algorithm) is a
simple checksum formula used to validate identification numbers such as credit
card numbers, IMEI numbers, and Canadian Social Insurance Numbers.

Algorithm:
  1. From the rightmost digit (the check digit) and moving left, double the
     value of every second digit.
  2. If the result of doubling is greater than 9, subtract 9.
  3. Sum all the digits (the undoubled ones and the doubled/adjusted ones).
  4. If the total modulo 10 is 0, then the number is valid.

References:
  - https://en.wikipedia.org/wiki/Luhn_algorithm
"""


def luhn_check(card_number: str) -> bool:
    """Validate a credit card number (given as a digit string) using the Luhn
    algorithm.

    :param card_number: A string containing only digit characters representing
                        the card number to validate.
    :raises ValueError: If *card_number* contains any non-digit characters.
    :return: ``True`` if the number is valid according to the Luhn algorithm,
             ``False`` otherwise.

    Examples:
    >>> luhn_check("4532015112830366")  # valid Visa
    True
    >>> luhn_check("4532015112830367")  # invalid — check digit off by one
    False
    >>> luhn_check("1234567890123456")  # invalid
    False
    >>> luhn_check("79927398713")  # canonical Luhn-valid test number
    True
    >>> luhn_check("79927398714")  # invalid
    False
    >>> luhn_check("0")  # single zero is valid (trivially)
    True
    >>> luhn_check("abc123")
    Traceback (most recent call last):
        ...
    ValueError: luhn_check() only accepts strings of digits
    >>> luhn_check("4111 1111 1111 1111")
    Traceback (most recent call last):
        ...
    ValueError: luhn_check() only accepts strings of digits
    """
    if not card_number.isdigit():
        raise ValueError("luhn_check() only accepts strings of digits")

    digits = [int(d) for d in card_number]
    # Double every second digit from the right (index from end: 1, 3, 5, …)
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    return sum(digits) % 10 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_numbers = [
        ("4532015112830366", True),
        ("4532015112830367", False),
        ("79927398713", True),
        ("1234567890123456", False),
    ]
    for number, expected in test_numbers:
        result = luhn_check(number)
        status = "✓" if result == expected else "✗"
        print(f"{status} luhn_check({number!r}) = {result}")
