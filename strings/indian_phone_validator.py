import re


def indian_phone_validator(phone: str) -> bool:
    """
    Determine whether the string is a valid phone number or not
    :param phone:
    :return: Boolean
    >>> indian_phone_validator("+91123456789")
    False
    >>> indian_phone_validator("+919876543210")
    True
    >>> indian_phone_validator("01234567896")
    False
    >>> indian_phone_validator("919876543218")
    True
    >>> indian_phone_validator("+91-1234567899")
    False
    >>> indian_phone_validator("+91-9876543218")
    True
    """
    pat = re.compile(r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")
    if match := re.search(pat, phone):
        return match.string == phone
    return False


if __name__ == "__main__":
    """
    Main entry point of the script.

    This block checks if the script is being run as the main module. If so, it calls
    the `indian_phone_validator` function with a sample phone number and
    prints the result.

    Functions:
        indian_phone_validator(phone: str) -> bool:
            Validates if the given phone number is a valid Indian phone number.
            The function is expected to return `True` if the number is valid,
            otherwise `False`.

    Example:
        $ python indian_phone_validator.py
        True  # (if the phone number "+918827897895" is valid)
    Note: Ensure that the `indian_phone_validator()` function is defined.
    """
    print(indian_phone_validator("+918827897895"))
