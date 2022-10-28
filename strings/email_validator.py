import re


def email_validator(email: str) -> bool:
    """
        Determine whether the string is a valid email or not
        :param email:
        :return: Boolean
        >>> email_validator("asdfg")
        False
        >>> email_validator("asdfg@gmail.com")
        True
        >>> email_validator("asdfg@gmail")
        False
        """
    email_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(email_pattern, email):
        return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
