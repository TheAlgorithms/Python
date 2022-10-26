import re

def srilanka_phone_validator(phone: str) -> bool:
    """
    Determine whether the string is a valid sri lankan phone number or not
    :param phone:
    :return: Boolean
    >>> srilanka_phone_validator("+94475682163")
    True   
    >>> srilanka_phone_validator("+94773283048")
    True
    >>> srilanka_phone_validator("0718382399")
    True
    >>> srilanka_phone_validator("0094112343221")
    True
    >>> srilanka_phone_validator("+94-3283048")
    False
    >>> srilanka_phone_validator("07779209245")
    False
    >>> srilanka_phone_validator("0957651234")
    False
    """

    pattern = re.compile(r'^(?:0|94|\+94|0094)?(?:(11|21|23|24|25|26|27|31|32|33|34|35|36|37|38|41|45|47|51|52|54|55|57|63|65|66|67|81|91)(0|2|3|4|5|7|9)|7(0|1|2|4|5|6|7|8)\d)\d{6}$')
    matched = re.search(pattern, phone)

    if matched:
        return True
    return False

if __name__ == '__main__':
    phone = "0957651234"

    print(srilanka_phone_validator(phone))