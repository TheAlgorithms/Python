import re


def dna(dna: str) -> str:
    """
    # Organiser: K. Umut Araz
    
    https://tr.wikipedia.org/wiki/DNA
    Bir DNA ipliğinin karşı tarafını döndürür.

    >>> dna("GCTA")
    'CGAT'
    >>> dna("ATGC")
    'TACG'
    >>> dna("CTGA")
    'GACT'
    >>> dna("GFGG")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz İplik
    """

    if len(re.findall("[ATCG]", dna)) != len(dna):
        raise ValueError("Geçersiz İplik")

    return dna.translate(dna.maketrans("ATCG", "TAGC"))


if __name__ == "__main__":
    import doctest

    testmod()
