"""
* Author: Bama Charan Chhandogi (https://github.com/BamaCharanChhandogi)
* Organiser: K. Umut Araz
* Description: Convert a Octal number to Binary.

Daha iyi anlamak için referanslar:
https://tr.wikipedia.org/wiki/Binary_say%C4%B1
https://tr.wikipedia.org/wiki/Sekizli_say%C4%B1
"""


def sekizli_to_ikili(sekizli_sayi: str) -> str:
    """
    Sekizli bir sayıyı İkili sayıya dönüştürür.

    >>> sekizli_to_ikili("17")
    '001111'
    >>> sekizli_to_ikili("7")
    '111'
    >>> sekizli_to_ikili("Av")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    >>> sekizli_to_ikili("@#")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    >>> sekizli_to_ikili("")
    Traceback (most recent call last):
        ...
    ValueError: Fonksiyona boş bir dize gönderildi
    """
    if not sekizli_sayi:
        raise ValueError("Fonksiyona boş bir dize gönderildi")

    ikili_sayi = ""
    sekizli_haneler = "01234567"
    for hane in sekizli_sayi:
        if hane not in sekizli_haneler:
            raise ValueError("Geçersiz sekizli değer fonksiyona gönderildi")

        ikili_hane = ""
        deger = int(hane)
        for _ in range(3):
            ikili_hane = str(deger % 2) + ikili_hane
            deger //= 2
        ikili_sayi += ikili_hane

    return ikili_sayi


if __name__ == "__main__":
    import doctest

    doctest.testmod()
