import re

def bangladeshi_phone_validator(phone: str) -> bool:
    """
    Determine whether the string is a valid phone number or not
    :param phone:
    :return: Boolean
    >>> bangladeshi_phone_validator("+880171234567")
    False
    >>> bangladeshi_phone_validator("+8801712345678")
    True
    >>> bangladeshi_phone_validator("+880-1712345678")
    False
    """
    pat = re.compile(r"^(?:\+88|01)?(?:\d{11}|\d{13})$")
    match = re.search(pat, phone)

    return match.string == phone if match else False


if __name__ == "__main__":
    print(bangladeshi_phone_validator("+8801712345678"))
