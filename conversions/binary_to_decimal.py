def ikili_to_onlu(ikili_dizi: str) -> int:
    """
    Organiser: K. Umut Araz

    İkili bir değeri ondalık karşılığına dönüştürür.

    >>> ikili_to_onlu("101")
    5
    >>> ikili_to_onlu(" 1010   ")
    10
    >>> ikili_to_onlu("-11101")
    -29
    >>> ikili_to_onlu("0")
    0
    >>> ikili_to_onlu("a")
    Traceback (most recent call last):
        ...
    ValueError: Fonksiyona geçersiz bir ikili değer gönderildi
    >>> ikili_to_onlu("")
    Traceback (most recent call last):
        ...
    ValueError: Fonksiyona boş bir dize gönderildi
    >>> ikili_to_onlu("39")
    Traceback (most recent call last):
        ...
    ValueError: Fonksiyona geçersiz bir ikili değer gönderildi
    """
    ikili_dizi = str(ikili_dizi).strip()
    if not ikili_dizi:
        raise ValueError("Fonksiyona boş bir dize gönderildi")
    negatif_mi = ikili_dizi[0] == "-"
    if negatif_mi:
        ikili_dizi = ikili_dizi[1:]
    if not all(char in "01" for char in ikili_dizi):
        raise ValueError("Fonksiyona geçersiz bir ikili değer gönderildi")
    ondalik_sayi = 0
    for char in ikili_dizi:
        ondalik_sayi = 2 * ondalik_sayi + int(char)
    return -ondalik_sayi if negatif_mi else ondalik_sayi


if __name__ == "__main__":
    from doctest import testmod

    testmod()
