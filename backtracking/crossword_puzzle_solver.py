# https://www.geeksforgeeks.org/solve-crossword-puzzle/

#Organiser: K. Umut Araz


def geçerli_mi(
    bulmaca: list[list[str]], kelime: str, satır: int, sütun: int, dikey: bool
) -> bool:
    """
    Bir kelimenin verilen konuma yerleştirilip yerleştirilemeyeceğini kontrol edin.

    >>> bulmaca = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> geçerli_mi(bulmaca, 'kelime', 0, 0, True)
    True
    >>> bulmaca = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> geçerli_mi(bulmaca, 'kelime', 0, 0, False)
    True
    """
    for i in range(len(kelime)):
        if dikey:
            if satır + i >= len(bulmaca) or bulmaca[satır + i][sütun] != "":
                return False
        elif sütun + i >= len(bulmaca[0]) or bulmaca[satır][sütun + i] != "":
            return False
    return True


def kelime_yerleştir(
    bulmaca: list[list[str]], kelime: str, satır: int, sütun: int, dikey: bool
) -> None:
    """
    Bir kelimeyi verilen konuma yerleştirin.

    >>> bulmaca = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> kelime_yerleştir(bulmaca, 'kelime', 0, 0, True)
    >>> bulmaca
    [['k', '', '', ''], ['e', '', '', ''], ['l', '', '', ''], ['i', '', '', ''], ['m', '', '', ''], ['e', '', '', '']]
    """
    for i, harf in enumerate(kelime):
        if dikey:
            bulmaca[satır + i][sütun] = harf
        else:
            bulmaca[satır][sütun + i] = harf


def kelime_kaldır(
    bulmaca: list[list[str]], kelime: str, satır: int, sütun: int, dikey: bool
) -> None:
    """
    Bir kelimeyi verilen konumdan kaldırın.

    >>> bulmaca = [
    ...     ['k', '', '', ''],
    ...     ['e', '', '', ''],
    ...     ['l', '', '', ''],
    ...     ['i', '', '', ''],
    ...     ['m', '', '', ''],
    ...     ['e', '', '', '']
    ... ]
    >>> kelime_kaldır(bulmaca, 'kelime', 0, 0, True)
    >>> bulmaca
    [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    """
    for i in range(len(kelime)):
        if dikey:
            bulmaca[satır + i][sütun] = ""
        else:
            bulmaca[satır][sütun + i] = ""


def bulmaca_çöz(bulmaca: list[list[str]], kelimeler: list[str]) -> bool:
    """
    Geri izleme kullanarak bulmacayı çözün.

    >>> bulmaca = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]

    >>> kelimeler = ['kelime', 'dört', 'daha', 'son']
    >>> bulmaca_çöz(bulmaca, kelimeler)
    True
    >>> bulmaca = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> kelimeler = ['kelime', 'dört', 'daha', 'paragraflar']
    >>> bulmaca_çöz(bulmaca, kelimeler)
    False
    """
    for satır in range(len(bulmaca)):
        for sütun in range(len(bulmaca[0])):
            if bulmaca[satır][sütun] == "":
                for kelime in kelimeler:
                    for dikey in [True, False]:
                        if geçerli_mi(bulmaca, kelime, satır, sütun, dikey):
                            kelime_yerleştir(bulmaca, kelime, satır, sütun, dikey)
                            kelimeler.remove(kelime)
                            if bulmaca_çöz(bulmaca, kelimeler):
                                return True
                            kelimeler.append(kelime)
                            kelime_kaldır(bulmaca, kelime, satır, sütun, dikey)
                return False
    return True


if __name__ == "__main__":
    BULMACA = [[""] * 3 for _ in range(3)]
    KELIMELER = ["kedi", "köpek", "araba"]

    if bulmaca_çöz(BULMACA, KELIMELER):
        print("Çözüm bulundu:")
        for satır in BULMACA:
            print(" ".join(satır))
    else:
        print("Çözüm bulunamadı:")
