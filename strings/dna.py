import re


def dna(dna: str) -> str:

    """
    https://en.wikipedia.org/wiki/DNA
    Returns the second side of a DNA strand

    >>> dna("GCTA")
    'CGAT'
    >>> dna("ATGC")
    'TACG'
    >>> dna("CTGA")
    'GACT'
    >>> dna("GFGG")
    'Invalid Strand'
    """

    r = len(re.findall("[ATCG]", dna)) != len(dna)
    val = dna.translate(dna.maketrans("ATCG", "TAGC"))
    return "Invalid Strand" if r else val


if __name__ == "__main__":
    __import__("doctest").testmod()
