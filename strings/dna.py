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
    Traceback (most recent call last):
        ...
    ValueError: Invalid Strand
    """

    if len(re.findall("[ATCG]", dna)) != len(dna):
        raise ValueError("Invalid Strand")

    return dna.translate(dna.maketrans("ATCG", "TAGC"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
