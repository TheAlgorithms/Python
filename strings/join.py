"""
Bir ayırıcı ile bir dizi stringi birleştiren program

Organiser: K. Umut Araz
"""


def birlestir(ayirici: str, birlesecek: list[str]) -> str:
    """
    Bir dizi stringi bir ayırıcı kullanarak birleştirir
    ve sonucu döner.

    :param ayirici: Stringleri birleştirmek için kullanılacak ayırıcı.
    :param birlesecek: Birleştirilecek stringlerin listesi.

    :return: Belirtilen ayırıcı ile birleştirilmiş string.

    Örnekler:

    >>> birlestir("", ["a", "b", "c", "d"])
    'abcd'
    >>> birlestir("#", ["a", "b", "c", "d"])
    'a#b#c#d'
    >>> birlestir("#", ["a"])
    'a'
    >>> birlestir(" ", ["Sen", "harikasın!"])
    'Sen harikasın!'

    Bu örnek, string olmayan elemanlar için bir
    istisna fırlatmalıdır:
    >>> birlestir("#", ["a", "b", "c", 1])
    Traceback (most recent call last):
        ...
    Exception: birlestir() yalnızca string kabul eder

    Farklı bir ayırıcı ile ek test durumu:
    >>> birlestir("-", ["elma", "muz", "kiraz"])
    'elma-muz-kiraz'
    """

    birlesmis = ""
    for kelime_veya_ifade in birlesecek:
        if not isinstance(kelime_veya_ifade, str):
            raise Exception("birlestir() yalnızca string kabul eder")
        birlesmis += kelime_veya_ifade + ayirici

    # Sonundaki ayırıcıyı kaldır
    # sonucu temizleyerek
    return birlesmis.strip(ayirici)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
