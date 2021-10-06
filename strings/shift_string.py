# Shifts the charcter by 1 through it's ACII


def shiftString(originalStr: str, shift: int = 1) -> str:
    """
    Shifts the charcter by 1 through it's ACII
    >>> shiftString('Hello')
    'Ifmmp'

    >>> shiftString('something')
    'tpnfuijoh'

    >>> shiftString('heyaaa', 2)
    'jg{ccc'
    """
    if shift < 1:
        return Exception("Shift can't be less than 1")
    if len(originalStr) < 1:
        return Exception("String can't be empty")
    newStr = ""
    # ord function gives the ascii of the charcter for ex. ord(a) gives 97
    # and it's inverse is chr which will turn 97 to a
    for i in originalStr:
        asc = ord(i)
        newStr += chr(asc + shift)
    return newStr


if __name__ == "__main__":
    from doctest import testmod

    testmod()
