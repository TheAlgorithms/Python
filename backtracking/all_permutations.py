"""
Bu problemde, verilen dizinin tüm olası permütasyonlarını belirlemek istiyoruz.
Bu problemi çözmek için geri izleme (backtracking) yöntemini kullanıyoruz.

Organiser: K. Umut Araz

Zaman karmaşıklığı: O(n! * n),
burada n, verilen dizinin uzunluğunu belirtir.
"""

from __future__ import annotations


def tum_permutasyonlari_olustur(dizi: list[int | str]) -> None:
    durum_uzayi_agaci_olustur(dizi, [], 0, [False] * len(dizi))


def durum_uzayi_agaci_olustur(
    dizi: list[int | str],
    mevcut_dizi: list[int | str],
    indeks: int,
    indeks_kullanildi: list[bool],
) -> None:
    """
    Her dalı derinlik öncelikli arama (DFS) kullanarak yinelemek için bir durum uzayı ağacı oluşturur.
    Verilen dizinin sonuna ulaştığında sona erer.

    :param dizi: Permütasyonların oluşturulduğu giriş dizisi.
    :param mevcut_dizi: Oluşturulan mevcut permütasyon.
    :param indeks: Dizideki mevcut indeks.
    :param indeks_kullanildi: Permütasyonda hangi elemanların kullanıldığını izlemek için liste.

    Örnek 1:
    >>> dizi = [1, 2, 3]
    >>> mevcut_dizi = []
    >>> indeks_kullanildi = [False, False, False]
    >>> durum_uzayi_agaci_olustur(dizi, mevcut_dizi, 0, indeks_kullanildi)
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]

    Örnek 2:
    >>> dizi = ["A", "B", "C"]
    >>> mevcut_dizi = []
    >>> indeks_kullanildi = [False, False, False]
    >>> durum_uzayi_agaci_olustur(dizi, mevcut_dizi, 0, indeks_kullanildi)
    ['A', 'B', 'C']
    ['A', 'C', 'B']
    ['B', 'A', 'C']
    ['B', 'C', 'A']
    ['C', 'A', 'B']
    ['C', 'B', 'A']

    Örnek 3:
    >>> dizi = [1]
    >>> mevcut_dizi = []
    >>> indeks_kullanildi = [False]
    >>> durum_uzayi_agaci_olustur(dizi, mevcut_dizi, 0, indeks_kullanildi)
    [1]
    """

    if indeks == len(dizi):
        print(mevcut_dizi)
        return

    for i in range(len(dizi)):
        if not indeks_kullanildi[i]:
            mevcut_dizi.append(dizi[i])
            indeks_kullanildi[i] = True
            durum_uzayi_agaci_olustur(dizi, mevcut_dizi, indeks + 1, indeks_kullanildi)
            mevcut_dizi.pop()
            indeks_kullanildi[i] = False


# Kullanıcıdan giriş almak için yorumu kaldırın
# print("Elemanları girin")
# dizi = list(map(int, input().split()))

dizi: list[int | str] = [3, 1, 2, 4]
tum_permutasyonlari_olustur(dizi)

dizi_2: list[int | str] = ["A", "B", "C"]
tum_permutasyonlari_olustur(dizi_2)
