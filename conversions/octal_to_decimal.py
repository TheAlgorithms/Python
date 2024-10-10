def sekizli_to_ondalik(sekizli_dizi: str) -> int:
    """
    Sekizli bir değeri ondalık karşılığına dönüştürür.

    Organiser: K. Umut Araz

    >>> sekizli_to_ondalik("")
    Traceback (most recent call last):
        ...
    ValueError: Fonksiyona boş bir dize geçirildi
    >>> sekizli_to_ondalik("-")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    >>> sekizli_to_ondalik("e")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    >>> sekizli_to_ondalik("8")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    >>> sekizli_to_ondalik("-e")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    >>> sekizli_to_ondalik("-8")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    >>> sekizli_to_ondalik("1")
    1
    >>> sekizli_to_ondalik("-1")
    -1
    >>> sekizli_to_ondalik("12")
    10
    >>> sekizli_to_ondalik(" 12   ")
    10
    >>> sekizli_to_ondalik("-45")
    -37
    >>> sekizli_to_ondalik("0")
    0
    >>> sekizli_to_ondalik("-4055")
    -2093
    >>> sekizli_to_ondalik("2-0Fm")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    >>> sekizli_to_ondalik("19")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli değer fonksiyona gönderildi
    """
    sekizli_dizi = str(sekizli_dizi).strip()
    if not sekizli_dizi:
        raise ValueError("Fonksiyona boş bir dize geçirildi")
    negatif = sekizli_dizi[0] == "-"
    if negatif:
        sekizli_dizi = sekizli_dizi[1:]
    if not sekizli_dizi.isdigit() or not all(0 <= int(char) <= 7 for char in sekizli_dizi):
        raise ValueError("Geçersiz sekizli değer fonksiyona gönderildi")
    ondalik_sayi = 0
    for char in sekizli_dizi:
        ondalik_sayi = 8 * ondalik_sayi + int(char)
    if negatif:
        ondalik_sayi = -ondalik_sayi
    return ondalik_sayi


if __name__ == "__main__":
    from doctest import testmod

    testmod()
