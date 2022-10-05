import re


def dna_matching_strand (dna: str) -> str:

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
    Exception: Invalid Strand
    """

    r = len(re.findall("[ATCG]", dna)) != len(dna)
    val = dna.translate(dna.maketrans("ATCG", "TAGC"))
    if r:
      raise Exception("Invalid Strand")
    else:
      return val


if __name__ == "__main__":
    __import__("doctest").testmod()
