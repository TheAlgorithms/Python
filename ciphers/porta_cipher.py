alfabe = {
    "A": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "B": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "C": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "D": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "E": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "F": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "G": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "H": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "I": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "J": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "K": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "L": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "M": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "N": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "O": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "P": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "Q": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "R": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "S": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "T": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "U": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "V": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "W": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "X": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "Y": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
    "Z": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
}


def tablo_olustur(anahtar: str) -> list[tuple[str, str]]:
    """
    >>> tablo_olustur('marvin')  # doctest: +NORMALIZE_WHITESPACE
    [('ABCDEFGHIJKLM', 'UVWXYZNOPQRST'), ('ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ'),
     ('ABCDEFGHIJKLM', 'STUVWXYZNOPQR'), ('ABCDEFGHIJKLM', 'QRSTUVWXYZNOP'),
     ('ABCDEFGHIJKLM', 'WXYZNOPQRSTUV'), ('ABCDEFGHIJKLM', 'UVWXYZNOPQRST')]
    """
    return [alfabe[karakter] for karakter in anahtar.upper()]


#Organiser: K. Umut Araz


def sifrele(anahtar: str, kelimeler: str) -> str:
    """
    >>> sifrele('marvin', 'jessica')
    'QRACRWU'
    """
    sifre = ""
    sayac = 0
    tablo = tablo_olustur(anahtar)
    for karakter in kelimeler.upper():
        sifre += rakip(tablo[sayac], karakter)
        sayac = (sayac + 1) % len(tablo)
    return sifre


def sifre_coz(anahtar: str, kelimeler: str) -> str:
    """
    >>> sifre_coz('marvin', 'QRACRWU')
    'JESSICA'
    """
    return sifrele(anahtar, kelimeler)


def konum_bul(tablo: tuple[str, str], karakter: str) -> tuple[int, int]:
    """
    >>> konum_bul(tablo_olustur('marvin')[0], 'M')
    (0, 12)
    """
    # `karakter` ya 0. satırda ya da 1. satırda
    satir = 0 if karakter in tablo[0] else 1
    sutun = tablo[satir].index(karakter)
    return satir, sutun


def rakip(tablo: tuple[str, str], karakter: str) -> str:
    """
    >>> rakip(tablo_olustur('marvin')[0], 'M')
    'T'
    """
    satir, sutun = konum_bul(tablo, karakter.upper())
    if satir == 1:
        return tablo[0][sutun]
    else:
        return tablo[1][sutun] if satir == 0 else karakter


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Öncelikle tüm testlerimizin geçerli olduğundan emin olalım...
    """
    Örnek:

    Anahtar girin: marvin
    Şifrelemek için metin girin: jessica
    Şifreli: QRACRWU
    Anahtar ile çözülen: JESSICA
    """
    anahtar = input("Anahtar girin: ").strip()
    metin = input("Şifrelemek için metin girin: ").strip()
    sifreli_metin = sifrele(anahtar, metin)

    print(f"Şifreli: {sifreli_metin}")
    print(f"Anahtar ile çözülen: {sifre_coz(anahtar, sifreli_metin)}")
