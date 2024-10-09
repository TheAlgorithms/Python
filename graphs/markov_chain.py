from __future__ import annotations

from collections import Counter
from random import random


class MarkovZinciriGrafiğiYönsüzAğırlıksız:
    """
    Markov Zinciri Algoritmasını çalıştırmak için Yönsüz Ağırlıksız Grafik
    """

    def __init__(self):
        self.bağlantılar = {}

    def düğüm_ekle(self, düğüm: str) -> None:
        self.bağlantılar[düğüm] = {}

    def geçiş_olasılığı_ekle(
        self, düğüm1: str, düğüm2: str, olasılık: float
    ) -> None:
        if düğüm1 not in self.bağlantılar:
            self.düğüm_ekle(düğüm1)
        if düğüm2 not in self.bağlantılar:
            self.düğüm_ekle(düğüm2)
        self.bağlantılar[düğüm1][düğüm2] = olasılık

    def düğümleri_al(self) -> list[str]:
        return list(self.bağlantılar)

    def geçiş(self, düğüm: str) -> str:
        mevcut_olasılık = 0
        rastgele_değer = random()

        for hedef in self.bağlantılar[düğüm]:
            mevcut_olasılık += self.bağlantılar[düğüm][hedef]
            if mevcut_olasılık > rastgele_değer:
                return hedef
        return ""


def geçişleri_al(
    başlangıç: str, geçişler: list[tuple[str, str, float]], adımlar: int
) -> dict[str, int]:
    """
    Markov Zinciri algoritmasını çalıştırmak ve her düğümün kaç kez ziyaret edildiğini
    hesaplamak

    >>> geçişler = [
    ... ('a', 'a', 0.9),
    ... ('a', 'b', 0.075),
    ... ('a', 'c', 0.025),
    ... ('b', 'a', 0.15),
    ... ('b', 'b', 0.8),
    ... ('b', 'c', 0.05),
    ... ('c', 'a', 0.25),
    ... ('c', 'b', 0.25),
    ... ('c', 'c', 0.5)
    ... ]

    >>> sonuç = geçişleri_al('a', geçişler, 5000)

    >>> sonuç['a'] > sonuç['b'] > sonuç['c']
    True
    """

    grafik = MarkovZinciriGrafiğiYönsüzAğırlıksız()

    for düğüm1, düğüm2, olasılık in geçişler:
        grafik.geçiş_olasılığı_ekle(düğüm1, düğüm2, olasılık)

    ziyaret_edilen = Counter(grafik.düğümleri_al())
    düğüm = başlangıç

    for _ in range(adımlar):
        düğüm = grafik.geçiş(düğüm)
        ziyaret_edilen[düğüm] += 1

    return ziyaret_edilen


if __name__ == "__main__":
    import doctest

    doctest.testmod()
