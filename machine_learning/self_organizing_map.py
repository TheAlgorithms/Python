"""
https://tr.wikipedia.org/wiki/Kendini_organize_eden_harita
"""

import math

# Organised to K. Umut Araz


class KendiniOrganizeEdenHarita:
    def kazanan_vektoru_bul(self, agirliklar: list[list[float]], ornek: list[int]) -> int:
        """
        Öklidyen mesafesi ile kazanan vektörü hesapla

        >>> KendiniOrganizeEdenHarita().kazanan_vektoru_bul([[1, 2, 3], [4, 5, 6]], [1, 2, 3])
        0
        """
        d0 = 0.0
        d1 = 0.0
        for i in range(len(ornek)):
            d0 += math.pow((ornek[i] - agirliklar[0][i]), 2)
            d1 += math.pow((ornek[i] - agirliklar[1][i]), 2)
        return 0 if d0 < d1 else 1

    def guncelle(
        self, agirliklar: list[list[int | float]], ornek: list[int], j: int, alfa: float
    ) -> list[list[int | float]]:
        """
        Kazanan vektörü güncelle.

        >>> KendiniOrganizeEdenHarita().guncelle([[1, 2, 3], [4, 5, 6]], [1, 2, 3], 1, 0.1)
        [[1, 2, 3], [3.7, 4.7, 5.7]]
        """
        for i in range(len(agirliklar[j])):
            agirliklar[j][i] += alfa * (ornek[i] - agirliklar[j][i])
        return agirliklar


# Ana kod
def main() -> None:
    # Eğitim Örnekleri ( m, n )
    egitim_ornekleri = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]

    # Ağırlıkların başlatılması ( n, C )
    agirliklar = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]

    # Eğitim
    kendini_organize_eden_harita = KendiniOrganizeEdenHarita()
    epoch_sayisi = 3
    alfa = 0.5

    for _ in range(epoch_sayisi):
        for j in range(len(egitim_ornekleri)):
            # Eğitim örneği
            ornek = egitim_ornekleri[j]

            # Kazanan vektörü hesapla
            kazanan = kendini_organize_eden_harita.kazanan_vektoru_bul(agirliklar, ornek)

            # Kazanan vektörü güncelle
            agirliklar = kendini_organize_eden_harita.guncelle(agirliklar, ornek, kazanan, alfa)

    # Test örneğini sınıflandır
    ornek = [0, 0, 0, 1]
    kazanan = kendini_organize_eden_harita.kazanan_vektoru_bul(agirliklar, ornek)

    # Sonuçlar
    print(f"Test örneğinin ait olduğu küme : {kazanan}")
    print(f"Eğitilmiş ağırlıklar : {agirliklar}")


# main() fonksiyonunu çalıştırma
if __name__ == "__main__":
    main()
