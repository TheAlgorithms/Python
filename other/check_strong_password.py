# This Will Check Whether A Given Password Is Strong Or Not
# It Follows The Rule that Length Of Password Should Be At Least 8 Characters
# And At Least 1 Lower, 1 Upper, 1 Number And 1 Special Character

from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def is_strong_password(password: str, min_length: int = 8) -> bool:
    """
    >>> is_strong_password('Hwea7$2!')
    True

    >>> is_strong_password('Sh0r1')
    False

    >>> is_strong_password('Hello123')
    False

    >>> is_strong_password('Hello1238udfhiaf038fajdvjjf!jaiuFhkqi1')
    True

    >>> is_strong_password(0)
    False
    """

    # Rudimentary check when an int or float type is used as a password
    # having no. of digits less than min_length
    if len(str(password)) < min_length:
        return False

    # Boolean character flags which are set on encountering a character of
    # a given type
    upper = any(char in ascii_uppercase for char in password)
    lower = any(char in ascii_lowercase for char in password)
    num = any(char in digits for char in password)
    spec_char = any(char in punctuation for char in password)

    return upper and lower and num and spec_char


def is_strong_password_2(password: str, min_length: int = 8) -> bool:
    """
    >>> is_strong_password_2('Hwea7$2!')
    True

    >>> is_strong_password_2('Sh0r1')
    False

    >>> is_strong_password_2('Hello123')
    False

    >>> is_strong_password_2('Hello1238udfhiaf038fajdvjjf!jaiuFhkqi1')
    True

    >>> is_strong_password_2(0)
    False
    """
    # Initialise boolean flags which toggle when the first occurrence of a
    # type is encountered
    upper = lower = num = spec_char = False

    # Rudimentary check when an int or float type is used as a password
    # having no. of digits less than min_length
    if len(str(password)) < min_length:
        return False

    # Parse each of the characters and check whether they are within the
    # concerned lexicographic boundaries
    # Toggle respective flags when you encounter a character type
    # Avoid the check when the concerned character flag is already set

    for char in password:
        if not num and "0" <= char <= "9":
            num = True
        elif not upper and "A" <= char <= "Z":
            upper = True
        elif not lower and "a" <= char <= "z":
            lower = True
        elif not spec_char and char in punctuation:
            spec_char = True

    return num and spec_char and upper and lower


if __name__ == "__main__":
    import doctest

    doctest.testmod()
