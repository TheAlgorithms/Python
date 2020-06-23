def upper(word: str) -> str:
    """
    Will convert the entire string to uppercase letters

    >>> upper("wow")
    'WOW'
    >>> upper("Hello")
    'HELLO'
    >>> upper("WHAT")
    'WHAT'

    >>> upper("wh[]32")
    'WH[]32'
    """

    # converting to ascii value int value and checking to see if char is a lower letter
    # if it is a capital letter it is getting shift by 32 which makes it a capital case
    # letter
    return "".join(
        chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char for char in word
    )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
