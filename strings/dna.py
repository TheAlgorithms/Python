import string
import re
def dna(dna: str) -> str:

    """
      >>> dna("GCTA")
      'CGAT'
      >>> dna("ATGC")
      'TACG'
      >>> dna("CTGA")
      'GACT'
      >>> dna("GFGG")
      'Invalid Strand'
    """

    """ https://en.wikipedia.org/wiki/DNA """

    """this algorithm, given one side
    of a DNA strand returns the other, 
    complementary side of said strand"""

    r = len(re.findall("[ATCG]", dna)) != len(dna) 
    val = dna.translate(dna.maketrans("ATCG","TAGC"))
    return "Invalid Strand" if r else val


if __name__ == "__main__":
    import doctest
    doctest.testmod()