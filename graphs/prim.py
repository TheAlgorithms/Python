"""Prim'in Algoritması.

Prim'in Algoritmasını kullanarak bir grafın minimum yayılma ağacını (MST) belirler.

Detaylar: https://en.wikipedia.org/wiki/Prim%27s_algorithm
"""

#Produced by: K. Umut Araz

import heapq as hq
import math
from collections.abc import Iterator


class Düğüm:
    """Düğüm Sınıfı."""

    def __init__(self, id_):
        """
        Argümanlar:
            id - düğümü tanımlamak için bir id girin
        Özellikler:
            komşular - bağlı olduğu düğümlerin bir listesi
            kenarlar - kenarların ağırlığını saklamak için bir sözlük
        """
        self.id = str(id_)
        self.anahtar = None
        self.pi = None
        self.komşular = []
        self.kenarlar = {}  # {düğüm:mesafe}

    def __lt__(self, diğer):
        """< operatörü için karşılaştırma kuralı."""
        return self.anahtar < diğer.anahtar

    def __repr__(self):
        """Düğüm id'sini döndür."""
        return self.id

    def komşu_ekle(self, düğüm):
        """Komşular listesine bir düğüm ekle."""
        self.komşular.append(düğüm)

    def kenar_ekle(self, düğüm, ağırlık):
        """Hedef düğüm ve ağırlık."""
        self.kenarlar[düğüm.id] = ağırlık


def bağla(graf, a, b, kenar):
    # komşuları ekle:
    graf[a - 1].komşu_ekle(graf[b - 1])
    graf[b - 1].komşu_ekle(graf[a - 1])
    # kenarları ekle:
    graf[a - 1].kenar_ekle(graf[b - 1], kenar)
    graf[b - 1].kenar_ekle(graf[a - 1], kenar)


def prim(graf: list, kök: Düğüm) -> list:
    """Prim'in Algoritması.

    Çalışma Zamanı:
        O(mn) `m` kenar ve `n` düğüm ile

    Döndür:
        Minimum Yayılma Ağacının Kenarları ile Liste

    Kullanım:
        prim(graf, graf[0])
    """
    a = []
    for u in graf:
        u.anahtar = math.inf
        u.pi = None
    kök.anahtar = 0
    q = graf[:]
    while q:
        u = min(q)
        q.remove(u)
        for v in u.komşular:
            if (v in q) and (u.kenarlar[v.id] < v.anahtar):
                v.pi = u
                v.anahtar = u.kenarlar[v.id]
    for i in range(1, len(graf)):
        a.append((int(graf[i].id) + 1, int(graf[i].pi.id) + 1))
    return a


def prim_heap(graf: list, kök: Düğüm) -> Iterator[tuple]:
    """Min yığın ile Prim'in Algoritması.

    Çalışma Zamanı:
        O((m + n)log n) `m` kenar ve `n` düğüm ile

    Döndür:
        Minimum Yayılma Ağacının Kenarları

    Kullanım:
        prim(graf, graf[0])
    """
    for u in graf:
        u.anahtar = math.inf
        u.pi = None
    kök.anahtar = 0

    h = list(graf)
    hq.heapify(h)

    while h:
        u = hq.heappop(h)
        for v in u.komşular:
            if (v in h) and (u.kenarlar[v.id] < v.anahtar):
                v.pi = u
                v.anahtar = u.kenarlar[v.id]
                hq.heapify(h)

    for i in range(1, len(graf)):
        yield (int(graf[i].id) + 1, int(graf[i].pi.id) + 1)


def test_vector() -> None:
    """
    # x düğümünü saklamak için bir liste oluşturur.
    >>> x = 5
    >>> G = [Düğüm(n) for n in range(x)]

    >>> bağla(G, 1, 2, 15)
    >>> bağla(G, 1, 3, 12)
    >>> bağla(G, 2, 4, 13)
    >>> bağla(G, 2, 5, 5)
    >>> bağla(G, 3, 2, 6)
    >>> bağla(G, 3, 4, 6)
    >>> bağla(G, 0, 0, 0)  # Minimum yayılma ağacını oluştur:
    >>> G_heap = G[:]
    >>> MST = prim(G, G[0])
    >>> MST_heap = prim_heap(G, G[0])
    >>> for i in MST:
    ...     print(i)
    (2, 3)
    (3, 1)
    (4, 3)
    (5, 2)
    >>> for i in MST_heap:
    ...     print(i)
    (2, 3)
    (3, 1)
    (4, 3)
    (5, 2)
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
