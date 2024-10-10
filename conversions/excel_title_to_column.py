def excel_sutununu_sayiya_cevir(sutun_basligi: str) -> int:
    """
    Verilen bir sutun_basligi stringi, bir Excel sayfasındaki
    sutun başlığını temsil eder ve karşılık gelen sutun numarasını döner.

    >>> excel_sutununu_sayiya_cevir("A")
    1
    >>> excel_sutununu_sayiya_cevir("B")
    2
    >>> excel_sutununu_sayiya_cevir("AB")
    28
    >>> excel_sutununu_sayiya_cevir("Z")
    26
    """
    assert sutun_basligi.isupper(), "Sutun başlığı büyük harflerden oluşmalıdır."
    cevap = 0
    indeks = len(sutun_basligi) - 1
    kuvvet = 0

    while indeks >= 0:
        deger = (ord(sutun_basligi[indeks]) - 64) * pow(26, kuvvet)
        cevap += deger
        kuvvet += 1
        indeks -= 1

    return cevap


if __name__ == "__main__":
    from doctest import testmod

    testmod()
