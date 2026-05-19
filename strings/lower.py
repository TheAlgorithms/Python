def lower(word: str) -> str:
    """
    Will convert the entire string to lowercase letters

    >>> lower("wow")
    'wow'
    >>> lower("HellZo")
    'hellzo'
    >>> lower("WHAT")
    'what'
    >>> lower("wh[]32")
    'wh[]32'
    >>> lower("whAT")
    'what'
    """

    # Converting to ASCII value, obtaining the integer representation
    # and checking to see if the character is a capital letter.
    # If it is a capital letter, it is shifted by 32, making it a lowercase letter.
    return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else char for char in word)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
