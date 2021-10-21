# Shifts the character by 1 through it's ASCII


def shift_string(original_str: str, shift: int = 1) -> str:
    """
    Shifts the character by 1 through it's ASCII
    >>> shift_string('Hello')
    'Ifmmp'

    >>> shift_string('something')
    'tpnfuijoh'

    >>> shift_string('heyaaa', 2)
    'jg{ccc'
    """
    if shift < 1:
        return Exception("Shift can't be less than 1")
    if len(original_str) < 1:
        return Exception("String can't be empty")
    new_str = ""
    # ord function gives the ascii of the charcter for ex. ord(a) gives 97
    # and it's inverse is chr which will turn 97 to a
    for i in original_str:
        asc = ord(i)
        new_str += chr(asc + shift)
    return new_str


if __name__ == "__main__":
    from doctest import testmod

    testmod()
