def dna_matching_strand(dna: str) -> str:
    """
    https://en.wikipedia.org/wiki/DNA
    Returns the second side of a DNA strand

    >>> dna_matching_strand("GCTA")
    'CGAT'
    >>> dna_matching_strand("ATGC")
    'TACG'
    >>> dna_matching_strand("CTGA")
    'GACT'
    >>> dna_matching_strand("GFGG")
    Traceback (most recent call last):
        ...
    ValueError: GFGG is not a valid strand of DNA
    """
    dna = dna.upper()
    if not all(c in "ATGC" for c in dna):
        raise ValueError(f"{dna} is not a valid strand of DNA")
    return dna.translate(str.maketrans("ATGC", "TACG"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
