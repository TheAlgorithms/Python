"""
0-1 grafında en kısa yolu O(E + V) süresinde bulma, bu dijkstra'dan daha hızlıdır.
0-1 grafı, ağırlıkları 0 veya 1 olan ağırlıklı grafiktir.
Link: https://codeforces.com/blog/entry/22276
"""

from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Kenar:
    """Ağırlıklı yönlendirilmiş grafik kenarı."""

    hedef_düğüm: int
    ağırlık: int


class KomşulukListesi:
    """Grafik komşuluk listesi."""

    def __init__(self, boyut: int):
        self._grafik: list[list[Kenar]] = [[] for _ in range(boyut)]
        self._boyut = boyut

    def __getitem__(self, düğüm: int) -> Iterator[Kenar]:
        """Verilen düğüme bitişik tüm düğümleri al."""
        return iter(self._grafik[düğüm])

    @property
    def boyut(self):
        return self._boyut

    def kenar_ekle(self, başlangıç_düğüm: int, bitiş_düğüm: int, ağırlık: int):
        """
        >>> g = KomşulukListesi(2)
        >>> g.kenar_ekle(0, 1, 0)
        >>> g.kenar_ekle(1, 0, 1)
        >>> list(g[0])
        [Kenar(hedef_düğüm=1, ağırlık=0)]
        >>> list(g[1])
        [Kenar(hedef_düğüm=0, ağırlık=1)]
        >>> g.kenar_ekle(0, 1, 2)
        Traceback (most recent call last):
            ...
        ValueError: Kenar ağırlığı 0 veya 1 olmalıdır.
        >>> g.kenar_ekle(0, 2, 1)
        Traceback (most recent call last):
            ...
        ValueError: Düğüm indeksleri [0; boyut) aralığında olmalıdır.
        """
        if ağırlık not in (0, 1):
            raise ValueError("Kenar ağırlığı 0 veya 1 olmalıdır.")

        if bitiş_düğüm < 0 or bitiş_düğüm >= self.boyut:
            raise ValueError("Düğüm indeksleri [0; boyut) aralığında olmalıdır.")

        self._grafik[başlangıç_düğüm].append(Kenar(bitiş_düğüm, ağırlık))

    def en_kısa_yolu_al(self, başlangıç_düğüm: int, bitiş_düğüm: int) -> int | None:
        """
        0-1 grafında başlangıç_düğüm'den bitiş_düğüm'e en kısa mesafeyi döndürür.
              1                  1         1
         0--------->3        6--------7>------->8
         |          ^        ^        ^         |1
         |          |        |        |0        v
        0|          |0      1|        9-------->10
         |          |        |        ^    1
         v          |        |        |0
         1--------->2<-------4------->5
              0         1        1
        >>> g = KomşulukListesi(11)
        >>> g.kenar_ekle(0, 1, 0)
        >>> g.kenar_ekle(0, 3, 1)
        >>> g.kenar_ekle(1, 2, 0)
        >>> g.kenar_ekle(2, 3, 0)
        >>> g.kenar_ekle(4, 2, 1)
        >>> g.kenar_ekle(4, 5, 1)
        >>> g.kenar_ekle(4, 6, 1)
        >>> g.kenar_ekle(5, 9, 0)
        >>> g.kenar_ekle(6, 7, 1)
        >>> g.kenar_ekle(7, 8, 1)
        >>> g.kenar_ekle(8, 10, 1)
        >>> g.kenar_ekle(9, 7, 0)
        >>> g.kenar_ekle(9, 10, 1)
        >>> g.kenar_ekle(1, 2, 2)
        Traceback (most recent call last):
            ...
        ValueError: Kenar ağırlığı 0 veya 1 olmalıdır.
        >>> g.en_kısa_yolu_al(0, 3)
        0
        >>> g.en_kısa_yolu_al(0, 4)
        Traceback (most recent call last):
            ...
        ValueError: Başlangıç_düğüm'den bitiş_düğüm'e yol yok.
        >>> g.en_kısa_yolu_al(4, 10)
        2
        >>> g.en_kısa_yolu_al(4, 8)
        2
        >>> g.en_kısa_yolu_al(0, 1)
        0
        >>> g.en_kısa_yolu_al(1, 0)
        Traceback (most recent call last):
            ...
        ValueError: Başlangıç_düğüm'den bitiş_düğüm'e yol yok.
        """
        kuyruk = deque([başlangıç_düğüm])
        mesafeler: list[int | None] = [None] * self.boyut
        mesafeler[başlangıç_düğüm] = 0

        while kuyruk:
            mevcut_düğüm = kuyruk.popleft()
            mevcut_mesafe = mesafeler[mevcut_düğüm]
            if mevcut_mesafe is None:
                continue

            for kenar in self[mevcut_düğüm]:
                yeni_mesafe = mevcut_mesafe + kenar.ağırlık
                hedef_düğüm_mesafesi = mesafeler[kenar.hedef_düğüm]
                if (
                    isinstance(hedef_düğüm_mesafesi, int)
                    and yeni_mesafe >= hedef_düğüm_mesafesi
                ):
                    continue
                mesafeler[kenar.hedef_düğüm] = yeni_mesafe
                if kenar.ağırlık == 0:
                    kuyruk.appendleft(kenar.hedef_düğüm)
                else:
                    kuyruk.append(kenar.hedef_düğüm)

        if mesafeler[bitiş_düğüm] is None:
            raise ValueError("Başlangıç_düğüm'den bitiş_düğüm'e yol yok.")

        return mesafeler[bitiş_düğüm]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
