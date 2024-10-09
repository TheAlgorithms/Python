from __future__ import annotations


class Grafik:
    def __init__(self, dugum_sayisi: int) -> None:
        """
        >>> grafik = Grafik(2)
        >>> grafik.dugum_sayisi
        2
        >>> len(grafik.grafik)
        2
        >>> len(grafik.grafik[0])
        2
        """
        self.dugum_sayisi = dugum_sayisi
        self.grafik = [[0] * dugum_sayisi for _ in range(dugum_sayisi)]

    def cozumu_yazdir(self, kaynak_mesafeleri: list[int]) -> None:
        """
        >>> Grafik(0).cozumu_yazdir([])  # doctest: +NORMALIZE_WHITESPACE
        Düğüm 	 Kaynaktan Mesafe
        """
        print("Düğüm \t Kaynaktan Mesafe")
        for dugum in range(self.dugum_sayisi):
            print(dugum, "\t\t", kaynak_mesafeleri[dugum])

    def minimum_mesafe(
        self, kaynak_mesafeleri: list[int], ziyaret_edilen: list[bool]
    ) -> int:
        """
        Henüz en kısa yol ağacına dahil edilmemiş düğümler arasından minimum mesafe değerine sahip düğümü bulmak için yardımcı bir fonksiyon.

        >>> Grafik(3).minimum_mesafe([1, 2, 3], [False, False, True])
        0
        """

        # Bir sonraki düğüm için minimum mesafeyi başlat
        minimum = 1e7
        min_indis = 0

        # En kısa yol ağacında olmayan en yakın düğümü ara
        for dugum in range(self.dugum_sayisi):
            if kaynak_mesafeleri[dugum] < minimum and ziyaret_edilen[dugum] is False:
                minimum = kaynak_mesafeleri[dugum]
                min_indis = dugum
        return min_indis

    def dijkstra(self, kaynak: int) -> None:
        """
        Bir grafiğin komşuluk matrisi temsili kullanılarak Dijkstra'nın tek kaynaklı en kısa yol algoritmasını uygulayan fonksiyon.

        >>> Grafik(4).dijkstra(1)  # doctest: +NORMALIZE_WHITESPACE
        Düğüm  Kaynaktan Mesafe
        0 		 10000000
        1 		 0
        2 		 10000000
        3 		 10000000
        """

        mesafeler = [int(1e7)] * self.dugum_sayisi  # kaynaktan mesafeler
        mesafeler[kaynak] = 0
        ziyaret_edilen = [False] * self.dugum_sayisi

        for _ in range(self.dugum_sayisi):
            u = self.minimum_mesafe(mesafeler, ziyaret_edilen)
            ziyaret_edilen[u] = True

            # Seçilen düğümün komşu düğümlerinin mesafe değerini güncelle
            for v in range(self.dugum_sayisi):
                if (
                    self.grafik[u][v] > 0
                    and ziyaret_edilen[v] is False
                    and mesafeler[v] > mesafeler[u] + self.grafik[u][v]
                ):
                    mesafeler[v] = mesafeler[u] + self.grafik[u][v]

        self.cozumu_yazdir(mesafeler)


if __name__ == "__main__":
    grafik = Grafik(9)
    grafik.grafik = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]
    grafik.dijkstra(0)
