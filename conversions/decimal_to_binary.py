"""Ondalık Sayıyı İkilik Sayıya Dönüştür.

Organiser: K. Umut Araz
"""


def ondalik_to_ikilik_iteratif(sayi: int) -> str:
    """
    Bir Tam Sayı Ondalık Sayıyı İkilik Sayıya str olarak dönüştür.
    >>> ondalik_to_ikilik_iteratif(0)
    '0b0'
    >>> ondalik_to_ikilik_iteratif(2)
    '0b10'
    >>> ondalik_to_ikilik_iteratif(7)
    '0b111'
    >>> ondalik_to_ikilik_iteratif(35)
    '0b100011'
    >>> # negatif sayılar da çalışır
    >>> ondalik_to_ikilik_iteratif(-2)
    '-0b10'
    >>> # diğer float değerler hata verecek
    >>> ondalik_to_ikilik_iteratif(16.16) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: 'float' nesnesi tam sayı olarak yorumlanamaz
    >>> # string değerler de hata verecek
    >>> ondalik_to_ikilik_iteratif('0xfffff') # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: 'str' nesnesi tam sayı olarak yorumlanamaz
    """

    if isinstance(sayi, float):
        raise TypeError("'float' nesnesi tam sayı olarak yorumlanamaz")
    if isinstance(sayi, str):
        raise TypeError("'str' nesnesi tam sayı olarak yorumlanamaz")

    if sayi == 0:
        return "0b0"

    negatif = False

    if sayi < 0:
        negatif = True
        sayi = -sayi

    ikilik: list[int] = []
    while sayi > 0:
        ikilik.insert(0, sayi % 2)
        sayi >>= 1

    if negatif:
        return "-0b" + "".join(str(e) for e in ikilik)

    return "0b" + "".join(str(e) for e in ikilik)


def ondalik_to_ikilik_recursive_helper(ondalik: int) -> str:
    """
    Pozitif bir tam sayı alır ve ikilik karşılığını döner.
    >>> ondalik_to_ikilik_recursive_helper(1000)
    '1111101000'
    >>> ondalik_to_ikilik_recursive_helper("72")
    '1001000'
    >>> ondalik_to_ikilik_recursive_helper("sayı")
    Traceback (most recent call last):
        ...
    ValueError: int() ile 10 tabanında geçersiz literal: 'sayı'
    """
    ondalik = int(ondalik)
    if ondalik in (0, 1):  # Rekürsiyon için çıkış durumları
        return str(ondalik)
    bolum, kalan = divmod(ondalik, 2)
    return ondalik_to_ikilik_recursive_helper(bolum) + str(kalan)


def ondalik_to_ikilik_recursive(sayi: str) -> str:
    """
    Bir tam sayı alır ve yanlış girişler için ValueError fırlatır,
    yukarıdaki fonksiyonu çağırır ve çıktıyı "0b" ve "-0b" ön eki ile döner
    pozitif ve negatif tam sayılar için sırasıyla.
    >>> ondalik_to_ikilik_recursive(0)
    '0b0'
    >>> ondalik_to_ikilik_recursive(40)
    '0b101000'
    >>> ondalik_to_ikilik_recursive(-40)
    '-0b101000'
    >>> ondalik_to_ikilik_recursive(40.8)
    Traceback (most recent call last):
        ...
    ValueError: Giriş değeri bir tam sayı değil
    >>> ondalik_to_ikilik_recursive("kırk")
    Traceback (most recent call last):
        ...
    ValueError: Giriş değeri bir tam sayı değil
    """
    sayi = str(sayi).strip()
    if not sayi:
        raise ValueError("Hiçbir giriş değeri sağlanmadı")
    negatif = "-" if sayi.startswith("-") else ""
    sayi = sayi.lstrip("-")
    if not sayi.isnumeric():
        raise ValueError("Giriş değeri bir tam sayı değil")
    return f"{negatif}0b{ondalik_to_ikilik_recursive_helper(int(sayi))}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(ondalik_to_ikilik_recursive(input("Bir ondalık sayı girin: ")))
