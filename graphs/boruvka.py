"""Borůvka algoritması.

Borůvka algoritması kullanarak bir grafın minimum yayılma ağacını (MST) belirler.
Borůvka algoritması, bağlı bir grafın minimum yayılma ağacını veya bağlı olmayan bir
grafın minimum yayılma ormanını bulmak için açgözlü bir algoritmadır.

Bu algoritmanın zaman karmaşıklığı O(ELogV) olup, burada E kenar sayısını, V ise düğüm
sayısını temsil eder. O(kenar_sayısı Log düğüm_sayısı)

Bu algoritmanın alan karmaşıklığı O(V + E) olup, düğüm sayısına eşit boyutta birkaç
liste tutmamız gerektiği ve grafın tüm kenarlarını veri yapısının içinde tutmamız
gerektiği için bu şekildedir.

Borůvka algoritması, diğer MST algoritmalarıyla hemen hemen aynı sonucu verir -
hepsi minimum yayılma ağacını bulur ve zaman karmaşıklığı yaklaşık olarak aynıdır.

Borůvka algoritmasının alternatiflerine göre bir avantajı, minimum yayılma ağacını
bulmak için kenarları önceden sıralaması veya bir öncelik kuyruğu tutması
gerekmemesidir. Bu, karmaşıklığına yardımcı olmasa da, çünkü yine de kenarları logE
kez geçer, kodlaması biraz daha basittir.

Detaylar: https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm
"""

from __future__ import annotations

from typing import Any

# Yazar: K. Umut Araz (https://github.com/arazumut)


class Grafik:
    def __init__(self, düğüm_sayısı: int) -> None:
        """
        Argümanlar:
            düğüm_sayısı - grafikteki düğüm sayısı
        Özellikler:
            m_düğüm_sayısı - grafikteki düğüm sayısı.
            m_kenarlar - kenarların listesi.
            m_bileşen - bir düğümün ait olduğu bileşenin indeksini saklayan sözlük.
        """

        self.m_düğüm_sayısı = düğüm_sayısı
        self.m_kenarlar: list[list[int]] = []
        self.m_bileşen: dict[int, int] = {}

    def kenar_ekle(self, u_düğüm: int, v_düğüm: int, ağırlık: int) -> None:
        """Grafiğe [ilk, ikinci, kenar ağırlığı] formatında bir kenar ekler."""

        self.m_kenarlar.append([u_düğüm, v_düğüm, ağırlık])

    def bileşen_bul(self, u_düğüm: int) -> int:
        """Belirli bir bileşen boyunca yeni bir bileşen yayar."""

        if self.m_bileşen[u_düğüm] == u_düğüm:
            return u_düğüm
        return self.bileşen_bul(self.m_bileşen[u_düğüm])

    def bileşen_ayarla(self, u_düğüm: int) -> None:
        """Belirli bir düğümün bileşen indeksini bulur"""

        if self.m_bileşen[u_düğüm] != u_düğüm:
            for k in self.m_bileşen:
                self.m_bileşen[k] = self.bileşen_bul(k)

    def birleştir(self, bileşen_boyutu: list[int], u_düğüm: int, v_düğüm: int) -> None:
        """Birleştirme, iki düğüm için bileşenlerin köklerini bulur, bileşenleri
        boyut açısından karşılaştırır ve daha küçük olanı daha büyük olana ekleyerek
        tek bir bileşen oluşturur"""

        if bileşen_boyutu[u_düğüm] <= bileşen_boyutu[v_düğüm]:
            self.m_bileşen[u_düğüm] = v_düğüm
            bileşen_boyutu[v_düğüm] += bileşen_boyutu[u_düğüm]
            self.bileşen_ayarla(u_düğüm)

        elif bileşen_boyutu[u_düğüm] >= bileşen_boyutu[v_düğüm]:
            self.m_bileşen[v_düğüm] = self.bileşen_bul(u_düğüm)
            bileşen_boyutu[u_düğüm] += bileşen_boyutu[v_düğüm]
            self.bileşen_ayarla(v_düğüm)

    def boruvka(self) -> None:
        """MST'yi bulmak için Borůvka algoritmasını uygular."""

        # Algoritma için gerekli ek listeleri başlat.
        bileşen_boyutu = []
        mst_ağırlığı = 0

        minimum_ağırlık_kenarı: list[Any] = [-1] * self.m_düğüm_sayısı

        # Bileşenlerin listesi (tüm düğümlerle başlatılır)
        for düğüm in range(self.m_düğüm_sayısı):
            self.m_bileşen.update({düğüm: düğüm})
            bileşen_boyutu.append(1)

        bileşen_sayısı = self.m_düğüm_sayısı

        while bileşen_sayısı > 1:
            for kenar in self.m_kenarlar:
                u, v, w = kenar

                u_bileşen = self.m_bileşen[u]
                v_bileşen = self.m_bileşen[v]

                if u_bileşen != v_bileşen:
                    """Eğer u bileşeninin mevcut minimum ağırlık kenarı
                    yoksa (yani -1 ise) veya şu anda gözlemlediğimiz
                    kenardan daha büyükse, gözlemlediğimiz kenarın
                    değerini ona atarız.

                    Eğer v bileşeninin mevcut minimum ağırlık kenarı
                    yoksa (yani -1 ise) veya şu anda gözlemlediğimiz
                    kenardan daha büyükse, gözlemlediğimiz kenarın
                    değerini ona atarız."""
                    for bileşen in (u_bileşen, v_bileşen):
                        if (
                            minimum_ağırlık_kenarı[bileşen] == -1
                            or minimum_ağırlık_kenarı[bileşen][2] > w
                        ):
                            minimum_ağırlık_kenarı[bileşen] = [u, v, w]

            for kenar in minimum_ağırlık_kenarı:
                if isinstance(kenar, list):
                    u, v, w = kenar

                    u_bileşen = self.m_bileşen[u]
                    v_bileşen = self.m_bileşen[v]

                    if u_bileşen != v_bileşen:
                        mst_ağırlığı += w
                        self.birleştir(bileşen_boyutu, u_bileşen, v_bileşen)
                        print(f"Kenar eklendi [{u} - {v}]\nEklenen ağırlık: {w}\n")
                        bileşen_sayısı -= 1

            minimum_ağırlık_kenarı = [-1] * self.m_düğüm_sayısı
        print(f"Minimum yayılma ağacının toplam ağırlığı: {mst_ağırlığı}")


def test_vector() -> None:
    """
    >>> g = Grafik(8)
    >>> for u_v_w in ((0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4),
    ...    (3, 4, 8), (4, 5, 10), (4, 6, 6), (4, 7, 5), (5, 7, 15), (6, 7, 4)):
    ...        g.kenar_ekle(*u_v_w)
    >>> g.boruvka()
    Kenar eklendi [0 - 3]
    Eklenen ağırlık: 5
    <BLANKLINE>
    Kenar eklendi [0 - 1]
    Eklenen ağırlık: 10
    <BLANKLINE>
    Kenar eklendi [2 - 3]
    Eklenen ağırlık: 4
    <BLANKLINE>
    Kenar eklendi [4 - 7]
    Eklenen ağırlık: 5
    <BLANKLINE>
    Kenar eklendi [4 - 5]
    Eklenen ağırlık: 10
    <BLANKLINE>
    Kenar eklendi [6 - 7]
    Eklenen ağırlık: 4
    <BLANKLINE>
    Kenar eklendi [3 - 4]
    Eklenen ağırlık: 8
    <BLANKLINE>
    Minimum yayılma ağacının toplam ağırlığı: 46
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
