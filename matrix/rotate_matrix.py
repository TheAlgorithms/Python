"""
Bu problemde, matris elemanlarını 90, 180 ve 270 derece (saat yönünün tersine) döndürmek istiyoruz.
Daha fazla bilgi için: https://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array

Organiser: K. Umut Araz
"""

from __future__ import annotations


def matris_oluştur(satır_boyutu: int = 4) -> list[list[int]]:
    """
    >>> matris_oluştur()
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> matris_oluştur(1)
    [[1]]
    >>> matris_oluştur(-2)
    [[1, 2], [3, 4]]
    >>> matris_oluştur(3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matris_oluştur() == matris_oluştur(4)
    True
    """
    satır_boyutu = abs(satır_boyutu) or 4
    return [[1 + x + y * satır_boyutu for x in range(satır_boyutu)] for y in range(satır_boyutu)]


def doksan_derece_dondur(matris: list[list[int]]) -> list[list[int]]:
    """
    >>> doksan_derece_dondur(matris_oluştur())
    [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
    >>> doksan_derece_dondur(matris_oluştur()) == transpoze(sütunları_ters_dondur(matris_oluştur()))
    True
    """

    return satırları_ters_dondur(transpoze(matris))


def yüzseksen_derece_dondur(matris: list[list[int]]) -> list[list[int]]:
    """
    >>> yüzseksen_derece_dondur(matris_oluştur())
    [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
    >>> yüzseksen_derece_dondur(matris_oluştur()) == sütunları_ters_dondur(satırları_ters_dondur(matris_oluştur()))
    True
    """

    return satırları_ters_dondur(sütunları_ters_dondur(matris))


def iki yüz yetmiş_derece_dondur(matris: list[list[int]]) -> list[list[int]]:
    """
    >>> iki_yüz_yetmiş_derece_dondur(matris_oluştur())
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    >>> iki_yüz_yetmiş_derece_dondur(matris_oluştur()) == transpoze(satırları_ters_dondur(matris_oluştur()))
    True
    """

    return sütunları_ters_dondur(transpoze(matris))


def transpoze(matris: list[list[int]]) -> list[list[int]]:
    matris[:] = [list(x) for x in zip(*matris)]
    return matris


def satırları_ters_dondur(matris: list[list[int]]) -> list[list[int]]:
    matris[:] = matris[::-1]
    return matris


def sütunları_ters_dondur(matris: list[list[int]]) -> list[list[int]]:
    matris[:] = [x[::-1] for x in matris]
    return matris


def matris_yazdır(matris: list[list[int]]) -> None:
    for i in matris:
        print(*i)


if __name__ == "__main__":
    matris = matris_oluştur()
    print("\nOrijinal Matris:\n")
    matris_yazdır(matris)
    print("\n90 derece saat yönünün tersine döndürülmüş:\n")
    matris_yazdır(doksan_derece_dondur(matris))

    matris = matris_oluştur()
    print("\nOrijinal Matris:\n")
    matris_yazdır(matris)
    print("\n180 derece döndürülmüş:\n")
    matris_yazdır(yüzseksen_derece_dondur(matris))

    matris = matris_oluştur()
    print("\nOrijinal Matris:\n")
    matris_yazdır(matris)
    print("\n270 derece saat yönünün tersine döndürülmüş:\n")
    matris_yazdır(iki_yüz_yetmiş_derece_dondur(matris))
