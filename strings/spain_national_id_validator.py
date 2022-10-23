NUMBERS_PLUS_LETTER = "Input must be a string of 8 numbers plus letter"
LOOKUP_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"


def validate(spanish_id: str) -> bool:
    """
    Spain National Id is a string composed by 8 numbers plus a letter
    The letter in fact is not part of the ID, it acts as a validator,
    checking you didn't do a mistake when entering it on a system or
    are giving a fake one.

    https://en.wikipedia.org/wiki/Documento_Nacional_de_Identidad_(Spain)#Number

    >>> validate("12345678Z")
    True
    >>> validate("12345678z") # It is case-insensitive
    True
    >>> validate("12345678x")
    False
    >>> validate("12345678I")
    False
    >>> validate("12345678-Z") # Some systems add a dash between number and letter
    True
    >>> validate("12345678")
    Traceback (most recent call last):
        ...
    ValueError: Input must be a string of 8 numbers plus letter
    >>> validate("123456709")
    Traceback (most recent call last):
        ...
    ValueError: Input must be a string of 8 numbers plus letter
    >>> validate("1234567--Z")
    Traceback (most recent call last):
        ...
    ValueError: Input must be a string of 8 numbers plus letter
    >>> validate("1234Z")
    Traceback (most recent call last):
        ...
    ValueError: Input must be a string of 8 numbers plus letter
    >>> validate("1234ZzZZ")
    Traceback (most recent call last):
        ...
    ValueError: Input must be a string of 8 numbers plus letter
    >>> validate(12345678)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found int
    """

    if not isinstance(spanish_id, str):
        raise ValueError(f"Expected string as input, found {type(spanish_id).__name__}")

    spanish_id_clean = spanish_id.replace("-", "").upper()
    if len(spanish_id_clean) != 9:
        raise ValueError(NUMBERS_PLUS_LETTER)

    try:
        number = int(spanish_id_clean[0:8])
        letter = spanish_id_clean[8]
    except ValueError as ex:
        raise ValueError(NUMBERS_PLUS_LETTER) from ex

    if letter in "0123456789":
        raise ValueError(NUMBERS_PLUS_LETTER)

    modulus = number % 23
    expected_letter = LOOKUP_LETTERS[modulus]

    return letter == expected_letter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
