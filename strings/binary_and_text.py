def text_to_binary(text: str) -> str:
    """
    Converts any string to binary
    >>> text_to_binary('A')
    '1000001'
    >>> text_to_binary('Dexter')
    '1000100 1100101 1111000 1110100 1100101 1110010'
    >>> text_to_binary('❤️')
    '10011101100100 1111111000001111'
    """
    return " ".join(map(lambda char: bin(ord(char))[2:], text))


def binary_to_text(binary: str) -> str:
    """
    Converts any binary to string
    >>> binary_to_text('1000001')
    'A'
    >>> binary_to_text('1000100 1100101 1111000 1110100 1100101 1110010')
    'Dexter'
    >>> binary_to_text('10011101100100 1111111000001111')
    '❤️'
    """
    return "".join(map(lambda bin_text: chr(int(bin_text, base=2)), binary.split()))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
