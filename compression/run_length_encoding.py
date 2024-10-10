# https://tr.wikipedia.org/wiki/Run-length_encoding

"""
Organiser: K. Umut Araz
"""

def run_length_encode(metin: str) -> list:
    """
    Run Length Encoding işlemi gerçekleştirir.
    >>> run_length_encode("AAAABBBCCDAA")
    [('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]
    >>> run_length_encode("A")
    [('A', 1)]
    >>> run_length_encode("AA")
    [('A', 2)]
    >>> run_length_encode("AAADDDDDDFFFCCCAAVVVV")
    [('A', 3), ('D', 6), ('F', 3), ('C', 3), ('A', 2), ('V', 4)]
    """
    kodlanmış = []
    sayac = 1

    for i in range(len(metin)):
        if i + 1 < len(metin) and metin[i] == metin[i + 1]:
            sayac += 1
        else:
            kodlanmış.append((metin[i], sayac))
            sayac = 1

    return kodlanmış


def run_length_decode(kodlanmış: list) -> str:
    """
    Run Length Decoding işlemi gerçekleştirir.
    >>> run_length_decode([('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)])
    'AAAABBBCCDAA'
    >>> run_length_decode([('A', 1)])
    'A'
    >>> run_length_decode([('A', 2)])
    'AA'
    >>> run_length_decode([('A', 3), ('D', 6), ('F', 3), ('C', 3), ('A', 2), ('V', 4)])
    'AAADDDDDDFFFCCCAAVVVV'
    """
    return "".join(karakter * uzunluk for karakter, uzunluk in kodlanmış)


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="run_length_encode", verbose=True)
    testmod(name="run_length_decode", verbose=True)
