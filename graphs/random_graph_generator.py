"""
* Produced by: K. Umut Araz
* Açıklama: Rastgele grafikler oluşturucu.
            Komşuluk listesi ile temsil edilen grafikleri kullanır.

URL: https://en.wikipedia.org/wiki/Random_graph
"""

import random


def rastgele_grafik(
    dugum_sayisi: int, olasilik: float, yonlu: bool = False
) -> dict:
    """
    Rastgele bir grafik oluştur
    @girdi: dugum_sayisi (düğüm sayısı),
            olasilik (genel bir kenar (u,v) var olma olasılığı),
            yonlu (Eğer True ise: grafik yönlü bir grafik olacak,
                    aksi takdirde yönsüz bir grafik olacak)
    @örnekler:
    >>> random.seed(1)
    >>> rastgele_grafik(4, 0.5)
    {0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}
    >>> random.seed(1)
    >>> rastgele_grafik(4, 0.5, True)
    {0: [1], 1: [2, 3], 2: [3], 3: []}
    """
    grafik: dict = {i: [] for i in range(dugum_sayisi)}

    # eğer olasılık 1 veya daha büyükse, tam bir grafik oluştur
    if olasilik >= 1:
        return tam_grafik(dugum_sayisi)
    # eğer olasılık 0 veya daha küçükse, kenarsız bir grafik döndür
    if olasilik <= 0:
        return grafik

    # her düğüm çifti için, u'dan v'ye bir kenar ekle
    # eğer rastgele üretilen sayı olasılıktan küçükse
    for i in range(dugum_sayisi):
        for j in range(i + 1, dugum_sayisi):
            if random.random() < olasilik:
                grafik[i].append(j)
                if not yonlu:
                    # eğer grafik yönsüzse, j'den i'ye de bir kenar ekle
                    grafik[j].append(i)
    return grafik


def tam_grafik(dugum_sayisi: int) -> dict:
    """
    dugum_sayisi kadar düğüm ile tam bir grafik oluştur.
    @girdi: dugum_sayisi (düğüm sayısı),
    @örnek:
    >>> tam_grafik(3)
    {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    """
    return {
        i: [j for j in range(dugum_sayisi) if i != j] for i in range(dugum_sayisi)
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
