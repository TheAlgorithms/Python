hex_tablo = {hex(i)[2:]: i for i in range(16)}  # '0x' kısmını çıkarmak için [:2] kullanılır

#Organiser: K. Umut Araz

def hex_to_decimal(hex_dizisi: str) -> int:
    """
    Bir onaltılık değeri ondalık karşılığına dönüştürür.
    #https://www.programiz.com/python-programming/methods/built-in/hex

    >>> hex_to_decimal("a")
    10
    >>> hex_to_decimal("12f")
    303
    >>> hex_to_decimal("   12f   ")
    303
    >>> hex_to_decimal("FfFf")
    65535
    >>> hex_to_decimal("-Ff")
    -255
    >>> hex_to_decimal("F-f")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz bir onaltılık değer fonksiyona geçirildi
    >>> hex_to_decimal("")
    Traceback (most recent call last):
        ...
    ValueError: Fonksiyona boş bir dize geçirildi
    >>> hex_to_decimal("12m")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz bir onaltılık değer fonksiyona geçirildi
    """
    hex_dizisi = hex_dizisi.strip().lower()
    if not hex_dizisi:
        raise ValueError("Fonksiyona boş bir dize geçirildi")
    negatif = hex_dizisi[0] == "-"
    if negatif:
        hex_dizisi = hex_dizisi[1:]
    if not all(char in hex_tablo for char in hex_dizisi):
        raise ValueError("Geçersiz bir onaltılık değer fonksiyona geçirildi")
    ondalik_sayi = 0
    for char in hex_dizisi:
        ondalik_sayi = 16 * ondalik_sayi + hex_tablo[char]
    return -ondalik_sayi if negatif else ondalik_sayi


if __name__ == "__main__":
    from doctest import testmod

    testmod()
