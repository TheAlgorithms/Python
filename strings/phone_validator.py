import re
def phone_validator(phone: str) -> bool:
    """
    Determine whether the string is a valid phone number or not
    :param phone:
    :return: Boolean
    >>> phone_validator("+91123456789")
    False
    >>> phone_validator("+919876543210")
    True
    >>> phone_validator("01234567896")
    False
    >>> phone_validator("919876543218")
    True
    >>> phone_validator("+91-1234567899")
    False
    """
    # Created a regex pattern to produce a valid phone number
    pat = re.compile(r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")
    # Find their matches
    match = re.search(pat, phone)
    # if match are present
    if match:
        # the match is the same as the phone string it means they are valid phone number.
        return match.string == phone
    # if match are none so return False.
    return False

if __name__ == "__main__":
    print(phone_validator('+91123456789'))