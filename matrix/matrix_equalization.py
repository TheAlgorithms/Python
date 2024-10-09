from sys import maxsize

def dizi_esitleme(vektör: list[int], adım_boyutu: int) -> int:
    """
    Bu algoritma, giriş vektöründeki tüm elemanları
    ortak bir değere eşitleyerek, adım boyutu (adım_boyutu)
    kısıtlaması altında en az sayıda "güncelleme" yapar.

    Organised By K. Umut Araz

    >>> dizi_esitleme([1, 1, 6, 2, 4, 6, 5, 1, 7, 2, 2, 1, 7, 2, 2], 4)
    4
    >>> dizi_esitleme([22, 81, 88, 71, 22, 81, 632, 81, 81, 22, 92], 2)
    5
    >>> dizi_esitleme([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 5)
    0
    >>> dizi_esitleme([22, 22, 22, 33, 33, 33], 2)
    2
    >>> dizi_esitleme([1, 2, 3], 0)
    Traceback (most recent call last):
    ValueError: Adım boyutu pozitif ve sıfırdan farklı olmalıdır.
    >>> dizi_esitleme([1, 2, 3], -1)
    Traceback (most recent call last):
    ValueError: Adım boyutu pozitif ve sıfırdan farklı olmalıdır.
    >>> dizi_esitleme([1, 2, 3], 0.5)
    Traceback (most recent call last):
    ValueError: Adım boyutu bir tam sayı olmalıdır.
    >>> dizi_esitleme([1, 2, 3], maxsize)
    1
    """
    if adım_boyutu <= 0:
        raise ValueError("Adım boyutu pozitif ve sıfırdan farklı olmalıdır.")
    if not isinstance(adım_boyutu, int):
        raise ValueError("Adım boyutu bir tam sayı olmalıdır.")

    benzersiz_elemanlar = set(vektör)
    min_güncellemeler = maxsize

    for eleman in benzersiz_elemanlar:
        eleman_indeksi = 0
        güncellemeler = 0
        while eleman_indeksi < len(vektör):
            if vektör[eleman_indeksi] != eleman:
                güncellemeler += 1
                eleman_indeksi += adım_boyutu
            else:
                eleman_indeksi += 1
        min_güncellemeler = min(min_güncellemeler, güncellemeler)

    return min_güncellemeler

if __name__ == "__main__":
    from doctest import testmod

    testmod()
