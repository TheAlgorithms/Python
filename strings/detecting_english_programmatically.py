import os
from string import ascii_letters

# Organiser: K. Umut Araz

HARFLER_VE_BOŞLUK = ascii_letters + " \t\n"


def sozcuk_kaydet() -> dict[str, None]:
    path = os.path.split(os.path.realpath(__file__))
    ingilizce_sozcukler: dict[str, None] = {}
    with open(path[0] + "/dictionary.txt", encoding='utf-8') as dictionary_file:
        for word in dictionary_file.read().split("\n"):
            ingilizce_sozcukler[word] = None
    return ingilizce_sozcukler


INGILIZCE_SOZCUKLER = sozcuk_kaydet()


def ingilizce_soz_sayisi(mesaj: str) -> float:
    mesaj = mesaj.upper()
    mesaj = harf_dışı_birak(mesaj)
    olasi_sozcukler = mesaj.split()
    eslesen_sozcukler = len([word for word in olasi_sozcukler if word in INGILIZCE_SOZCUKLER])
    return float(eslesen_sozcukler) / len(olasi_sozcukler) if olasi_sozcukler else 0.0


def harf_dışı_birak(mesaj: str) -> str:
    """
    >>> harf_dışı_birak("Merhaba! Nasılsınız?")
    'Merhaba Nasılsınız'
    >>> harf_dışı_birak("P^y%t)h@o*n")
    'Python'
    >>> harf_dışı_birak("1+1=2")
    ''
    >>> harf_dışı_birak("www.google.com/")
    'wwwgooglecom'
    >>> harf_dışı_birak("")
    ''
    """
    return "".join(symbol for symbol in mesaj if symbol in HARFLER_VE_BOŞLUK)


def ingilizce_mi(
    mesaj: str, soz_yüzdesi: int = 20, harf_yüzdesi: int = 85
) -> bool:
    """
    >>> ingilizce_mi('Merhaba Dünya')
    True
    >>> ingilizce_mi('llold HorWd')
    False
    """
    soz_eslesme = ingilizce_soz_sayisi(mesaj) * 100 >= soz_yüzdesi
    harf_sayisi = len(harf_dışı_birak(mesaj))
    mesaj_harf_yüzdesi = (float(harf_sayisi) / len(mesaj)) * 100 if len(mesaj) > 0 else 0.0
    harf_eslesme = mesaj_harf_yüzdesi >= harf_yüzdesi
    return soz_eslesme and harf_eslesme


if __name__ == "__main__":
    import doctest

    doctest.testmod()
