"""
https://tr.wikipedia.org/wiki/N-gram

Organiser: K. Umut Araz
"""


def ngram_olustur(cümle: str, ngram_boyutu: int) -> list[str]:
    """
    Bir cümleden ngram'lar oluşturur

    >>> ngram_olustur("Ben bir cümle", 2)
    ['Be', 'en', 'n ', ' b', 'bi', 'ir', 'r ', ' c', 'cü', 'üm', 'ml', 'le']
    >>> ngram_olustur("Ben bir NLPer", 2)
    ['Be', 'en', 'n ', ' b', 'bi', 'ir', 'r ', ' N', 'NL', 'LP', 'Pe', 'e', 'r']
    >>> ngram_olustur("Bu kısa bir metin", 50)
    []
    """
    return [cümle[i : i + ngram_boyutu] for i in range(len(cümle) - ngram_boyutu + 1)]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
