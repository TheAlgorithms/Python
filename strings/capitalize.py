from string import ascii_lowercase, ascii_uppercase

def buyuk_harf_yap(cumle: str) -> str:
    """
    Bir cümlenin veya kelimenin ilk harfini büyük yapar.

    # Organiser: K. Umut Araz

    >>> buyuk_harf_yap("merhaba dünya")
    'Merhaba dünya'
    >>> buyuk_harf_yap("123 merhaba dünya")
    '123 merhaba dünya'
    >>> buyuk_harf_yap(" merhaba dünya")
    ' merhaba dünya'
    >>> buyuk_harf_yap("a")
    'A'
    >>> buyuk_harf_yap("")
    ''
    """
    if not cumle:
        return ""

    # Küçük harfleri büyük harflere eşleyen bir sözlük oluştur
    # İlk karakter küçük harfse büyük harf yap
    # Büyük harf yapılmış karakteri geri kalan string ile birleştir
    kucuktenBuyuge = dict(zip(ascii_lowercase, ascii_uppercase))
    return kucuktenBuyuge.get(cumle[0], cumle[0]) + cumle[1:]

if __name__ == "__main__":
    from doctest import testmod

    testmod()
