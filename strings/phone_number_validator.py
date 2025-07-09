import re


def validate_phone_number(phone: str) -> bool:
    """
    Validates a 10-digit Indian phone number.
    >>> validate_phone_number("9876543210")
    True
    >>> validate_phone_number("1234567890")
    False
    >>> validate_phone_number("abcd123456")
    False
    >>> validate_phone_number("abcdedad")
    False
    """
    pattern = r"^[6-9]\d{9}$"
    return re.fullmatch(pattern, phone) is not None
