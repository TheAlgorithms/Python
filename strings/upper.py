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

    # Converting to ASCII value, obtaining the integer representation, 
    # and checking to see if the character is a lowercase letter. 
    # If it is a lowercase letter, it is shifted by 32, making it an uppercase letter.
    return "".join(chr(ord(char) - 32) if "a" <= char <= "z" else char for char in word)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
