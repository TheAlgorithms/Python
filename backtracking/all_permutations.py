"""
Bu problemde, verilen dizinin tüm olası permütasyonlarını belirlemek istiyoruz.
Bu problemi çözmek için geri izleme (backtracking) kullanıyoruz.

Zaman karmaşıklığı: O(n! * n),
burada n, verilen dizinin uzunluğunu belirtir.
"""

from __future__ import annotations


def tüm_permütasyonları_oluştur(dizi: list[int | str]) -> None:
    durum_uzayı_ağacı_oluştur(dizi, [], 0, [0 for i in range(len(dizi))])


def durum_uzayı_ağacı_oluştur(
    dizi: list[int | str],
    mevcut_dizi: list[int | str],
    indeks: int,
    indeks_kullanıldı: list[int],
) -> None:
    """
    Her dalı DFS kullanarak yinelemek için bir durum uzayı ağacı oluşturur.
    Her durumun tam olarak len(dizi) - indeks çocuğu olduğunu biliyoruz.
    Verilen dizinin sonuna ulaştığında sona erer.

    :param dizi: Permütasyonların oluşturulduğu giriş dizisi.
    :param mevcut_dizi: Oluşturulan mevcut permütasyon.
    :param indeks: Dizideki mevcut indeks.
    :param indeks_kullanıldı: Permütasyonda hangi elemanların kullanıldığını izlemek için liste.

    Örnek 1:
    >>> dizi = [1, 2, 3]
    >>> mevcut_dizi = []
    >>> indeks_kullanıldı = [False, False, False]
    >>> durum_uzayı_ağacı_oluştur(dizi, mevcut_dizi, 0, indeks_kullanıldı)
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]

    Örnek 2:
    >>> dizi = ["A", "B", "C"]
    >>> mevcut_dizi = []
    >>> indeks_kullanıldı = [False, False, False]
    >>> durum_uzayı_ağacı_oluştur(dizi, mevcut_dizi, 0, indeks_kullanıldı)
    ['A', 'B', 'C']
    ['A', 'C', 'B']
    ['B', 'A', 'C']
    ['B', 'C', 'A']
    ['C', 'A', 'B']
    ['C', 'B', 'A']

    Örnek 3:
    >>> dizi = [1]
    >>> mevcut_dizi = []
    >>> indeks_kullanıldı = [False]
    >>> durum_uzayı_ağacı_oluştur(dizi, mevcut_dizi, 0, indeks_kullanıldı)
    [1]
    """

    if indeks == len(dizi):
        print(mevcut_dizi)
        return

    for i in range(len(dizi)):
        if not indeks_kullanıldı[i]:
            mevcut_dizi.append(dizi[i])
            indeks_kullanıldı[i] = True
            durum_uzayı_ağacı_oluştur(dizi, mevcut_dizi, indeks + 1, indeks_kullanıldı)
            mevcut_dizi.pop()
            indeks_kullanıldı[i] = False


"""
Kullanıcıdan giriş almak için yorumu kaldırın

print("Elemanları girin")
dizi = list(map(int, input().split()))
"""

dizi: list[int | str] = [3, 1, 2, 4]
tüm_permütasyonları_oluştur(dizi)

dizi_2: list[int | str] = ["A", "B", "C"]
tüm_permütasyonları_oluştur(dizi_2)
