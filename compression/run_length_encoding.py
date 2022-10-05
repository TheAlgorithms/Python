# https://en.wikipedia.org/wiki/Run-length_encoding


def run_length_encode(text: str) -> list:
    """
    Performs Run Length Encoding
    >>> run_length_encode("AAAABBBCCDAA")
    [('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]
    >>> run_length_encode("A")
    [('A', 1)]
    >>> run_length_encode("AA")
    [('A', 2)]
    >>> run_length_encode("AAADDDDDDFFFCCCAAVVVV")
    [('A', 3), ('D', 6), ('F', 3), ('C', 3), ('A', 2), ('V', 4)]
    """
    encoded=[]
    while text > "":
        z=text.lstrip(text[0])    
        encoded.append((text[0],str(len(text)-len(z))))
        text=z
    return encoded


def run_length_decode(encoded: list) -> str:
    """
    Performs Run Length Decoding
    >>> run_length_decode([('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)])
    'AAAABBBCCDAA'
    >>> run_length_decode([('A', 1)])
    'A'
    >>> run_length_decode([('A', 2)])
    'AA'
    >>> run_length_decode([('A', 3), ('D', 6), ('F', 3), ('C', 3), ('A', 2), ('V', 4)])
    'AAADDDDDDFFFCCCAAVVVV'
    """
    return "".join(char * length for char, length in encoded)


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="run_length_encode", verbose=True)
    testmod(name="run_length_decode", verbose=True)
