import re


def is_valid_international_phone_number(phone: str) -> bool:
    """
    Determine whether the string is a valid international phone number or not.

    >>> is_valid_international_phone_number("+919136812895")
    True
    >>> is_valid_international_phone_number("+91 9136812895")
    True
    >>> is_valid_international_phone_number("+123 123456")
    True
    >>> is_valid_international_phone_number("654294563")
    False
    """

    pattern = r"^\+(?:\d{6,15}|\d{2}\s\d{6,15})$"

    return bool(re.match(pattern, phone))


if __name__ == "__main":
    str1 = "+919132896815"
    print(is_valid_international_phone_number(str1))
