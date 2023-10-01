""" These are the implementations of the basic string functions in python,
like isupper(), islower() and so on"""


def is_upper(string):
    """
    This function checks if a given string contains only upper case characters.
    """
    if not string:
        return False
    for character in string:
        if ord(character) > 96 and ord(character) < 123:
            return False
    return True


def is_lower(string):
    """
    This function checks if a given string contains only lower case characters.
    """
    for character in string:
        if ord(character) in range(65, 97):
            return False
    return True


def is_alpha(string):
    """
    This function checks whether all characters in a string are alphabetical
    """
    if not string:
        return False
    for character in string:
        if (ord(character) in range(65, 91)) or (ord(character) in range(97, 123)):
            continue
        else:
            return False
    return True


def is_alnum(string):
    """
    This function checks if all the characters in a string are alphanumeric
    """
    if not string:
        return False
    for character in string:
        if (
            (ord(character) in range(65, 91))
            or (ord(character) in range(97, 123))
            or (ord(character) in range(48, 58))
        ):
            continue
        else:
            return False
    return True


def is_decimal(string):
    """
    This function returns true if all of the characters in the string are digits
    """
    if not string:
        return False
    for character in string:
        if ord(character) not in range(48, 58):
            return False
    return True


def is_space(string):
    """
    This function checks for the strings constituing only of spaces, tabs and newlines
    """
    if not string:
        return False
    for character in string:
        if character != " ":  # solve for newline pending
            return False
    return True


def is_title(string):
    """
    This function checks that every word starts with an uppercase letter.
    """
    for substring in string.split():
        if ord(substring[0]) not in range(65, 91):
            return False
        for character in range(1, len(substring)):
            if is_upper(substring[character]):
                return False
    return True


print(is_upper("HEY"))  # True
print(is_lower("there"))  # True
print(is_alpha("you"))  # True
print(is_alnum("are3"))  # True
print(is_decimal("400"))  # True
print(is_space("   "))  # True
print(is_title("Times Pretty"))  # True
